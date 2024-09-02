# AutoFarm TabiZoo

- Collects points every 8 hours
- Claims daily rewards
- Can load hundreds of accounts
- Operates via key, no authorization needed
- Automatically upgrades accounts
- Completes tasks

# Installation:
1. Install Python (Tested on version 3.11)

2. No gitclone:
   ```
   download file or copy code to you PC
   ```

3. Install the modules:
   
   ```
   pip install -r requests
   ```

   ```
   pip install -r colorama
   ```
 
   or
   
   ```
   pip3 install -r requests
   ```

   ```
   pip3 install -r colorama
   ```

5. Run:
   ```
   python main.py
   ```

   or

   ```
   python3 main.py
   ```


## Insert the keys of this format into the init_data file, each new key on a new line:
   ```
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   query_id=xxxxxxxxxx&user=xxxxxxfirst_namexxxxxlast_namexxxxxxxusernamexxxxxxxlanguage_codexxxxxxxallows_write_to_pmxxxxxxx&auth_date=xxxxxx&hash=xxxxxxx
   ```
`query_id=` can be replaced with `user=`, it makes no difference.

# How to get query_id:

Go to Telegram Web, open the bot, press F12 or in the desktop version go to settings, additional settings, experimental settings, and enable "Enable webview inspecting". 
When you press F12, a window will open. Go to [Network]. 
Start game in the web version or refresh the page in the desktop version (click on the three dots), 
look for a request named getMe, and find `query_id=` or `user=` in the right column.

![photo_2024-07-18_21-54-55](https://github.com/user-attachments/assets/7e432a6f-d944-406b-80fd-0a3931b1876e)

---
