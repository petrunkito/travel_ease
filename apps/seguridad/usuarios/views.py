from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer  
from drf_yasg.utils import swagger_auto_schema 

class UsuariosView(APIView):

    @swagger_auto_schema(request_body=UsuarioSerializer)
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"message": "Usuario creado exitosamente."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # ya tenemos este endpoint de usuarios, pero tenemos que estar autorizados para la creacion de uno
