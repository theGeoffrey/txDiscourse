from txDiscourse import DiscourseClient
from twisted.internet import reactor
 
from pprint import pprint
import json
 
host = "http://HOSTNAME.TLD"
api_key = "XXXXXX" # to be found at /admin/api
username = "system"
 
client = DiscourseClient(host, api_key, username)
 
if __name__ == "__main__":
client.latest_topics(
).addCallback(json.loads
).addCallback(pprint
).addCallback(lambda x:reactor.stop())
 
reactor.run() 