# _*_ coding: utf-8 _*_

# 获取各分数段电影数量
SQL_LEVEL_OF_SCORE_COUNT = "SELECT m_name, m_score, m_country " \
                           "FROM tb_doudou WHERE m_score>0 AND CAST(m_comment AS signed)>1000;"

# 各国2016年电影电视剧产量
SQL_COUNT_OF_COUNTRY = "SELECT m_name, m_score, m_country FROM tb_doudou WHERE LOCATE('2016', m_year)>0;"

# 各年度高分占比
SQL_COUNT_OF_YEAR = "SELECT m_year, m_score FROM tb_doumovies " \
                    "WHERE m_year != '' AND m_ismovie=1 "\
                    "AND CAST(m_comment AS signed)>100000;"

# 中国电影产量变化
SQL_COUNT_CHINA_OF_YEAR = "SELECT m_year, m_score FROM tb_doudou WHERE m_year != '' " \
                          "AND (LOCATE('中国', m_country)>0 OR LOCATE('香港', m_country)>0 " \
                          "OR LOCATE('台湾', m_country)>0 OR LOCATE('内地', m_country)>0) " \
                          "AND CAST(m_comment AS signed)>1000;"

# 美国电影产量变化
SQL_COUNT_AMERICAN_OF_YEAR = "SELECT m_year, m_score FROM tb_doudou WHERE m_year != '' " \
                          "AND LOCATE('美国', m_country)>0 AND CAST(m_comment AS signed)>1000;"


# 低分电影类别
SQL_WORLD_LOW_GENRE = "SELECT m_screenwriter, m_score, m_name FROM tb_doumovies " \
                      "WHERE m_year!='' AND m_ismovie=1 AND m_comment>100000;"


# 获取文件列表
SQL_FILE_LIST = "SELECT f_name, f_showname FROM tb_file ORDER BY f_uploaddate DESC;"
