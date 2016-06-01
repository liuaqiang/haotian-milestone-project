from flask import Flask, render_template, request, redirect
import requests
from bokeh.plotting import figure
from bokeh.embed import components
#from bokeh.resources import INLINE
#from bokeh.util.string import encode_utf8
import numpy as np
import pandas as pd

app = Flask(__name__)
app.vars = {}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        app.vars['ticker']  = request.form['ticker']
        #features = request.form.getlist('features')
        #return ticker
        return redirect('/graph')
    else:
        return render_template('index.html')

@app.route('/graph')
def graph():
    ticker = app.vars['ticker']
    head_title = "Stock Data for " + ticker
    page_title = "Generated Graph for " + ticker
    
    # obtaining data through API
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/' + ticker + '.json'
    session = requests.Session()
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    raw_data = session.get(api_url)
    json_data = raw_data.json()
    
    # json_data.keys() # display keys of concern
    # [value for key,value in json_data.items() if key not in ['data']] # understand the structure of the data
    plot_data = { key:value for key, value in json_data.items() if key in ['column_names', 'data'] }
    plot_data = pd.DataFrame(plot_data['data'],columns = plot_data['column_names'])
    plot_data['Date'] = pd.to_datetime(plot_data['Date'])
    
    plot = figure(title = "~ Data from Quandle WIKI set ~", x_axis_label='date', x_axis_type='datetime')
    plot.line(plot_data['Date'], plot_data['Open'], line_width=2, legend = "Opening Price")
    
    #js_resources = INLINE.render_js()
    #css_resources = INLINE.render_css()
    
    script, div = components(plot)#, INLINE)
    
    return render_template('graph.html', script=script, div=div, head_title = head_title, page_title = page_title)

if __name__ == '__main__':
  app.run(host = '0.0.0.0')
