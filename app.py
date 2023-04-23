from datetime import datetime
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    """
    Render the index.html template
    """
    return render_template('index.html')


@app.route('/fetch', methods=['POST'])
def fetch():
    """
    Fetch the 100 most rated public repositories for a GitHub user and render the output.html template with the data
    """
    # Get the GitHub username from the form data
    github_username = request.form['username']

    # Make a request to the GitHub API to get the 100 most rated public repositories for the given username
    response = requests.get(
        f"https://api.github.com/users/{github_username}/repos?sort=stars&per_page=100"
    )

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Convert the response data to JSON format
        data = response.json()

        # Create a list to store the repository data
        repos_data = []

        # Loop through each repository in the response data
        for repo in data:
            # Extract the repository data we want
            name = repo["name"]
            stars = repo["stargazers_count"]
            forks = repo["forks_count"]
            language = repo["language"]
            created_date = datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()

            # Add the repository data to the list
            repos_data.append((name, stars, forks, language, created_date))

        # Render the output.html template with the repository data
        return render_template('output.html', repos_data=repos_data)

    # If the response is not successful, return an error message
    return f"Error: {response.status_code} - {response.json()['message']}"


if __name__ == '__main__':
    app.run(debug=True)
