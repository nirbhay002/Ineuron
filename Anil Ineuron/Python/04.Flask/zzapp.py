#this is the latest video on API taught by Krishnaik but as most of the things as shown in the video is unable to run on PW lab
#So I am going to refer to previous year video of sudhanshu which is save test.py
# but I am not deleting this file, bcz maybe able to understand after watching Sudhanshu Video 

from flask import Flask,request,render_template

app=Flask(__name__)

## Routes

@app.route('/') #Home Route: Defines the route for the home page, accessible at the root URL (/).
def welcome():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return "We are ineuron"

@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=='division':
            result=num1/num2
        else:
            result=num1-num2

        return "The operation is {} and the result is {}".format(operation ,result)

@app.route('/operation',methods=['POST'])
def operation():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0

        if operation=="add":
            result=num1+num2
        elif operation=="multiply":
            result=num1*num2
        elif operation=='division':
            result=num1/num2
        else:
            result=num1-num2

        return render_template("result.html",result=result)
 


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000) #Starts the Flask web server on all available IP addresses (0.0.0.0) at port 5000.
    
    #As we are running it on PW Lab, so whenever we write 0.0.0.0, this will automatically map to the cloud IP address where this program is running
    #basically the localhost address is 127.0.0.1, Localhost is a hostname that refers to the current machine used to access it.
    #port basically specifies through which port, we have to access this application
    #bydefault flask runs on 5000 port

#As soon as you run this file, you will get following output:
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:5000    it is the local ip address
#  * Running on http://172.18.0.8:5000:  this ip is the ip of the specific cloud server where we are running it. we can not access the ip directly
#as we are running it on PW lab so this ip is mapped to the website url i.e. https://blue-pilot-akrim.pwskills.app and to access the we need to add
#the port no. as: https://blue-pilot-akrim.pwskills.app:5000
    

