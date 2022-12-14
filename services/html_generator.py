
import os

# Tạo html table cho những yêu cầu xem dữ liệu dưới dạng danh sách


def html_table(dataframe, note='', format='center'):
    # dataframe: là một python dictionnary với 3 trường type, columns và data.
    # type: xác định kiểu bảng dòng đơn hay gồm nhiều nhóm.
    # columns: tên những cột trong bảng
    # data: mảng các dòng dữ liệu.
    # note: ghi chú đi kèm với bảng, kiểu chuỗi
    # format: canh lề các ô trong văn bản, kiểu chuỗi
    html = ''

    if note:
        html += f'<p><span style="font-weight: bold;">Note: </span>{note}</p>'

    n_col = len(dataframe['columns'])
    columns = dataframe['columns']

    data = dataframe['data']
    type = dataframe['type']

    html += f'<table class="{format}">'

    html += '<tr class="first-row">'
    for column in columns:
        html += f'<th>{column}</th>'
    html += '</tr>'

    if type == 'single':
        n_row = len(dataframe['data'])

        for i in range(n_row):
            html += '<tr class="'
            if i % 2 == 1:
                html += 'odd-row '
            if i == n_row - 1:
                html += 'last-row '
            html += '">'

            for j in range(n_col):
                html += f'<td>{data[i][j]}</td>'
            html += '</tr>'

    elif type == 'group':
        n_group = len(data)

        for i in range(n_group):
            group_name = data[i][0]
            group_data = data[i][1]
            n_row = len(group_data)

            # Dòng đầu tiên
            html += '<tr class="'
            if i % 2 == 1:
                html += 'odd-row '
            if i == n_group - 1 and 0 == n_row - 1:
                html += 'last-row '
            html += '">'
            # Loại
            html += f'<td rowspan="{n_row}" style="font-weight: bold;">{group_name}</td>'
            for k in range(n_col - 1):
                html += f'<td>{group_data[0][k]}</td>'
            html += '</tr>'

            # Những dòng dữ liệu tiếp theo
            for j in range(1, n_row):
                html += '<tr class="'
                if i % 2 == 1:
                    html += 'odd-row '
                if i == n_group - 1 and j == n_row - 1:
                    html += 'last-row '
                html += '">'

                for k in range(n_col - 1):
                    html += f'<td>{group_data[j][k]}</td>'
                html += '</tr>'

    return html

# tạo ra html text để trả lời cho người điều khiển dưới dạng văn bản


def html_msg(msg, status=None, bold_all=False):
    content = msg
    _class = ''

    if bold_all:
        _class += 'bold '
    if status is not None:
        if not status:
            content += ' Please try again later.'
        _class += ('ok' if status else 'error')

    html = f'<p lang="en" class="message {_class}">{content}</p>'
    return html

# Tạo ra mã html ở dạng ASCII để phục vụ cho thao tác duyệt xem cây thư mục.


def html_tree(path, sub_dirs):
    path = path if path else 'this device'

    path = path.replace('\\', '/')

    if os.path.isdir(path):
        path += '/'

    html = f'<p>The directory tree for <span style="font-weight: bold;">{path}</span> (1 - level):</p>'

    ascii_tree = path if path else 'This device/'

    if len(sub_dirs) > 0:
        for i in range(len(sub_dirs)):
            name = sub_dirs[i]
            if os.path.isdir(os.path.join(path, name)):
                name = name + '/'

            chars = '├──' if i < len(sub_dirs) - 1 else '└──'
            ascii_tree += '\n' + chars + ' ' + name

    html += f'<p class="ascii">{ascii_tree}</p>'

    return html

# tạo ra html đầy đủ để trả lời cho người điều khiển
# request: Lệnh điều khiển
# content: nội dung được tạo ra từ các hàm khác để trả lời lệnh


def html_mail(request, content):
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <style>
            * {
                box-sizing: border-box;
            }

            html {
                font-family: 'Roboto', sans-serif;
            }
            
            p, td, th, span, ul {
                color: #333;
                font-size: 16px;
            }

            .main {
                margin: 0 auto;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 6px 30px 30px 30px;
                width: 700px;
                background: #fff8ed;
            }

            .app__name {
                text-align: center;
                font-size: 24px;
                color: #54bded;
                font-weight: bold;
            }

            .app__greeting
            {
                text-align: right;
                font-style: italic;
            }

            .app__desc {
                text-align: center;
            }

            .divider {
                border-bottom: 1px solid #ccc;
                margin: 20px 0;
            }

            .request {
                font-weight: bold;
                word-break: break-all;
            }

            /* CSS for tables */
            table {
                /* width: 100%; */
                margin: 0 auto;
                border-collapse: collapse;
                overflow: hidden;
                border: outset;
            }

            table td, table th {
                font-size: 14px;
            }

            table.left {
                text-align: left;
            }

            table.center {
                text-align: center;
            }

            td,
            th {
                border-top: 1px solid #c6cccde6;
                padding: 10px 14px;
            }

            th {
                background-color: #54bded;
                border-left: 1px solid #c6cbcd;
                border-right: 1px solid #c6cbcd;
                color: white;
            }

            td {
                border-left: 1px solid #c6cbcd;
                border-right: 1px solid #c6cbcd;
            }
            
            tr.first-row {
                text-align: center;
            }

            tr.last-row {
                border-bottom: 1px solid #c6cccde6;
            }

            tr.odd-row td {
                background-color: #ffedfd;
            }


            /* CSS for message */
            .message {
                margin: 0;
            }

            .message.bold {
                font-weight: bold;
            }

            .message.ok {
                color: #1e9d95;
            }

            .message.error {
                color: red;
            }

            .ascii {
                font-family: 'Courier New', monospace;
                font-size: 16px;
                margin: 0;
                margin-left: 40px;
                white-space: pre-wrap;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class='main'>
            <div class="container">
                <p class="app__name">Remote Control Computer with Email Service</p>
                <p class="app__greeting">Greeting from 21HCB - HCMUS</p>
                <p class="app__greeting">21424028 - 21424031 - 21424057</p>
                <div class='divider'></div>
            </div>
            <div class="container">
                <p>This mail responses to the request: <span class="request" lang="en">''' + request + '''</span></p>
            </div>
    '''

    html_template += f'''
        <section>
            {content}
        </section>
        </div>
        </body>
    </html>
    '''

    return html_template
