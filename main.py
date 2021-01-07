from api.service.email.provider import ProviderEnum, provider_factory

if __name__ == '__main__':
    provider = ProviderEnum.MailGun
    provider_instance = provider_factory(provider)
    provider_instance.send_mail(
        'arunangshubsws@gmail.com',
        'arunangshu.biswas@gcettb.ac.in',
        'MailGun Test E-Mail',
        'This is a test email sent via MailGun using the Python requests library.'
    )
