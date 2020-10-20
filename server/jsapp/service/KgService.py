
#登录的业务逻辑
def MainKgCheck():

    nodes = [{'group': 'Event', 'id': 79, 'label': '隐身'}, {'group': 'Event', 'id': 98, 'label': '轰炸'},
             {'group': 'Event', 'id': 86, 'label': '空中加油'}, {'group': 'Event', 'id': 85, 'label': '加油'},
             {'group': 'Event', 'id': 93, 'label': '联合'}, {'group': 'Event', 'id': 96, 'label': '攻击'},
             {'group': 'Event', 'id': 100, 'label': '部署'}, {'group': 'Event', 'id': 14, 'label': '歼击'},
             {'group': 'Event', 'id': 99, 'label': '武装'}, {'group': 'Event', 'id': 18, 'label': '滑跃起飞'},
             {'group': 'Event', 'id': 19, 'label': '起飞'}, {'group': 'Event', 'id': 94, 'label': '打击'},
             {'group': 'Event', 'id': 76, 'label': '飞行'}, {'group': 'Event', 'id': 25, 'label': '驾驶'},
             {'group': 'Event', 'id': 26, 'label': '协同'}, {'group': 'Event', 'id': 27, 'label': '协同作战'},
             {'group': 'Event', 'id': 97, 'label': '作战'}, {'group': 'Event', 'id': 55, 'label': '训练'},
             {'group': 'Event', 'id': 31, 'label': '出动'}, {'group': 'Event', 'id': 33, 'label': '起降'},
             {'group': 'Event', 'id': 35, 'label': '反潜'}, {'group': 'Event', 'id': 36, 'label': '巡逻'},
             {'group': 'Event', 'id': 88, 'label': '击落'}, {'group': 'Event', 'id': 43, 'label': '电子干扰'},
             {'group': 'Event', 'id': 44, 'label': '干扰'}, {'group': 'Event', 'id': 54, 'label': '侦察'},
             {'group': 'Event', 'id': 48, 'label': '携带'}, {'group': 'Event', 'id': 57, 'label': '激光制导'},
             {'group': 'Event', 'id': 82, 'label': '制导'}, {'group': 'Event', 'id': 59, 'label': '对抗'},
             {'group': 'Event', 'id': 60, 'label': '演练'}, {'group': 'Event', 'id': 91, 'label': '发射'},
             {'group': 'Event', 'id': 67, 'label': '合作'}, {'group': 'Event', 'id': 81, 'label': '挂载'},
             {'group': 'Event', 'id': 74, 'label': '替换'}, {'group': 'Event', 'id': 84, 'label': '护航'},
             {'group': 'Event', 'id': 92, 'label': '防空'}, {'group': 'Eve', 'id': 90, 'label': '潜射'}];

    edges = [{'from': 79, 'label': '顺承', 'to': 98}, {'from': 98, 'label': '顺承', 'to': 79},
             {'from': 86, 'label': '顺承', 'to': 85}, {'from': 93, 'label': '顺承', 'to': 96},
             {'from': 96, 'label': '顺承', 'to': 98}, {'from': 98, 'label': '顺承', 'to': 96},
             {'from': 100, 'label': '顺承', 'to': 98}, {'from': 14, 'label': '顺承', 'to': 98},
             {'from': 99, 'label': '顺承', 'to': 96}, {'from': 18, 'label': '顺承', 'to': 19},
             {'from': 94, 'label': '顺承', 'to': 98}, {'from': 98, 'label': '顺承', 'to': 76},
             {'from': 76, 'label': '顺承', 'to': 25}, {'from': 26, 'label': '顺承', 'to': 27},
             {'from': 27, 'label': '顺承', 'to': 97}, {'from': 76, 'label': '顺承', 'to': 55},
             {'from': 31, 'label': '顺承', 'to': 98}, {'from': 33, 'label': '顺承', 'to': 55},
             {'from': 35, 'label': '顺承', 'to': 36}, {'from': 99, 'label': '顺承', 'to': 88},
             {'from': 98, 'label': '顺承', 'to': 97}, {'from': 96, 'label': '顺承', 'to': 97},
             {'from': 43, 'label': '顺承', 'to': 44}, {'from': 88, 'label': '顺承', 'to': 54},
             {'from': 98, 'label': '顺承', 'to': 48}, {'from': 79, 'label': '顺承', 'to': 97},
             {'from': 96, 'label': '顺承', 'to': 99}, {'from': 99, 'label': '顺承', 'to': 54},
             {'from': 55, 'label': '顺承', 'to': 76}, {'from': 57, 'label': '顺承', 'to': 82},
             {'from': 59, 'label': '顺承', 'to': 60}, {'from': 98, 'label': '顺承', 'to': 94},
             {'from': 91, 'label': '顺承', 'to': 82}, {'from': 79, 'label': '顺承', 'to': 96},
             {'from': 67, 'label': '顺承', 'to': 97}, {'from': 76, 'label': '顺承', 'to': 98},
             {'from': 96, 'label': '顺承', 'to': 81}, {'from': 98, 'label': '顺承', 'to': 74},
             {'from': 79, 'label': '顺承', 'to': 76}, {'from': 98, 'label': '顺承', 'to': 100},
             {'from': 79, 'label': '顺承', 'to': 94}, {'from': 81, 'label': '顺承', 'to': 82},
             {'from': 98, 'label': '顺承', 'to': 84}, {'from': 85, 'label': '顺承', 'to': 86},
             {'from': 92, 'label': '顺承', 'to': 88}, {'from': 91, 'label': '顺承', 'to': 90},
             {'from': 91, 'label': '顺承', 'to': 92}, {'from': 93, 'label': '顺承', 'to': 94},
             {'from': 97, 'label': '顺承', 'to': 96}, {'from': 97, 'label': '顺承', 'to': 98},
             {'from': 99, 'label': '顺承', 'to': 100}];
    data={
        "nodes":nodes,
        "edges":edges
    }
    return data