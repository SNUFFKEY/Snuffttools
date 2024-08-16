

def text_to_ascii_hex(text):
  ascii_hex = []
  for char in text:
      # Convert character to ASCII code
      ascii_code = ord(char)
      # Convert ASCII code to hexadecimal
      hex_code = hex(ascii_code)[2:]
      ascii_hex.append(hex_code)
  return ' '.join(ascii_hex)

# Example usage
input_text = input("Enter Text: ")
result = text_to_ascii_hex(input_text)
print(f"Original text: {input_text}")
print(f"Hexadecimal: {result}")
pyperclip.copy(result)
