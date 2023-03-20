# InvestorsGPT
Automatize writing the tedious monthly investor update using the ChatGPT API and the GitHub API.

## Requirements
In order to use InvestorsGPT you need a valid GitHub [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) and a valid OpenAI [API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key).

## Usage
In order to use the script, first create a `.env` file in the root of the repository and place your `GITHUB_PA_TOKEN` and your `OPENAI_API_KEY` there. The file should look something like:

```
GITHUB_PA_TOKEN = "your_github_token"
OPENAI_API_KEY = "your_openai_key"
```

Once you have created and added your credentials to the `.env` file, make sure to modify the [`config.ini`](./config.ini) file with the `Organization` and `Repositories` you want to target for your update.

Now that you have everything setup, proceed to install the required dependencies:

```bash
pip install -r requirements.txt
```

Finally, run the script to get the update from InvestorsGPT:

```bash
python main.py
```

Example output:
```json
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Exein Platform\n- Enhancements to loading and graphics with live histograms and data tables for a more user-friendly experience\n- Improved functionality for monitoring ESP32 devices including better parsing and tooltips\n- Refined design for better visual appeal including clearer display of event and threat counters\n\nPulsar\n- Improvements for compatibility with different Linux security modules and higher kernel versions\n- New tools to improve cross-compiling and SSH target functionality\n- Enhancements to streaming monitoring, including ergonomic filtering and string representation of event_type field\n\nPulsar-Enterprise\n- Additional API endpoints and features for greater flexibility and customization of event and threat monitoring,\n    including pagination and limits\n- Improved agent and threat centre details for a clearer picture of system activity and security risks\n- Implementation of file system monitoring and optimized API endpoints for enhanced data handling and performance.",
        "role": "assistant"
      }
    }
  ],
  "created": 1679320542,
  "id": "chatcmpl-6wAH83dUzCRY4UIrhTgImfKHiLkII",
  "model": "gpt-3.5-turbo-0301",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 170,
    "prompt_tokens": 1987,
    "total_tokens": 2157
  }
}
```




