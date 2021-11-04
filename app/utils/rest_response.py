import json
import time

from flask import Response


def build_response(data, code=200, http_status=200, message="Success"):
    if data is None:
        data = {}
    rest = {"code": code, "timestamp": int(round(time.time() * 1000)), "message": message, "data": data}
    response = Response(json.dumps(rest), http_status)
    return response
