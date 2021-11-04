import time

from flask import Response, jsonify


def created(data, message="", status=201, headers=None, mimetype='application/json', content_type='application/json'):
    rest = {"data": data, "status": status, "timestamp": int(round(time.time() * 1000)), "message": message}
    # return Response(rest, status=status, headers=headers, mimetype=mimetype, content_type=content_type)
    return jsonify(rest)
