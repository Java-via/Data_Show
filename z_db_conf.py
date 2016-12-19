# _*_ coding: utf-8 _*_

import pymysql


def db_conf():
    conn = pymysql.connect(host="localhost", db="db_doumovies", user="root", passwd="123", charset="utf8")
    cur = conn.cursor()
    return conn, cur


def db_conf_file():
    conn = pymysql.connect(host="localhost", db="db_datashow", user="root", passwd="123", charset="utf8")
    cur = conn.cursor()
    return conn, cur
