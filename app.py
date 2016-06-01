from flask import Flask, render_template, request, redirect
import requests
from bokeh.plotting import figure
from bokeh.embed import components
#from bokeh.resources import INLINE
#from bokeh.util.string import encode_utf8
import numpy as np

app = Flask(__name__)
app.vars = {}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index', methods = ['get', 'post'])
def index():
    return redirect('http://google.com')
    #ticker = request.form['ticker']
    #features = request.form.getlist('features')
    #return ticker
    #return redirect('/graph')
    #if request.method == 'post':
        #ticker  = request.form['ticker']
        #features = request.form.getlist('features')
        #return ticker
        #return redirect('/graph')
    #else:
        #return render_template('index.html')
#ticker = 'GOOG'
@app.route('/graph')
def graph():
    head_title = "Stock Data for GOOG"
    page_title = "Generated Graph for GOOG"
    
    x = np.random.random(10)
    y = np.random.random(10)
    
    plot = figure(title = "~ Data from Quandle WIKI set ~")
    plot.line(x, y, line_width=2)
    
    #js_resources = INLINE.render_js()
    #css_resources = INLINE.render_css()
    
    script, div = components(plot)#, INLINE)
    
    return render_template('graph.html', script=script, div=div, head_title = head_title, page_title = page_title)
    #return redirect('http://google.com')

# ticker = 'GOOG'

# @app.route('/plot-'+ ticker,methods=['POST'])
# def next_app():  #remember the function name does not need to match the URL
#     return redirect('graph.html',)

# # obtaining data through API
# api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/' + ticker + '.json'
# session = requests.Session()
# session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
# raw_data = session.get(api_url)
# json_data = raw_data.json()
# # json_data.keys() # display keys of concern
# # [value for key,value in json_data.items() if key not in ['data']]
# plot_data = { key:value for key, value in json_data.items() if key in ['column_names', 'data'] }
# # Use plot_data for plotting



# Plotting
# plot = figure(tools=TOOLS,
#               title='Data from Quandle WIKI set',
#               x_axis_label='date',
#               x_axis_type='datetime')
# script, div = components(plot)

if __name__ == '__main__':
  app.run(host = '0.0.0.0')
