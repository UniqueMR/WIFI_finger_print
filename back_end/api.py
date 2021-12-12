from collections import UserList
from typing_extensions import ParamSpec
from django.contrib import auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from back_end.models import Rss
# from myblog.models import Classes
# from myblog.toJson import Classes_data,Userinfo_data
# from myblog.models import UserInfo
import json

@api_view(['GET'])
def getRssList(request):
    rsslist = Rss.objects.all()
    data = []
    for item in rsslist:
        rss = []
        rss.append(item.position1)
        rss.append(item.position2)
        rss.append(item.position3)
        rss.append(item.position4)
        rss.append(item.position5)
        rss.append(item.position6)
        rss.append(item.position7)
        rss.append(item.position8)
        rss.append(item.position9)
        rss.append(item.position10)
        rss.append(item.position11)
        rss.append(item.position12)
        rss.append(item.position13)
        rss.append(item.position14)
        rss.append(item.position15)
        rss.append(item.position16)
        rss.append(item.position17)
        rss.append(item.position18)
        rss.append(item.position19)
        rss.append(item.position20)
        rss.append(item.position21)
        rss.append(item.position22)
        rss.append(item.position23)
        rss.append(item.position24)
        rss.append(item.position25)
        rss.append(item.position26)
        rss.append(item.position27)
        rss.append(item.position28)
        rss.append(item.position29)
        rss.append(item.position30)
        data_item = {
            'id':item.id,
            'rss':rss,
            'xlabel':item.xlabel,
            'ylabel':item.ylabel
        }
        data.append(data_item)
    return Response(data)