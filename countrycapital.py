from flask import Flask,jsonify
app= Flask(__name__)



file=open("./country.txt","r")
d={}
for line in file:
	x=line.split(",")
	a=x[0]
	b=x[1]
	c=len(b)-1
	b=b[0:c]
	d[a]=b


@app.route('/<country>')


def home(country):
	flag =0 	
	for k,v in d.items():
		if(country==k):
			country=k
			capital=v
			flag=1
	#print(d) 
	if flag==1:
		 return jsonify(country +":"+ capital)
	else:
		#abort(400)
		return("invalid country name given")
		
app.run(port=5000)
