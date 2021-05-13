from flask import Flask, render_template,request
import pymysql

app = Flask(__name__)


@app.route("/")
def root():
    """
    主页
    :return: Index.html
    """
    return render_template('index.html')

@app.route("/header")
def header():
    """
    主页
    :return: Index.html
    """
    return render_template('index.html')

@app.route("/maoyantop")
def maoyantop():
    """
    主页
    :return: maoyantop.html
    """
    req_prf()
    offset=request.args.get("offset")
    if offset == None:
        offset=0

    print(offset)
    datalist = []
    conn = pymysql.connect(
        host='xxx.xx.xxx.xxx',  # host
        port=3306,  # 默认端口，根据实际修改
        user='root',  # 用户名
        passwd='123456',  # 密码
        db='luke_db',  # DB name
    )
    cur = conn.cursor()

    cur.execute("select * from luke_db.t_movie_top100_maoyan limit "+str(offset)+",10")
    data = cur.fetchall()

    for dat in data :
        datalist.append(dat)
        # print(dat)
    cur.close()
    conn.close()
    return render_template("maoyantop.html",movies = datalist)

@app.route("/doubantop")
def doubantop():
    """
    主页
    :return: doubantop.html
    """
    return render_template('doubantop.html')

@app.route("/anx")
def anx():
    """
    主页
    :return: anx.html
    """
    return render_template('anx.html')

@app.route("/team")
def team():
    """
    主页
    :return: team.html
    """
    return render_template('team.html')

def req_prf():
    print()
    # name = request.args.get('name', 'Flask')
    # print("request.args:", request.args)
    # print("request.args.items():", request.args.items())
    # print("request.full_path:", request.full_path)
    # print("request.path:", request.path)
    # print("request.host:", request.host)
    # print("request.host_url:", request.host_url)
    # print("request.headers:\n", request.headers)
    # print("请求数据request.data:", request.data)
    # print("request.endpoint:", request.endpoint)
    # print("request.json:", request.json)
    # print("request.method:", request.method)
    # print("请求的url模式（http或https）request.scheme:", request.scheme)
    # print("request.user_agent:\n", request.user_agent)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
