original_text = "HELLO"

x = "ABCDEFGHIKLMNOPQRSTVXYZ"
y = "BCDEFGHIKLMNOPQRSTVXYZA"

encoded_text = original_text.maketrans(x, y)
print(original_text.translate(encoded_text))

# TODO: BUG!
decoded_text = encoded_text.maketrans(y, x)
print(encoded_text.translate(decoded_text))

