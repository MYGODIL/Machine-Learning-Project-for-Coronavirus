from flask import Flask,render_template , request
app = Flask(__name__)
import pickle

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        MyDict=request.form
        fever=int(MyDict['fever'])
        bodypain=int(MyDict['pain'])
        age=int(MyDict['age'])
        RUNNYNOSE=int(MyDict['RUNNYNOSE'])
        difficultyinbreathing=int(MyDict['difficulty in breathing'])


        InputFeatures=[fever,bodypain,age,RUNNYNOSE,difficultyinbreathing]
        InfProb = clf.predict_proba([InputFeatures])[0][1]
        print(InfProb)
        return render_template('show.html', inf = InfProb)
    return render_template('index.html')
    #return 'Hello, World!' + str(InfProb)
    



if __name__ == "__main__":
    app.run(debug=True)    