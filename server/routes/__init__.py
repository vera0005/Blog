from apiflask import APIBlueprint

api = APIBlueprint("api", __name__)


# 响应式结构消息、状态码、数据
def make_response(message, status_code, data):
    return {"message": message, "code": status_code, "data": data}
