# 模拟推理
# coding=utf-8
import threading
import time
from enum import Enum
from EnAndCh import sql
from ComputeRel import get_scene, get_taishi
from jsapp.utils.DataBase import DataBase
COOR_ = 0  # 协同度阈值
DAMAGE_ = 0.8  # 毁伤阈值

_, data = sql("select * from AddEntityChEng")
en_ch = {d['en']: d['ch'] for d in data}


class Solution:
    def __init__(self, time_):
        # 态势信息  字典形式
        self.scene = get_scene(time_)
        self.coordination_dic_H = None
        self.coordination_dic_L = None
        self.threaten_dic = None
        self.COOR = None
        self.DAMAGE = None
        self.state = None
        self.A = None
        self.A_coors = None
        self.D = None

    def run(self):
        self.coordination_dic_H, self.coordination_dic_L, self.threaten_dic = get_taishi(self.scene)

        self.COOR = COOR_  # 协同度阈值
        self.DAMAGE = DAMAGE_  # 毁伤阈值
        self.state = self.init_state()
        self.A = self.get_most_threaten()  # 对蓝方实体l_ent威胁最大的红方实体A
        self.A_coors = self.get_coordination()  # 得到与A协同度达到阈值COOR_的实体
        self.D = self.choose_attack()  # 选出用于攻击红方实体的蓝方实体
        # self.assess_info = self.pre_assess()

    def update(self, last_state):
        """
        通过上一个状态更新当前时刻的一些信息
        :param last_state:
        :return:
        """
        H = last_state.scene["H"]
        for key, value in H.items():
            self.scene['H'][key]['PH'] = value['PH']
            self.scene['H'][key]['status'] = value['status']
        L = last_state.scene["L"]
        for key, value in L.items():
            self.scene['L'][key]['PH'] = value['PH']
            self.scene['L'][key]['status'] = value['status']

    def init_state(self):
        """
        事件链
        :return:
        """
        class State(Enum):
            qf = 0
            bscd = 1
            ddzdqy = 2
            fxmb = 3
            kh = 4
            qh = 5
            hh = 6
            fh = 7
        return State

    def if_fxmb(self):
        return True

    def next_order(self, ent_uid):
        next_order = None
        try:
            cur_state = self.scene['H'][ent_uid]['status']
        except:
            cur_state = self.scene['L'][ent_uid]['status']

        try:
            ent_info = self.scene['L'][ent_uid]
        except:
            ent_info = self.scene['H'][ent_uid]

        fxmb = self.if_fxmb()

        if cur_state == self.state.qf:  # 起飞状态下根据实体的任务类型判断
            if ent_info['mission'] == "护航":
                next_order = self.state.bscd
            else:  # 打击
                next_order = self.state.ddzdqy
        elif cur_state == self.state.bscd:  # 伴随出动状态下根据态势信息判断是否发现目标
            if fxmb:
                next_order = self.state.kh
            else:
                next_order = self.state.fh
        elif cur_state == self.state.ddzdqy:
            if ent_info['mission'] == "护航":
                next_order = self.state.fh
            else:
                next_order = self.state.kh
        elif cur_state == self.state.fxmb:
            next_order = self.state.kh
        elif cur_state == self.state.kh:
            if ent_info['mission'] == "护航":
                next_order = self.state.ddzdqy
            else:
                next_order = self.state.fh
        elif cur_state == self.state.qh:
            if ent_info['mission'] == "护航":
                next_order = self.state.hh
            else:
                next_order = self.state.ddzdqy
        elif cur_state == self.state.hh:
            if fxmb:
                next_order = self.state.fxmb
            else:
                next_order = self.state.ddzdqy
        else:  # 返航 损毁
            pass
        return next_order

    def get_most_threaten(self):
        """
        得到红方对蓝方实体l_ent威胁最大的实体A
        :return:
        """
        max_t = 0
        h_ent = None
        for key, value in self.threaten_dic.items():
            tmp = 0
            for v in value:
                tmp += v[1]
            if tmp > max_t:
                max_t = tmp
                h_ent = key
        return h_ent

    def get_coordination(self):
        """
        得到与A协同度达到阈值的实体
        :return:
        """
        try:
            tmp = self.coordination_dic_H[self.A]
            res = [t for t in tmp if t[1] >= self.COOR]
            res = sorted(res, key=lambda x: x[1], reverse=True)
            res = [r[0] for r in res]
        except:
            res = [self.A]
        return res

    def choose_attack(self):
        """
        选出用于攻击红方实体的蓝方实体
        :return:
        """
        l_ent = None
        l_ents = self.scene["L"]
        h_icon_type = self.scene['H'][self.A]['Icontype']
        if h_icon_type == 'AIRCRAFT':
            max_pok_air = 0
            for key, value in l_ents.items():
                if value['AirPoK'] > max_pok_air:
                    max_pok_air = value['AirPoK']
                    l_ent = value['uID']
        else:  # 'MINE_SWEEPER'
            max_pok_sur = 0
            for key, value in l_ents.items():
                if value['AirPoK'] > max_pok_sur:
                    max_pok_sur = value['AirPoK']
                    l_ent = value['uID']
        return l_ent

    def pre_assess(self):
        """
        预评估打击任务完成情况,根据预评估结果决定派遣多少
        :return:
        """
        target_status = self.scene['H'][self.A_coors[0]]['PH']
        icontype = self.scene['H'][self.A_coors[0]]['Icontype']
        if icontype == 'AIRCRAFT':
            damage = self.scene['L'][self.D]['AirPoK']
        else:
            damage = self.scene['L'][self.D]['SurfacePoK']
        i = 0
        while i * damage <= target_status:
            i += 1
        return i

    def get_ent_info(self):
        """
        得到实体的图谱信息与应该下达的指令
        :return:
        """
        order = ""
        A = self.scene['H'][self.A]
        B = self.scene['H'][self.A_coors[0]]
        D = self.scene['L'][self.D]
        num = self.pre_assess()
        if self.A == self.A_coors[0]:
            order += "暂为发现与" + A['PlantName'] + "协同的实体！"
        else:
            order += "与" + A['PlantName'] + "协同性最强的为" + B['PlantName']
        order += "指定" + D['PlantName'] + "*" + str(num) + " 打击 " + A['PlantName']

        # 根据事件链更新实体的状态
        for key, _ in self.scene['L'].items():
            self.next_order(key)
        for key, _ in self.scene['H'].items():
            self.next_order(key)

        # 更改涉及到实体的属性  B self.scene['H'][self.A_coors[0]] 指向同一个地址
        B['PH'] = 0.0
        B['status'] = "损毁"
        D['PH'] /= 2
        return A, B, D, order


