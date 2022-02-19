
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
				  'u', 'v', 'w', 'x', 'y', 'z', " ", "#", "€", "%", "$", "&", "0","1", "2", "3", "4", "5", "6", "7", "8",
				  "9", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
				  't', 'u','v', 'w', 'x', 'y', 'z', " ", "#", "€", "%", "$", "&", "0","1", "2", "3", "4", "5", "6", "7",
				  "8", "9"]
app_state = True


def start(state):
	while state:
		operation = input("Choose operation \"encode\", \"decode\" or \"cancel\": ").lower()
		if operation == "encode":
			inputs = ask()
			encrypt(inputs["message"] , inputs["shift"])
		elif operation == "decode":
			inputs = ask()
			encrypt(inputs["message"] , inputs["shift"] * -1)
		elif operation == "cancel":
			state = False


def ask():
	message = input("Write your message: ").lower()
	shift = int(input("Write shift level: "))
	return { "message": message, "shift": shift }


def encrypt(message, shift):
	message_array = []
	for char in list(message) :
		char_index = alphabet.index(char) + shift
		message_array.append(alphabet[char_index])
	print( f'Your encoded message is: {"".join(message_array)}')


start(app_state)
