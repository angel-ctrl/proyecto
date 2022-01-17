from rest_framework import serializers
from django.contrib.auth.models import User
from core.app1.models import Escritores

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        if validate_data.get('password') == None or validate_data.get('password') == '':
            raise serializers.ValidationError('Debe ingresar una contraseña')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        if User.objects.filter(username=data):
            raise serializers.ValidationError('Ya hay un usuario con este nombre')
        else:
            return data
        
class ModelSerializer(serializers.Serializer):
    autor = serializers.CharField(max_length=50)
    libro = serializers.CharField(max_length=50)
    
    class Meta:
        model = Escritores
    
    def create(self, validate_data):
        instance = Escritores()
        instance.autor = validate_data.get('autor')
        instance.libro = validate_data.get('libro')
        if validate_data.get('autor') == None or validate_data.get('autor') == '':
            raise serializers.ValidationError('Debe ingresar el nombre del autor')
        if validate_data.get('libro') == None or validate_data.get('libro') == '':
            raise serializers.ValidationError('Debe ingresar un libro escrito por el autor')
        instance.save()
        return instance
    
    def update(self, instance, validated_data): 
        instance.autor = validated_data.get('autor', instance.autor)
        instance.libro = validated_data.get('libro', instance.libro)
        instance.save()
        return instance