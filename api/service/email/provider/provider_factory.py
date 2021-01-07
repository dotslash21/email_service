import enum

from api.service.email.provider.providers import Provider, SendGridProvider, MailGunProvider


class ProviderEnum(enum.Enum):
    SendGrid = 'SendGrid'
    MailGun = 'MailGun'


def provider_factory(provider: ProviderEnum) -> Provider:
    """
    Provider factory to return a provider instance.

    :param provider: The requested provider.
    :return: An instance of Provider.
    """
    if provider.value == 'SendGrid':
        return SendGridProvider()
    elif provider.value == 'MailGun':
        return MailGunProvider()
    else:
        raise Exception('Invalid provider')
