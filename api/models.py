from django.db import models


class Email(models.Model):
    from_email = models.EmailField(max_length=254)
    to_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=78)
    content = models.TextField()

    def __str__(self):
        return {
            'from_email': self.from_email,
            'to_email': self.to_email,
            'subject': self.subject,
            'content': self.content,
        }.__str__()
