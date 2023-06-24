import requests
import time
import tomli
import subprocess


start = float(time.perf_counter())
print("[UPDATER] Started updating...")


fabric = []
discord = []
updater_ver = 3.0

def init():
    try:
        f = open("updater.toml", "r")
        f.close()
    except FileNotFoundError:
        print("[UPDATER] updater.toml doesn't exist. Creating one :D")
        f = open("updater.toml", "w")
        f.write('[UPDATER]\n\n# Options: Paper, Purpur, Vanilla\n\nsoftware = "purpur"\n\n# When using Vanilla\n# Visit https://fabricmc.net/use/server/ and grep latest Fabric Loader Version and Installer Version\nfabricloader = "0.14.21"\nfabricversion = "0.11.2"\n\n[Discord]\n#URL for the Webhook\nwebhook = ""\navatar = ""\nserver = ""')

    try:
        f = open("updated.md", "r")
        f.close()
    except FileNotFoundError:
        print("[UPDATER] updated.md doesn't exist. Creating one :D")
        f = open("updated.md", "w")
        f.write("[Placeholder.md]")
        f.close()


def config_parse():
    try:
        with open("updater.toml", "rb") as f:
            temp = tomli.load(f)
            fabrictmp = temp
            temp = temp["UPDATER"]["software"]
            fabric.append(fabrictmp["UPDATER"]["fabricloader"])
            fabric.append(fabrictmp["UPDATER"]["fabricversion"])
            discord.append(fabrictmp["Discord"]["webhook"])
            discord.append(fabrictmp["Discord"]["avatar"])
            discord.append(fabrictmp["Discord"]["server"])
            print("[UPDATER] Config seems to be a valid toml file")
            return temp
            

    except tomli.TOMLDecodeError:
        print("[UPDATER] Config (>> updater.toml) invalid. Won't do anything! >> Took: " + str(round(time.perf_counter() - start, 5)))
        exit(1)
    except KeyError:
        print("[UPDATER] Config (>> updater.toml) invalid. Won't do anything! >> Took: " + str(round(time.perf_counter() - start, 5)))
        exit(1)



def fetch_version(ver):
    if ver.lower() == "paper":
        re = requests.get("https://api.papermc.io/v2/projects/paper/")
        version = re.json()["versions"][-1]

        rebuild = requests.get("https://api.papermc.io/v2/projects/paper/versions/" + version + "/builds/")
        build = rebuild.json()["builds"][-1]["build"]

        TBD = ["paper", version, build]
        return TBD





    elif ver.lower() == "purpur":
        re = requests.get("https://api.purpurmc.org/v2/purpur/")
        version = re.json()["versions"][-1]

        rebuild = requests.get("https://api.purpurmc.org/v2/purpur/" + str(version) + "/latest/")
        build = rebuild.json()["build"]

        TBD = ["purpur", version, build]
        return TBD



    elif ver.lower() == "vanilla":
        re = requests.get("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json")
        version = re.json()["latest"]["release"]
        TBD = ["vanilla", version, "n/a"]
        return TBD

    else:
        print("[UPDATER] This server-software is not supported >> Is this a typo? >> Exiting >> Took: " + str(round(time.perf_counter() - start, 5)))
        exit(1)
    

def dl(downloadthis):
    if downloadthis[0] == "paper":
        downloadurl = "https://api.papermc.io/v2/projects/paper/versions/" + str(downloadthis[1]) + "/builds/" + str(downloadthis[2]) + "/downloads/" + "paper-" + str(downloadthis[1]) + "-" + str(downloadthis[2]) + ".jar"
    elif downloadthis[0] == "purpur":
        downloadurl = "https://api.purpurmc.org/v2/purpur/" + str(downloadthis[1]) + "/latest/download"
    elif downloadthis[0] == "vanilla":
        ## Fabric Download >> Version >> Loader >> Installer
        downloadurl = "https://meta.fabricmc.net/v2/versions/loader/" + str(downloadthis[1]) + "/" + str(fabric[0]) + "/" + str(fabric[1]) + "/server/jar"
    
    return [downloadthis, downloadurl]


def check():
    f = open("updated.md", "r")
    if str(f.read()) == str(cache[0]):
        print("[UPDATER] You are running the latest Version! >> Took: " + str(round(time.perf_counter() - start, 5)))
              
    else:
        print("[UPDATER] Downloading " + str(cache[0][0]) + " Version " + str(cache[0][1]) + " Build " + str(cache[0][2]) + " (" + str(cache[1]) + ")" )
        subprocoutput = subprocess.run("wget -Oboot.jar " + str(cache[1]) , shell=True, capture_output=True)
        errors = subprocoutput.stderr.decode('utf-8')
        if "saved" in str(errors):
            print("[UPDATER] File was downloaded sucessfully! Server will start now!")
        else:
            print("[UPDATER] Errors executing the download! Please check everything. Exiting... >> Took: " + str(round(time.perf_counter() - start, 5)))
            print(errors)
            exit()
        f.close()
        f = open("updated.md", "w")
        f.write(str(cache[0]))
        f.close
        webhook()
        print("[UPDATER] Updater is done now! >> Took: " + str(round(time.perf_counter() - start, 5)))




def webhook():
    payload = "## Automated Server Update\n**Details:**\nServer: " + str(discord[2]) + "\nSoftware: " + str(cache[0][0]) + "\nNew Version: " + str(cache[0][1]) + "\nNew Build: " + str(cache[0][2]) + "\nUpdater Version: " + str(updater_ver) + "\nTrigger: Crash/Restart"
    data = {
        "content" : payload,
        "username" : "Updater.py",
        "avatar_url" : discord[1]
    }



    result = requests.post(discord[0], json = data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


init()
cache = dl(fetch_version(config_parse()))
check()
