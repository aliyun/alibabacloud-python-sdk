# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateWhiteIpsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpdateWhiteIpsResponseBodyResult = None,
    ):
        # The updated whitelist.
        self.request_id = request_id
        # The network configurations.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.UpdateWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class UpdateWhiteIpsResponseBodyResult(DaraModel):
    def __init__(
        self,
        es_ipwhitelist: List[str] = None,
        network_config: main_models.UpdateWhiteIpsResponseBodyResultNetworkConfig = None,
    ):
        # The list of whitelists.
        self.es_ipwhitelist = es_ipwhitelist
        # The name of the whitelist. By default, the default whitelist is included.
        self.network_config = network_config

    def validate(self):
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.es_ipwhitelist is not None:
            result['esIPWhitelist'] = self.es_ipwhitelist

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esIPWhitelist') is not None:
            self.es_ipwhitelist = m.get('esIPWhitelist')

        if m.get('networkConfig') is not None:
            temp_model = main_models.UpdateWhiteIpsResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        return self

class UpdateWhiteIpsResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        white_ip_group_list: List[main_models.UpdateWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList] = None,
    ):
        # The IP addresses in the whitelist.
        self.white_ip_group_list = white_ip_group_list

    def validate(self):
        if self.white_ip_group_list:
            for v1 in self.white_ip_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k1 in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k1 in m.get('whiteIpGroupList'):
                temp_model = main_models.UpdateWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k1))

        return self

class UpdateWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # The type of the whitelist. The value of this parameter is fixed as PRIVATE_ES, which indicates a private IP address whitelist.
        self.group_name = group_name
        self.ips = ips
        self.white_ip_type = white_ip_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.ips is not None:
            result['ips'] = self.ips

        if self.white_ip_type is not None:
            result['whiteIpType'] = self.white_ip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('ips') is not None:
            self.ips = m.get('ips')

        if m.get('whiteIpType') is not None:
            self.white_ip_type = m.get('whiteIpType')

        return self

