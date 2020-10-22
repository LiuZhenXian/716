# coding=utf-8
import sqlite3
import os
from jsapp.utils import AppConfig

conn = sqlite3.connect(AppConfig.database_path)


def en_ch(filename):
    """
    添加中英对照  文件内容  ch\ten
    :param filename:
    :return:
    """
    cursor = conn.cursor()
    f = open(filename, encoding="utf-8")
    for line in f:
        line = line.strip('\n').split('\t')
        ch, en = line[0], line[1]
        sql_str = "insert into tbadd values('" + en + "', '" + ch + "')"
        cursor.execute(sql_str)
    f.close()
    cursor.close()
    conn.commit()


def sql(sql_str):
    cursor = conn.cursor()
    res = cursor.execute(sql_str)
    columns = [tup[0] for tup in res.description]
    res = cursor.fetchall()
    data = []
    for r in res:
        d = {k: v for k, v in zip(columns, r)}
        data.append(d)
    return columns, data


if __name__ == '__main__':
    cursor = conn.cursor()
    sq = "select * from tbadd"
    _, data = sql(sq)
    for d in data:
        print(d)