def nodes_edges_entity(ent):
    ns = []
    root = {'group': 'entity', 'id': 0, 'label': en_ch[ent['PlantName']]}
    ns.append(root)
    root = {'group': 'entity', 'id': 1, 'label': ent['Lat']}
    ns.append(root)
    root = {'group': 'entity', 'id': 2, 'label': ent['LandPoK']}
    ns.append(root)
    root = {'group': 'entity', 'id': 3, 'label': ent['SurfacePoK']}
    ns.append(root)
    root = {'group': 'entity', 'id': 4, 'label': ent['AirPoK']}
    ns.append(root)

    es = []
    e = {'from': 0, 'label': 'attribute', 'to': 1}
    es.append(e)
    e = {'from': 0, 'label': 'LandPoK', 'to': 2}
    es.append(e)
    e = {'from': 0, 'label': 'SurfacePoK', 'to': 3}
    es.append(e)
    e = {'from': 0, 'label': 'AirPoK', 'to': 4}
    es.append(e)
    return ns, es


def nodes_edges_relation(s):

    ns = []
    es = []

    def helper(uid):
        for node in ns:
            tmp = node['label'].split('|')[0]
            if tmp == uid:
                return node['id']
    n = 0
    coor_H, coor_L, thr = s.coordination_dic_H, s.coordination_dic_L, s.threaten_dic
    ents = s.scene
    for _, ent in ents['H'].items():
        root = {'group': 'entity', 'id': n, 'label': ent['uID']+'|'+ent['PlantName']}
        ns.append(root)
        n += 1
    for _, ent in ents['L'].items():
        root = {'group': 'entity', 'id': n, 'label': ent['uID']+'|'+ent['PlantName']}
        ns.append(root)
        n += 1

    for key, value in coor_H.items():
        f = helper(ents['H'][key]['uID'])
        for v in value:
            t = helper(ents['H'][v[0]]['uID'])
            edge = {'from': f, 'label': '协同'+str(v[1])[:3], 'to': t}
            es.append(edge)
    for key, value in coor_L.items():
        f = helper(ents['L'][key]['uID'])
        for v in value:
            t = helper(ents['L'][v[0]]['uID'])
            edge = {'from': f, 'label': '协同'+str(v[1])[:3], 'to': t}
            es.append(edge)

    for key, value in thr.items():
        f = helper(ents['H'][key]['uID'])
        for v in value:
            t = helper(ents['L'][v[0]]['uID'])
            edge = {'from': f, 'label': '威胁' + str(v[1])[:3], 'to': t}
            es.append(edge)
    return ns, es


if __name__ == '__main__':

    # 初始化剧本信息
    s0 = Solution(0)
    s0.run()
    info = s0.get_ent_info()
    rel = nodes_edges_relation(s0)
    ent_a = nodes_edges_entity(info[0])
    ent_b = nodes_edges_entity(info[1])
    ent_d = nodes_edges_entity(info[2])
    order = info[3]
    time.sleep(2)

    # 初始化剧本信息
    s1 = Solution(1)
    s1.update(s0)
    s1.run()
    rel = nodes_edges_relation(s1)
    info = s1.get_ent_info()  # A,B,D,order
    ent_a = nodes_edges_entity(info[0])
    ent_b = nodes_edges_entity(info[1])
    ent_d = nodes_edges_entity(info[2])
    order = info[3]
    time.sleep(2)

    # s2 = Solution(2)
    # info = s2.get_ent_info()
    # ent_a = nodes_edges(info[0])
    # ent_b = nodes_edges(info[1])
    # ent_d = nodes_edges(info[2])
    # order = info[3]
    # time.sleep(2)

    # s3 = Solution(3)
    # info = s3.get_ent_info()
    # ent_a = nodes_edges(info[0])
    # ent_b = nodes_edges(info[1])
    # ent_d = nodes_edges(info[2])
    # order = info[3]
    # time.sleep(2)



