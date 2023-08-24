import requests, random, threading
r = requests.session()
def yout():
    try:
        while True:
            user='cxznsaeruomwvcxznsaeruomwv_'
            usery=str("".join(random.choice(user)for i in range(4)))
            url = (f'https://www.youtube.com/@{usery}')
            re = requests.get(url, ).text

            if not'404 Not Found' in re:
                a=1
            else:
                print(f' yout-hunt | @{usery} | ')
                message = f"""		
[ ! ] Done Get Youtube User Sir .
[ ! ] Attempts: Undefined
[ ! ] Username: @{usery} 
	
	- By King  @waawx
	"""
                url = f"https://api.telegram.org/bot6367966214:AAHfQ755Rvk0OjWYcEBS2Y-TEnwziMANxFM/sendMessage"
                params = {
	            "chat_id": -1001962598923,
	            "text": message
	        }
                requests.get(url, params=params)
    except:
        ff=3
threads = []
for i in range(50):
    thread1 = threading.Thread(target=yout)
    thread1.start()
    threads.append(thread1)
for thread2 in threads:
    thread2.join()
