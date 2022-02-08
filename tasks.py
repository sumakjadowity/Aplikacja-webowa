# from celery import Celery
# import matlab.engine
# eng = matlab.engine.connect_matlab()
# import asyncio
# import sys
#
# if sys.platform == 'win32':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
#
# @app.task
# def image(path1):
#     print('1')
#     eng.load(path1)
#     print('2')
#     plik = eng.evalc(r"run C:\Users\marty\Documents\studia\TSwM\projekt\ProjectFlask\kod_matlab.m")
#     print('3')
#     x = eng.load(r"C:\Users\marty\Documents\studia\TSwM\projekt\ProjectFlask\mat2.mat")
#     print('4')
#     return x
