import json 

from flask import Flask,request,jsonify

from my_parser import parse

app = Flask(__name__)

@app.route('/parse',methods = ['GET'])
def parsepage():
    query = request.args.get('query')
    if not query:
        return jsonify({'error':'вы не ввели запрос'})
    
    parsed_data = parse(query=query)
    
    with open('data.json', 'w',encoding='utf-8') as json_file:
        json.dump(parsed_data,json_file,ensure_ascii=False,indent=4,)

    

    return json.dumps(parsed_data,indent=4)
if __name__ == '__main__':
    app.run()

    
