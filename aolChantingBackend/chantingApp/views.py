# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os, requests, json, uuid, time
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.template.loader import get_template
from datetime import datetime, timedelta
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def register_user(request):
    print("request=====",request)
    print("In delete data api=====",request.data['phone'])
    print("email====",request.data['email'])
    chk_user_ph = chanting_users.objects.filter(phone_no=request.data['phone'])
    if chk_user_ph:
         data = {
        "result":"Fail",
        "message":"Cannot add User, Provided phone number already exist in database.",
        "response":"400"
    }
    chk_user_email = chanting_users.objects.filter(email_id=request.data['email'])
    if chk_user_email:
         data = {
        "result":"Fail",
        "message":"Cannot add User, Provided email id already exist in database.",
        "response":"400"
    }
    else:
        if request.data['password'] != None:
            user = chanting_users.objects.create(first_name=request.data['first_name'],last_name=request.data['last_name'],phone_no=request.data['phone'],email_id=request.data['email'],password=request.data['password'])
            user.save()
            data = {
            "result":"Success",
            "message":"User added to Chanting Database Succefully",
            "response":"200"
            }
        else:
            data = {
            "result":"Fail",
            "message":"Cannot add User, Details missing, please fill all required fields.",
            "response":"400"
        }
    
    return JsonResponse(data)

@csrf_exempt
@api_view(['POST'])
def login(request):
    print("request==login=ss==",request)
    email = request.data['email']
    password = request.data['password']
    chk_user = chanting_users.objects.filter(email_id=email)
    if chk_user:
        chk_user_pwd = chanting_users.objects.filter(password=password)
        if chk_user_pwd:
            for user in chk_user:
                print("Login Successfully=====")
                data = {
                    "result":"Success",
                    "message":"Login Successfully",
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    "email_id":user.email_id,
                    "phone_no":user.phone_no,
                    "response":"200"
                }
        else:
            data = {
            "result":"Fail",
            "message":"Password Wrong,Please check again and login",
            "response":"401"
        }
    else:
        data = {
        "result":"Fail",
        "message":"Email Wrong,Please check again and login",
        "response":"402"
    }
    print("login data==",data)
    return JsonResponse(data)


@csrf_exempt
@api_view(['POST'])
def add_chants(request):
    print("request==add_chants===",request)
    email = request.data['email']
    password = request.data['password']
    chant_name = request.data['chant_name']
    if chant_name:
        chk_user = chanting_users.objects.filter(email_id=email)
        if chk_user:
            chk_user_pwd = chanting_users.objects.filter(password=password)
            if chk_user_pwd:
                chant_chk = chanting_menu.objects.filter(chant_name=chant_name)
                if chant_chk:
                    data = {
                    "result":"Fail",
                    "message":"Given Chant Already Exist!",
                    "response":"400"
                }
                else:
                    chant = chanting_menu.objects.create(chant_name=chant_name)
                    chant.save()
                    data = {
                        "result":"Success",
                        "message":"New Chant added Successfully",
                        "response":"200"
                    }
            else:
                data = {
                "result":"Fail",
                "message":"Password Wrong,Please check again and login",
                "response":"401"
            }
        else:
            data = {
            "result":"Fail",
            "message":"Email Wrong,Please check again and login",
            "response":"402"
        }
    else:
        data = {
            "result":"Fail",
            "message":"Chant Name Missing",
            "response":"403"
        }

    print("chant dashboard data==",data)
    return JsonResponse(data)


@csrf_exempt
@api_view(['POST'])
def chanting_dashboard(request):
    print("request==chanting_dashboard===",request)
    chants_list = []
    email = request.data['email']
    # japa_count = 0
    # japa_mala_count = 0
    chants = chanting_menu.objects.all()
    for ch in chants:
        # chants_list.append(ch.chant_name)
        japa_count,japa_mala_count = get_user_chant_details(ch.chant_name,email)
        print("japa_count====",type(japa_count))
        tot_chant = get_chant_tot_count(ch.chant_name)
        chants_dict = {
            "chant_name":ch.chant_name,
            "japa_count":japa_count,
            "japa_mala_count":japa_mala_count,
            "chant_tot_count": tot_chant
        }
        chants_list.append(chants_dict)

    if len(chants_list) > 0:
        data = {
            "result":"Success",
            "message":"Data Successfully",
            "data":chants_list,
            "response":"200"
        }
    else:
        data = {
        "result":"Fail",
        "message":"No Chanting List Available",
        "response":"400"
    }
    
    return JsonResponse(data)

