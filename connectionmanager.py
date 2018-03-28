# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import ConfigParser


# config.ini.template
class ConnectionManager(object):
    def __init__(self):
        settings = ConfigParser.ConfigParser()
        settings.read('config.ini')

        url = settings.get('mysql', 'url')
        maxoverflow = settings.get('mysql', 'max_overflow')
        poolsize = settings.get('mysql', 'pool_size')
        showsql = settings.get('mysql', 'echo')

        self.engine = create_engine(url,
                                    max_overflow=int(maxoverflow),  # 超过连接池大小外最多创建的连接
                                    pool_size=int(poolsize),  # 连接池大小
                                    echo=bool(showsql)  # 是否打印sql
                                    )

        self.session = scoped_session(sessionmaker(bind=self.engine))


manager = ConnectionManager()
manager.session
