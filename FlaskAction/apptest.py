import os
import sys
import json
import random

from flask import Flask, render_template, request, send_file, Response

app = Flask(__name__)

@app.get('/')
async def root():
    return {'example' : 'This is an example', 'data' : 0}

@app.get('/buttons')
async def get_buttons():
    return os.listdir('./button')

@app.get('/button/<button_number>')
async def get_button_number(button_number : str):
    return {'button_number ' : os.path.isdir('./button/'+button_number)}

@app.get('/button/<button_number>/launch')
async def launch_script(button_number : str):
    path_dir = './button/'+button_number
    path_file = path_dir+'/script.py'
    if os.path.isdir(path_dir):
        if os.path.isfile(path_file):
            os.system('python '+ path_file)
            return Response("<h2> Script executed, Status : 200</h2>",status=200)
        else:
            return Response("<h2> Script not found, Status : 404</h2>", status=404)
    else :
        return Response("<h2> Directory not found, Status : 400</h2>",status=400)
    
@app.get('/button/<button_number>/config')
async def get_config(button_number : str):
    path_dir = './button/'+button_number
    path_file = path_dir+'/config.json'
    if os.path.isdir(path_dir):
        if os.path.isfile(path_file):
            return open(path_file).read()
            # return Response("<h2> Image found, Status : 200</h2>",status=200)
        else:
            return Response("<h2> Config file not found, Status : 404</h2>", status=404)
    else :
        return Response("<h2> Directory not found, Status : 400</h2>",status=400)
    
@app.get('/button/<button_number>/image')
async def get_image(button_number : str):
    path_dir = './button/'+button_number
    path_file = None
    if os.path.isdir(path_dir):
        for f in os.listdir(path_dir):
            if os.path.isfile(path_dir+'/'+f) and 'image' in f:
                path_file = path_dir + "/" + f
        print(str(path_file))
        if path_file is not None and os.path.isfile(path_file):
            return send_file(path_file)
            # return Response("<h2> Image found, Status : 200</h2>",status=200)
        else:
            return Response("<h2> Image not found, Status : 404</h2>", status=404)
    else :
        return Response("<h2> Directory not found, Status : 400</h2>",status=400)
    
if __name__ == '__main__':
    app.run(debug=True)
