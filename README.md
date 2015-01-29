# txDiscourse - Twisted Discourse Client

Discourse API wrapper written for [Twisted](https://twistedmatrix.com/trac/), the event-driven network programming framework written in Python.

## Installation:

	pip install txDiscourse

### Requirements:

 - Twisted > 14.0.0
 - treq==0.2.1
 - service-identity==14.0.0
 
For development/testing:
 - nosetests == 1.3.4

### Try it out!
Add your Discourse Hostname and Api Key and run:

	python txDiscourse/example.py

this should give you your latest posts.

### Usage:

Create a new client and give it your [discourse host, api key and username](https://meta.discourse.org/t/using-discourse-api/17587):
	
	from txDiscoure import DiscourseClient

	client = DiscourseClient(host, api_key, username)

Get latest topics:

	client.latest_topics

Create a new topic:

	client.create_topic('title', 'text text text')

Get all topics created:
	
	client.topic_by('username')

returns a list of topics in a json string.

For more examples check out the test_api_calls.

### Testing:

At the moment tests only cover topics. To run tests:

    export DC_HOST="test.discourse.com"
    export DC_API_KEY="1234567890"
    export DC_USERNAME="system"
    nosetest txDiscourse.test_api_calls


### License

Copyright 2015 Anouk Ruhaak

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.