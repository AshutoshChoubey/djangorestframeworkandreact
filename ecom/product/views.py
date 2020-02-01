from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from product.serializers import UserSerializer, GroupSerializer, ProductsSerializer
from rest_framework.generics import GenericAPIView
from product.models import Products
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.utils.text import slugify
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import FormParser, MultiPartParser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class ProductViewSet(GenericAPIView):
    @classmethod
    def get(self,request):
        # print(request.GET.get('id'))
        if request.GET.get('id'):
            productsData = Products.objects.get(pk=request.GET.get('id'))
            SnippetSerializer = ProductsSerializer(productsData)
        elif request.GET.get('slug'):
            productsData = Products.objects.get(slug=request.GET.get('slug'))
            SnippetSerializer = ProductsSerializer(productsData)
        else:
            productsData = Products.objects.all()
            SnippetSerializer = ProductsSerializer(productsData,many="true")
        response={"status":1,"message":"Product List","productList":SnippetSerializer.data}
        return JsonResponse(response, safe=False)

    @classmethod
    def post(self,request):
        data = request.data
        # parser_classes = (MultiPartParser, FormParser,FileUploadParser,)
        # if 'file' not in request.data:
        #     raise ParseError("Empty content")
        # f = request.data['image']
        # Products.image.save(f.name, f, save=True)
        # return Response(status=status.HTTP_201_CREATED)
        data['slug']= slugify(request.data['title'])
        serializerData=''
        saveProduct = ProductsSerializer(data=data)
        if saveProduct.is_valid():
            saveProduct.save()
            serializerData=saveProduct.data
            statusResponse=status.HTTP_201_CREATED
        else:
            serializerData=saveProduct.errors
            statusResponse=status.HTTP_400_BAD_REQUEST
        response={"status":1,"message":"Product Added Successfully","statusResponse":statusResponse,"serializerData":serializerData}
        # response={"status":1,"serializerData":f.name}
        return JsonResponse(response, safe=False)