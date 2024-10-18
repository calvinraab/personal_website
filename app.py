from flask import Flask, render_template, send_from_directory, jsonify
import json
import os

app = Flask(__name__)

# Load blog posts from the JSON file
def load_blog_posts():
    with open('data/blog_posts.json') as f:
        return json.load(f)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the blog listing page
@app.route('/blog')
def blog():
    posts = load_blog_posts()
    return render_template('blog.html', posts=posts)


@app.route('/blog/<string:post_slug>')
def blog_post(post_slug):
    post_filename = f'{post_slug}.html'
    posts_dir = 'static/posts'

    # Check if the file exists in the correct directory
    if os.path.exists(os.path.join(posts_dir, post_filename)):
        return send_from_directory(posts_dir, post_filename)
    else:
        # Return 404 if the post is not found
        return "Post not found", 404

# Route to download the resume
@app.route('/resume')
def download_resume():
    return send_from_directory(directory='.', path='resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
