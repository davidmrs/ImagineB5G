# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from capif_events.models.base_model_ import Model
from capif_events.models.invalid_param import InvalidParam
import re
from capif_events import util

from capif_events.models.invalid_param import InvalidParam  # noqa: E501
import re  # noqa: E501

class ProblemDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, cause=None, invalid_params=None, supported_features=None):  # noqa: E501
        """ProblemDetails - a model defined in OpenAPI

        :param type: The type of this ProblemDetails.  # noqa: E501
        :type type: str
        :param title: The title of this ProblemDetails.  # noqa: E501
        :type title: str
        :param status: The status of this ProblemDetails.  # noqa: E501
        :type status: int
        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type detail: str
        :param instance: The instance of this ProblemDetails.  # noqa: E501
        :type instance: str
        :param cause: The cause of this ProblemDetails.  # noqa: E501
        :type cause: str
        :param invalid_params: The invalid_params of this ProblemDetails.  # noqa: E501
        :type invalid_params: List[InvalidParam]
        :param supported_features: The supported_features of this ProblemDetails.  # noqa: E501
        :type supported_features: str
        """
        self.openapi_types = {
            'type': str,
            'title': str,
            'status': int,
            'detail': str,
            'instance': str,
            'cause': str,
            'invalid_params': List[InvalidParam],
            'supported_features': str
        }

        self.attribute_map = {
            'type': 'type',
            'title': 'title',
            'status': 'status',
            'detail': 'detail',
            'instance': 'instance',
            'cause': 'cause',
            'invalid_params': 'invalidParams',
            'supported_features': 'supportedFeatures'
        }

        self._type = type
        self._title = title
        self._status = status
        self._detail = detail
        self._instance = instance
        self._cause = cause
        self._invalid_params = invalid_params
        self._supported_features = supported_features

    @classmethod
    def from_dict(cls, dikt) -> 'ProblemDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProblemDetails of this ProblemDetails.  # noqa: E501
        :rtype: ProblemDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this ProblemDetails.

        string providing an URI formatted according to IETF RFC 3986.  # noqa: E501

        :return: The type of this ProblemDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetails.

        string providing an URI formatted according to IETF RFC 3986.  # noqa: E501

        :param type: The type of this ProblemDetails.
        :type type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this ProblemDetails.

        A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem.  # noqa: E501

        :return: The title of this ProblemDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetails.

        A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem.  # noqa: E501

        :param title: The title of this ProblemDetails.
        :type title: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this ProblemDetails.

        The HTTP status code for this occurrence of the problem.  # noqa: E501

        :return: The status of this ProblemDetails.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetails.

        The HTTP status code for this occurrence of the problem.  # noqa: E501

        :param status: The status of this ProblemDetails.
        :type status: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this ProblemDetails.

        A human-readable explanation specific to this occurrence of the problem.  # noqa: E501

        :return: The detail of this ProblemDetails.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetails.

        A human-readable explanation specific to this occurrence of the problem.  # noqa: E501

        :param detail: The detail of this ProblemDetails.
        :type detail: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this ProblemDetails.

        string providing an URI formatted according to IETF RFC 3986.  # noqa: E501

        :return: The instance of this ProblemDetails.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ProblemDetails.

        string providing an URI formatted according to IETF RFC 3986.  # noqa: E501

        :param instance: The instance of this ProblemDetails.
        :type instance: str
        """

        self._instance = instance

    @property
    def cause(self):
        """Gets the cause of this ProblemDetails.

        A machine-readable application error cause specific to this occurrence of the problem. This IE should be present and provide application-related error information, if available.  # noqa: E501

        :return: The cause of this ProblemDetails.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this ProblemDetails.

        A machine-readable application error cause specific to this occurrence of the problem. This IE should be present and provide application-related error information, if available.  # noqa: E501

        :param cause: The cause of this ProblemDetails.
        :type cause: str
        """

        self._cause = cause

    @property
    def invalid_params(self):
        """Gets the invalid_params of this ProblemDetails.

        Description of invalid parameters, for a request rejected due to invalid parameters.  # noqa: E501

        :return: The invalid_params of this ProblemDetails.
        :rtype: List[InvalidParam]
        """
        return self._invalid_params

    @invalid_params.setter
    def invalid_params(self, invalid_params):
        """Sets the invalid_params of this ProblemDetails.

        Description of invalid parameters, for a request rejected due to invalid parameters.  # noqa: E501

        :param invalid_params: The invalid_params of this ProblemDetails.
        :type invalid_params: List[InvalidParam]
        """
        if invalid_params is not None and len(invalid_params) < 1:
            raise ValueError("Invalid value for `invalid_params`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._invalid_params = invalid_params

    @property
    def supported_features(self):
        """Gets the supported_features of this ProblemDetails.

        A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported  # noqa: E501

        :return: The supported_features of this ProblemDetails.
        :rtype: str
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this ProblemDetails.

        A string used to indicate the features supported by an API that is used as defined in clause 6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\", \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in table 5.2.2-3. The most significant character representing the highest-numbered features shall appear first in the string, and the character representing features 1 to 4 shall appear last in the string. The list of features and their numbering (starting with 1) are defined separately for each API. If the string contains a lower number of characters than there are defined features for an API, all features that would be represented by characters that are not present in the string are not supported  # noqa: E501

        :param supported_features: The supported_features of this ProblemDetails.
        :type supported_features: str
        """
        if supported_features is not None and not re.search(r'^[A-Fa-f0-9]*$', supported_features):  # noqa: E501
            raise ValueError("Invalid value for `supported_features`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supported_features = supported_features
