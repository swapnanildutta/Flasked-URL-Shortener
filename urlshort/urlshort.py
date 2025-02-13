from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort', __name__)

@bp.route('/')
def home():
    return render_template('home.html', codes=session.keys())

@bp.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls ={}
        #Extracts file contents
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        #Check for conflicts
        if request.form['code'] in urls.keys():
            flash('That short name is already taken, please choose another name.')
            return redirect(url_for('urlshort.home'))

        #Check if url is given
        if 'url' in request.form.keys():
            urls[request.form['code']] = { 'url' : request.form['url']}
        #Check if file is given
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/home/swapnanildutta/Desktop/d/Flasked-URL-Shortener/urlshort/static/user_files/' + full_name)
            urls[request.form['code']] = { 'file' : full_name }

        #Append all contents to JSON Directory
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
            session[request.form['code']] = True
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('urlshort.home'))

#Access shortened content
@bp.route('/<string:code>')
def redirect_to_url(code):
    #Check if file exists
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                #Check if URL
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                #Check if file
                else:
                     return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    #Error handling
    return abort(404)

@bp.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@bp.route('/api')
def session_api():
    return jsonify(list(session.keys()))