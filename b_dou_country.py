# _*_ coding: utf-8 _*_

from z_db_conf import *
from z_db_sql import *


def year_2016_coutry():
    level_country = ["中国", "美国", "日本", "英国",
                     "法国", "韩国", "德国", "意大利",
                     "印度", "泰国", "西班牙", "加拿大",
                     "澳大利亚", "俄罗斯", "伊朗", "爱尔兰",
                     "瑞典", "巴西", "丹麦", "波兰",
                     "捷克", "阿根廷", "比利时", "墨西哥",
                     "新西兰", "荷兰", "奥地利", "土耳其",
                     "匈牙利", "以色列"]
    dict_level_country = {item: [0 for i in range(6)] for item in level_country}
    dict_score_country = {item: [0 for i in range(5)] for item in level_country}
    try:
        conn, cur = db_conf()
        cur.execute(SQL_COUNT_OF_COUNTRY)
        for name, score, country in cur.fetchall():
            if ("中国" in country) or ("中国大陆" in country) or ("香港" in country) or ("台湾" in country) or ("内地" in country):
                dict_level_country["中国"][0] += 1
                dict_level_country["中国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["中国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["中国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["中国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["中国"][5] += 1 if 0 > score else 0
            if "美国" in country:
                dict_level_country["美国"][0] += 1
                dict_level_country["美国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["美国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["美国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["美国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["美国"][5] += 1 if 0 > score else 0
            if "日本" in country:
                dict_level_country["日本"][0] += 1
                dict_level_country["日本"][1] += 1 if score >= 8.5 else 0
                dict_level_country["日本"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["日本"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["日本"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["日本"][5] += 1 if 0 > score else 0

            if "英国" in country:
                dict_level_country["英国"][0] += 1
                dict_level_country["英国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["英国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["英国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["英国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["英国"][5] += 1 if 0 > score else 0

            if "法国" in country:
                dict_level_country["法国"][0] += 1
                dict_level_country["法国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["法国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["法国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["法国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["法国"][5] += 1 if 0 > score else 0
            if "韩国" in country:
                dict_level_country["韩国"][0] += 1
                dict_level_country["韩国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["韩国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["韩国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["韩国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["韩国"][5] += 1 if 0 > score else 0
            if "德国" in country:
                dict_level_country["德国"][0] += 1
                dict_level_country["德国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["德国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["德国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["德国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["德国"][5] += 1 if 0 > score else 0
            if "意大利" in country:
                dict_level_country["意大利"][0] += 1
                dict_level_country["意大利"][1] += 1 if score >= 8.5 else 0
                dict_level_country["意大利"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["意大利"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["意大利"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["意大利"][5] += 1 if 0 > score else 0

            if "印度" in country:
                dict_level_country["印度"][0] += 1
                dict_level_country["印度"][1] += 1 if score >= 8.5 else 0
                dict_level_country["印度"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["印度"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["印度"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["印度"][5] += 1 if 0 > score else 0
            if "泰国" in country:
                dict_level_country["泰国"][0] += 1
                dict_level_country["泰国"][1] += 1 if score >= 8.5 else 0
                dict_level_country["泰国"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["泰国"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["泰国"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["泰国"][5] += 1 if 0 > score else 0
            if "西班牙" in country:
                dict_level_country["西班牙"][0] += 1
                dict_level_country["西班牙"][1] += 1 if score >= 8.5 else 0
                dict_level_country["西班牙"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["西班牙"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["西班牙"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["西班牙"][5] += 1 if 0 > score else 0
            if "加拿大" in country:
                dict_level_country["加拿大"][0] += 1
                dict_level_country["加拿大"][1] += 1 if score >= 8.5 else 0
                dict_level_country["加拿大"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["加拿大"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["加拿大"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["加拿大"][5] += 1 if 0 > score else 0

            if "澳大利亚" in country:
                dict_level_country["澳大利亚"][0] += 1
                dict_level_country["澳大利亚"][1] += 1 if score >= 8.5 else 0
                dict_level_country["澳大利亚"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["澳大利亚"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["澳大利亚"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["澳大利亚"][5] += 1 if 0 > score else 0
            if "俄罗斯" in country:
                dict_level_country["俄罗斯"][0] += 1
                dict_level_country["俄罗斯"][1] += 1 if score >= 8.5 else 0
                dict_level_country["俄罗斯"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["俄罗斯"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["俄罗斯"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["俄罗斯"][5] += 1 if 0 > score else 0
            if "伊朗" in country:
                dict_level_country["伊朗"][0] += 1
                dict_level_country["伊朗"][1] += 1 if score >= 8.5 else 0
                dict_level_country["伊朗"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["伊朗"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["伊朗"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["伊朗"][5] += 1 if 0 > score else 0
            if "爱尔兰" in country:
                dict_level_country["爱尔兰"][0] += 1
                dict_level_country["爱尔兰"][1] += 1 if score >= 8.5 else 0
                dict_level_country["爱尔兰"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["爱尔兰"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["爱尔兰"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["爱尔兰"][5] += 1 if 0 > score else 0

            if "瑞典" in country:
                dict_level_country["瑞典"][0] += 1
                dict_level_country["瑞典"][1] += 1 if score >= 8.5 else 0
                dict_level_country["瑞典"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["瑞典"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["瑞典"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["瑞典"][5] += 1 if 0 > score else 0
            if "巴西" in country:
                dict_level_country["巴西"][0] += 1
                dict_level_country["巴西"][1] += 1 if score >= 8.5 else 0
                dict_level_country["巴西"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["巴西"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["巴西"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["巴西"][5] += 1 if 0 > score else 0
            if "丹麦" in country:
                dict_level_country["丹麦"][0] += 1
                dict_level_country["丹麦"][1] += 1 if score >= 8.5 else 0
                dict_level_country["丹麦"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["丹麦"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["丹麦"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["丹麦"][5] += 1 if 0 > score else 0
            if "波兰" in country:
                dict_level_country["波兰"][0] += 1
                dict_level_country["波兰"][1] += 1 if score >= 8.5 else 0
                dict_level_country["波兰"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["波兰"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["波兰"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["波兰"][5] += 1 if 0 > score else 0

            if "捷克" in country:
                dict_level_country["捷克"][0] += 1
                dict_level_country["捷克"][1] += 1 if score >= 8.5 else 0
                dict_level_country["捷克"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["捷克"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["捷克"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["捷克"][5] += 1 if 0 > score else 0
            if "阿根廷" in country:
                dict_level_country["阿根廷"][0] += 1
                dict_level_country["阿根廷"][1] += 1 if score >= 8.5 else 0
                dict_level_country["阿根廷"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["阿根廷"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["阿根廷"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["阿根廷"][5] += 1 if 0 > score else 0
            if "比利时" in country:
                dict_level_country["比利时"][0] += 1
                dict_level_country["比利时"][1] += 1 if score >= 8.5 else 0
                dict_level_country["比利时"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["比利时"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["比利时"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["比利时"][5] += 1 if 0 > score else 0
            if "墨西哥" in country:
                dict_level_country["墨西哥"][0] += 1
                dict_level_country["墨西哥"][1] += 1 if score >= 8.5 else 0
                dict_level_country["墨西哥"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["墨西哥"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["墨西哥"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["墨西哥"][5] += 1 if 0 > score else 0

            if "新西兰" in country:
                dict_level_country["新西兰"][0] += 1
                dict_level_country["新西兰"][1] += 1 if score >= 8.5 else 0
                dict_level_country["新西兰"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["新西兰"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["新西兰"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["新西兰"][5] += 1 if 0 > score else 0
            if "荷兰" in country:
                dict_level_country["荷兰"][0] += 1
                dict_level_country["荷兰"][1] += 1 if score >= 8.5 else 0
                dict_level_country["荷兰"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["荷兰"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["荷兰"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["荷兰"][5] += 1 if 0 > score else 0
            if "奥地利" in country:
                dict_level_country["奥地利"][0] += 1
                dict_level_country["奥地利"][1] += 1 if score >= 8.5 else 0
                dict_level_country["奥地利"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["奥地利"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["奥地利"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["奥地利"][5] += 1 if 0 > score else 0
            if "土耳其" in country:
                dict_level_country["土耳其"][0] += 1
                dict_level_country["土耳其"][1] += 1 if score >= 8.5 else 0
                dict_level_country["土耳其"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["土耳其"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["土耳其"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["土耳其"][5] += 1 if 0 > score else 0

            if "匈牙利" in country:
                dict_level_country["匈牙利"][0] += 1
                dict_level_country["匈牙利"][1] += 1 if score >= 8.5 else 0
                dict_level_country["匈牙利"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["匈牙利"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["匈牙利"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["匈牙利"][5] += 1 if 0 > score else 0
            if "以色列" in country:
                dict_level_country["以色列"][0] += 1
                dict_level_country["以色列"][1] += 1 if score >= 8.5 else 0
                dict_level_country["以色列"][2] += 1 if (8.5 > score) and (score >= 7) else 0
                dict_level_country["以色列"][3] += 1 if (7 > score) and (score >= 5.5) else 0
                dict_level_country["以色列"][4] += 1 if (5.5 > score) and (score >= 0) else 0
                dict_level_country["以色列"][5] += 1 if 0 > score else 0

        for key in dict_level_country:
            dict_score_country[key] = dict_level_country[key][1:]
        print(dict_level_country)
        print(dict_score_country)

    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    year_2016_coutry()
