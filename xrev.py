# -*- coding: utf-8 -*-
import requests, re, sys, threading
from Queue import Queue
from itertools import cycle

# XploitSec #
# nicedre4m@yahoo.com #
# https://xploitsecid.or.id & https://www.linuxploit.com #
# why u see this source ? you want to recode it ? #

proxy = ""

def reverse_viewdns(ip):
	total = 0
	try:
		text = requests.get("https://viewdns.info/reverseip/?host="+ip+"&t=1", headers={"User-agent":"Linux Mozilla 5/0"}).text
		if "Sorry we could not find the IP address for the domain you specified." in text:
			pass
		else:
			dom = re.findall('</tr><tr> <td>(.*?)</td><td align="center">', text)
			for i in dom:
				ini = i
				w = open(result, "a")
				f = open(result).read()
				if ini in f:
					pass
				else:
					total = total + 1
					w.write(i+"\n")
					w.close()
	except:
		pass
	print("View DNS: "+str(total))

def hackertarget(ip):
	total = 0
	global proxy_cycle
	global proxy
	try:
		text = requests.get("http://api.hackertarget.com/reverseiplookup/?q="+ip, headers={"User-agent":"Linuz Mozilla 5/0"}, proxies=proxy, timeout=8).text
		if "error check your search parameter" in text:
			pass
		elif "API count exceeded - Increase Quota with Membership" in text:
			soc = next(proxy_cycle)
			proxy = {"http":soc,"https":soc}
			hackertarget(ip)
		else:
			dom = text.splitlines()
			for i in dom:
				ini = i
				w = open(result, "a")
				f = open(result).read()
				if ini in f:
					continue
				else:
					total = total + 1
					w.write(i+"\n")
					w.close()
	except:
		print("PROXY DIE")
		soc = next(proxy_cycle)
		proxy = {"http":soc,"https":soc}
		pass
	print("Hacker Target: "+str(total))

try:
	mmc = sys.argv[1]
	result = sys.argv[2]
	aburame = open(sys.argv[3]).read()
	hyuga = aburame.splitlines()
	proxy_cycle = cycle(hyuga)
	thre = sys.argv[4]
except:
	print ('\033[92mReverse Ip Lookup\033[91m Hackertarget & ViewDNS.info\033[91m')
	print('\033[97mpython xrev.py list.txt output.txt proxy.txt thread \033[91m')
	print('\033[97mEx : python xrev.py ips.txt result.txt proxy.txt 20 \033[97m')
	exit()

jobs = Queue()
def do_stuff(q):
	while not q.empty():
		i = q.get()
		reverse_viewdns(i)
		hackertarget(i)
		print("\n")
		q.task_done()

for i in open(mmc).read().splitlines():
	if i.startswith("http://"):
		y = i.split("http://")[1]
	elif i.startswith("https://"):
		y = i.split("https://")[1]
	else:
		y = i
	if "/" in y:
		final = y.split("/")[0]
	else:
		final = y
	jobs.put(final)

for i in range(int(thre)):
	worker = threading.Thread(target=do_stuff, args=(jobs,))
	worker.start()
jobs.join()