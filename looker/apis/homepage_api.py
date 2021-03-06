# coding: utf-8

"""
HomepageApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class HomepageApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def all_homepage_items(self, **kwargs):
        """
        Get All Homepage Items
        ### Get information about all homepage items.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_homepage_items(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param str sorts: Fields to sort by.
        :param str homepage_section_id: Filter to a specific homepage section
        :return: list[HomepageItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'sorts', 'homepage_section_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_homepage_items" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/homepage_items'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'sorts' in params:
            query_params['sorts'] = params['sorts']
        if 'homepage_section_id' in params:
            query_params['homepage_section_id'] = params['homepage_section_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[HomepageItem]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def all_homepage_sections(self, **kwargs):
        """
        Get All Homepage sections
        ### Get information about all homepage sections.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_homepage_sections(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :param str sorts: Fields to sort by.
        :return: list[HomepageSection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields', 'sorts']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_homepage_sections" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/homepage_sections'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'sorts' in params:
            query_params['sorts'] = params['sorts']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[HomepageSection]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_homepage_item(self, **kwargs):
        """
        Create Homepage Item
        ### Create a new homepage item.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_homepage_item(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HomepageItem body: Homepage Item
        :param str fields: Requested fields.
        :return: HomepageItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_homepage_item" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/homepage_items'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HomepageItem',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_homepage_section(self, **kwargs):
        """
        Create Homepage section
        ### Create a new homepage section.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_homepage_section(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HomepageSection body: Homepage section
        :param str fields: Requested fields.
        :return: HomepageSection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_homepage_section" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/homepage_sections'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HomepageSection',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_homepage_item(self, homepage_item_id, **kwargs):
        """
        Delete Homepage Item
        ### Delete a homepage item.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_homepage_item(homepage_item_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int homepage_item_id: Id of homepage_item (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['homepage_item_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_homepage_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'homepage_item_id' is set
        if ('homepage_item_id' not in params) or (params['homepage_item_id'] is None):
            raise ValueError("Missing the required parameter `homepage_item_id` when calling `delete_homepage_item`")

        resource_path = '/homepage_items/{homepage_item_id}'.replace('{format}', 'json')
        path_params = {}
        if 'homepage_item_id' in params:
            path_params['homepage_item_id'] = params['homepage_item_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_homepage_section(self, homepage_section_id, **kwargs):
        """
        Delete Homepage section
        ### Delete a homepage section.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_homepage_section(homepage_section_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int homepage_section_id: Id of homepage_section (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['homepage_section_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_homepage_section" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'homepage_section_id' is set
        if ('homepage_section_id' not in params) or (params['homepage_section_id'] is None):
            raise ValueError("Missing the required parameter `homepage_section_id` when calling `delete_homepage_section`")

        resource_path = '/homepage_sections/{homepage_section_id}'.replace('{format}', 'json')
        path_params = {}
        if 'homepage_section_id' in params:
            path_params['homepage_section_id'] = params['homepage_section_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def homepage_item(self, homepage_item_id, **kwargs):
        """
        Get Homepage Item
        ### Get information about a homepage item.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.homepage_item(homepage_item_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int homepage_item_id: Id of homepage item (required)
        :param str fields: Requested fields.
        :return: HomepageItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['homepage_item_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method homepage_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'homepage_item_id' is set
        if ('homepage_item_id' not in params) or (params['homepage_item_id'] is None):
            raise ValueError("Missing the required parameter `homepage_item_id` when calling `homepage_item`")

        resource_path = '/homepage_items/{homepage_item_id}'.replace('{format}', 'json')
        path_params = {}
        if 'homepage_item_id' in params:
            path_params['homepage_item_id'] = params['homepage_item_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HomepageItem',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def homepage_section(self, homepage_section_id, **kwargs):
        """
        Get Homepage section
        ### Get information about a homepage section.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.homepage_section(homepage_section_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int homepage_section_id: Id of homepage section (required)
        :param str fields: Requested fields.
        :return: HomepageSection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['homepage_section_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method homepage_section" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'homepage_section_id' is set
        if ('homepage_section_id' not in params) or (params['homepage_section_id'] is None):
            raise ValueError("Missing the required parameter `homepage_section_id` when calling `homepage_section`")

        resource_path = '/homepage_sections/{homepage_section_id}'.replace('{format}', 'json')
        path_params = {}
        if 'homepage_section_id' in params:
            path_params['homepage_section_id'] = params['homepage_section_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HomepageSection',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_homepage_item(self, homepage_item_id, body, **kwargs):
        """
        Update Homepage Item
        ### Update a homepage item definition.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_homepage_item(homepage_item_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int homepage_item_id: Id of homepage item (required)
        :param HomepageItem body: Homepage Item (required)
        :param str fields: Requested fields.
        :return: HomepageItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['homepage_item_id', 'body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_homepage_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'homepage_item_id' is set
        if ('homepage_item_id' not in params) or (params['homepage_item_id'] is None):
            raise ValueError("Missing the required parameter `homepage_item_id` when calling `update_homepage_item`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_homepage_item`")

        resource_path = '/homepage_items/{homepage_item_id}'.replace('{format}', 'json')
        path_params = {}
        if 'homepage_item_id' in params:
            path_params['homepage_item_id'] = params['homepage_item_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HomepageItem',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_homepage_section(self, homepage_section_id, body, **kwargs):
        """
        Update Homepage section
        ### Update a homepage section definition.\n

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_homepage_section(homepage_section_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int homepage_section_id: Id of homepage section (required)
        :param HomepageSection body: Homepage section (required)
        :param str fields: Requested fields.
        :return: HomepageSection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['homepage_section_id', 'body', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_homepage_section" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'homepage_section_id' is set
        if ('homepage_section_id' not in params) or (params['homepage_section_id'] is None):
            raise ValueError("Missing the required parameter `homepage_section_id` when calling `update_homepage_section`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_homepage_section`")

        resource_path = '/homepage_sections/{homepage_section_id}'.replace('{format}', 'json')
        path_params = {}
        if 'homepage_section_id' in params:
            path_params['homepage_section_id'] = params['homepage_section_id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='HomepageSection',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
