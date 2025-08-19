import sys, json, io, contextlib

def handler(request):
    code = request.query.get("code")
    if not code:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No code provided"})
        }
    try:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exec(code, {})
        output = buffer.getvalue().strip()
        return {
            "statusCode": 200,
            "body": json.dumps({"output": output})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
