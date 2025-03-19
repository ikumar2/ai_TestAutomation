import asyncio
import os
import yaml
from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from src.agent.views import CheckoutResult

print(os.getcwd())
def load_config(filepath= "../config/config.yaml"):
    with open(filepath, "r") as file:
        return yaml.safe_load(file)

async def run_site_validation():
    config = load_config()
    os.environ['GEMINI_API_KEY'] = config['gemini_api_key']

    task = (
        'Important: I am UI automation tester validating the tasks'
        f'Open base Website {config["website_url"]}'
        'Login with username and password. login Detail available in the same page'
        'Get Attribute and url of the page'
        'After login, select first 2 products and add them to cart'
        'Then checkout and store the total value you see in screen'
        'Increase the quantity of any product and check if total value update accordingly'
        'check and select country, agree term and purchase'
        'verify thankyou message is displayed'
    )

    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-pro-exp-02-05', api_key=SecretStr(api_key))
    controller = Controller(output_model=CheckoutResult)
    agent = Agent(task, llm, controller=controller, use_vision=True)
    history = await agent.run()
    history.save_to_file('../data/agentresults.json')
    test_result = history.final_result()
    validate_result = CheckoutResult.model_validate_json(test_result)
    print(test_result)
    assert validate_result.confirmation_mesage == "Thank you! Your order will be delivered in next few weeks :-)."

if __name__ == "__main__":
    asyncio.run(run_site_validation())