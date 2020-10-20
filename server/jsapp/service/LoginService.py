from jsapp.utils import DBHelper

#登录的业务逻辑
def loginCheck(user,pwd):
    sql = "SELECT * FROM JS_User  "
    sql += "WHERE Username='{username}' and Password='{password}' ".format(username=user, password=pwd)
    res=DBHelper.query(sql)
    return res
