from gmail import Gmail

# gmail = Gmail()  # will open a browser window to ask you to log in and authenticate

# params = {
#     "to": "nigamreetesh84@gmail.com",
#     "sender": "nigamreetesh84@gmail.com",
#     "subject": "My first email",
#     "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
#     "msg_plain": "Hi\nThis is a plain text email.",
#     "signature": True  # use my account signature
# }
# message = gmail.send_message(**params)


def send(file_name):
    gmail = Gmail()

    params = {
        "to": "nigamreetesh84@gmail.com",
        "sender": "nigamreetesh84@gmail.com",
        "subject": "My first email",
        "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
        "msg_plain": "Hi\nThis is a plain text email.",
        "attachments": [file_name],
        "signature": True  # use my account signature
    }
    message = gmail.send_message(**params)
    print(message)
    return message
