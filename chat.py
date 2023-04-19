import tkinter
from tkinter import *
import customtkinter
import openai
import os
import pickle

# Initiate app
root = customtkinter.CTk()
root.title("chatGPT bot")
root.geometry('600x500')

#set color scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Submit to chatGPT
def speak():
	if chat_entry.get():
		#define your filename
		filename = "api_key"

		#error handling part 1
		try:
			if os.path.isfile(filename):
				# open the file
				input_file = open(filename, 'rb')

				#load the data from the file into a variable
				stuff = pickle.load(input_file)

				#Querry chatgpt

				#define our api key to chaagpt
				openai.api_key = stuff

				#create an instant
				openai.Model.list()

				#define our querry / response
				response = openai.Completion.create(
					model = "text-davinci-003",
					prompt = chat_entry.get(),
					temperature = 0,
					max_tokens = 60,
					top_p = 1.0,
					frequency_penalty = 0.0,
					presense_penalty = 0.0,
					)
				my_text.insert(END, (response["choices"][0]["text"]).strip())
				my_text.insert(END, "\n\n")

			else:
				#create the file
				input_file = open(filename, 'wb')
				#close the file
				input_file.close()
				#Error massage - you need an api key
				my_text.insert(END, "\n\n You need a API key to talk with chatGPT ! Get one here : \nhttps://platform.openai.com/account/api-keys ")

	    #error heandling part 2
		except Exception as e:
			my_text.insert(END, f"\n\n There was an error \n\n{e}")

	else:
		my_text.insert(END, "\n\n Hey you forget to type anything !")
#clear the screen
def clear():
	#clear the main text box
	my_text.delete(1.0, END)

	#clear the querry entry box
	chat_entry.delete(0, END)

# Do Api staff
def key():

	# define our filename
	filename = "api_key"

	#error handling part 1
	try:
		if os.path.isfile(filename):
			# open the file
			input_file = open(filename, 'rb')

			#load the data from the file into a variable
			stuff = pickle.load(input_file)

			# output stuff to our entry box
			api_entry.insert(END, stuff)

		else:
			#create the file
			input_file = open(filename, 'wb')
			#close the file
			input_file.close()

    #error heandling part 2
	except Exception as e:
		my_text.insert(END, f"\n\n There was an error \n\n{e}")



	#resize app larger
	root.geometry('600x650')
	#reshow api frame
	api_frame.pack(pady=30)

# save api key
def save_key():
	# define our file name
	filename = "api_key"

	try:
		# open file
		output_file = open(filename, 'wb')

		#add the data in file
		pickle.dump(api_entry.get(), output_file)

		#delete entry box
		api_entry.delete(0, END)
		#hide api frame 
		api_frame.pack_forget()
		#resize app smaller 
		root.geometry('600x500')

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error \n\n{e}")


# Create text frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

#add text widget to get chatGPT responces
my_text = Text(text_frame,
	bg="#343638",
	width=80,
	bd=1,
	fg="#d6d6d6",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")
my_text.grid(row=0, column=0)

# Create scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

# Add the scrollbar to the text bar
my_text.configure(yscrollcommand=text_scroll.set)

# Entry widget to type stuff to chat
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type something to chat bot ....",
	width= 535,
	height= 50,
	border_width= 1)
chat_entry.pack(pady=10)

# Create button frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# Create submit buttons
submit_button = customtkinter.CTkButton(button_frame,
	text= "Speak to chatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

# Create clear buttons
clear_button = customtkinter.CTkButton(button_frame,
	text= "Clear response",
	command=clear)
clear_button.grid(row=0, column=1, padx=35)

# Create api buttons
api_button = customtkinter.CTkButton(button_frame,
	text= "Update api key",
	command=key)
api_button.grid(row=0, column=2, padx=25)

# add api key frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

#add api entry widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter your API key",
	width=350, height=50, border_width=1)
api_entry.grid(row=0,column=0, padx=20, pady=20)

# add api button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save key!",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)





root.mainloop()