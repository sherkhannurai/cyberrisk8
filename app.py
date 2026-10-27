from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="kk">
<head>
    <meta charset="UTF-8">
    <title>Cyber Security Portal</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #121212; color: #e0e0e0; margin: 0; padding: 40px; }
        .container { max-width: 700px; margin: auto; background: #1e1e1e; padding: 25px; border-radius: 10px; border-top: 4px solid #00e676; }
        h1 { color: #00e676; }
        ul { line-height: 1.8; }
        li { margin-bottom: 10px; }
        .badge { background: #333; padding: 4px 8px; border-radius: 4px; color: #ff9800; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔐 Киберриск & Қауіпсіздік порталы</h1>
        <p>Кастомды веб-қосымша (Python / Flask)</p>
        <hr>
        <h3>Ақпараттық қауіпсіздік ережелері:</h3>
        <ul>
            <li><span class="badge">1-ереже</span> Күрделі құпия сөздерді және MFA қолданыңыз.</li>
            <li><span class="badge">2-ереже</span> Серверлерді Docker контейнерлерінде оқшаулаңыз.</li>
            <li><span class="badge">3-ереже</span> Деректер базасын тұрақты шифрлаңыз.</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
