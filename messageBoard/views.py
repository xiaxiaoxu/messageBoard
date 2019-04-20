#encoding=utf-8

from flask import flash, redirect, url_for, render_template

from messageBoard import app, db
from messageBoard.models import Message
from messageBoard.forms import HelloForm

@app.route('/messageBoard', methods=['GET', 'POST'])
def index():
    #  加载所有的记录
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name = name)  #实例化Message模型类（表），创建记录
        db.session.add(message)  #添加记录到数据库会话
        db.session.commit()  #提交会话
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))  #重定向到index视图
    return render_template('index.html', form=form, messages=messages)  #渲染模板，处理get请求



@app.route('/csstest')
def cssTest():
    return render_template('cssTest.html')
























