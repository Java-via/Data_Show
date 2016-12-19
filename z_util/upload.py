# _*_ coding: utf-8 _*_

import os
import time
from flask import jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired

basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径


class FileForm(FlaskForm):
    file = FileField("请选择文件", validators=[DataRequired("请选择文件")])
    submit = SubmitField("上传")


def api_upload(app, file):
    # file_dir = app.config['UPLOAD_FOLDER']  # 拼接成合法文件夹地址
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])  # 拼接成合法文件夹地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    # f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    fname = file.filename
    ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
    unix_time = int(time.time())
    new_filename = str(unix_time)+'.'+ext   # 修改文件名
    file.save(os.path.join(file_dir, new_filename))  #保存文件到upload目录
    return jsonify({"result": 1, "new_name": new_filename, "errmsg": "上传成功"})
