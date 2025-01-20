from flask import Flask,render_template
from views import views
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

@app.route("/")
def portfolio():
    categories = [
        {'id': 'all', 'label': 'Show all'},
        {'id': 'data-mining', 'label': 'Data mining'},
        {'id': 'dataviz', 'label': 'Dataviz'},
        {'id': 'scientific-paper', 'label': 'Scientific paper'},
        {'id': 'dashboard', 'label': 'Dashboard'},
        {'id': 'shiny', 'label': 'Shiny'},
    ]

    portfolio_items = [
        {
            "id": 1,
            "title": "Hexagonal Map Analysis",
            "category": "dataviz",
            "imageUrl": "https://your-image-url.com/image1.png",
        },
        {
            "id": 2,
            "title": "Dashboard Visualization",
            "category": "dashboard",
            "imageUrl": "https://your-image-url.com/image2.png",
        },
        # Add more items here
    ]

    active_filter = 'all'

    return render_template(
        'index.html',
        categories=categories,
        portfolio_items=portfolio_items,
        active_filter=active_filter,
    )
def home():
    return "This is the home page"

if __name__== '__main__':
    app.run(debug=True,port=5000)
