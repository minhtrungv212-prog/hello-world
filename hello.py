# hello.py
# My first Python program for the Hello World repository

def introduction():
    print("👋 Hello, I'm Trung!")
    print("💻 I'm a self-taught developer and a student.")
    print("🚀 Currently learning programming basics step by step.")
    print("🌱 Interested in open-source and small projects.")
    print("✨ This is my very first code on GitHub!")

def favorite_languages():
    langs = ["Python","JavaScript"]
    print("\n📚 Languages I'm exploring:")
    for lang in langs:
        print(f"- {lang}")

def motivation_quote():
    print("\n💡 Quote I like: 'The best way to learn to code is to write code.'")

if __name__ == "__main__":
    introduction()
    favorite_languages()
    motivation_quote()
