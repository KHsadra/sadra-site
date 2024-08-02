from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from utils.mail_user import send_mail

# Create your views here.


def main(req):
    return render(req, "main.html")
