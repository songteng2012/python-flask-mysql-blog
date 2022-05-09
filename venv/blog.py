from flask import Flask,render_template,request,url_for,flash,redirect
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb.cursors

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maishu is fat agagin'

def get_db_conn():
    global conn1
    conn1 = pymysql.connect(host = 'localhost',port = 3306,user = 'root',password = 'yaoll100.',database = 'mysql',charset = 'utf8',cursorclass = MySQLdb.cursors.DictCursor)
    conn = conn1.cursor()
    return conn


def get_post(post_id):
    conn = get_db_conn()
    post = conn.execute('select * from posts where id = {} order by created DESC'.format(post_id))
    post =conn.fetchone()
    return post


@app.route('/')
def index():
    conn = get_db_conn()
    conn.execute('select * from posts')
    posts = conn.fetchall()
    return render_template('index.html',posts=posts)

@app.route('/posts/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html',post=post)


@app.route('/posts/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('标题不能为空!')
        elif not content:
            flash('内容不能为空')
        else:
            conn = get_db_conn()
            conn.execute('INSERT INTO posts(title,content) VALUES ("{}","{}")'.format(title,content))
            conn1.commit()
            conn1.close()
            return redirect(url_for('index'))

    return render_template('new.html')


@app.route('/posts/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    post = get_post(post_id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('标题不能为空!')
        elif not content:
            flash('内容不能为空')
        else:
            conn = get_db_conn()
            conn.execute('update posts SET title = "{}",content = "{}" WHERE id = {}'.format(title,content,post_id))
            conn1.commit()
            conn1.close()
            return redirect(url_for('index'))

    return render_template('edit.html',post=post)


@app.route('/posts/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    post = get_post(post_id)
    conn = get_db_conn()
    conn.execute('delete FROM posts WHERE id = {}'.format(post_id))
    conn1.commit()
    conn1.close()
    flash('"{}"删除成功！'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')