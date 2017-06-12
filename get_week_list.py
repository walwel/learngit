# coding=utf-8

from datetime import timedelta
from datetime import datetime

def get_week_list(d=datetime.now()):
    """
    d = datetime.now()
    return:['0602', '0603', '0604', '0605', '0606', '0607', '0608']
    """
    week_length = timedelta(days=-6)
    day_start = d + week_length
    start_day = day_start.strftime('%m,%d').split(',')
    end_day = d.strftime('%m,%d').split(',')
    e_end = int(end_day[1])
    s_start = int(start_day[1])
    if start_day[0] == end_day[0]:
        # 同一个月时
        day_list = [str(i) if len(str(i)) == 2 else '0'+str(i) for i in range(s_start, e_end+1)]
        return ['-'.join([start_day[0], i]) for i in day_list]
    else:
        # 两个月
        e_day_list = [str(i) if len(str(i)) == 2 else '0'+str(i) for i in range(1, e_end+1)]
        s_day_list = [str(i) if len(str(i)) == 2 else '0'+str(i) for i in range(s_start, s_start+(7-e_end))]
        week_list = ['-'.join([start_day[0], i]) for i in s_day_list] + ['-'.join([end_day[0], i]) for i in e_day_list]
        return week_list

if __name__ == "__main__":
    d=datetime.now()
    week_length = timedelta(days=-6)
    print get_week_list(d+week_length)