from flask import Flask,url_for,render_template,redirect,session,request,Response
from Model import dao
from flask_restful import Resource
import uuid #universally unique identifier
# 중복로그인 막기
# 페이지 이동 마다 DB의 세션 값과 현재 세션값 비교하기.

class User(Resource):
    def get(self):
        if session.get('auth'):
            try:
                user = dao.User.query.filter_by(id=str(session.get('auth'))).first()
                if str(user.sessionId) == str(session.get('_id')):
                    return Response(render_template('View/index.htm', Auth=session.get('auth'), Title='StartPage'),mimetype='text/html')
                else:
                    return Response(render_template('View/index.htm', Title='StartPage'),mimetype='text/html')  
            
            except:
                return False
        else:
            return Response(render_template('View/index.htm', Title='StartPage'),mimetype='text/html')
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

                return True;
        except:
            return False
    def put(self):
        #register 
        try:
            new_user = dao.User(username=request.form['username'], password=request.form['password'])
            dao.db.session.add(new_user)
            dao.db.session.commit()
            return True;
        except:
            return False;
    def delete(self):
        #logout
        try:
            user = dao.User.query.filter_by(id=str(session.get('auth'))).first()
            dao.db.session.commit()
            session.clear() 
            return True
        except:
            return False
