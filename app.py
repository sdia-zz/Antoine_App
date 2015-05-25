#!/usr/bin/env python
#-*- coding:utf-8 -*-


from flask import Flask, request, session, render_template


DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)


def merge(s, t):
    # example of merge
    m = s + t
    m = m.split()
    m.sort()
    return ' '.join(m)


def is_valid(s, t):

    # validation
    black_list = None, ''
    if s in black_list and t in black_list:
        return False

    return True
    
    

# home page
@app.route('/', methods=['GET', 'POST'])
def home():

    result = dict(
        text1 = '',
        text2 = '',
        text3 = '')

    if request.method == 'POST':

        # get data here
        text1 = request.form['text1']
        text2 = request.form['text2']

        # validate and clean
        if is_valid(text1, text2):
            # custom processing
            text3 = merge(text1, text2)
            result['text1'] = text1
            result['text2'] = text2
            result['text3'] = text3

        else: # not valid
            pass # best is to put error in result

    return render_template('home.html', result=result)

if __name__ == '__main__':

    app.debug = True # remove in prod
    app.run()
