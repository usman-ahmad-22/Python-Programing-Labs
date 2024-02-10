import string

def cipher(text, key):
  """ Ciphers a text string using the given key.

  Args:
    text: The text string to be ciphered.
    key: The cipher key.

  Returns:
    The ciphered text string. """

  ciphered_text = ""
  for character in text:
    ciphered_text += chr(ord(character) + key)

  return ciphered_text


def main():
  text = "This is a simple text file."
  key = 10
  ciphered_text = cipher(text, key)

  print(ciphered_text)


if __name__ == "__main__":
  main()
