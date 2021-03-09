# -*- coding: utf-8 -*-

import datetime

from productiontest.server import db
from sqlalchemy import Column, DateTime, Integer, String


class TestResult(db.Model):
    __tablename__ = 'production_test_result'

    id = Column(Integer, primary_key=True)
    test_system_id = Column(Integer)
    test_framework_version = Column(String(64))
    test_script = Column(String(64))
    test_script_version = Column(String(64))
    test_result = Column(String(64))
    test_data = Column(String())
    timestamp = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    def to_dict(self):
        return {
            'id': self.id,
            'test_system_id': self.test_system_id,
            'test_framework_version': self.test_framework_version,
            'test_script': self.test_script,
            'test_script_version': self.test_script_version,
            'test_result': self.test_result,
            'test_data': self.test_data,
            'timestamp': self.timestamp,
        }
