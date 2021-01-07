import abc
import os

import requests
from sendgrid import Mail, SendGridAPIClient


class Provider(abc.ABC):
    @abc.abstractmethod
    def send_mail(self, from_email: str, to_email: str, subject: str, content: str) -> dict:
        """
        Method to send mail.

        :param from_email: The email address of sender.
        :param to_email: The email address of receiver.
        :param subject: The subject of email.
        :param content: The content of email.
        :raises Exception: Error sending the email.
        :return: The response data from the provider.
        """
        pass


class SendGridProvider(Provider):
    def __init__(self):
        pass

    def send_mail(self, from_email: str, to_email: str, subject: str, content: str) -> dict:
        message = Mail(
            from_email=from_email,
            to_emails=to_email,
            subject=subject,
            plain_text_content=content
        )

        try:
            api_key = os.environ.get('SENDGRID_API_KEY')
            send_grid = SendGridAPIClient(api_key)
            response = send_grid.send(message)
            if response.status_code != 202:
                raise Exception('Failed to send the email via SendGrid!')
        except Exception as e:
            raise e


class MailGunProvider(Provider):
    def __init__(self):
        pass

    def send_mail(self, from_email: str, to_email: str, subject: str, content: str) -> dict:
        try:
            api_key = os.environ.get('MAILGUN_API_KEY')
            response = requests.post(
                'https://api.mailgun.net/v3/sandbox04d38322acde40c3a571f25d11a2fe9d.mailgun.org/messages',
                auth=('api', api_key),
                data={'from': from_email,
                      'to': [to_email],
                      'subject': subject,
                      'text': content})
            if response.status_code != 200:
                raise Exception('Failed to send the email via MailGun!')
        except Exception as e:
            raise e