# @csrf_exempt
# @api_view(['POST'])
def get_user_chant_details(chant_name,email):
    # email = request.data['email']
    # chant_name = request.data['chant_name']
    chant =  chanting_menu.objects.filter(chant_name=chant_name)
    chant_obj = self_chant_dashboard.objects.filter(parent_chant=chant[0],email_id=email)
    japa_count = 0
    japa_mala_count = 0
    if chant_obj:
        for ch in chant_obj:
            count=ch.japa_count,
            mala_count=int(ch.japa_count)/108,
            japa_count = count[0]
            japa_mala_count = mala_count[0]
    else:
        japa_count = 0
        japa_mala_count = 0
        # data = {
        #     "result":"Fail",
        #     "message":"No Data Available",
        #     "response":"401"
        # }
    
    # return JsonResponse(data)
    return japa_count,japa_mala_count


@csrf_exempt
@api_view(['POST'])
def add_japa(request):
    """ API For Adding JAPA Count on Button Click"""
    print("request==add_japa===",request)
    email = request.data['email']
    chant_name = request.data['chant_name']
    japa = int(request.data['japa'])
    user_obj = chanting_users.objects.filter(email_id=email)
    chant =  chanting_menu.objects.filter(chant_name=chant_name)
    chant_obj = self_chant_dashboard.objects.filter(parent_chant=chant[0],email_id=email)
    if chant_obj:
        for chants in chant_obj:
            chants.japa_count = int(chants.japa_count) + int(japa)
            chants.save()
        data = {
            "result":"Success",
            "message":"Japa Added Successfully", 
            "response":"200"
        }
    else:
        chant_obj = self_chant_dashboard()
        chant_obj.japa_count = japa
        chant_obj.email_id = email
        chant_obj.japa_mala_count = int(japa)/108
        chant_obj.parent_chant = chant[0]
        chant_obj.save()
        data = {
            "result":"Success",
            "message":"Japa Added Successfully",
            "response":"201"
        }
    print("====data=====",data)
    return JsonResponse(data)


# @csrf_exempt
# @api_view(['POST'])
def get_chant_tot_count(chant_name):
    # print("request==add_japa===",request)
    # email = request.data['email']
    # chant_name = request.data['chant_name']
    # japa = request.data['japa']
    chant =  chanting_menu.objects.filter(chant_name=chant_name)
    chant_obj = self_chant_dashboard.objects.filter(parent_chant=chant[0])
    # chant_obj = self_chant_dashboard.objects.filter(parent_chant=chant_name)
    # user_obj = chanting_users.objects.filter(email=email)
    if chant_obj:
        tot = 0
        for chants in chant_obj:
            tot = tot + int(chants.japa_count)
        tot_chant_obj = chanting_menu.objects.filter(chant_name=chant_name)
        for tot_chant in tot_chant_obj:
            tot_chant.tot_chant_count = tot
            tot_chant.save()
        # data = {
        #     "result":"Success",
        #     "message":"Japa Added Successfully",
        #     "tot_chant_count":tot,
        #     "response":"200"
        # }
    else:
        tot = 0
    #     data = {
    #     "result":"Fail",
    #     "message":"No Japa Added",
    #     "response":"400"
    # }
    # print("====data=====",data)
    # return JsonResponse(data)
    return tot

@csrf_exempt
@api_view(['GET'])
def view_all_users(request):
    # print("request==chanting_dashboard===",request)
    user_data = []
    # email = request.data['email']
    chants = chanting_menu.objects.all()
    user_obj = chanting_users.objects.all()
    for user in user_obj:
        email = user.email_id
        chants_list = []
        for ch in chants:
            chants_dict = {}
            # chants_list.append(ch.chant_name)
            japa_count,japa_mala_count = get_user_chant_details(ch.chant_name,email)
            tot_chant = get_chant_tot_count(ch.chant_name)
            chants_dict = {
                "chant_name":ch.chant_name,
                "japa_count":japa_count,
            }
            chants_list.append(chants_dict)
        user_dict = {
            "user_name":user.first_name + ' ' + user.last_name,
            "chants_detail":chants_list
        }
        user_data.append(user_dict)

    if len(user_data) > 0:
        data = {
            "result":"Success",
            "message":"Data Successfully",
            "data":user_data,
            "response":"200"
        }
    else:
        data = {
        "result":"Fail",
        "message":"No Chanting List Available",
        "response":"400"
    }
    
    return JsonResponse(data)