# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateKibanaWhiteIpsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.UpdateKibanaWhiteIpsResponseBodyResult = None,
    ):
        # The details of the Elasticsearch cluster.
        self.request_id = request_id
        # The private IP address whitelists for access to the Kibana console of the cluster.
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
            temp_model = main_models.UpdateKibanaWhiteIpsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class UpdateKibanaWhiteIpsResponseBodyResult(DaraModel):
    def __init__(
        self,
        kibana_ipwhitelist: List[str] = None,
        kibana_private_ipwhitelist: List[str] = None,
        network_config: main_models.UpdateKibanaWhiteIpsResponseBodyResultNetworkConfig = None,
    ):
        # The public IP address whitelists for access to the Kibana console of the cluster.
        self.kibana_ipwhitelist = kibana_ipwhitelist
        # The private IP address whitelists for access to the Kibana console of the cluster.
        self.kibana_private_ipwhitelist = kibana_private_ipwhitelist
        # The ID of the virtual private cloud (VPC).
        self.network_config = network_config

    def validate(self):
        if self.network_config:
            self.network_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kibana_ipwhitelist is not None:
            result['kibanaIPWhitelist'] = self.kibana_ipwhitelist

        if self.kibana_private_ipwhitelist is not None:
            result['kibanaPrivateIPWhitelist'] = self.kibana_private_ipwhitelist

        if self.network_config is not None:
            result['networkConfig'] = self.network_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kibanaIPWhitelist') is not None:
            self.kibana_ipwhitelist = m.get('kibanaIPWhitelist')

        if m.get('kibanaPrivateIPWhitelist') is not None:
            self.kibana_private_ipwhitelist = m.get('kibanaPrivateIPWhitelist')

        if m.get('networkConfig') is not None:
            temp_model = main_models.UpdateKibanaWhiteIpsResponseBodyResultNetworkConfig()
            self.network_config = temp_model.from_map(m.get('networkConfig'))

        return self

class UpdateKibanaWhiteIpsResponseBodyResultNetworkConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        vpc_id: str = None,
        vs_area: str = None,
        vswitch_id: str = None,
        white_ip_group_list: List[main_models.UpdateKibanaWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList] = None,
    ):
        # The IP address whitelists.
        self.type = type
        # The ID of the vSwitch.
        self.vpc_id = vpc_id
        # The network type.
        self.vs_area = vs_area
        # The region ID.
        self.vswitch_id = vswitch_id
        # The IP address whitelists.
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
        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vs_area is not None:
            result['vsArea'] = self.vs_area

        if self.vswitch_id is not None:
            result['vswitchId'] = self.vswitch_id

        result['whiteIpGroupList'] = []
        if self.white_ip_group_list is not None:
            for k1 in self.white_ip_group_list:
                result['whiteIpGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vsArea') is not None:
            self.vs_area = m.get('vsArea')

        if m.get('vswitchId') is not None:
            self.vswitch_id = m.get('vswitchId')

        self.white_ip_group_list = []
        if m.get('whiteIpGroupList') is not None:
            for k1 in m.get('whiteIpGroupList'):
                temp_model = main_models.UpdateKibanaWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList()
                self.white_ip_group_list.append(temp_model.from_map(k1))

        return self

class UpdateKibanaWhiteIpsResponseBodyResultNetworkConfigWhiteIpGroupList(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        ips: List[str] = None,
        white_ip_type: str = None,
    ):
        # The IP addresses in the whitelist.
        self.group_name = group_name
        # The IP addresses in the whitelist.
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

