from flask import request, Flask, abort, jsonify, send_from_directory
import os, json, requests
import notarize
import reviewer
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

PROOF_DIR = "proofs"
data_dir = os.path.dirname(os.path.realpath(__file__))
PROOF_DIR = os.path.join(data_dir, PROOF_DIR)
# this is a all in one function,
# generate a proof
# review the proof
# post the proof to a public ipfs gateway
@app.route('/foo', methods=['POST'])
def foo():
    if request.method == 'POST':
        args = request.json
        print("args:" + json.dumps(args))
        header = args.get("header")
        target = args.get('target')
        ok, filename = notarize.generate(target, header)
#        ok, content = review(target, header)
        if not ok:
            return filename, 400
        filepath = os.path.join(PROOF_DIR, filename)
        ok, report, html = reviewer.review(filepath)
        result = {
            "filename": filename,
            "report": report,
            "html": html.decode().encode("utf-8")
        }
        if ok:
            return json.dumps(result,ensure_ascii=False,encoding="utf-8"), 200
        else:
            return json.dumps(result), 400

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        args = request.json
        print("args:" + json.dumps(args))
        header = args.get("header")
        target = args.get('target')
        try:
            ok, prooffile = notarize.generate(target, header)
        except Exception as e:
            print(e)
            return "The cipher suites of this server are not supported", 500
        if ok:
            return prooffile, 200

    return result, 500

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    """Download a file."""
    return send_from_directory(PROOF_DIR, filename, as_attachment=True)


@app.route('/ipfs/<filename>', methods=['GET', 'POST'])
def ipfs(filename):
    with open(os.path.join(PROOF_DIR, filename)) as fp:
        content = fp.read()

    response = requests.post(
        'https://www.nondual.ga/peace/', data=content
    )
#    print("reponse:", repr(response.headers))
    full_location = response.headers["Location"]
    location = full_location[6:]
#    print("location:",location)
    url = "https://www.nondual.ga/peace/"+location
    return url, 200

@app.route('/upload', methods=['POST'])
def upload(filename):
    """Upload a file."""

    date = time_str = time.strftime('%d-%b-%Y-%H-%M-%S-', time.gmtime())
    session_id = ''.join(random.choice(string.ascii_lowercase+string.digits) for x in range(10))
    filename = date + session_id +".pgsg"
    with open(os.path.join(PROOF_DIR, filename), 'wb') as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return filename, 201

@app.route('/review/<filename>', methods=['GET', 'POST'])
def review(filename):
    filepath = os.path.join(PROOF_DIR, filename)
    ok, result, html = reviewer.review(filepath)
    if ok:
        return result, 200
    return result, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
