from twisted.internet import defer
import logging
import treq
import json

logger = logging.getLogger("DiscourseAPI")


class DiscourseApiError(Exception):
    pass


class DiscourseConfigError(Exception):
    pass


class DiscourseClient(object):
    def __init__(self, dc_host, dc_key, dc_username):
        self.host = dc_host
        self.api_key = dc_key
        self.api_username = dc_username

    def request(self, request_type, method, payload={}):
        def _read_response(response):
            #logger.info("Received Data: %s", response)
            if response.code != 200:
                raise DiscourseApiError("{}".format(response.phrase))
            return response.content()

        def print_response(response):
            print(response)
            return response

        payload.update(dict(api_key=self.api_key,
                            api_username=self.api_username))

        dfr = treq.request(request_type, "{}{}".format(self.host, method),
                           params=payload,
                           headers={"Content-Type": "application/json"})

        return dfr.addCallback(_read_response)

#TOPICS:
    def create_topic(self, title, topic_body,
                     category=None, skip_val=True, auto_track=False):

        return self.request('POST', '/posts', {'title': title,
                                               'raw': topic_body,
                                               'category': category,
                                               'skip_validations': skip_val,
                                               'auto_track': auto_track})
        # "reply_to_post_number"

    def latest_topics(self):
        return self.request('GET', '/latest.json')

    def new_topics(self):
        return self.request('GET', '/new.json')

    def rename_topic(self, topic_id, title):
        return self.request('PUT', '/t/{}.json'.format(topic_id),
                            {'title': title, 'topic_id': topic_id})

    def recategorize_topic(self, topic_id, category_id):
        return self.request('PUT', '/t/{}.json'.format(topic_id),
                            {'category_id': category_id, 'topic_id': topic_id})

    def get_topic(self, topic_id):
        return self.request('GET', '/t/{}.json'.format(topic_id))

    def topics_by(self, username):
        return self.request('GET',
                            '/topics/created-by/{}.json'.format(username))

    def delete_topic(self, topic_id):
        return self.request('DELETE', "/t/{}.json".format(topic_id))

#GROUPS:
    def create_group(self, name, visible=False):
        return self.request('POST', '/admin/groups',
                            {'group': {'name': name, 'visible': visible}})

    def get_all_groups(self):
        return self.request('GET', 'admin/groups')

#USERS:
    def activate_user(self, user_id):
        return self.request('PUT', 'admin/users/{}/activate'.format(user_id))

    def get_user(self, username):
        return self.request('GET', '/users/{}.json'.format(username))

    def update_avatar(self, username, av_file):
        return self.request('PUT',
                            '/users/{}/preferences/avatar'.format(username),
                            {'file': av_file})

    def update_email(self, username, email):
        return self.request('PUT',
                            '/users/{}/preferences/email'.format(username),
                            {'email': email})

    def update_user(self, username, params={}):
        return self.request('PUT', "/users/{}".format(username), params)

    def update_username(self, username, new_username):
        return self.request('PUT',
                            '/users/{}/preferences/username'.format(username),
                            {'new_username': new_username})

    def create_user(self, user_dict={}):
        def get_user_values(response):
            user_dict['password_confirmation'] = response['body']['value']
            user_dict['challenge'] = response['body']['challenge'][::-1]
            return user_dict

        def post_user_values(user_dict):
            return self.request('POST', '/users', user_dict)

        dfr = self.request('GET', '/users/hp.json')
        return dfr.addCallback(get_user_values).addCallback(post_user_values)

    def log_out_and_refresh_browser(self, user_id):
        self.request('POST',
                     '/admin/users/{}/log_out_and_refresh_browser'.format(user_id))

#PRIVATE MESSAGE:
    def get_private_messages(self, username):
        return self.request('GET',
                            'topics/private-messages/{}.json'.format(username))

#CATEGORIES:
    def create_category(self, name, color, text_color,
                        parent_category_id=None):
        return self.request('POST', '/categories',
                            {'name': name,
                             'color': color,
                             'text_color': text_color,
                             'parent_category_id': parent_category_id})

    def get_categories(self):
        return self.request('GET', '/categories.json')

    def category_latest_topics(self, category_slug):
        return self.request('GET',
                            'category/{}/l/latest.json'.format(category_slug))

#INVITES:
    def invite_users(self, user_dict={}):
        return self.request('POST', '/invites', user_dict)

    #NEEDS TESTING, MAY NEED MORE PARAMS
    def invite_user_to_topic(self, topic_id, user_id):
        return self.request('POST', '/t/{}/invite'.format(topic_id),
                            {'topic_id': topic_id, 'user_id': user_id})

    def disposable_tokens(self, params={}):
        return self.request('POST', '/invites/disposable', params)
