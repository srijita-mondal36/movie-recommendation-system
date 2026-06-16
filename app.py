from flask import Flask, render_template, request

app = Flask(__name__)

def recommend(movie):
    return [
        "Avengers: Endgame",
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Titanic"
    ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie = request.form['movie']
    results = recommend(movie)
    return render_template('index.html', recommendation=results, movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
