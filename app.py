from flask import Flask, render_template, request
import paramiko

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    output = ""
    if request.method == "POST":
        host = request.form.get("host")
        port = request.form.get("port") 
        username = request.form.get("username") 
        password = request.form.get("password") 
        command = request.form.get("command") 
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host,port=port,username=username,password=password)
        _stdin, _stdout, _stderr = client.exec_command(command)
        output = _stdout.read().decode() + _stderr.read().decode()
        client.close()
    return render_template("index.html",output=output)

if __name__ == "__main__":
    app.run(debug=True)