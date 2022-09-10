import psutil
import os
from .html_generator import html_table, html_msg

#Liệt kê process đang chạy
def __process_df():
    result = {
        'status': 'OK',
        'type': 'single',
        'columns': ['No.', 'Description', 'Id', 'ThreadCount'],
        'data': []
    }

    data = []
    cnt = 0
    for process in psutil.process_iter():
        try:
            cnt += 1
            data.append([cnt, process.name(), str(process.pid), process.num_threads()])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            cnt -= 1
            pass
    
    result['data'] = data

    return result

#Lấy kết quả trả về từ hàm __process_df
def get_processes():
    dataframe = __process_df()
    response = {
        'html': html_table(dataframe, format='center'),
        'data': None
    }
    return response

#Đóng process đang chạy và trả về trạng thái cũng như thông báo
def __closing(id):
    data = __process_df()
    exist = False
    for row in data['data']:
        if row[2] == id:
            exist = True
            break

    if not exist:
        return False, 'There is no process with pID ' + id + ' running on this device.'

    # Close the process
    try:
        p = psutil.Process(int(id))
        p.terminate()
        return True, 'The process with pID ' + id + ' is closed.'
    except:
        return False, 'There is an error when closing the process with pID ' + id + '.'

#Lấy kết quả trả về từ hàm __closing
def close_process(id):
    status, msg = __closing(id)
    response = {
        'html': html_msg(msg, status, bold_all=True),
        'data': None
    }
    return response
