# Whatsapp Mention Everyone

## Description
This Python script uses the `pyautogui` library to automate sending a message to multiple members in a messaging group. It emulates the process of typing a message, mentioning each member in the group, and sending the message.

## Prerequisites
1. Python installed on your system.
2. Install the `pyautogui` library using the following command:


```bash
  pip install pyautogui
```


## Usage
1. Run the script by executing the  command in your terminal:
   ```
   python tag.py
   ```
   Or you can run it in VSCode Terminal also.

2. Enter the total number of members in the group when prompted.

3. Enter the message you want to send when prompted.(add a `space` after the message )

4. After a 5-second delay, the script will start typing the message, mentioning each member, and sending it.

## Important Note
Ensure that Whatsapp is open and focused on the chat window before running the script to prevent any issues.

## Customization
You can customize the script by modifying the `peep` and `msg` variables in the script according to your needs.

- `peep`: Total members in the group.
- `msg`: The message you want to send.

## Dependencies
- [pyautogui](https://pyautogui.readthedocs.io/): Used for automating keyboard and mouse actions.

## Disclaimer
This script is intended for educational purposes and should be used responsibly. Be aware of any terms of service or community guidelines of the messaging platform you are using to avoid any violations.
