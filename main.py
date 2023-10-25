import os
from aiohttp import web

PORT = int(os.environ.get("LISTEN_AT", 8080)) #récuperer la variable d'environnement

def check_login(request): #fonction à exécuter
    if str(request.match_info['username']) == "user" and str(request.match_info['password']) == "root":
        return web.Response(text="1") #login sucessful
    else:
        return web.Response(text="0") #login failed

app = web.Application()
app.add_routes([web.get('/login/$usr={username}&psswd={password}', check_login)]) #dans quel cas
app.add_routes([web.static('/', 'front/' )])

web.run_app(app, port=PORT)