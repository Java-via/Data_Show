# _*_ coding: utf-8 _*_

from z_db_conf import db_conf
from z_db_sql import SQL_WORLD_LOW_GENRE


def get_low_genre():
    dict_genre_count = {}
    dict_genre_score = {}
    conn, cur = db_conf()
    cur.execute(SQL_WORLD_LOW_GENRE)
    for item in cur.fetchall():
        for genre in item[0].split("/"):
            this_genre = genre.strip()
            if this_genre not in dict_genre_count:
                dict_genre_count[this_genre] = 1
                dict_genre_score[this_genre] = item[1]
            else:
                dict_genre_count[this_genre] += 1
                dict_genre_score[this_genre] += item[1]
    for key in dict_genre_count:
        if dict_genre_count[key] > 5:
            print(key, ":", dict_genre_count[key], ":", dict_genre_score[key]/dict_genre_count[key])


if __name__ == '__main__':
    get_low_genre()
