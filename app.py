from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    password = request.args.get('password')
    if password:
        if password == "72935":
            return "Goed gedaan! De stormen van huis C zijn Joost, Joris en Alex"
        else:
            return "Helaas, dit was niet goed!"
    else:
        return "Please provide a password"


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)
