# Advanced Emoji Converter with Custom Emojis, Slack/Discord Format, and Categories

import re
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum

# ================== EMOJI CATEGORIES ==================
class EmojiCategory(Enum):
    FACES = "😊😃😄😁😆😅🤣😂🙂😉😋😎🤔😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹️🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱🥵🥶😳🤢😵😡🤬😷🤒🤕"
    GESTURES = "👋🤚🖐✋🖖👌🤌🤏✌️🤞🤟🤘🤙👈👉👆🖕👇☝️👍👎✊👊🤛🤜👏🙌👐🤲🤝🙏✍️💪🦾🦿"
    HEARTS = "❤️🧡💛💚💙💜🖤🤍🤎💔❣️💕💞💓💗💖💘💝"
    OBJECTS = "⌚📱📲💻⌨️🖥🖨️🖱🖲💽💾💿📀📼📷📸📹🎥📞☎️📟📠📺📻🎙🎚🎛🧭⏱⏲⏰🕰️💡🔦🕯️🪔🧯📔📕📖📗📘📙📚📓📒📑📐🖊🖋✏️🖌🖍📝✒️🖏📎🖇🔗📐🧮📏📍📎🖊📌📍✂️🖥💻🖱💽💾💿📀"
    WEATHER = "☀️🌤️⛅🌥️☁️🌦️🌧️⛈️🌩️🌨️❄️⛄🌬️💨🌪️🌈☂️☔⚡🌊"
    ANIMALS = "🐶🐱🐭🐹🐰🦊🐻🐼🐨🐯🦁🐮🐷🐸🐵🐔🐧🐦🐤🐣🐥🦆🦅🦉🦇🐺🐗🐴🦄🐝🪲🐜🦋🐌🐞🐜🪰🪲🦂🦟🪳🦗🐢🐍🦎🦖🦕🐙🐚🐠🐟🐡🐬🐳🦈🐊🐅🐆🦓🦍🦧🦣🐘🦛🦏🐪🐫🦒🦬🐃🐂🐄🫁🫀🦘🦬🐕🐩🐈🐈‍⬛🪶🐇🦫🦦🦥🐁🐀🐿️🦔"
    FRUITS = "🍏🍎🍐🍊🍋🍌🍉🍇🍓🫐🍈🍒🍑🥭🍍🥝🥑🍅🫒🥥🥝🍅"
    FOOD = "🍞🥐🥖🫓🥨🥯🧇🥞🧈🍳🥚🧀🥓🥪🍔🍟🍕🌭🥪🌮🌯🫔🥙🧆🍜🍝🍣🍱🍛🍤🍙🍚🍘🍥🥟🍱🍚"
    SYMBOLS = "❤️🧡💛💚💙💜🖤🤍🤎💔❤️‍🔥❤️‍⚧️⚧️♻️✅❌❓❔❕💯🔴🟠🟡🟢🔵🟣⚫️⚪🟤🔶🔷🔸🔹💠🌀💤🏁🚩🎌🛑⛔🚫💲➰➿🔚🔙🔛🔝✔️☑️🔘🔳▫️◻️◼️◽▫️◾⬛⬜💭🗯️💬🗯️🗨️"

# ================== CUSTOM EMOJI ==================
@dataclass
class CustomEmoji:
    """Custom emoji definition"""
    code: str
    emoji: str
    name: str
    description: str = ""

# ================== EMOJI CONVERTER ==================
class EmojiConverter:
    """Advanced emoji converter"""
    
    def __init__(self):
        # Default emoji mapping
        self.emojis: Dict[str, str] = {
            ":)": "😊",
            ":(": "😢",
            ":D": "😄",
            "<3": "❤️",
            ":O": "😮",
            ":P": "😜",
            ":*": "😗",
            ";)": "😉",
            "XD": "😎",
            ":'(": "😢",
            ":|": "😐",
            ">:(": "😠",
            "<:)": "🤔",
        }
        
        # Slack-style emojis
        self.slack_emojis = {
            "smile": "😊",
            "smile_cat": "😺",
            "heart": "❤️",
            "thumbsup": "👍",
            "thumbsdown": "👎",
            "check": "✅",
            "x": "❌",
            "warning": "��️",
            "question": "❓",
            "exclamation": "❗",
        }
        
        # Custom emojis
        self.custom: List[CustomEmoji] = []
    
    def add_custom(self, code: str, emoji: str, name: str) -> None:
        """Add custom emoji"""
        custom_emoji = CustomEmoji(code=code, emoji=emoji, name=name)
        self.custom.append(custom_emoji)
        self.emojis[code] = emoji
    
    def convert_to_emoji(self, text: str) -> str:
        """Convert text codes to emojis"""
        result = text
        
        # Replace custom emojis first
        for code, emoji in self.emojis.items():
            result = result.replace(code, emoji)
        
        # Replace slack format :emoji:
        for code, emoji in self.slack_emojis.items():
            result = result.replace(f":{code}:", emoji)
        
        # Replace unicode format :U+XXXX
        pattern = r':U\+([0-9A-Fa-f]{4,5}):'
        def replace_unicode(match):
            code = int(match.group(1), 16)
            return chr(code)
        result = re.sub(pattern, replace_unicode, result)
        
        return result
    
    def convert_to_text(self, text: str) -> str:
        """Convert emojis back to text codes"""
        result = text
        
        # Reverse mapping
        reverse = {v: k for k, v in self.emojis.items()}
        
        for emoji, code in reverse.items():
            result = result.replace(emoji, code)
        
        return result
    
    def get_category_emojis(self, category: EmojiCategory) -> List[str]:
        """Get all emojis in category"""
        return list(category.value)
    
    def find_emoji_by_name(self, name: str) -> Optional[str]:
        """Find emoji by name or keyword"""
        name = name.lower()
        
        # Search in default emojis
        for code, emoji in self.emojis.items():
            # Check if code matches
            if name in code.lower():
                return emoji
        
        return None
    
    def show_emoji_info(self, emoji: str) -> Optional[Dict]:
        """Get information about an emoji"""
        # Get emoji name (approximate)
        emoji_names = {
            "😊": {"name": "smiling face", "category": "faces"},
            "❤️": {"name": "red heart", "category": "hearts"},
            "👍": {"name": "thumbs up", "category": "gestures"},
            "😂": {"name": "face with tears of joy", "category": "faces"},
            "😢": {"name": "loudly crying face", "category": "faces"},
        }
        
        return emoji_names.get(emoji)

