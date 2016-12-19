# _*_ coding: utf-8 _*_

import decimal
from z_db_conf import db_conf
from z_db_sql import SQL_COUNT_AMERICAN_OF_YEAR


def high_score_for_years():
    dict_year_count = {}
    dict_year_rate = {}
    list_year = []
    list_rate = []
    list_count = []
    for i in range(1988, 2017):
        dict_year_count[str(i)] = [0 for i in range(3)]
        dict_year_rate[str(i)] = 0
    conn, cur = db_conf()
    cur.execute(SQL_COUNT_AMERICAN_OF_YEAR)
    for item in cur.fetchall():
        for key in dict_year_count:
            if key in item[0]:
                dict_year_count[key][0] += 1
                dict_year_count[key][1] += 1 if item[1] >= 9 else 0
                break

    for key in dict_year_count:
        dict_year_count[key][2] = dict_year_count[key][1]/dict_year_count[key][0]
        dict_year_rate[key] = dict_year_count[key][2]

    for key in sorted(dict_year_rate.keys()):
        list_year.append(key)
        list_count.append(dict_year_count[key][0])
        list_rate.append(float(decimal.Decimal((dict_year_rate[key] * 100)).quantize(decimal.Decimal('0.00'))))
    print(list_year)
    print(list_rate)
    print(list_count)
    return


if __name__ == '__main__':
    high_score_for_years()
