from flask import Flask, render_template, request, redirect, url_for
import bleach

app = Flask(__name__)

vulnerable_comments = []
sanitized_comments = []

ALLOWED_TAGS = ['b', 'i', 'u', 'em', 'strong', 'a', 'span']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username', 'Anonymous')
        comment = request.form.get('comment', '')

        vulnerable_comments.append({
            'username': username,
            'comment': comment
        })
        sanitized_comments.append({
            'username': username,
            'comment': bleach.clean(comment, tags=ALLOWED_TAGS)
        })
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        vulnerable_comments=vulnerable_comments,
        sanitized_comments=sanitized_comments
    )

if __name__ == '__main__':
    app.run(debug=True)