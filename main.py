import os
import sys
import time
import requests
from colorama import *
from datetime import datetime, timezone


script_dir = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(script_dir, "init_data.txt")


class TabiZoo:
    def __init__(self):
        self.line = Fore.LIGHTWHITE_EX + "-" * 50

    def headers(self, data):
        return {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://miniapp.tabibot.com",
        "Pragma": "no-cache",
        "Referer": "https://miniapp.tabibot.com/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
        "Rawdata": f"{data}",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": '"Android"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36'
    }

    def user_info(self, data):
        url = f"https://api.tabibot.com/api/user/v1/profile"
        headers = self.headers(data=data)
        response = requests.get(url=url, headers=headers)
        return response

    def mining_info(self, data):
        url = f"https://api.tabibot.com/api/mining/v1/info"
        headers = self.headers(data=data)
        response = requests.get(url=url, headers=headers)
        return response

    def check_in(self, data):
        url = f"https://api.tabibot.com/api/user/v1/check-in"
        headers = self.headers(data=data)
        response = requests.post(url=url, headers=headers)
        return response

    def level_up(self, data):
        url = f"https://api.tabibot.com/api/user/v1/level-up"
        headers = self.headers(data=data)
        response = requests.post(url=url, headers=headers)
        return response

    def claim(self, data):
        url = f"https://api.tabibot.com/api/mining/v1/claim"
        headers = self.headers(data=data)
        response = requests.post(url=url, headers=headers)
        return response

    def task_info(self, data):
        url = f"https://api.tabibot.com/api/task/v1/list"
        headers = self.headers(data=data)
        response = requests.get(url=url, headers=headers)
        return response

    def do_task(self, data, task_tag):
        url = "https://api.tabibot.com/api/task/v1/verify/task"
        headers = self.headers(data=data)
        payload = {"task_tag": task_tag}
        response = requests.post(url=url, headers=headers, json=payload)
        return response

    def banner_info(self, data):
        url = f"https://api.tabibot.com/api/task/v1/mine/banners"
        headers = self.headers(data=data)
        response = requests.get(url=url, headers=headers)
        return response

    def banner_task(self, data, task_tag):
        url = f"https://api.tabibot.com/api/task/v1/mine?project_tag=mine_{task_tag}"
        headers = self.headers(data=data)

        response = requests.get(url=url, headers=headers)
        return response

    def do_banner(self, data, task_tag):
        url = "https://api.tabibot.com/api/task/v1/verify/task"
        headers = self.headers(data=data)
        payload = {"task_tag": task_tag}
        response = requests.post(url=url, headers=headers, json=payload)
        return response

    def do_project(self, data, task_tag):
        url = "https://api.tabibot.com/api/task/v1/verify/project"
        headers = self.headers(data=data)
        payload = {"project_tag": f"mine_{task_tag}"}
        response = requests.post(url=url, headers=headers, json=payload)
        return response

    def log(self, message):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{Fore.LIGHTBLACK_EX}[{now}]{Style.RESET_ALL} {message}")

    def main(self):
        while True:

            data = open(data_file, "r").read().splitlines()
            num_acc = len(data)
            self.log(self.line)
            self.log(f"{Fore.LIGHTYELLOW_EX}Total Accounts: {Fore.LIGHTWHITE_EX}{num_acc}")
            end_at_list = []
            for no, data in enumerate(data):
                self.log(self.line)
                self.log(f"{Fore.LIGHTYELLOW_EX}Account number: {Fore.LIGHTWHITE_EX}{no+1}/{num_acc}")


                #user infor
                try:
                    user_info = self.user_info(data=data).json()

                    user = user_info["data"]["user"]

                    username = user["name"]
                    balance = user["coins"]
                    level = user["level"]
                    streak = user["streak"]
                    self.log(f"{Fore.LIGHTYELLOW_EX}Account: {Fore.LIGHTWHITE_EX}{username}")
                    self.log(f"{Fore.LIGHTYELLOW_EX}Balance: {Fore.LIGHTWHITE_EX}{balance:,}")
                    self.log(f"{Fore.LIGHTYELLOW_EX}Level: {Fore.LIGHTWHITE_EX}{level}")
                    self.log(f"{Fore.LIGHTYELLOW_EX}Streak: {Fore.LIGHTWHITE_EX}{streak}")
                except Exception as e:
                    self.log(f"{Fore.LIGHTRED_EX}Error getting account info: {str(e)}")
                time.sleep(1)
                
                
                
                #task
                try:
                    response = self.task_info(data=data)

                    if response.text.strip():
                        tasks2 = response.json()


                        for project2 in tasks2.get('data', []):
                            task_listt = project2.get('task_list', [])
                            for task in task_listt:
                                status = task.get("user_task_status")
                                if status == 2:
                                    tag = task.get('task_tag')
                                    dtask3 = self.do_task(data=data, task_tag=tag).json()

                                    if dtask3.get("message") == "success":
                                        reward = dtask3["data"]['reward']
                                        self.log(
                                            f"{Fore.LIGHTYELLOW_EX}Task completed: {Fore.LIGHTWHITE_EX}{tag} {Fore.LIGHTYELLOW_EX}Received: {Fore.LIGHTWHITE_EX}{reward}")

                    else:

                        return response

                except Exception as e:
                    self.log(f"{Fore.LIGHTRED_EX}Task error: {e}")
                time.sleep(1)


               
               
                #task banner
                try:
                    tasks = self.banner_info(data=data).json()

                    for project in tasks.get('data', []):
                        task_list = project.get('title', [])

                        dtask = self.banner_task(data=data, task_tag=task_list).json()

                        status_d = dtask["data"]["user_project_status"]
                        if status_d == 2:
                            task_list1 = dtask["data"].get("list", [])
                            all_status_one = False
                            for task1 in task_list1:
                                status = task1.get("user_task_status")

                                if status == 2:
                                    tag = task1.get('task_tag')
                                    self.do_banner(data=data, task_tag=tag).json()
                                else:
                                    all_status_one = True
                            if all_status_one:

                                proj = self.do_project(data=data, task_tag=task_list).json()

                                if proj.get("message") == "success":
                                    rew = proj["data"]["reward"]
                                    self.log(f"{Fore.LIGHTYELLOW_EX}Task completed: {Fore.LIGHTWHITE_EX}{task_list} {Fore.LIGHTYELLOW_EX}Received: {Fore.LIGHTWHITE_EX}{rew}")

                except Exception as e:
                    self.log(f"{Fore.LIGHTRED_EX}Task error: {e}")
                time.sleep(1)
                
                
               
               
                #Claim 8hrs
                try:
                    info = self.claim(data=data).json()

                    claim = info["data"]
                    if claim:
                        self.log(f"{Fore.LIGHTYELLOW_EX}Reward claimed")
                    else:
                        self.log(f"{Fore.LIGHTYELLOW_EX}Cooldown for reward not finished yet")
                except Exception as e:
                    self.log(f"{Fore.LIGHTRED_EX}Reward error!")
                time.sleep(1)
                
                
                
                
                #check-in
                try:
                    check_in = self.check_in(data=data).json()

                    if check_in["data"]["check_in_status"] == 1:
                        self.log(f"{Fore.LIGHTYELLOW_EX}Check-in done")
                    else:
                        self.log(f"{Fore.LIGHTYELLOW_EX}Check-in has been claimed before")
                except Exception as e:
                    self.log(f"{Fore.LIGHTRED_EX}Check-in error!")
                time.sleep(1)


                
                
                #level-up
                try:
                    level_up = self.level_up(data=data).json()

                    current_level = level_up['data']['user']["level"]
                    if level_up["message"] == "success":
                        self.log(f"{Fore.LIGHTYELLOW_EX}Upgraded")
                        self.log(f"{Fore.LIGHTYELLOW_EX}Current level: {Fore.LIGHTWHITE_EX}{current_level}")
                    else:
                        self.log(f"{Fore.LIGHTYELLOW_EX}Upgrade not yet available")
                except Exception as e:
                    self.log(f"{Fore.LIGHTRED_EX}Level-up error!")
                end_at_list.append(time.time())
                time.sleep(1)


                #cooldown for next account
                self.log(f"{Fore.LIGHTYELLOW_EX}----------> Wait 20s to run next account")
                time.sleep(20)

            
            if end_at_list:
                self.log(self.line)
                min_time = min(end_at_list)
                max_time = max(end_at_list)
                interval = max_time - min_time
                self.log(f"{Fore.LIGHTYELLOW_EX}Task completion time: {Fore.LIGHTWHITE_EX}{interval:.2f} sec.")
            else:
                self.log(f"{Fore.LIGHTYELLOW_EX}No tasks found for execution")


            
            #next turn
            self.log(self.line)
            self.log(f"{Fore.LIGHTYELLOW_EX}Sleeping: {Fore.LIGHTWHITE_EX} 8 hours")
            self.log(self.line)
            time.sleep(8*3600+60)

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    init(autoreset=True)
    tabi = TabiZoo()
    tabi.main()
