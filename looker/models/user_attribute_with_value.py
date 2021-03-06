# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class UserAttributeWithValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserAttributeWithValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'label': 'str',
            'rank': 'int',
            'value': 'str',
            'user_id': 'int',
            'user_can_edit': 'bool',
            'value_is_hidden': 'bool',
            'user_attribute_id': 'int',
            'source': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'name': 'name',
            'label': 'label',
            'rank': 'rank',
            'value': 'value',
            'user_id': 'user_id',
            'user_can_edit': 'user_can_edit',
            'value_is_hidden': 'value_is_hidden',
            'user_attribute_id': 'user_attribute_id',
            'source': 'source',
            'can': 'can'
        }

        self._name = None
        self._label = None
        self._rank = None
        self._value = None
        self._user_id = None
        self._user_can_edit = None
        self._value_is_hidden = None
        self._user_attribute_id = None
        self._source = None
        self._can = None

    @property
    def name(self):
        """
        Gets the name of this UserAttributeWithValue.
        Name of user attribute

        :return: The name of this UserAttributeWithValue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserAttributeWithValue.
        Name of user attribute

        :param name: The name of this UserAttributeWithValue.
        :type: str
        """
        self._name = name

    @property
    def label(self):
        """
        Gets the label of this UserAttributeWithValue.
        Human-friendly label for user attribute

        :return: The label of this UserAttributeWithValue.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this UserAttributeWithValue.
        Human-friendly label for user attribute

        :param label: The label of this UserAttributeWithValue.
        :type: str
        """
        self._label = label

    @property
    def rank(self):
        """
        Gets the rank of this UserAttributeWithValue.
        Precedence for setting value on user (lowest wins)

        :return: The rank of this UserAttributeWithValue.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this UserAttributeWithValue.
        Precedence for setting value on user (lowest wins)

        :param rank: The rank of this UserAttributeWithValue.
        :type: int
        """
        self._rank = rank

    @property
    def value(self):
        """
        Gets the value of this UserAttributeWithValue.
        Value of attribute for user

        :return: The value of this UserAttributeWithValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserAttributeWithValue.
        Value of attribute for user

        :param value: The value of this UserAttributeWithValue.
        :type: str
        """
        self._value = value

    @property
    def user_id(self):
        """
        Gets the user_id of this UserAttributeWithValue.
        Id of User

        :return: The user_id of this UserAttributeWithValue.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserAttributeWithValue.
        Id of User

        :param user_id: The user_id of this UserAttributeWithValue.
        :type: int
        """
        self._user_id = user_id

    @property
    def user_can_edit(self):
        """
        Gets the user_can_edit of this UserAttributeWithValue.
        Can the user set this value

        :return: The user_can_edit of this UserAttributeWithValue.
        :rtype: bool
        """
        return self._user_can_edit

    @user_can_edit.setter
    def user_can_edit(self, user_can_edit):
        """
        Sets the user_can_edit of this UserAttributeWithValue.
        Can the user set this value

        :param user_can_edit: The user_can_edit of this UserAttributeWithValue.
        :type: bool
        """
        self._user_can_edit = user_can_edit

    @property
    def value_is_hidden(self):
        """
        Gets the value_is_hidden of this UserAttributeWithValue.
        If true, the \"value\" field will be null, because the attribute settings block access to this value

        :return: The value_is_hidden of this UserAttributeWithValue.
        :rtype: bool
        """
        return self._value_is_hidden

    @value_is_hidden.setter
    def value_is_hidden(self, value_is_hidden):
        """
        Sets the value_is_hidden of this UserAttributeWithValue.
        If true, the \"value\" field will be null, because the attribute settings block access to this value

        :param value_is_hidden: The value_is_hidden of this UserAttributeWithValue.
        :type: bool
        """
        self._value_is_hidden = value_is_hidden

    @property
    def user_attribute_id(self):
        """
        Gets the user_attribute_id of this UserAttributeWithValue.
        Id of User Attribute

        :return: The user_attribute_id of this UserAttributeWithValue.
        :rtype: int
        """
        return self._user_attribute_id

    @user_attribute_id.setter
    def user_attribute_id(self, user_attribute_id):
        """
        Sets the user_attribute_id of this UserAttributeWithValue.
        Id of User Attribute

        :param user_attribute_id: The user_attribute_id of this UserAttributeWithValue.
        :type: int
        """
        self._user_attribute_id = user_attribute_id

    @property
    def source(self):
        """
        Gets the source of this UserAttributeWithValue.
        How user got this value for this attribute

        :return: The source of this UserAttributeWithValue.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this UserAttributeWithValue.
        How user got this value for this attribute

        :param source: The source of this UserAttributeWithValue.
        :type: str
        """
        self._source = source

    @property
    def can(self):
        """
        Gets the can of this UserAttributeWithValue.
        Operations the current user is able to perform on this object

        :return: The can of this UserAttributeWithValue.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this UserAttributeWithValue.
        Operations the current user is able to perform on this object

        :param can: The can of this UserAttributeWithValue.
        :type: dict(str, bool)
        """
        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

