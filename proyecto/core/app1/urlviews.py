from django.urls import path
from core.app1.views import *
from rest_framework_simplejwt import views as jwt_views

app_name = 'app1'

urlpatterns = [
    path('registrarse/', SignUpAPI.as_view()),
    path('agregar_autor/', CreateAutor.as_view()),
    path('editar/<int:pk>/', ActualizarDatos.as_view()),
    path('eliminar/<int:pk>/', EliminarEscritor.as_view()),
    path('mostrar/', MostrarEscritor.as_view()),
    path('exportar/', ExportarXlsx.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]