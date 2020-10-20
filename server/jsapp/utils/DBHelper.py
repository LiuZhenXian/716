import sqlite3
import jsapp.utils.AppConfig as ag
conn = sqlite3.connect(ag.database_path,check_same_thread = False)
#获取数据库对应表中的字段名
def get_index_dict(cursor):
    index_dict=dict()
    index=0
    for desc in cursor.description:
        index_dict[desc[0]]=index
        index=index+1
    return index_dict

#查询数据库，返回字典
def query(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    index_dict = get_index_dict(cursor)
    res = []
    for datai in data:
        resi = dict()
        for indexi in index_dict:
            resi[indexi] = datai[index_dict[indexi]]
        res.append(resi)
    return res



if __name__ == '__main__':
    res=query("select * from JS_User  ")

    print(res)