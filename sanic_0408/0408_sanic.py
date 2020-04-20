# coding=utf-8
from sanic import Sanic
from sanic.response import text,json,redirect
app=Sanic(__name__)
"""
@app.route("/")
async def test(request):
    for i in range(1,100):
        i+=1
    return text('Hello world!')

@app.route('/')
async  def test(request):
    return json({"hello":"world"})
"""
#请求参数
#要指定一个参数，可以用像这样的角引号<PARAM>包围它。请求参数将作为关键字参数传递给路线处理程序函数。
@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))
@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))
@app.route('/person/<name:[A-z]+>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))
@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))

#请求类型
#路由装饰器接受一个可选的参数，方法，它允许处理程序函数与列表中的任何HTTP方法一起工作。
@app.route('/post')
async def post_handler(request):
    return text('POST request - {}'.format(request.json))
@app.route('/get', methods=['GET'])
async def get_handler(request):
    return text('GET request - {}'.format(request.args))

#增加路由
async  def handler1(request):
    return text('OK')
async def handler2(request,name):
    return text('Folder-{}'.format(name))
async def person_handler2(request,name):
    return text('Person-{}'.format(name))
app.add_route(handler1,'/test')
app.add_route(handler2,'/folder/<name>')
app.add_route(person_handler2,'/person/<name:[A-z]>',methods=['GET'])

#url_for
#Sanic提供了一个urlfor方法，根据处理程序方法名生成url。避免硬编码url路径到您的应用程序
@app.route('/')
async def index(request):
    url=app.url_for('post_handler',post_id=5)
    return redirect(url)
@app.route('/post/<post_id>')
async def post_handler(request,post_id):
    return text('Post-{}'.format(post_id))

app.run(host="0.0.0.0",port=8001,debug=True)
