from flask import Flask, render_template
app = Flask(__name__)


def read_rb():
	dynamodb = boto3.resource('dynamodb',region_name='us-east-1',endpoint_url="https://dynamodb.us-east-1.amazonaws.com")
    table = dynamodb.Table('Open_Account')
    response = table.get_item(
        Key={
            'Identifier': '001'       
        }
    )
    return jsonify(response = response['Item'])

@app.route("/")
def main():
	open_table = read_db()
    return render_template('index.html',people = open_table)
    
if __name__ == "__main__":
    app.run()

