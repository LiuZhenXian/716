# coding=utf-8
import sqlite3
import os

conn = sqlite3.connect('F:/716/DB3000_CMANO_CN.db3')


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


if __name__ == '__main__':
    # en_ch('中英对照.txt')
    _, result = sql("select * from tbadd")
    print(result)