import json
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from book.models import Book
from book.serializers import BookSerializer, ContactSerializer
import smtplib
from email.mime.text import MIMEText
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.core.mail import send_mail
from rest_framework.decorators import api_view



class MyBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request,format=None):
        book = self.queryset
        serializer = self.serializer_class(book, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyBookViewList(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        book_id = request.query_param.get("id")
        print(book_id)
        book = self.get_object(book_id)
        serializer = self.serializer_class(book)
        return Response(serializer.data)
    

    def put(self, request, id, format=None):
        book = self.get_object(id)
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, id, format=None):
        book = self.get_object(id)
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Contact(request):
    if request.method == 'POST':
        data = request.data

        try:
            contact_name = data['Name']
            contact_email = data['Email']
            contact_message = data['Message']
            contact_subject = data['Subject']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        send_mail(
            contact_Subject, #subject
            contact_Message, #message
            contact_Email, #from email 
            ['pururaj2000@gmail.com'] , #to email
            contact_Name, # senders name
            )
        
    return Response(status=status.HTTP_201_CREATED)