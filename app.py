from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_socketio import SocketIO
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket = SocketIO(app, async_mode=async_mode)



@app.route('/')
def index():
    username = request.args.get('nickname')
    if username == None:
        username = request.cookies.get('nickname')
        if username == None:
            return "Hi I am the ChatBot\nSend me your nickname please."
        else:
            return "Welcome back " + username + ".\n If you are oneother user please send your new nickname"
    else:
        return redirect(url_for('setcookie',newuid = username))
        uid = request.cookies.get('nickname')

@app.route('/setcookie/<newuid>')
def setcookie(newuid):
   resp = make_response()
   print('resp='+str(resp))
   print('hello '+newuid)
   resp.set_cookie('nickname', newuid)
   return resp


if __name__ == '__main__':
    socket.run(app, debug=True)