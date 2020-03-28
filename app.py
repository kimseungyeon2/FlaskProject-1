# -- coding: utf-8 --
from flask import Flask,url_for,render_template,redirect,session,request, make_response
from flask_restful import Api, Resource
from Model import dao
from Controller import User, Main
import config
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Main.Main,'/main')
api.add_resource(User.User,'/')


if __name__ == '__main__':
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = config.Result
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 사용자에게 원하는 정보를 전달완료했을때가 TEARDOWN, 그 순간마다 COMMIT을 하도록 한다.라는 설정
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # True하면 warrnig메시지 유발,
    dao.db.init_app(app)
    dao.db.app = app
    dao.db.create_all()
    app.secret_key = config.secret_key
    app.run(debug = True)