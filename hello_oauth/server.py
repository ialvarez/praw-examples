from flask import Flask, request
import praw
import app_config_data

app = Flask(__name__)


@app.route('/')
def homepage():
    link = r.auth.url(['identity'], '...', 'permanent')
    text = "<a href='{}'>LINK</a>".format(link)
    return text


@app.route('/authorize_callback')
def authorized():
    code = request.args.get('code', '')
    r.auth.authorize(code)
    user = r.user.me()
    text = 'You are %s and have %u link karma.' % (user.name,
                                                   user.link_karma)
    back_link = "<a href='/'>Try again</a>"
    return text + '</br></br>' + back_link

if __name__ == '__main__':
    r = praw.Reddit(user_agent='praw-examples/hello_oauth',
                    client_id=app_config_data.CLIENT_ID,
                    client_secret=app_config_data.CLIENT_SECRET,
                    redirect_uri=app_config_data.REDIRECT_URI)
    app.run(debug=True, port=65010)
