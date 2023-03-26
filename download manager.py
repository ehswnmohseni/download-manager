print("Welcome To Download Manager...")

option = input("""set option for your download
1.download from text list
2.turn of computer after dowloading
3.Start downloading at the time you want
Note : for all options enter '123'\n(enter here):""")

def main():
    name = input("plaese enter name file\n(game):")
    type = input("please enter type of file\n(.zip-.mp3):")

    if "1" in option:
        global u_time
        u_time = input("When will the download start\n(20:00)?")
        time(u_time)

    if "2" in option:
        location = input("where is your text file?")
        reader_file(location,name,type)

    if "3" in option:
        turn_off()

    else:
        url = input("enter download link \n:")
        download (url,name)

def time(u_time):
    import time
    import datetime
    now = "00:00"
    while now != u_time:
        now = datetime.datetime.now()
        now = (now.strftime("%H:%M"))
        time.sleep(30)
    print("download starting...")

def download(url,name,type,number):
    try:
        import requests
        responce = requests.get(url,allow_redirects = True)
        print("file downloaded!")
        with open('C:/Users/asus/Downloads/%s'%(name+str(number)+type),"wb") as file:
            file.write(responce.content)
    except ConnectionError:
        print("connection lost...")
        print("try again")
        download(url,name,type,number)

def reader_file(location,name,type):
    with open ('C:/Users/asus/Downloads/%s'%(location)) as file:
        links = file.readlines()
        number = 0
        for link in links:
            number += 1
            link = link.replace("\n","")
            download(link,name,type,number)

def turn_off():
    import os
    os.system("shutdown /s /t 1")


main()