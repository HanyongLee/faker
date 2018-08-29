# -*- coding: utf-8 -*- 
# 한글 써도 에러 안남
from flask import Flask, render_template, request
import random
import csv



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/result")
def result():
    # 이름 받기
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    # 궁합 구라쳐서 랜덤 뽑기
    match = random.randrange(50, 101)
    #names라는 배열에 입력된 두 이름을 넣는다.
    # 'names.csv' 파일을 만들어서 저장한다.
    f = open('names.csv', 'a', encoding="utf-8" )
    a = csv.writer(f)
    a.writerow([name1, name2]) #csv는 2차원 배열(리스트)
    f.close()
    return render_template('result.html', name1 = name1, name2 = name2, match = match)
    
@app.route("/admin")
def admin():
    # names에 들어가 있는 모든 이름을 출력한다.
    f = open('names.csv', 'r')
    rr = csv.reader(f)
    names = rr
    return render_template('admin.html', names = names)
    
    
#app.run(host='0.0.0.0', port='8080', debug=True) #위 run 누르면 됨
