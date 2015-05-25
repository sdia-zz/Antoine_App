#!/usr/bin/env python
#-*- coding:utf-8 -*-


# How to merge file on server side using Python's Flask
# A demo for Antoine

# Copyright (C) 2015 Seydou Dia

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from flask import Flask, request, session, render_template


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
    app.debug = True # remove in prod.
    app.run()
