# . Write a program to fill in a letter template given below with name and date.

latter = '''Dear <|Name|>,
        you are selected!
        <|Date|> '''

print(latter.replace("<|Name|>", "pintu").replace("<|Date|>", "2 September 2024"))