import os
import sys
import json
import random

from execute_from_folder import execute_function_from_module

from flask import Flask, render_template, request, send_file, Response

app = Flask(__name__)

@app.get('/')
async def root():
    return "Fill here"

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
        return Response(f"<h2> Directory not found, Status : 400</h2>",status=400)
    
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
    target_directory = f"./button/{button_number}"
    if os.path.isdir(path_dir):
        path_file = execute_function_from_module(f"{target_directory}/update.py", "main_update")
        if path_file is not None:
            path_file = target_directory + "/" + path_file
        else:
            print(f"output was none for {target_directory}/update.py")
        if path_file is not None and os.path.isfile(path_file):
            
            return send_file(path_file)
            # return Response("<h2> Image found, Status : 200</h2>",status=200)
        else:
            return Response("<h2> Image not found, Status : 404</h2>", status=404)
    else :
        return Response("<h2> Directory not found, Status : 400</h2>",status=400)
    
if __name__ == '__main__':
    app.run(debug=True)
