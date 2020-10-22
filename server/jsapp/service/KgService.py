from jsapp.utils import SituationFun
#登录的业务逻辑
def MainKgCheck():

    s1=SituationFun.Solution(1)
    info = s1.get_ent_info()  # A,B,D,order
    ent_a = SituationFun.nodes_edges(info[0])
    ent_b = SituationFun.nodes_edges(info[1])
    ent_d = SituationFun.nodes_edges(info[2])
    order = info[3]
    print("ent_a:", ent_a)
    print("ent_b:", ent_b)
    print("ent_d:", ent_d)
    print("order:", order)
    #加入到集合中
    data = {
        "ent_a": ent_a,
        "ent_b": ent_b,
        "ent_d": ent_d,
        "order":order
    }
    print(data)


    return data
