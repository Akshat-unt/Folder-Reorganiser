# Folder-Reorganiser
Troubled by the bulky stuff in any folder! 

just copy and paste the file in that folder 📂 and run it.
get the shit off!

## How it works?
1. Inspection whether the ``Media, Docs, Images, Others`` folder already exists.
  - The following code accomplishes it: 
    ```
    def createIfNotExist(folder):
          if not os.path.exists(folder):
              os.makedirs(folder)
2. If it is then the program moves directly to 3rd step otherwise it creates them.
 - The following code accomplishes it:
    ```
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')
3. Identification/sorting of extensions
  - The following code accomplishes it:
    ```
    imgExts = [".png", ".jpg", ".jpeg", ".img", ".ico"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".doc", ".docx", ".pdf", ".txt"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp4", ".mp3", ".flv"]
    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    
    others = []
5. Moving files into their respective folders.
  - The following code accomplishes it:
    ```
    move("Images", images)
    move("Docs", docs)
    move("Media", media)
    move("Others", others)

## Contribute:
Contributions and Issues are welcome!
- [ ] Add a menu from which the user can choose which folder to declutter.
- [ ] Add a Welcome & Thank You splash-screen {OPTIONAL}.
- [ ] Add a GUI.

## Contributers: 
- [Akshat](https://github.com/Akshat-unt)
- Maybe YOU!!
