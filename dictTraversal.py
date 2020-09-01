# -*- coding: utf-8 -*-
# @Time : 2020/8/30 22:35
# @Author : KevinHoo
# @Site : 
# @File : dictTraversal.py
# @Software: PyCharm 
# @Email : hu.rui0530@gmail.com
rtnList = []
def get_dict_allkeys(key, dict_a): # 查询字典a中键值，并将键值放入字典b
    """
    多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
    :param key:
    :param dict_a:
    :return:
    """
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
        for x in range(len(dict_a)):
            temp_key = list(dict_a.keys())[x]
            temp_value = dict_a[temp_key]
            if temp_key == key:
                rtnList.append(temp_key + ':' + temp_value)
            get_dict_allkeys(key, rtnList)  # 自我调用实现无限遍历

    elif isinstance(dict_a, list):
        for k in dict_a:
            if isinstance(k, dict):
                for x in range(len(k)):
                    temp_key = list(k.keys())[x]
                    temp_value = k[temp_key]
                    if temp_key == key:
                        rtnList.append(temp_value)
                    get_dict_allkeys(key, rtnList)


if __name__ == '__main__':
    pass
