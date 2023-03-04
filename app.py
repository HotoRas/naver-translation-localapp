import os
import sys
import urllib.request
import json
import time

try:
    import translationApp.secret as Secret # "secret.py" has ignored. Please check /.gitignore.
except Exception as e:
    print("Secret file does not exist. Please create it with copying and editing from \"secret-example.py\" to \"secret.py\".")
    raise Exception(e)
import translationApp.settings as Settings # Default settings are loaded from here.

print("Before you start, you can change the default language type\nof your inputs and target at ./translationApp/settings.py.\nThe target is set to \"ko\" as default,\nso you might want to change it.")
print()
print()

# Source string is set firstly.
print("Please input the string to translate and press Enter")
sourceString: str = input("(Input line break as \\n): ")

# The API URL hardcoded.
translateUrl: str = "https://openapi.naver.com/v1/papago/n2mt"

print()

# Set input language code.
try:
    print("Please type which language you've entered")
    print("(If you don't know, please enter \"auto\"\n or leave it as blank.)")
    print()
    print()
    print("e.g. korean -> ko | english -> en | japanese -> ja")
    print("Please check the list from here: https://developers.naver.com/docs/papago/papago-detectlangs-overview.md")
    source: str = input("Type here: ")
except:
    source: str = Settings.sourceLanguage
if source == "": source = Settings.sourceLanguage

print("Source language has set to", source, sep=" ")

print()

# Set output language code.
try:
    print("Please type which language you're to translate into")
    print("(If you want to use this from settings\n (at \"translationApp/settings.py\"),\n leave it blank.)")
    print()
    print()
    print("e.g. korean -> ko | english -> en | japanese -> ja")
    target: str = input("Type here: ")
except:
    target: str = Settings.targetLanguage
if target == "": target = Settings.targetLanguage

print("Target language has set to", target, sep=" ")

print()
time.sleep(1.0)

# Set qurey data
qureyData: str = "source=" + source + "&target=" + target + "&text=" + urllib.parse.quote(sourceString)

# Create HTTP POST request
request = urllib.request.Request(translateUrl)
request.add_header("X-Naver-Client-Id", Secret.clientId)
request.add_header("X-Naver-Client-Secret", Secret.clientSecret)

# Send qurey and get response
try:
    response = urllib.request.urlopen(request, data=qureyData.encode("utf-8"))
    returnCode = response.getcode()
except Exception as e:
    print(response)
    print(e)
    print("URL:", translateUrl, ", Data:", qureyData)

if(returnCode == 200):
    print("Translation successful!")
    print()
    # print(response.read().decode('utf-8'))
    result = json.loads(response.read()).get("message").get("result")
    print("Source language: ", result.get("srcLangType"), "\nTarget Language: ", result.get("tarLangType"), "\n\nResult:\n", result.get("translatedText").replace("\\n", "\n"), sep="")
else:
    print("Please check the upper code for more details.")

# EOF
