
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_ai_response(messages):
    try:
        # cooking_instruction = {"role": "system", "content": "You are a knowledgeable cooking assistant. Provide helpful advice on recipes, cooking techniques, and ingredient information."}
        cooking_instruction = {"role": "system", "content": "You are CulinaryGenius, an AI cooking assistant. Answer the following question about cooking or food only.Provide helpful, accurate advice on recipes and ingredients. Consider nutrition, dietary restrictions, and global cuisines. Offer tips for beginners and advanced cooks alike. Suggest substitutions when relevant. Be friendly and encouraging. Include relevant links to YouTube videos or food blog posts that demonstrate corresponding recipe or provide additional information. Your goal is to inspire confidence and creativity in the kitchen while helping users create delicious, nutritious meals. any questions apart from this should not give answer"}
        messages.insert(0, cooking_instruction)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in OpenAI API call: {e}")
        return "I'm sorry, I couldn't process your cooking request at the moment."


