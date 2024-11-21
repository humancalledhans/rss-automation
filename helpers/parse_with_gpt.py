
import asyncio
import random
from dotenv import load_dotenv
from openai import OpenAI
import openai
import os

# from get_prompt import get_email_remix_user_prompt
# from get_prompt import get_email_remix_system_prompt


def get_email_remix_system_prompt():
    return """
You are a finance expert that helps users understand the market. Please paraphrase the article attached below. It will be sent as an email to our email list.
Format it as an email. Don't use asterisks for punctuation.
"""


def get_email_remix_user_prompt(news_content_list):
    base_prompt = f"""
Please rephrase the content in an engaging and accessible way, focusing on how it impacts trading strategies and the broader financial outlook for the types of traders and investors listed below.

Provide only the email body. Assume the sender’s name is TradeKlub.

TradeKlub Money Clips Email Format:
Remix of Title to Make It Engaging
Start with a hook on why this topic is timely and relevant for traders.
Summarize the article’s main points with any cited sources of data, translating technical terms into digestible concepts with relatable analogies to millennials.
Briefly explain how this news impacts trading decisions and market outlook, adding TradeKlub’s unique perspective.

Offer one real world practical suggestion that traders can use to apply this information effectively:
For Day Traders:
For Swing Traders:
For Position Traders:
For Long Term Investment:

Start the email without using any formal greetings like "Dear traders" and "Subject". Failure to do so will result in deaths.

End with a friendly hook, encouraging readers to stay tuned for more insights.

Below, there may be multiple articles to remix. Please remix all article into one email, so that users are up to date with the latest market trends.
"""

    # Iterate over each article and add its details to the prompt
    for index, news_content in enumerate(news_content_list, start=1):
        base_prompt += f"""

Article {index}:
Title of the article: {news_content.get('title')}
Description of the article: {news_content.get('description')}
"""

    return base_prompt


def append_read_more(final_response, news_content):

    options = ['Read the full article for more insights: ', 'For more details, read the full article: ',
               'To learn more, read the full article: ', 'To learn more, read the full article here: ']
    return final_response + "\n\n" + random.choice(options) + news_content.get('url')


# Load environment variables from a .env file
load_dotenv()

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


async def parse_with_chatgpt(news_content_list):
    client = OpenAI()

    """Parse news content using ChatGPT with system and user prompts."""
    try:

        response = await asyncio.wait_for(
            asyncio.to_thread(
                client.chat.completions.create,
                model="gpt-4o",
                # response_format={"type": "json_object"},
                messages=[
                    {"role": "system",
                     "content": get_email_remix_system_prompt()},
                    {"role": "user", "content": get_email_remix_user_prompt(
                        news_content_list)}
                ],
                temperature=0.9,
            ),
            timeout=90
        )

        print("Response from ChatGPT:", response)

        # Extract the content from the response
        parsed_content = response.choices[0].message.content
        return parsed_content
    except Exception as e:
        print("Error parsing with ChatGPT:", e)
        return None  # Fallback in case of an error


if __name__ == '__main__':
    # Define the sample news content
    news_content = {
        "title": "Rest of World’s Markets Broken By Trump’s America-First Plan",
        "description": """Worries around overheating stocks took over the narrative on Tuesday, underscoring the sense of froth in risky parts of the market that had surged after President-elect Donald Trump’s decisive election victory.

A number of trades that took flight since last week faltered before key US inflation data to be released Wednesday. Small-cap stocks — which tend to be more sensitive to economic conditions than their larger peers — fell from near an all-time high. Equities with a large concentration of bearish bets also sank, as did unprofitable technology shares. Bitcoin briefly dropped from a record before resuming gains, and the stock of Elon Musk-led Tesla Inc. slumped from the highest in more than two years.""",
        "url": "https://www.bloomberg.com/news/articles/2024-11-13/riskiest-stocks-at-frothy-levels-show-trump-trade-vulnerability?srnd=phx-markets",
        "pubDate": "2024-11-20T10:30:00Z",
        "author": "Author Name",
        "content": "Full content of the news article goes here."
    }

    # Run the async function
    parsed_content = asyncio.run(parse_with_chatgpt(news_content))
    # parsed_content = append_read_more(parsed_content, news_content)
    print("Parsed Content:", parsed_content)
