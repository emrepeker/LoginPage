from website import create_app

app = create_app()

if __name__ == '__main__': #Checks whether the given file is actual website
    app.run(debug=True) #Turn it off on production
