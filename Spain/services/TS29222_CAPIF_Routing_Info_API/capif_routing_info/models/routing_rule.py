# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from capif_routing_info.models.base_model_ import Model
from capif_routing_info.models.aef_profile import AefProfile
from capif_routing_info.models.ipv4_address_range import Ipv4AddressRange
from capif_routing_info.models.ipv6_address_range import Ipv6AddressRange
from capif_routing_info import util

from capif_routing_info.models.aef_profile import AefProfile  # noqa: E501
from capif_routing_info.models.ipv4_address_range import Ipv4AddressRange  # noqa: E501
from capif_routing_info.models.ipv6_address_range import Ipv6AddressRange  # noqa: E501

class RoutingRule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ipv4_addr_ranges=None, ipv6_addr_ranges=None, aef_profile=None):  # noqa: E501
        """RoutingRule - a model defined in OpenAPI

        :param ipv4_addr_ranges: The ipv4_addr_ranges of this RoutingRule.  # noqa: E501
        :type ipv4_addr_ranges: List[Ipv4AddressRange]
        :param ipv6_addr_ranges: The ipv6_addr_ranges of this RoutingRule.  # noqa: E501
        :type ipv6_addr_ranges: List[Ipv6AddressRange]
        :param aef_profile: The aef_profile of this RoutingRule.  # noqa: E501
        :type aef_profile: AefProfile
        """
        self.openapi_types = {
            'ipv4_addr_ranges': List[Ipv4AddressRange],
            'ipv6_addr_ranges': List[Ipv6AddressRange],
            'aef_profile': AefProfile
        }

        self.attribute_map = {
            'ipv4_addr_ranges': 'ipv4AddrRanges',
            'ipv6_addr_ranges': 'ipv6AddrRanges',
            'aef_profile': 'aefProfile'
        }

        self._ipv4_addr_ranges = ipv4_addr_ranges
        self._ipv6_addr_ranges = ipv6_addr_ranges
        self._aef_profile = aef_profile

    @classmethod
    def from_dict(cls, dikt) -> 'RoutingRule':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RoutingRule of this RoutingRule.  # noqa: E501
        :rtype: RoutingRule
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ipv4_addr_ranges(self):
        """Gets the ipv4_addr_ranges of this RoutingRule.


        :return: The ipv4_addr_ranges of this RoutingRule.
        :rtype: List[Ipv4AddressRange]
        """
        return self._ipv4_addr_ranges

    @ipv4_addr_ranges.setter
    def ipv4_addr_ranges(self, ipv4_addr_ranges):
        """Sets the ipv4_addr_ranges of this RoutingRule.


        :param ipv4_addr_ranges: The ipv4_addr_ranges of this RoutingRule.
        :type ipv4_addr_ranges: List[Ipv4AddressRange]
        """
        if ipv4_addr_ranges is not None and len(ipv4_addr_ranges) < 1:
            raise ValueError("Invalid value for `ipv4_addr_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv4_addr_ranges = ipv4_addr_ranges

    @property
    def ipv6_addr_ranges(self):
        """Gets the ipv6_addr_ranges of this RoutingRule.


        :return: The ipv6_addr_ranges of this RoutingRule.
        :rtype: List[Ipv6AddressRange]
        """
        return self._ipv6_addr_ranges

    @ipv6_addr_ranges.setter
    def ipv6_addr_ranges(self, ipv6_addr_ranges):
        """Sets the ipv6_addr_ranges of this RoutingRule.


        :param ipv6_addr_ranges: The ipv6_addr_ranges of this RoutingRule.
        :type ipv6_addr_ranges: List[Ipv6AddressRange]
        """
        if ipv6_addr_ranges is not None and len(ipv6_addr_ranges) < 1:
            raise ValueError("Invalid value for `ipv6_addr_ranges`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ipv6_addr_ranges = ipv6_addr_ranges

    @property
    def aef_profile(self):
        """Gets the aef_profile of this RoutingRule.


        :return: The aef_profile of this RoutingRule.
        :rtype: AefProfile
        """
        return self._aef_profile

    @aef_profile.setter
    def aef_profile(self, aef_profile):
        """Sets the aef_profile of this RoutingRule.


        :param aef_profile: The aef_profile of this RoutingRule.
        :type aef_profile: AefProfile
        """
        if aef_profile is None:
            raise ValueError("Invalid value for `aef_profile`, must not be `None`")  # noqa: E501

        self._aef_profile = aef_profile
