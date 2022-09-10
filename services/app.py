import os
from .html_generator import html_table, html_msg

#hàm private liệt kê danh sách app 
def __app_df():
    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    ps_result = os.popen(cmd).read().split('\n')
    
    result = {
        'status': 'OK',
        'type': 'single',
        'columns': ['No.', 'Description', 'Id', 'ThreadCount'],
        'data': []
    }

    data = []
    cnt = 0
    try:
        for line in ps_result[3:]:
            if line.isspace() or len(line) == 0:
                continue

            arr = line.split(" ")

            # thread count
            thread_count = arr[-1]

            # id
            pos = len(arr) - 2
            for i in range(pos, -1, -1):
                if len(arr[i]) != 0:
                    id = arr[i]
                    pos = i
                    break

            name = ''
            for i in range(0, pos):
                if len(arr[i]) != 0:
                    name = name + arr[i] + ' '
            name = name[:-1]

            if len(name) == 0:
                continue

            cnt += 1
            data.append([cnt, name, id, thread_count])
    except:
        result['status'] = 'ERROR'

    result['data'] = data

    return result

#Trả về danh sách app từ hàm __app_df
def get_apps():
    dataframe = __app_df()
    response = {
        'html': html_table(dataframe, format='center'),
        'data': None
    }
    return response

#kill ứng dụng với pID và trả về trạng thái
def __closing(id):
    data = __app_df()
    exist = False
    for row in data['data']:
        if row[2] == id:
            exist = True
            break

    if not exist:
        return False, 'There is no app with pID ' + id + ' running on this device.'

    #Lệnh đóng ứng dụng
    try:
        cmd = 'powershell "gps | where {$_.mainWindowTitle} | where {$_.ID -eq ' + id + '} | select ID | kill"'
        ps_result = os.popen(cmd).read().split('\n')
        return True, 'The app with pID ' + id + ' is closed.'
    except:
        return False, 'There is an error when closing the app with pID ' + id + '.'

#Gọi đến hàm __closing để lấy kết quả trả về
def close_app(id):
    print('App to be closed:', id)
    
    status, msg = __closing(id)
    response = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }
    return response
