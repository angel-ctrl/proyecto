from core.app1.forms import *
from rest_framework.response import Response
from core.app1.serializer import ModelSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.app1.models import Escritores
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from django.http import HttpResponse
import csv
# Create your views here.


class SignUpAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

class CreateAutor(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EliminarEscritor(DestroyAPIView):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = ModelSerializer
    lookup_field = 'pk'
    queryset = Escritores.objects.all()
     
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Eliminacion con exito", status=status.HTTP_400_BAD_REQUEST)
        
class ActualizarDatos(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Escritores.objects.all()
    serializer_class = ModelSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Actualizacion exitosa"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
        
      
class MostrarEscritor(APIView):
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        
        serializer = ModelSerializer(Escritores.objects.all(), many=True)
        
        return Response(serializer.data)

    
class ExportarXlsx(APIView):
    
    def get(self, request):
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=autores_libros.csv'
        
        writer = csv.writer(response)
        writer.writerow(['autor', 'libro'])
        
        autores_libros = Escritores.objects.all()
        
        for expense in autores_libros:
            writer.writerow([expense.autor, expense.libro])
            
        return response