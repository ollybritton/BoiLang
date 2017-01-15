def toBoiLang(text):
    text = text.replace(" ", "")

    text = "yeah " + text

    text = text.replace("+", "boii ")
    text = text.replace("-", "bboi ")

    text = text.replace("[", "bois ")
    text = text.replace("]", "boie ")

    text = text.replace(">", "booii ")
    text = text.replace("<", "bbooi ")

    text = text.replace(".", "boi! ")
    text = text.replace(",", "boi? ")
    return text

def toBrainFudge(text):
    text = text.replace(" ", "")

    text = text.replace("yeah", "")

    text = text.replace("boii", "+")
    text = text.replace("bboi", "-")

    text = text.replace("bois", "[")
    text = text.replace("boie", "]")

    text = text.replace("booii", ">")
    text = text.replace("bbooi", "<")

    text = text.replace("boi!", ".")
    text = text.replace("boi?", ",")
    return text
