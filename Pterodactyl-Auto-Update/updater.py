import requests
import time
import tomli
import subprocess


start = float(time.perf_counter())
print("[UPDATER] Starting update process...")


updater_ver = "4.0"





def config_parse():

    ## Initial file setup

    try:
        f = open("updater.toml", "r")
        f.close()
    except FileNotFoundError:
        print("[UPDATER] updater.toml doesn't exist. That should be impossible!")

    try:
        f = open("updated.md", "r")
        f.close()
    except FileNotFoundError:
        print("[UPDATER] updated.md doesn't exist. Creating one :D")
        f = open("updated.md", "w")
        f.write("[Placeholder.md]")
        f.close()

    ## Config loader

    try:
        with open("updater.toml", "rb") as f:
            temp = tomli.load(f)
            return temp
    except tomli.TOMLDecodeError:
        print("[UPDATER] Config (>> updater.toml) invalid. Won't do anything! >> Took: " + str(round(time.perf_counter() - start, 5)))
        exit(1)







def fetch_version(conf):

    global config
    config = conf

    global ver
    ver = conf["UPDATER"]["software"]
    

    if ver == "paper":
        re = requests.get("https://api.papermc.io/v2/projects/paper/")
        version = re.json()["versions"][-1]

        rebuild = requests.get("https://api.papermc.io/v2/projects/paper/versions/" + version + "/builds/")
        build = rebuild.json()["builds"][-1]["build"]

        TBD = ["paper", version, build]
        return TBD


    elif ver == "purpur":
        re = requests.get("https://api.purpurmc.org/v2/purpur/")
        version = re.json()["versions"][-1]

        rebuild = requests.get("https://api.purpurmc.org/v2/purpur/" + str(version) + "/latest/")
        build = rebuild.json()["build"]

        TBD = ["purpur", version, build]
        return TBD


    elif ver == "vanilla":
        re = requests.get("https://serverjars.com/api/fetchDetails/vanilla/vanilla")
        version = re.json()["response"]["version"]
        TBD = ["vanilla", version, "n/a"]
        return TBD


    elif ver == "fabric":
        re = requests.get("https://serverjars.com/api/fetchDetails/modded/fabric")
        version = re.json()["response"]["version"]
        TBD = ["fabric", version, "n/a"]
        return TBD


    else:
        print("[UPDATER] This server-software is not supported >> Is this a typo? >> Exiting >> Took: " + str(round(time.perf_counter() - start, 5)))
        exit(1)
    




def dl(updateddotmd):
    global updatedmd
    updatedmd = updateddotmd 
    if ver == "paper":
        downloadurl = "https://api.papermc.io/v2/projects/paper/versions/" + str(updateddotmd[1]) + "/builds/" + str(updateddotmd[2]) + "/downloads/" + "paper-" + str(updateddotmd[1]) + "-" + str(updateddotmd[2]) + ".jar"
    elif ver == "purpur":
        downloadurl = "https://api.purpurmc.org/v2/purpur/" + str(updateddotmd[1]) + "/latest/download"
    elif ver == "vanilla":
        downloadurl = "https://serverjars.com/api/fetchJar/vanilla/vanilla"
    elif ver == "fabric":
        downloadurl = "https://serverjars.com/api/fetchJar/modded/fabric"

    f = open("updated.md", "r")
    if str(f.read()) == str(updateddotmd):
        print("[UPDATER] You are running the latest Version! >> Took: " + str(round(time.perf_counter() - start, 5)))
              
    else:
        print("[UPDATER] Downloading a new jar file, as its not matching with the latest version." )
        subprocoutput = subprocess.run("wget -Oboot.jar " + str(downloadurl) , shell=True, capture_output=True)
        errors = subprocoutput.stderr.decode('utf-8')
        if "saved" in str(errors):
            print("[UPDATER] File was downloaded sucessfully! Server will start now!")
        else:
            print("[UPDATER] Errors executing the download! Please check everything. Exiting... >> Took: " + str(round(time.perf_counter() - start, 5)))
            print(errors)
            exit()
        f.close()
        f = open("updated.md", "w")
        f.write(str(updateddotmd))
        f.close
        webhook()
        print("[UPDATER] Updater is done now! >> Took: " + str(round(time.perf_counter() - start, 5)))




def webhook():
    payload = "## Automated Server Update\n**Details:**\nServer: " + str(config["Discord"]["server"]) + "\nSoftware: " + str(updatedmd[0]) + "\nNew Version: " + str(updatedmd[1]) + "\nNew Build: " + str(updatedmd[2]) + "\nUpdater Version: " + str(updater_ver) + "\nTrigger: Crash/Restart \n Source Code: https://github.com/Feuersteinium/mountain/"
    data = {
        "content" : payload,
        "username" : "Updater.py",
        "avatar_url" : config["Discord"]["avatar"]
    }



    result = requests.post(config["Discord"]["webhook"], json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


dl(fetch_version(config_parse()))

