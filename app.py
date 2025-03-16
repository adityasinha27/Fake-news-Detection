from flask import Flask, request, render_template
from markupsafe import escape  # Import escape from markupsafe
import pickle

vector = pickle.load(open("vectorized.pkl",'rb'))
model = pickle.load(open("finalized_model.pkl",'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news=str(request.form['news'])
        print (news)
        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html",prediction_text="News headline is -> {}".format(predict))
    else:
        return render_template("prediction.html")

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()