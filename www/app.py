#!/d:\\awesome-python-webapp/www python3
# -*- coding: utf-8 -*-
# software: sublime
# name: app.py
# date: 2020.05.02

__author__ = "ddw20191222"

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web # 选择web服务器

# 定义视图
def index(request):
	return web.Response(body='<h1>Awesome</h1>', content_type="text/html")


async def init(loop):
	app = web.Application(loop=loop) #创建应用程序对象
	app.router.add_route("GET", '/', index) #插入路径
	srv = await loop.create_server(app.make_handler(), host='127.0.0.1', port=9001)
	logging.info("server started at http://127.0.0.1:9000...")
	return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
