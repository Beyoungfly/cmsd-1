# -*- coding: UTF-8 -*-
__author__ = 'lijie'
import path
from response import *
from template import render


@path.route(path='/', method=['GET'])
def index(request):
    return render(request, "首页模板.html")


@path.route(path='/redir/', method=['GET'])
def index(request):
    return HttpResponseRedirect("http://www.baidu.com")


@path.route(path='/json/', method=['GET'])
def index(request):
    return {'id': 111, "name": "杭州"}


@path.route(path='/print/<str:msg>/<int:id>', method=['GET', 'POST'])
def index(request, msg, id):
    return msg + str(id)


"""
    JS 测试代码:
    var ws = new WebSocket("ws://localhost:8000/live/");
    ws.onopen = function(evt) {
        console.log("Connection open ...");
        ws.send('1234');
    };
    ws.onclose = function(evt){
        console.log("connection closed...")
    };
"""
@path.route(path='/live/', method=['GET'])
def live(request):
    check_head_pairs = {
        'Upgrade': 'websocket',
        'Connection': 'Upgrade'
    }

    key = request.headers['Sec-WebSocket-Key']
    version = request.headers['Sec-WebSocket-Version']
    return HttpResponseWebSocket(key, version)
