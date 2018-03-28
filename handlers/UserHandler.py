from handlers.AbstractHandler import AbstractHandler
from data.entity.UserEntity import UserEntity
from data.dao.UserDao import UserDao
import datetime
import json

from sqlalchemy.ext.declarative import DeclarativeMeta
from utils.AlchemyEncoder import AlchemyEncoder


class UserHandler(AbstractHandler):
    def get(self, *args, **kwargs):
        user_name = self.path_args[0][1::]
        print user_name
        userId = self.get_arguments("id")
        print userId
        id = int(unicode.encode(userId[0], 'utf-8'))
        try:
            user = UserDao.select_user_by_id(id)
            self.set_header('Content-Type', 'application/json; charset=UTF-8')
            self.write(json.dumps(user, cls=AlchemyEncoder))
            self.finish()
            # print isinstance(user.__class__, DeclarativeMeta)
        except BaseException as e:
            print e
            self.write("No user found")

    def post(self, *args, **kwargs):
        user = UserEntity(user_name='wangjinzhao', accesskey='testtest', accesskey_secret='sssssssssssssss',
                          created_time=datetime.datetime.now(), deleted=False, enable=False,
                          last_modified_time=datetime.datetime.now())
        try:
            UserDao.insert_user(user)
        except BaseException as e:
            print e

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
