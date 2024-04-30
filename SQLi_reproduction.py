from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# 初始化並創建一個簡單的數據庫
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    conn.commit()
    conn.close()

init_db()

# 登錄頁面
@app.route('/')
def login():
    return '''
    <form action="/login" method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

# 處理登錄的路由
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    # 這裡包含了一個SQL注入漏洞
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    # 如果查詢返回結果，認為是有效的登錄
    if result:
        return "登錄成功!"
    else:
        return "登錄失敗!"

if __name__ == '__main__':
    app.run(debug=True)