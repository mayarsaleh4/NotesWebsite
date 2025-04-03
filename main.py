from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True) #debug= True means every time we make a change in the code it will automatically rerun the web server
    