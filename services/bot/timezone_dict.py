from datetime import datetime

timezone_id_vs_sending_time = {
    1: ['23', 0],
    2: ['22', 1],
    3: ['21', 2],
    4: ['20', 3],
    5: ['19', 4],
    6: ['18', 5],
    7: ['17', 6],
    8: ['16', 7],
    9: ['15', 8],
    10: ['14', 9],
    11: ['13', 10],
    12: ['12', 11],
    13: ['11', 12],
    14: ['10', -11],
    15: ['9', -10],
    16: ['8', -9],
    17: ['7', -8],
    18: ['6', -7],
    19: ['5', -6],
    20: ['4', -5],
    21: ['3', -4],
    22: ['2', -3],
    23: ['1', -2],
    24: ['0', -1],
}

now_time = str(int(datetime.now().strftime('%H')) + 1)
now_time_w_sec = datetime.now().strftime('%H:%M:%S')
print(now_time_w_sec)

# 0 23
# 1 22