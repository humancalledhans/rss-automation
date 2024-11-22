def get_email_remix_system_prompt(format):
    return f"""
You are a finance expert that helps users understand the market. Please paraphrase the article attached below. It will be sent as an email to our email list.
Format it as an email. Don't use asterisks for punctuation.

Format: {format}
Return the result in JSON format.
"""


def get_email_remix_user_prompt(news_content_list, format):
    base_prompt = f"""
Please rephrase the content in an engaging and accessible way, focusing on how it impacts trading strategies and the broader financial outlook for the types of traders and investors listed below.

Provide only the subject and the email body, following the json format listed below:
{format}

Assume the sender’s name is TradeKlub.

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
