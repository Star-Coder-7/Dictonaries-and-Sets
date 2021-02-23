sentence = input("Please enter a sentence: ")


def identify_constants(user_input: str) -> None:
    set_sentence = set(user_input)
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    output = sorted(consonants.intersection(user_input))

    upgraded_output = ", ".join(output)
    print(f"There are {len(output)} types of consonants in the sentence: {upgraded_output}")


identify_constants(sentence.casefold())


def identify_vowels(user_sentence: str) -> None:
    sentence_set = set(user_sentence)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = sorted(vowels.intersection(user_sentence))
    better_result = ", ".join(result)
    print(f"There are {len(result)} types of vowels in the sentence: {better_result}")


identify_vowels(sentence.casefold())
