from flask import Flask, request, redirect, render_template, jsonify
from flask_cors import CORS,cross_origin
from bs4 import BeautifulSoup
# from urllib.request import urlopen as uReq
# import logging
import requests
import pandas as pd
# logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

application = Flask(__name__)
app=application

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/get-reviews",methods = ['POST'])
def fetch_reviews(): 
    # print(request.form)
    try:
        reviews_all = []

        for page in range(1,int(request.form['page'])):
            query = f"&page={page}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
            url = request.form['url']+query
            # print(page)
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")
            # print(response,response.content)
            reviews=soup.find_all(attrs={"class":"t-ZTKy"})
            rating = soup.find_all(attrs={"class":"_3LWZlK _1BLPMq"})
            title = soup.find_all("p", attrs={"class":"_2-N8zT"})
            name_of_customer = soup.find_all("p",attrs={"class":"_2sc7ZR _2V5EHH"})
            for i in range(len(name_of_customer)):
                try:
                    reviews_all.append({
                        'customer_name':name_of_customer[i].text.strip(),
                        'title':title[i].text.strip(),
                        'review':reviews[i].text.strip(),
                        'rating':rating[i].text.strip()
                        
                                        })
                except Exception as e:
                    # logging.error(e)
                    continue
            
        df=pd.DataFrame(reviews_all)
        # print(df.head())
        df.to_csv('reviews.csv')
        return render_template('output.html',data=reviews_all)
    except Exception as e:
            # logging.info(e)
            return 'something is wrong'

@app.route('/view',methods=['GET'])
def view_for_review():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)