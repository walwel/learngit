# coding=utf-8
from calendar import monthrange
from datetime import timedelta
from datetime import datetime


def get_md_list(start_date, end_date):
    """
    start,end格式为'2017-06-03'，'2017-06-08'
    return:['06-03', '06-04', '06-05', '06-06', '06-07', '06-08']
    """
    if start_date > end_date:
        return 'error date'
    s_date = start_date.split('-')
    e_date = end_date.split('-')
    s_0, s_1, s_2 = [int(i) for i in s_date]
    e_0, e_1, e_2 = [int(i) for i in e_date]
    if (s_0 == e_0) and (s_1 == e_1):
        # 同一月
        e_1_str = str(e_1) if len(str(e_1))==2 else '0'+str(e_1)
        day_list = [str(i) if len(str(i))==2 else '0'+str(i) for i in range(s_2, e_2+1)]
        return ['-'.join([e_1_str, i]) for i in day_list]
    else:
        # 不同月,月份相邻时
        _, s_length = monthrange(s_0, s_1) # 该月天数
        s_1_str = str(s_1) if len(str(s_1))==2 else '0'+str(s_1)
        e_1_str = str(e_1) if len(str(e_1))==2 else '0'+str(e_1)
        s_day_list = [str(i) if len(str(i))==2 else '0'+str(i) for i in range(s_2, s_length+1)]
        d_day_list = [str(i) if len(str(i))==2 else '0'+str(i) for i in range(1, e_2)]
        return ['-'.join([s_1_str, i]) for i in s_day_list]+['-'.join([e_1_str, i]) for i in d_day_list]
if __name__ == "__main__":
    print get_md_list('2016-12-03', '2017-01-29')