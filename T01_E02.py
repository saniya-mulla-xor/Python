def clean_name(raw):
    return " ".join(raw.split()).title()


def initials(name):
    return "".join(f"{word[0]}." for word in name.split())


names = ["  aNNa   maRIA  smith ", "o'brien   john", "MARY-JANE watson", "li   wei"]

for raw_name in names:
    cleaned_name = clean_name(raw_name)
    print(f"{cleaned_name!r} -> {initials(cleaned_name)}")