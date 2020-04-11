def main():
    vowels = 'aeiouy'
    try_again = ""

    while try_again.lower() != "n":
        word = input("Type a word to get its pig Latin translation: ")

        if word[0] in vowels:
            translated_word = word + 'way'
        else:
            translated_word = word[1:] + word[0] + 'ay'

        print("\n", translated_word)
        try_again = input("\n\nTry again? Press Enter else n to exit")


if __name__ == "__main__":
    main()
