import google.generativeai as genai
import pyttsx3

# Configure the API key
genai.configure(api_key="AIzaSyDOf1kda2pOrmZsNwp7usXbb8g655UZ8GA")

# Initialize text-to-speech engine for Raspberry Pi
engine = pyttsx3.init()
engine.setProperty('rate', 150) # Adjust speech rate
engine.setProperty('volume', 1.0) # Set volume to maximum

# Function to speak text
def speak(text):
engine.say(text)
engine.runAndWait()

# Choose the model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Function to interact with Google GenAI for storytelling
def ask_openai(prompt):
response = chat.send_message(prompt)
return response['text'].strip()

# Start the story by getting initial inputs
def start_story():
speak("Welcome to the AI Storytelling System for Children!")
speak("Where do you want the story to take place? For example, a jungle, outer space, or a magical land.")
setting = input("Where do you want the story to take place (e.g., jungle, outer space, magical land)?: ")
speak("Who should be the main character of the story? For example, a brave knight or a talking dog.")
main_character = input("Who should be the main character of the story (e.g., a brave knight, a talking dog)?: ")
speak("What should the main plot of the story be? For example, a quest to find treasure or saving a kingdom.")
plot = input("What should the main plot of the story be (e.g., a quest to find treasure, saving a kingdom)?: ")
initial_prompt = f"""Create a children's story set in {setting}, where the main character is {main_character}. The plot revolves around {plot}. Keep the story fun, interactive, and creative for a child."""
story_part = ask_openai(initial_prompt)
speak("Here's how the story begins.")
speak(story_part)
return {"setting": setting, "main_character": main_character, "plot": plot}

# Evolve the story with user inputs
def evolve_story(story_elements):
while True:
speak("How do you want the story to continue? You can add new characters, challenges, or events. Type 'end' to finish the story.")
user_input = input("How do you want the story to continue? You can add new characters, challenges, or events (or type 'end' to finish the story): ")
if user_input.lower() == "end":
speak("The story has come to an end. Hope you enjoyed it!")
break
evolve_prompt = f"""
Continue the story set in {story_elements['setting']}, with the main character {story_elements['main_character']}.
The plot revolves around {story_elements['plot']}.
Now, include the following idea from the user: {user_input}
Keep the tone fun and engaging for a child.
"""
story_part = ask_openai(evolve_prompt)
speak("The story continues.")
speak(story_part)

# Main function
def main():
# Start the story by getting initial inputs
story_elements = start_story()
# Evolve the story with real-time feedback
evolve_story(story_elements)

if __name__ == "__main__":
main()
