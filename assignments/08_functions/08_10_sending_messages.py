msgs = ["Hello,","Goodbye.","Goodo!"]
sent_messages = []

def show_messages():
    for msg in msgs:
        print(msg)

def send_messages():
    for msg in msgs:
        sent_messages.append(msg)
        print(msg)
    
    msgs.clear()

send_messages()

print(msgs)
print(sent_messages)
