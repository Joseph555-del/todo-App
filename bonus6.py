contents = ["All carrots are to be sliced "
            "Longitudinaly.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "reported.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)


a = "I am a string " \
    "on my " \
    "own"