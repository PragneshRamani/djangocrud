from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect
from .models import Information
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .forms import UserFrom
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InformationSerializer
from rest_framework import status
import django_filters
from rest_framework import filters
from rest_framework import generics


# Create your views here.

# def index(request):
#   info = Information.objects.all()
#  return render(request,'data/index.html',{'info':info})

class IndexView(generic.ListView):
    template_name = 'data/index.html'

    # def get_absolute_url(self):
    #  return reverse('index',kwargs={'pk':self.})

    def get_queryset(self):
        return Information.objects.all()


class DetailView(generic.DetailView):
    model = Information
    template_name = 'data/detail.html'


class InfoCreate(generic.CreateView):
    model = Information
    fields = ['first_name', 'last_name', 'email', 'mobile', 'salary']
    # template_name = "data/information_form.html"
    success_url = reverse_lazy('index')


class InfoUpdate(generic.UpdateView):
    model = Information
    template_name = 'data/update.html'
    fields = ['first_name', 'last_name', 'email', 'mobile', 'salary']
    success_url = reverse_lazy('index')


class InfoDelete(generic.DeleteView):
    model = Information
    template_name = 'data/index.html'
    success_url = reverse_lazy('index')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    form = UserFrom()
    return render(request, "registration/register.html", {'form': form})


class InformationList(APIView):
    """
    emp list api.
    """

    def get(self, request):
        info = Information.objects.all()
        serializer = InformationSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request, formate="None"):
        serializer = InformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoDetailView(APIView):
    def get_object(self, pk):
        try:
            return Information.objects.get(pk=pk)
        except Information.DoesNotExist:
            raise Http404

    def get(self, request, pk, fromat=None):
        info = Information.objects.get(pk=pk)
        serializer = InformationSerializer(info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        info = Information.objects.get(pk=pk)
        serializer = InformationSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        info = Information.objects.get(pk=pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InfoFilterList(generics.ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)


class FilterField(generics.ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('salary','email',)




class InfoSearchView(generics.ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("first_name","last_name","email")

class InformationOrder(generics.ListAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("first_name",)