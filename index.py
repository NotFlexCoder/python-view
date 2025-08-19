from flask import Flask, request, Response
import io, contextlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def run_code():
    code = request.args.get("code")
    if request.method == "POST" and not code:
        code = request.data.decode("utf-8")

    if not code:
        return Response("No code provided", mimetype="text/plain", status=400)

    try:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exec(code, {})
        output = buffer.getvalue()
        return Response(output, mimetype="text/plain")
    except Exception as e:
        return Response(str(e), mimetype="text/plain", status=500)
