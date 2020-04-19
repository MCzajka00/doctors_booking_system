def printer(name, number, doctor, time):
    text = f"| Patient: {name}, Office and number: {number}, Doctor: {doctor}, Date: {time} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    empty_frame = f"|{' ' * (len(text) - 2)}|"

    border = [frame, empty_frame, text, empty_frame, frame]
    border_text = "\n".join(border)
    print(border_text)
