import datetime
import decimal
import json
import time
import uuid

from flask import Response
from flask.json import JSONEncoder


def build_response(data, code=200, http_status=200, message="Success"):
    if data is None:
        data = {}
    rest = {"code": code, "timestamp": int(round(time.time() * 1000)), "message": message, "data": data}
    response = Response(json.dumps(rest), http_status)
    return response


class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, datetime.datetime):
            # 格式化时间
            return o.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(o, datetime.date):
            # 格式化日期
            return o.strftime('%Y-%m-%d')
        if isinstance(o, decimal.Decimal):
            # 格式化高精度数字
            return str(o)
        if isinstance(o, uuid.UUID):
            # 格式化uuid
            return str(o)
        if isinstance(o, int):
            # 格式化int
            return int(o)
        if isinstance(o, bytes):
            # 格式化字节数据
            return o.decode("utf-8")
        raise TypeError()
