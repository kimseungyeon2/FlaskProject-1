from flask import Flask,url_for,render_template,redirect,session,request,Response
from Model import dao
from flask_restful import Resource
import uuid #universally unique identifier

# 중복로그인 막기
# 페이지 이동 마다 DB의 세션 값과 현재 세션값 비교하기.

class Home(Resource):
    def get(self):
        if not session.get('auth'):
            return Response(render_template('index.html'),mimetype='text/html')
        else:
            return Response(render_template('index.html',Auth=session.get('auth')),mimetype='text/html') 
    def post(self):
        return ''           
    def put(self):
        return ''
    def delete(self):
        return ''

class Login(Resource):
    def get(self):
        return Response(render_template('login.html'),mimetype='text/html')
    def post(self):
        username = request.form['username']
        password = request.form['password']
        try:
            data = dao.User.query.filter_by(username=username, password=password).first()
            if data.sessionId is not None:
                # sessionId have
                return False
            else:
                # sessionId not
                session['_id'] = uuid.uuid4()# 고유키 
                session['auth'] = data.id

                user = dao.User.query.filter_by(username=username, password=password).first()
                user.sessionId = str(session.get('_id'))
                dao.db.session.commit()

                return redirect('/')
        except:
            return "except false"
    def put(self):
        return ''
    def delete(self):
        return ''

class Register(Resource):
    def get(self):
        return Response(render_template('register.html'),mimetype='text/html')
    def post(self):
        new_user = dao.User(username=request.form['username'], password=request.form['password'])
        dao.db.session.add(new_user)
        dao.db.session.commit()
        return Response(render_template('login.html'),mimetype='text/html')
    def put(self):
        return ''
    def delete(self):
        return ''

class Logout(Resource):
    def get(self):
        session['logged_in'] = False
        return redirect('/')
    def post(self):
        return ''
    def put(self):
        return ''
    def delete(self):
        return ''