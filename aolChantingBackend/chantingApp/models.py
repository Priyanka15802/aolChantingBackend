# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class chanting_users(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email_id = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email_id

class chanting_menu(models.Model):

    chant_name = models.CharField(max_length=100)
    tot_chant_count = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chant_name


class self_chant_dashboard(models.Model):

    # chant_name = models.CharField(max_length=100)
    parent_chant = models.ForeignKey('chanting_menu', on_delete=models.SET_NULL,null=True,blank=True)
    japa_count = models.IntegerField(default=0,blank=True, null=True)
    japa_mala_count = models.IntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email_id


# class self_chant_japa(models.Model):

#     # chant_name = models.CharField(max_length=100)
#     parent_chant = models.ForeignKey('chanting_menu', on_delete=models.SET_NULL,null=True,blank=True)
#     japa_count = models.IntegerField(blank=True, null=True)
#     email_id = models.CharField(max_length=100)
#     active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.chant_name



