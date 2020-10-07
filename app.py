# -*- coding: utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def render_main():
    output = render_template('index.html')
    return output

@app.route('/goals/<goal>/')
def render_goals(goal):
    output = render_template('goals.html', goal=goal)
    return output

@app.route('/profiles/<id>/')
def render_profiles(id):
    output = render_template('profiles.html', id=id)
    return output

@app.route('/request/')
def render_request():
    output = render_template('request.html')
    return output

@app.route('/request_done/')
def render_request_done():
    output = render_template('request_done.html')
    return output

@app.route('/booking/<id>/<week_day>/<time>/')
def render_booking(id, week_day, time):
    output = render_template('booking.html', id=id, week_day=week_day, time=time)
    return output

@app.route('/booking_done/')
def render_booking_done():
    output = render_template('booking_done.html')
    return output


if __name__ == '__main__':
    app.run()