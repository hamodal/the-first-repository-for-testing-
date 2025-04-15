from flask  Flask, render_template, request, redirect, url_for

#app = Flask(__name__)


USER_CREDENTIALS = {"admin": "password123"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return f"مرحبًا، {username}! تسجيل دخول ناجح ✅"
        else:
            return "❌ اسم المستخدم أو كلمة المرور غير صحيحة."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تسجيل الدخول</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="d-flex justify-content-center align-items-center vh-100 bg-light">

    <div class="card p-4 shadow-lg" style="width: 350px;">
        <h3 class="text-center">تسجيل الدخول</h3>
        <form method="POST">
            <div class="mb-3">
                <label for="username" class="form-label">اسم المستخدم</label>
                <input type="text" id="username" name="username" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">كلمة المرور</label>
                <input type="password" id="password" name="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary w-100">تسجيل الدخول</button>
        </form>
    </div>

</body>
</html>
