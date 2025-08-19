from flask import Flask, request, jsonify
import io, contextlib

app = Flask(__name__)

@app.route("/api/run", methods=["GET"])
def run_code():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "No code provided"}), 400
    try:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exec(code, {})
        output = buffer.getvalue().strip()
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
