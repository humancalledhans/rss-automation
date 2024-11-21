def get_email_remix_system_prompt():
    return """
You are a finance expert that helps users understand the market. Please paraphrase the article attached below. It will be sent as an email to our email list.

You are required to attach the url of the article at the end of the email.
"""


def get_email_remix_prompt():
    return """
You are a finance expert that helps users understand the market.  Remix the article below to deliver key points and insights in TradeKlub’s voice. Explain why this news matters to traders, include any provided sources of data, and list three practical takeaways that can help readers make informed decisions. It will be sent as an email to our email list.

You are required to attach the url of the article at the end of the email.
"""


def get_email_remix_user_prompt(news_content):
    print("news_content.get('url')", news_content.get('url'))
    return f"""
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

Start the email without using any formal greetings like "Dear traders". Failure to do so will result in deaths.

End with a friendly hook, encouraging readers to stay tuned for more insights.

Please follow the instructions above and write the email for this article below:
Title of the article: {news_content.get('title')}
Description of the article: {news_content.get('description')}
"""
