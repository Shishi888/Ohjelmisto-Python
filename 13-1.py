from flask import Flask, jsonify

def onko_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    return jsonify({"Number": luku, "isPrime": onko_alkuluku(luku)})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
