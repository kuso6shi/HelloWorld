from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

INDEX_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>GitHub Master Service</title>
</head>
<body>
    <h1>GitHub Master Service</h1>
    <p>GitHub の学習用サービスへようこそ。</p>
    <form method="post" action="/repos">
        <label for="token">Personal Access Token:</label>
        <input type="password" name="token" id="token" required>
        <button type="submit">リポジトリ取得</button>
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(INDEX_HTML)

@app.route("/repos", methods=["POST"])
def list_repos():
    token = request.form.get("token")
    headers = {"Authorization": f"token {token}"}
    response = requests.get("https://api.github.com/user/repos", headers=headers)
    if response.status_code == 200:
        repos = [repo["full_name"] for repo in response.json()]
    else:
        repos = ["リポジトリを取得できませんでした"]
    return "<br>".join(repos)

if __name__ == "__main__":
    app.run(debug=True)
