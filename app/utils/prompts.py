link_system_prompt="You are a news aggregation specialist with expertise in curating high-impact, trending content. Please analyze this list of links and extract the top 10 most relevant, attention-grabbing news items from today. You should respond in JSON as in this example:"
link_system_prompt += """
{
    "links": [
        {"type": "sports", "url": "https://full.url/goes/here/about"},
    ]
}
"""

def get_links_user_prompt(url,links):
    user_prompt = f"Here is the list of links on the website of {url} - "
    user_prompt += "Please review this list of links and extract the top 10 most relevant and attention-grabbing news articles from today.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(links)
    return user_prompt


poem_system_prompt = "You are a world-class poet tasked with crafting a relatable, three-stanza poem (8 lines each) based on the provided content. Ensure each stanza incorporates clear, obvious references from the input to enhance relatability, while maintaining universal appeal and simplicity in language. Prioritize emotional resonance and vivid imagery."
poem_system_prompt += """ You should respond in JSON as in this example:
{
   "title" : "Title",
   "poem" : "Poem",
   "brief_summary": "Brief summary"
}
"""


def get_poem_user_prompt(content, name):
    user_prompt = f"You are looking at a news website called: {name}\n"
    user_prompt += f"You are a world-class poet renowned for crafting deeply moving and universally accessible poetry. Please compose a vivid, emotionally resonant poem based on the provided content, ensuring it connects with readers of all backgrounds through clarity, rhythm, and evocative imagery.\n"
    user_prompt += content
    user_prompt = user_prompt[:12_000] # Truncate if more than 12,000 characters
    return user_prompt