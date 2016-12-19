# _*_ coding: utf-8 _*_
from z_db_sql import *
from z_db_conf import db_conf


def score_level_count():
    level_name = []
    level = [0 for i in range(10)]
    level_country = ["American", "UK", "Korea", "Japan", "China", "Other"]
    dict_level_country = {item: [0 for i in range(10)] for item in level_country}
    all_count = 0
    conn, cur = db_conf()
    cur.execute(SQL_LEVEL_OF_SCORE_COUNT)
    for name, score, country in cur.fetchall():
        all_count += 1
        if score >= 9.0:
            level[0] += 1
        elif score >= 8.0:
            level[1] += 1
        elif score >= 7.0:
            level[2] += 1
        elif score >= 6.0:
            level[3] += 1
        elif score >= 5.0:
            level[4] += 1
        elif score >= 4.0:
            level[5] += 1
        elif score >= 3.0:
            level[6] += 1
        elif score >= 2.0:
            level[7] += 1
        elif score >= 1.0:
            level[8] += 1
        else:
            level[9] += 1

        if "美国" in country:
            level_american = dict_level_country["American"]
            if score >= 9.0:
                level_american[0] += 1
            elif score >= 8.0:
                level_american[1] += 1
            elif score >= 7.0:
                level_american[2] += 1
            elif score >= 6.0:
                level_american[3] += 1
            elif score >= 5.0:
                level_american[4] += 1
            elif score >= 4.0:
                level_american[5] += 1
            elif score >= 3.0:
                level_american[6] += 1
            elif score >= 2.0:
                level_american[7] += 1
            elif score >= 1.0:
                level_american[8] += 1
            else:
                level_american[9] += 1
            dict_level_country["American"] = level_american
        if "英国" in country:
            level_uk = dict_level_country["UK"]
            if score >= 9.0:
                level_uk[0] += 1
            elif score >= 8.0:
                level_uk[1] += 1
            elif score >= 7.0:
                level_uk[2] += 1
            elif score >= 6.0:
                level_uk[3] += 1
            elif score >= 5.0:
                level_uk[4] += 1
            elif score >= 4.0:
                level_uk[5] += 1
            elif score >= 3.0:
                level_uk[6] += 1
            elif score >= 2.0:
                level_uk[7] += 1
            elif score >= 1.0:
                level_uk[8] += 1
            else:
                level_uk[9] += 1
            dict_level_country["UK"] = level_uk
        if "韩国" in country:
            level_korea = dict_level_country["Korea"]
            if score >= 9.0:
                level_korea[0] += 1
            elif score >= 8.0:
                level_korea[1] += 1
            elif score >= 7.0:
                level_korea[2] += 1
            elif score >= 6.0:
                level_korea[3] += 1
            elif score >= 5.0:
                level_korea[4] += 1
            elif score >= 4.0:
                level_korea[5] += 1
            elif score >= 3.0:
                level_korea[6] += 1
            elif score >= 2.0:
                level_korea[7] += 1
            elif score >= 1.0:
                level_korea[8] += 1
            else:
                level_korea[9] += 1
            dict_level_country["Korea"] = level_korea
        if "日本" in country:
            level_japan = dict_level_country["Japan"]
            if score >= 9.0:
                level_japan[0] += 1
            elif score >= 8.0:
                level_japan[1] += 1
            elif score >= 7.0:
                level_japan[2] += 1
            elif score >= 6.0:
                level_japan[3] += 1
            elif score >= 5.0:
                level_japan[4] += 1
            elif score >= 4.0:
                level_japan[5] += 1
            elif score >= 3.0:
                level_japan[6] += 1
            elif score >= 2.0:
                level_japan[7] += 1
            elif score >= 1.0:
                level_japan[8] += 1
            else:
                level_japan[9] += 1
            dict_level_country["Japan"] = level_japan
        if ("中国" in country) or ("中国大陆" in country) or ("香港" in country) or ("台湾" in country) or ("内地" in country):
            level_china = dict_level_country["China"]
            if score >= 9.0:
                level_china[0] += 1
            elif score >= 8.0:
                level_china[1] += 1
            elif score >= 7.0:
                level_china[2] += 1
            elif score >= 6.0:
                level_china[3] += 1
            elif score >= 5.0:
                level_china[4] += 1
            elif score >= 4.0:
                level_china[5] += 1
            elif score >= 3.0:
                level_china[6] += 1
            elif score >= 2.0:
                level_china[7] += 1
            elif score >= 1.0:
                level_china[8] += 1
            else:
                level_china[9] += 1
            dict_level_country["China"] = level_china
    for i in range(10):
        level_name.append(str(9-i) + "+")
    print("级别名称: ", level_name)
    print("各级别数量：", level)
    print("各国情况：", dict_level_country)

if __name__ == '__main__':
    score_level_count()
