# coding=utf-8
from sanic import Sanic
from sanic.response import text
app=Sanic(__name__)
@app.route("/")
async def test(request):
    for i in range(1,100):
        i+=1
    return text('Hello tomorrow!')
app.run(host="0.0.0.0",port=8002,debug=True)