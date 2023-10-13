from rest_framework.views import APIView
from rest_framework.response import Response

from apps.user.serializers import UserRegistrationSerializer


from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegistrationView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None:
            return Response({
            'error':'user with such username is already exists'
            }, status=400
            )
        else:
            user = User.objects.create(
                username=username,
                email=email

            )
            user.set_password(password)
            user.save()
            return Response({'message':'Success'}, status=201)

