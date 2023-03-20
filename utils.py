import requests


def fetch_issues(orgName, repoName, startDate, TOKEN):
    """
    Fetches a list of closed issues from a GitHub repository.

    Args:
        orgName (str): The name of the GitHub organization.
        repoName (str): The name of the GitHub repository.
        startDate (datetime.date): The start date for filtering issues (issues closed after this date will be included).
        TOKEN (str): Your personal access token for authenticating with the GitHub API.

    Returns:
        A list of dictionaries representing the closed issues, with the following keys:
        - 'repo': The name of the repository.
        - 'title': The title of the issue.
        - 'body': The body text of the issue.
        - 'labels': A list of labels associated with the issue.

    Raises:
        requests.exceptions.HTTPError: If the API request fails.

    """
    # Set up the API endpoint
    api_url = f"https://api.github.com/repos/{orgName}/{repoName}/issues"

    # Set up the headers with your personal access token
    headers = {"Authorization": f"token {TOKEN}"}

    # Set up the query parameters
    params = {"state": "closed", "since": startDate.isoformat()}

    # Make the API request
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()

    # get rid of everything except title and body
    issues = [{'repo': repoName,
                'title': resp.get('title'), 
                'labels': [labl['name'] for labl in resp['labels']]} for resp in response.json()]

    return issues
