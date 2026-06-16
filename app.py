from flask import Flask, render_template, request

app = Flask(__name__)

# ----------------------------
# TEMPORARY RECOMMENDATION FUNCTION
# (we will replace this with your ML model later)
# ----------------------------
def recommend(movie):
    return [
        "Avengers: Endgame",
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Titanic"
    ]

# ----------------------------
# HOME PAGE ROUTE
# ----------------------------
@app.route('/')
def home():
    return render_template('index.html')

# ----------------------------
# RECOMMENDATION ROUTE
# ----------------------------
@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie = request.form['movie']   # get input from user
    results = recommend(movie)      # get recommendations

    return render_template(
        'index.html',
        recommendation=results,
        movie=movie
    )

# ----------------------------
# RUN APP
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")