from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone

from .models import Transporte
from .serializers import TransporteSerializer
#quede en probar la api de transporte

class TransportesView(APIView):

    def get_one(self, pk):
        try:
            item = Transporte.objects.get(pk=pk, activo=True)
            return item
        except(Transporte.DoesNotExist):
            return None

    def get(self, request, pk=None):
        if  pk:
            item = self.get_one(pk)
            if item == None: 
                return Response({"message":"resource not found"}, status=404)
            serializer = TransporteSerializer(item)
            return Response(serializer.data)

        items = Transporte.objects.filter(activo=True) 
        serializer = TransporteSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = TransporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        item = self.get_one(pk)
        if item == None: 
            return Response({"message":"resource not found"}, status=404)
        
        serializer = TransporteSerializer(item, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
 
        return Response(serializer.errors, status=404)
    
    def delete(self, request, pk):
        item = self.get_one(pk)
        if item == None:
            return Response({"message":"resource not found"}, status=404)
        item.activo = False
        item.eliminado_en = timezone.now()
        item.save()
        return Response(status=204)

