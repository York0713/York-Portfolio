import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 定義照片清單
    photo_configs = [
        {"folder": "1", "cat": "filter-app", "count": 20},      
        {"folder": "2", "cat": "filter-web", "count": 20},    
        {"folder": "3", "cat": "filter-card", "count": 20}, 
        {"folder": "4", "cat": "filter-do", "count": 20}
        ]
    
    # 組合出照片路徑與分類的清單
    all_photos = []
    for config in photo_configs:
        for i in range(1, config["count"] + 1):
            all_photos.append({
                "url": f"static/img/portfolio/{config['folder']}/pic-{i}.jpg",
                "filter": config["cat"],
                "id": f"{config['folder']}-{i}"
            })
            
    return render_template('index.html', photos=all_photos)

if __name__ == "__main__":
    #存取網站
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)