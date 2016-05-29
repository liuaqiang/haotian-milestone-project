from flask import Flask, render_template, request, redirect
import requests
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host = '0.0.0.0')

ticker = 'GOOG'

# obtaining data through API
api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/' + ticker + '.json'
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)


# Plotting
plot = figure(tools=TOOLS,
              title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')
script, div = components(plot)
return render_template('graph.html', script=script, div=div)