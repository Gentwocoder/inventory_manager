from rest_framework import serializers
from .models import CustomUser, Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone_number', 'is_email_verified', 'is_phone_verified', 'is_active', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone_number', 'password']

        def create(self, validated_data):
            user = CustomUser.objects.create(
                email=validated_data['email'],
                phone_number=validated_data['phone_number'],
            )
            return user
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'address', 'phone_number', 'birthday', 'gender', 'profile_picture', 'is_verified']

class CustomTokenSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        login_field = attrs.get('email') or attrs.get('phone_number')
        password = attrs.get('password')
        user = authenticate(email=login_field, password=password) or authenticate(phone_number=login_field, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or phone number")
        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        refresh = self.get_token(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'phone_number': user.phone_number,
            }
        }
    
    def validate(self, attrs):
        user = authenticate(email=attrs.get('email'), password=attrs.get('password')) or authenticate(phone_number=attrs.get('phone_number'), password=attrs.get('password'))
        if user and user.check_password(attrs.get('password')):
            attrs['email'] = user.email
        return super().validate(attrs)
    
class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer