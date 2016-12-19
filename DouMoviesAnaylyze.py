# _*_ coding: utf-8 _*_

import json
import logging
from flask_bootstrap import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, send_from_directory, render_template, request
from z_util.upload import *
from z_db_conf import db_conf_file
from z_db_sql import SQL_FILE_LIST

logging.basicConfig(level=logging.WARN)
dou = Flask(__name__)
bootstrap = Bootstrap(dou)
db = SQLAlchemy(dou)

UPLOAD_FOLDER = '../static/doc'
dou.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # 设置文件上传的目标文件夹
dou.config['SECRET_KEY'] = 'hard to guess string'
dou.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@localhost:3306/db_datashow?charset=utf8"


@dou.route('/')
def hello_world():
    return render_template("a_index.html")


@dou.route('/movies')
def show_movies():
    return render_template("b_showmovie.html")


@dou.route('/musics')
def show_musics():
    return render_template("b_showmusic.html")


@dou.route('/apps')
def show_apps():
    return render_template("b_showapp.html")


@dou.route('/reports')
def download_reports():
    return render_template("b_report.html")


@dou.route('/reports/upload', methods=["GET", "POST"])
def upload_test():
    form = FileForm()
    if form.validate_on_submit():
        file = form.data.get("file")
        msg = api_upload(dou, file)
        upload_msg = json.loads(msg.data.decode("utf-8"))
        result = upload_msg.get("result")
        new_name = upload_msg.get("new_name")
        errmsg = upload_msg.get("errmsg")
        if not result:
            flash(errmsg)
        else:
            model_file = File()
            model_file.name = new_name
            model_file.show_name = file.filename
            model_file.uploaddate = time.strftime("%Y-%m-%d %H:%M:%S")
            model_file.downloadetimes = 0
            model_file.sharetimes = 0
            try:
                db.session.add(model_file)
                db.session.commit()
            except Exception as excep:
                logging.error("Save file error: %s", str(excep))
                db.session.rollback()
    return render_template("upload.html", form=form)


@dou.route("/reports/download/<path:filename>")
def downloader(filename):
    dirpath = os.path.join(dou.root_path, './static/doc')
    print(dirpath)
    return send_from_directory(dirpath, filename, as_attachment=True)


@dou.route("/reports/online")
def test():
    return render_template("report_readonline.html")


class File(db.Model):
    __tablename__ = 'tb_file'
    id = db.Column("f_id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("f_name", db.String)
    show_name = db.Column("f_showname", db.String)
    uploaddate = db.Column("f_uploaddate", db.DateTime)
    downloadetimes = db.Column("f_downloadtimes", db.Integer)
    sharetimes = db.Column("f_sharetimes", db.Integer)

    def __repr__(self):
        return '<Role %r>' % self.name


@dou.route("/api/upload", methods=["GET", "POST"])
def upload():
    file = request.files.get("input_file")
    msg = api_upload(dou, file)
    upload_msg = json.loads(msg.data.decode("utf-8"))
    result = upload_msg.get("result")
    new_name = upload_msg.get("new_name")
    errmsg = upload_msg.get("errmsg")
    if not result:
        flash(errmsg)
    else:
        model_file = File()
        model_file.name = new_name
        model_file.show_name = file.filename
        model_file.uploaddate = time.strftime("%Y-%m-%d %H:%M:%S")
        model_file.downloadetimes = 0
        model_file.sharetimes = 0
        try:
            db.session.add(model_file)
            db.session.commit()
        except Exception as excep:
            db.session.rollback()
    return jsonify({"message": "上传成功"})


@dou.route("/api/getfiles")
def get_file():
    conn, cur = db_conf_file()
    try:
        cur.execute(SQL_FILE_LIST)
        list_files = list(cur.fetchall())
        conn.close()
        return jsonify({"result": 1, "data": list_files})
    except Exception as exce:
        return jsonify({"result": 0, "data": str(exce)})


if __name__ == '__main__':
    dou.run(debug=True)
