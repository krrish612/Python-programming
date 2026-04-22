# Emoji Converter
# Convert text to emoji or vice versa

emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😄",
    "<3": "❤️",
    ":)": "😴",
    ":O": "😮",
    ":P": "😜",
    ":*": "😗"
}

def convert_to_emoji(text):
    for key, emoji in emojis.items():
        text = text.replace(key, emoji)
    return text

def convert_to_text(text):
    for key, emoji in emojis.items():
        text = text.replace(emoji, key)
    return text

print("=== EMOJI CONVERTER ===")
print("1. Text to Emoji")
print("2. Emoji to Text")

choice = input("Choose: ")

if choice == "1":
    text = input("Enter text: ")
    print(convert_to_emoji(text))
elif choice == "2":
    text = input("Enter emoji text: ")
    print(convert_to_text(text))
else:
    print("Invalid choice!")