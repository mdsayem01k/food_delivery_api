from rest_framework import serializers
from apps.users.models import Customer, User
from rest_framework.authtoken.models import Token



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password','role']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)  # Generate token upon registration
        return user
    


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
#         extra_kwargs = { "password": {"write_only": True, },}
    

#     def create(self, validated_data):
#         try:
#             role = validated_data.get("role", "customer")
#             username = validated_data.get("username")
#             first_name = validated_data.get("first_name")
#             last_name = validated_data.get("last_name")
#             email = validated_data.get("email")
#             password = validated_data.get("password")

#             user = User.objects.create(
#                 email=email, 
#                 role=role,
#                 username=username,
#                 first_name=first_name,
#                 last_name=last_name
#             )
#             user.set_password(password)
#             user.save()

#             if role.lower() == "customer":
#                 Customer.objects.create(
#                     user=user
#                 )
#             return user
#         except Exception as e:
#             raise e


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = "__all__"
