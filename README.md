##Description:

**UNDER CONSTRUCTION **

Discourse API wrapper written for [Twisted](https://twistedmatrix.com/trac/), the event-driven network programming framework written in Python.

##Installation:

	pip install tx_discource_api

###Requirements:

 - Twisted > 14.0.0
 - treq==0.2.1

 For development/testing:
 - nosetests == 1.3.4

###Usage:

Create a new client and give it hostname, you discourse api_key and username:
	
	from tx_discourse_api import DiscourseClient

	client = DiscourseClient(host, api_key, username)

Create a new topic:

	client.create_topic('title', 'text text text')

Get all topics created:
	
	client.topic_by('username')

returns a list of topics in a json string.

For more examples check out the test_api_calls.

##Testing:

At the moment tests only cover topics. To run tests:

 1. Add you instance of Discourse as DC_HOST, Discourse Api key as DC_API_KEY and username as DC_USERNAME as environment variables.

 2. Go tx_discourse_api library and run:

 	nosetests 