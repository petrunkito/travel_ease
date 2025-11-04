from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status

from .models import Municipio
from apps.catalogos.departamentos.models import Departamento
from .serializers import MunicipioSerializer

class MunicipiosView(APIView):

    def get_one(self, pk):
        try:
            item = Municipio.objects.get(pk=pk, activo=True)
            return item
        except(Municipio.DoesNotExist):
            return None
        
    def is_department_active(self, pk_department):
        department = Departamento.objects.filter(id=pk_department, activo=True).first()
        
        if department:
            return True
        return False

    def get(self, request, pk=None):
        if  pk:
            item = self.get_one(pk)
            if item == None: 
                return Response({"message":"resource not found"}, status=404)
            serializer = MunicipioSerializer(item)
            return Response(serializer.data)

        items = Municipio.objects.filter(activo=True) 
        serializer = MunicipioSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data;
        if not self.is_department_active(data['departamento']):
            return Response({"message":"department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(data=data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        item = self.get_one(pk)
        if item == None: 
            return Response({"message":"resource not found"}, status=404)
        
        data = request.data
        

        if 'departamento' in data and not self.is_department_active(data['departamento']):
            return Response({"message":"department not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MunicipioSerializer(item, data = data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
 
        return Response(serializer.errors, status=404)
    
    def delete(self, request, pk):
        municipality = self.get_one(pk)
        if municipality == None:
            return Response({"message":"resource not found"}, status=404)
        municipality.activo = False
        municipality.eliminado_en = timezone.now()
        municipality.save()
        return Response(status=204)
