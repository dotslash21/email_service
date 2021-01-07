from rest_framework import response, viewsets, status

from api.models import Email
from api.serializers import EmailSerializer
from api.service.email import send_email


class EmailViewSet(viewsets.GenericViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, format=None):
        """
        Method to send an email.

        :param request: The request object.
        :return: The response object.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                send_email(
                    serializer.data.get('from_email'),
                    serializer.data.get('to_email'),
                    serializer.data.get('subject'),
                    serializer.data.get('content')
                )
                # Mail sent successfully, return the response
                return response.Response({'message': 'success'}, status=status.HTTP_200_OK)
            except Exception as e:
                # Some error occurred during sending the mail.
                return response.Response(
                    {'message': e.__str__()},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return response.Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
