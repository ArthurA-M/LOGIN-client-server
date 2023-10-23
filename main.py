import os
from aiohttp import web

PORT = int(os.environ.get("LISTEN_AT", 8080)) #récuperer la variable d'environnement

async def check_login(request): #fonction à exécuter
    if str(request.match_info['username']) == "user" and str(request.match_info['password']) == "root":
        return web.Response(text="Login sucessful, hello {}".format(request.match_info['username']))
    else:
        return web.Response(text="Login failed")

app = web.Application()
app.add_routes([web.get('/login/$usr={username}&psswd={password}', check_login)]) #dans quel cas

web.run_app(app, port=PORT)