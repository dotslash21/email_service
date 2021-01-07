from api.service.email.provider import ProviderEnum, provider_factory


def send_email(from_email: str, to_email: str, subject: str, content: str) -> None:
    for provider in ProviderEnum:
        try:
            # Get the appropriate provider
            provider_instance = provider_factory(provider)
            # Try to send the mail
            provider_instance.send_mail(
                from_email,
                to_email,
                subject,
                content
            )
            # Email sent successfully, return from the method
            return
        except Exception:
            # Some error occurred during sending the mail.
            # Continue with the next provider.
            continue

    # Raise exception if flow reaches here.
    raise Exception('Failed to send the email.')
