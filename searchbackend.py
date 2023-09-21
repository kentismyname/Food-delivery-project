from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data: List of dictionaries containing page content and food keywords
pages = [
    {"content": "Discover the best pizza places in town.", "keywords": ["pizza", "food"]},
    {"content": "Burgers that will leave you craving for more.", "keywords": ["burgers", "fast food"]},
    {"content": "Explore a variety of cuisines and dishes.", "keywords": ["cuisine", "food"]},
    # Add more pages here
]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing 'q' parameter"}), 400
    
    results = []
    for page in pages:
        if any(query.lower() in keyword.lower() for keyword in page['keywords']):
            results.append(page['content'])
    
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
