def load_data():

    with open("training_data.txt", "r", encoding="utf-8") as file:
        text = file.read()

    return text.split("\n")


def search_answer(question, data):

    results = []

    for sentence in data:

        if question.lower() in sentence.lower():
            results.append(sentence)

    return results