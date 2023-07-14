'''ASCII Error'''
def asc():
    '''aera'''
    text = input()
    process1 = text.split("\"")
    text1 = len(process1[0])
    text2 = len(text)
    if text1 == text2:
        print("No error")
    else:
        #print(process1)
        process2 = int(process1[1])
        #print(process2)
        process2 = chr(process2)
        #print(process2)
        print(process1[0] + process2 + process1[2])
asc()

# """ASCII Error"""
 
 
# def message_check(message):
#     """Check if message have ASCII"""
#     if '"' in message:
#         new_message = message.split('"')
#         new_message[1] = chr(int(new_message[1]))
#         print(''.join(new_message))
#     else:
#         print("No error")
 
 
# message_check(input())

# '''ASCII Error'''
# def main():
#     '''ASCII Error'''
#     text = input()
#     start = text.find('"')
#     end = text.find('"', start+1)
#     if start*end != 1:
#         print(text.replace(text[start:end+1], chr(int(text[start+1:end]))))
#     else:
#         print("No error")
# main()