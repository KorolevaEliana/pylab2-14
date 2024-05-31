def intint():
    import tkinter as tk
    import requests
    from PIL import ImageTk, Image

    def get_joke():
        api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(1)
        response = requests.get(api_url, headers={'X-Api-Key': 'LHem6s7ER/trir6E3PmoeA==HlWRh6ymAxIoI1l3'})
        if response.status_code == requests.codes.ok:
            joke_text.set(response.json()[0]['joke'])
        else:
            joke_text.set("Error: {} {}".format(response.status_code, response.text))

    root = tk.Tk()

    root.geometry('550x315')
    root.title("Joke Generator")
    joke_text = tk.StringVar()
    joke_label = tk.Label(root, textvariable=joke_text, wraplength=400)
    joke_label.pack()

    get_joke_button = tk.Button(root, text="Get a joke", bg="black", command=get_joke, fg="yellow")
    get_joke_button.pack()
    background_img = Image.open("14lab.png")
    background_img = ImageTk.PhotoImage(background_img)
    background_label = tk.Label(root, image=background_img)
    background_label.place(x=0, y=58, relwidth=1, relheight=1)

    root.mainloop()
intint()