# ================== DISCORD SLACK FORMAT ==================
class FormatConverter:
    """Convert between different platforms"""
    
    @staticmethod
    def to_slack_format(text: str) -> str:
        """Convert to Slack emoji format"""
        replacers = {
            "😊": ":smile:",
            "❤️": ":heart:",
            "👍": ":thumbsup:",
            "❌": ":x:",
            "✅": ":white_check_mark:",
        }
        
        result = text
        for emoji, code in replacers.items():
            result = result.replace(emoji, code)
        
        return result
    
    @staticmethod
    def to_markdown(text: str) -> str:
        """Convert to markdown with emojis"""
        return text
    
    @staticmethod
    def to_html(text: str) -> str:
        """Convert to HTML entities"""
        result = ""
        for char in text:
            if ord(char) > 127:  # Emoji range
                result += f"&#x{ord(char):X};"
            else:
                result += char
        return result
    
    @staticmethod
    def to_unicode(text: str) -> str:
        """Convert to unicode format"""
        result = ""
        for char in text:
            if ord(char) > 127:
                result += f":U+{ord(char):X}:"
            else:
                result += char
        return result

# ================== EMOJI GAME ==================
def emoji_quiz():
    """Guess the emoji meaning"""
    import random
    
    questions = {
        "🎉": ["party", "congratulations", "celebration"],
        "💡": ["idea", "lightbulb", "thought"],
        "🚫": ["no", "forbidden", "stop"],
        "❤️": ["love", "heart", "favorite"],
        "🔥": ["hot", "fire", "trending"],
        "⭐": ["star", "favorite", "rating"],
        "✅": ["check", "done", "complete"],
        "❓": ["question", "help", "unknown"],
    }
    
    print("=== EMOJI QUIZ ===")
    score = 0
    
    emojis = list(questions.keys())
    for i in range(5):
        emoji = random.choice(emojis)
        emojis.remove(emoji)
        
        print(f"\nWhat does {emoji} mean?")
        answer = input("Your answer: ").lower()
        
        if answer in questions[emoji]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong! Answer: {questions[emoji][0]}")
    
    print(f"\nScore: {score}/5")

# ================== MAIN INTERFACE ==================
def main():
    converter = EmojiConverter()
    
    while True:
        print("\n=== EMOJI CONVERTER ===")
        print("1. Text to Emoji")
        print("2. Emoji to Text")
        print("3. Add custom emoji")
        print("4. View categories")
        print("5. Find emoji")
        print("6. Format converter")
        print("7. Emoji quiz")
        print("8. Exit")
        
        choice = input("\nChoice: ")
        
        # TEXT TO EMOJI
        if choice == "1":
            text = input("Enter text: ")
            result = converter.convert_to_emoji(text)
            print(f"Emoji: {result}")
        
        # EMOJI TO TEXT
        elif choice == "2":
            text = input("Enter emoji text: ")
            result = converter.convert_to_text(text)
            print(f"Text: {result}")
        
        # ADD CUSTOM EMOJI
        elif choice == "3":
            code = input("Code (e.g., :mylist): ")
            emoji = input("Emoji: ")
            name = input("Name: ")
            converter.add_custom(code, emoji, name)
            print("Emoji added!")
        
        # VIEW CATEGORIES
        elif choice == "4":
            print("\nCategories:")
            for cat in EmojiCategory:
                sample = cat.value[:20]
                print(f"{cat.name}: {sample}...")
            
            cat_choice = input("\nCategory name: ")
            try:
                category = EmojiCategory[cat_choice.upper()]
                emojis = converter.get_category_emojis(category)
                print(f"\n{''.join(emojis)}")
            except KeyError:
                print("Category not found!")
        
        # FIND EMOJI
        elif choice == "5":
            name = input("Search: ")
            emoji = converter.find_emoji_by_name(name)
            if emoji:
                print(f"Found: {emoji}")
            else:
                print("Not found")
        
        # FORMAT CONVERTER
        elif choice == "6":
            print("\nFormat converter:")
            print("1. To Slack format")
            print("2. To Unicode")
            print("3. To HTML")
            
            sub_choice = input("Choice: ")
            text = input("Text: ")
            
            if sub_choice == "1":
                print(FormatConverter.to_slack_format(text))
            elif sub_choice == "2":
                print(FormatConverter.to_unicode(text))
            elif sub_choice == "3":
                print(FormatConverter.to_html(text))
        
        # EMOJI QUIZ
        elif choice == "7":
            emoji_quiz()
        
        elif choice == "8":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()