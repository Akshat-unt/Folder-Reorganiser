import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

files = os.listdir()
files.remove("main.py")
print(files)

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Others')

imgExts = [".png", ".jpg", ".jpeg", ".img", ".ico"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".doc", ".docx", ".pdf", ".txt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".flv"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

move("Images", images)
move("Docs", docs)
move("Media", media)
move("Others", others)