from flask import Flask, render_template, request, jsonify, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.url

@app.route('/')
def home():
   return render_template('index.html')
   # return render_template('index.html')

@app.route('/url/get', methods=['GET'])
def api_get_url():
   url_receive = list(db.url.find({}, {"_id": False}))

   return jsonify(
      {'url_list': url_receive},
      {'result': 'success'}
   )

@app.route('/url/insert', methods=['POST'])
def api_insert_url():
   url_receive = request.form['url_give']
   url_info_receive = request.form['url_info_give']

   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
   }
   data = requests.get(url_receive, headers=headers)

   soup = BeautifulSoup(data.text, 'html.parser')

   og_image = soup.select_one('meta[property="og:image"]')['content']
   og_title = soup.select_one('meta[property="og:title"]')['content']
   og_description = soup.select_one('meta[property="og:description"]')['content']

   url = {
      'url': url_receive,
      'url_info': url_info_receive,
      'url_meta_image': og_image,
      'url_meta_title': og_title,
      'url_meta_desciption': og_description
   }

   db.url.insert_one(url)

   return jsonify({'result': 'success'})

@app.route('/url/delete', methods=['POST'])
def api_delete_url():
   url_receive = request.form['url_give']
   url_info_receive = request.form['url_info_give']

   db.url.delete_one( 
      {
      'url': url_receive,
      'url_info': url_info_receive
      }
      )

   return jsonify({'result': 'success'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

