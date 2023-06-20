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
import base64
import os

class MyBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request,format=None):
        book = self.queryset
        serializer = self.serializer_class(book, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
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
        category= request.query_param.get("category")

        if book_id:
            book = self.get_object(book_id)
            serializer = self.serializer_class(book)
            return Response(serializer.data)
        if category:
            book = Book.objects.filter(category=category)
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
        print(data)

        try:
            contact_name = data['name']
            contact_email = data['email']
            contact_message = data['message']
            contact_subject = data['subject']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        send_mail(
            contact_subject, #subject
            contact_message, #message
            contact_email, #from email 
            ['tmttevgb711@gmail.com'] , #to email
            contact_name, # senders name
            )
        
    return Response(status=status.HTTP_201_CREATED)