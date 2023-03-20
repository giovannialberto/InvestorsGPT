import os
from dotenv import load_dotenv
import requests
import datetime
import openai
import configparser
from utils import fetch_issues


# Fetch the GitHub personal access token and OpenAI API key from the .env file 
load_dotenv()
GITHUB_PA_TOKEN = os.getenv('GITHUB_PA_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

# Fetch the organization and repositories you are interested in
config = configparser.ConfigParser()
config.read('config.ini')
repositories = [config['Repositories'][key] for key in config['Repositories']]
ORG = config['Organization']['ORG']

# Calculate the date 30 days ago
today = datetime.datetime.now()
thirty_days_ago = today - datetime.timedelta(days=30)

# get all the closed issues
issues = [issue for repoName in repositories for issue in fetch_issues(orgName=ORG, repoName=repoName, startDate=thirty_days_ago, TOKEN=GITHUB_PA_TOKEN)]

# set up prompts for chatGPT
system_description = """You are a product assistant tasked with writing reports about technical the Exein
                        product advancements for investors. You need to speak a clear language for a non-technical 
                        audience and you must focus on the most important advancements only."""

user_prompt = f"""These are all the issues that were successfully closed during the last month: '{str(issues)}'. 
                  Write an investors update report based on these. Make sure to summarise for a non-technical audience 
                  who is mainly interested in how the technical features being implemented can impact the business.
                  Write it in bullet points format and divide it into different sections for each of the underlying repositories.
                  Write at most 5 bullet points per section."""

# ask openai to write the report for you
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_description},
        {"role": "user", "content": user_prompt},
    ]    
)
print(response)