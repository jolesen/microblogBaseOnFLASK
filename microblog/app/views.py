#视图函数
from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World"