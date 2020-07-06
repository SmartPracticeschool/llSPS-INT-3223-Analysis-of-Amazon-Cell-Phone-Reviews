from flask import render_template, Flask, request,url_for
from keras.models import load_model
import pickle 
import tensorflow as tf
#global graph
from tensorflow.python.keras.backend import set_session
sess = tf.Session()
graph = tf.get_default_graph()
set_session(sess)
with open(r'CountVectorizer','rb') as file:
    cv=pickle.load(file)
cla = load_model('nlp.h5')
cla.compile(optimizer='adam',loss='binary_crossentropy')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def page2():
    if request.method == 'POST':
        json_data = request.get_json()
        topic = json_data['tweet']
        print("Hey " +topic)
        topic=cv.transform([topic])
        print("\n"+str(topic.shape)+"\n")
        global sess
        global graph
        global model
            
        with graph.as_default():
            set_session(sess)
            y_p1 = cla.predict(topic)
            print("pred is "+str(y_p1))
            topic = ''
            if(y_p1 > 0.5):
                topic = "Positive"
            elif(y_p1 < 0.5):
                topic = "Negative"
            return topic
        
if __name__ == '__main__':
    app.run(host = 'localhost', debug = True , threaded = False)
    
