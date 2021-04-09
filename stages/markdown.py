#1
# formatters = ["plain", "bold", "italic", "link", "inline-code", "header", "ordered-list", "unordered-list", "line-break"]
#
# while 1:
#     print("Choose a formatter:")
#     formatter = input()
#     if formatter in formatters:
#         continue
#     elif formatter == "!help":
#         print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
# Special commands: !help !done""")
#     elif formatter == "!done":
#         break
#     else:
#         print("Unknown formatting type or command. Please try again")

# 2
# formatted_text = ""
#
#
# def plain():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += text
#     print(formatted_text)
#
#
# def header():
#     global formatted_text
#     level = int(input("- Level:"))
#     text = input("- Text:")
#     if level > 6:
#         print("The level should be within the range of 1 to 6")
#     else:
#         formatted_text += "#"*level + " " + text + "\n"
#     print(formatted_text)
#
#
# def line_break():
#     global formatted_text
#     formatted_text += "\n"
#     print(formatted_text)
#
#
# def inline_code():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += "`" + text + "`"
#     print(formatted_text)
#
#
# def link():
#     global formatted_text
#     label = input("- Label:")
#     url = input("- URL:")
#     formatted_text += "[" + label + "]" + "(" + url + ")"
#     print(formatted_text)
#
#
# def bold():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += "**" + text + "**"
#     print(formatted_text)
#
#
# def italic():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += "*" + text + "*"
#     print(formatted_text)
#
#
# while 1:
#     formatter = input("- Choose a formatter:")
#     if formatter == "plain":
#         plain()
#     elif formatter == "header":
#         header()
#     elif formatter == "new-line":
#         line_break()
#     elif formatter == "link":
#         link()
#     elif formatter == "bold":
#         bold()
#     elif formatter == "italic":
#         italic()
#     elif formatter == "inline-code":
#         inline_code()
#     elif formatter == "!help":
#         print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
# Special commands: !help !done""")
#     elif formatter == "!done":
#         break
#     else:
#         print("Unknown formatting type or command. Please try again")

# 3
# formatted_text = ""
#
#
# def plain():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += text
#     print(formatted_text)
#
#
# def header():
#     global formatted_text
#     level = int(input("- Level:"))
#     text = input("- Text:")
#     if level > 6:
#         print("The level should be within the range of 1 to 6")
#     else:
#         formatted_text += "#"*level + " " + text + "\n"
#     print(formatted_text)
#
#
# def line_break():
#     global formatted_text
#     formatted_text += "\n"
#     print(formatted_text)
#
#
# def inline_code():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += "`" + text + "`"
#     print(formatted_text)
#
#
# def link():
#     global formatted_text
#     label = input("- Label:")
#     url = input("- URL:")
#     formatted_text += "[" + label + "]" + "(" + url + ")"
#     print(formatted_text)
#
#
# def bold():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += "**" + text + "**"
#     print(formatted_text)
#
#
# def italic():
#     global formatted_text
#     text = input("- Text:")
#     formatted_text += "*" + text + "*"
#     print(formatted_text)
#
#
# def order_list(formatter):
#     global formatted_text
#     while 1:
#         rows = int(input("- Number of rows:"))
#         if rows <= 0:
#             print("The number of rows should be greater than zero")
#         else:
#             for i in range(1, rows+1):
#                 text = input(f"- Row #{i}:")
#                 if formatter == "ordered-list":
#                     formatted_text += f"{i}. " + text + "\n"
#                     print(formatted_text)
#                 else:
#                     formatted_text += "* " + text + "\n"
#                     print(formatted_text)
#             break
#
#
# while 1:
#     formatter = input("- Choose a formatter:")
#     if formatter == "plain":
#         plain()
#     elif formatter == "header":
#         header()
#     elif formatter == "new-line":
#         line_break()
#     elif formatter == "link":
#         link()
#     elif formatter == "bold":
#         bold()
#     elif formatter == "italic":
#         italic()
#     elif formatter == "inline-code":
#         inline_code()
#     elif formatter in ["unordered-list", "ordered-list"]:
#         order_list(formatter)
#     elif formatter == "!help":
#         print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
# Special commands: !help !done""")
#     elif formatter == "!done":
#         break
#     else:
#         print("Unknown formatting type or command. Please try again")

# 4
def plain():
    global formatted_text
    text = input("- Text:")
    formatted_text += text
    print(formatted_text)


def header():
    global formatted_text
    level = int(input("- Level:"))
    text = input("- Text:")
    if level not in range(1, 7):
        print("The level should be within the range of 1 to 6")
    else:
        formatted_text += "#" * level + " " + text + "\n"
    print(formatted_text)


def line_break():
    global formatted_text
    formatted_text += "\n"
    print(formatted_text)


def inline_code():
    global formatted_text
    text = input("- Text:")
    formatted_text += "`" + text + "`"
    print(formatted_text)


def link():
    global formatted_text
    label = input("- Label:")
    url = input("- URL:")
    formatted_text += "[" + label + "]" + "(" + url + ")"
    print(formatted_text)


def bold():
    global formatted_text
    text = input("- Text:")
    formatted_text += "**" + text + "**"
    print(formatted_text)


def italic():
    global formatted_text
    text = input("- Text:")
    formatted_text += "*" + text + "*"
    print(formatted_text)


def order_list(formatter):
    global formatted_text
    while 1:
        rows = int(input("- Number of rows:"))
        if rows <= 0:
            print("The number of rows should be greater than zero")
        else:
            for i in range(1, rows+1):
                text = input(f"- Row #{i}:")
                if formatter == "ordered-list":
                    formatted_text += f"{i}. " + text + "\n"
                    print(formatted_text)
                else:
                    formatted_text += "* " + text + "\n"
                    print(formatted_text)
            break


formatted_text = ""

while 1:
    formatter = input("- Choose a formatter:")
    if formatter == "plain":
        plain()
    elif formatter == "header":
        header()
    elif formatter == "new-line":
        line_break()
    elif formatter == "link":
        link()
    elif formatter == "bold":
        bold()
    elif formatter == "italic":
        italic()
    elif formatter == "inline-code":
        inline_code()
    elif formatter in ["unordered-list", "ordered-list"]:
        order_list(formatter)
    elif formatter == "!help":
        print("""Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break
Special commands: !help !done""")
    elif formatter == "!done":
        save_file = open("output.md","w")
        save_file.write(formatted_text)
        save_file.close()
        break
    else:
        print("Unknown formatting type or command. Please try again")

# Program implements the formatters from Markdown language: plain, bold, italic, link, inline-code, header, ordered-list, unordered-list, line-break.
# Special commands:
# !help — prints available syntax commands.
# !done — saves the final markdown to a file and exits the app.