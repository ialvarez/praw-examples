import app_config_data

from flask import Flask, request
import praw

app = Flask(__name__)


@app.route('/')
def homepage():
    url = r.get_authorize_url(state='praw_examples',
                              scope='read,mysubreddits')
    return "<a href=%s>authorize</a>" % url


@app.route('/authorize_callback')
def authorized():
    code = request.args.get('code', '')
    r.get_access_information(code)

    subs = []
    recs = []
    already_rec = []

    template = "<li>" \
               "<a target='_blank' href='http://reddit.com/r/%s'>%s</a>" \
               "</li>"

    for sub in r.get_my_subreddits(limit=250):
        subs.append(template % (sub.display_name, sub.display_name))
        recommendations = r.get_subreddit_recommendations(sub.display_name)
        for rec in recommendations:
            if rec.display_name not in already_rec:
                recs.append(template % (rec.display_name, rec.display_name))
                already_rec.append(rec.display_name)

    html_code = "<h1>Thanks for waiting!</h1>" \
                "<h2>You are subscribed to %s subreddits</h2>" \
                "<ul>%s</ul>" \
                "<h2>You get recommended %s subreddits</h2>" \
                "<ul>%s</ul>" \
                "<a href='/'>Try again</a>" \
                % (len(subs), ''.join(subs), len(recs), ''.join(recs))

    return html_code


if __name__ == '__main__':
    r = praw.Reddit('praw-examples/hello_oauth')
    r.set_oauth_app_info(app_config_data.CLIENT_ID,
                         app_config_data.CLIENT_SECRET,
                         app_config_data.REDIRECT_URI)
    app.run(debug=True, port=65010)
