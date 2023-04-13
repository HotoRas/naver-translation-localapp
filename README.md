# Naver Translation API Python 3.11 Sample
Originally meant to use for myself, but it's very usable so I'm updating the readme.

## Prepare
1. Install Python 3. You'll need to install Python 3.9 or later.
2. Clone this git.
3. Create `translationApp/secret.py` based on `translationApp/secret-example.py`.
  - Since it's using OpenAPI but you need "App" created, API configuration is required.

## Practice
Run: shell
```sh
python3 ./app.py
```

Run: windows (Both CMD and Powershell)
```bat
ren Please note that you've installed Python 3.
ren If you installed both Python 2 and 3, maybe you'll need to
ren use python3 to properly boot the app.
python .\app.py
```

### Source String Syntax
You should type `\n` for line breaks on input.  
On output, the raw `\n` will be automatically decoded to line breaks.

### Output example if success
```raw
Before you start, you can change the default language type
of your inputs and target at ./translationApp/settings.py.
The target is set to "ko" as default,
so you might want to change it.


Please input the string to translate and press Enter
(Input line break as \n): <Type your own source string> [ENTER]

Please type which language you've entered
(If you don't know, please enter "auto"
 or leave it as blank.)


e.g. korean -> ko | english -> en | japanese -> ja
Please check the list from here: https://developers.naver.com/docs/papago/papago-detectlangs-overview.md
Type here: <Type the lang code> [ENTER]
Source language has set to (your input)

Please type which language you're to translate into
(If you want to use this from settings
 (at "translationApp/settings.py"),
 leave it blank.)

e.g. korean -> ko | english -> en | japanese -> ja
Type here: <Type the lang code> [ENTER]
Target language has set to (your input)

Translation successful!

Source language: (your input or detected)
Target Language: (your input)

Result:
(Translation result displays here. Line breaks are auto-applied.)
```

## Secret
This app uses NAVER OpenAPI which is for registered applications.  
You should register your app to [Naver Developers](https://developers.naver.com/main/).

After that you'll have to create secret file.  
The example file is included in this repositiory.  
Please check [secret-example.py](./translationApp/secret-example.py) for more details.

## Default language I/O settings
You can set the default I/O language code at [settings.py](./translationApp/settings.py).  
The language code you can use can be found [here](https://developers.naver.com/docs/papago/papago-detectlangs-overview.md).

Source language can be set to `auto`, which is "automatical detection".  
Target language can't be set to `auto`.

Prompt will be displayed to override the language settings when running.  
You can just press `Enter` to skip.  
To override, type the code there.

## Troubleshooting
I've done the minimum test for this app, so you'll meet some exceptions.  
Please raise issues if found.

You'll have to include Python version, OS type, and the tracebacks.  
Please hide your secrets from traceback!

### My test environment
- Python: 3.11.2, x64 (Python 3.9 works)
- OS: Windows 11 Pro
  - Locale: ko-KR
  - Code page: 949 `MS949` (65001 `UTF-8` support for modern CLI apps)
- Tested file encoding: `CRLF`, `LF`
