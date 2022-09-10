from random import randint
import yaml
import re
import email.message
import subprocess

from win32com.client import Dispatch

#tạo email để trả lời cho người điều khiển
def build_email_content(mail_from, mail_to, subject, content, format = 'html'):
    body = content['html']
    data = content['data']

    email_message = email.message.EmailMessage()
    email_message.add_header('To', ','.join(mail_to))
    email_message.add_header('From', mail_from)
    email_message.add_header('Subject', subject)
    email_message.add_header('X-Priority', '1')  
    email_message.set_content(body, format)

    if data is not None:
        #Đính kèm file image vào email
        email_message.add_attachment(data[1], maintype='image', subtype='png', filename=data[0])
        #Đính kèm file video vào email
        email_message.add_attachment(data[1], maintype='video', subtype='avi', filename=data[0])

    return email_message

#kiểm tra email có hợp lệ hay không
def mail_validate(mail):
    s = '^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(s, mail)

class text_format:
    HEADER = ['\033[95m', '']
    OKBLUE = ['\033[94m', '']
    OKCYAN = ['\033[96m', '']
    OKGREEN = ['\033[92m', '']
    WARNING = ['\033[93m', 'Warning: ']
    FAIL = ['\033[91m', 'Failed: ']
    ENDC = ['\033[0m', '']
    BOLD = ['\033[1m', '']
    UNDERLINE = ['\033[4m', '']
    NORMAL = ['','']
    DEBUG = ['\033[91m', '[DEBUG]: ']
    YELLOW = ['\033[93m', '']
    RED = ['\033[91m', '']
    EXCEPTION = ['\033[91m', '[Exception]: ']

#load dữ liệu config trong file .yaml
def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)
#lưu dữ liệu config vào file .yaml 
def save_config(config, file_Path):
    with open(file_Path, 'w') as fp:
        return yaml.dump(config, fp)
#Cập nhật giá trị config
def update_config_value(key, value, filename):
    yaml_dict = load_config(filename)
    
    yaml_dict[key] = value
    
    with open(filename, 'w') as f:
        yaml.dump(yaml_dict, f)
#lấy đường dẫn đến thư mục starup của người dùng hiện tại
def get_startup_path():
    cmd = '''echo %appdata%\Microsoft\Windows\Start Menu\Programs\Startup'''

    result = subprocess.check_output(cmd, shell=True)

    result = result.decode('utf-8')
    result = result.replace('\n', '')
    result = result.replace('\r', '')
    result = result.replace('"', '')

    return result

#tạo shortcut đến thư mục thực thi của ứng dụng và lưu nó vào thư mục startup của máy tính đang chạy ứng dụng đó.
def create_shortcut(path, runner, argument='', wDir='', icon=''):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = runner
    if argument != '':
        shortcut.Arguments  = argument
    shortcut.WorkingDirectory = wDir
    
    if icon == '':
        pass
    else:
        shortcut.IconLocation = icon
    
    shortcut.save()