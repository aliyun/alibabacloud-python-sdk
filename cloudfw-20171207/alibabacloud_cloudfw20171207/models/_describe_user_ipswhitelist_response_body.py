# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeUserIPSWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6whitelists: List[main_models.DescribeUserIPSWhitelistResponseBodyIpv6Whitelists] = None,
        request_id: str = None,
        whitelists: List[main_models.DescribeUserIPSWhitelistResponseBodyWhitelists] = None,
    ):
        self.ipv_6whitelists = ipv_6whitelists
        self.request_id = request_id
        self.whitelists = whitelists

    def validate(self):
        if self.ipv_6whitelists:
            for v1 in self.ipv_6whitelists:
                 if v1:
                    v1.validate()
        if self.whitelists:
            for v1 in self.whitelists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Whitelists'] = []
        if self.ipv_6whitelists is not None:
            for k1 in self.ipv_6whitelists:
                result['Ipv6Whitelists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Whitelists'] = []
        if self.whitelists is not None:
            for k1 in self.whitelists:
                result['Whitelists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6whitelists = []
        if m.get('Ipv6Whitelists') is not None:
            for k1 in m.get('Ipv6Whitelists'):
                temp_model = main_models.DescribeUserIPSWhitelistResponseBodyIpv6Whitelists()
                self.ipv_6whitelists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.whitelists = []
        if m.get('Whitelists') is not None:
            for k1 in m.get('Whitelists'):
                temp_model = main_models.DescribeUserIPSWhitelistResponseBodyWhitelists()
                self.whitelists.append(temp_model.from_map(k1))

        return self

class DescribeUserIPSWhitelistResponseBodyWhitelists(DaraModel):
    def __init__(
        self,
        direction: int = None,
        list_type: int = None,
        list_value: str = None,
        white_list_value: List[str] = None,
        white_type: int = None,
    ):
        self.direction = direction
        self.list_type = list_type
        self.list_value = list_value
        self.white_list_value = white_list_value
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.list_value is not None:
            result['ListValue'] = self.list_value

        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value

        if self.white_type is not None:
            result['WhiteType'] = self.white_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')

        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')

        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')

        return self

class DescribeUserIPSWhitelistResponseBodyIpv6Whitelists(DaraModel):
    def __init__(
        self,
        direction: int = None,
        list_type: int = None,
        list_value: str = None,
        white_list_value: List[str] = None,
        white_type: int = None,
    ):
        self.direction = direction
        self.list_type = list_type
        self.list_value = list_value
        self.white_list_value = white_list_value
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.list_value is not None:
            result['ListValue'] = self.list_value

        if self.white_list_value is not None:
            result['WhiteListValue'] = self.white_list_value

        if self.white_type is not None:
            result['WhiteType'] = self.white_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')

        if m.get('WhiteListValue') is not None:
            self.white_list_value = m.get('WhiteListValue')

        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')

        return self

