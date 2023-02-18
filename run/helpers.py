import json

def GetBody(request):
    #decode request body from binary into unicode string (json string?)
    unicode = request.body.decode('utf-8')
    #turn unicode string into json
    return json.loads(unicode)
