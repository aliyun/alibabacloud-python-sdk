# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListCloudGtmMonitorNodesResponseBody(DaraModel):
    def __init__(
        self,
        ipv_4isp_city_nodes: main_models.ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodes = None,
        ipv_6isp_city_nodes: main_models.ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodes = None,
        request_id: str = None,
    ):
        # Public IPv4 monitoring node list.
        self.ipv_4isp_city_nodes = ipv_4isp_city_nodes
        # List of public IPv6 monitoring nodes.
        self.ipv_6isp_city_nodes = ipv_6isp_city_nodes
        # Unique request identification code.
        self.request_id = request_id

    def validate(self):
        if self.ipv_4isp_city_nodes:
            self.ipv_4isp_city_nodes.validate()
        if self.ipv_6isp_city_nodes:
            self.ipv_6isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4isp_city_nodes is not None:
            result['Ipv4IspCityNodes'] = self.ipv_4isp_city_nodes.to_map()

        if self.ipv_6isp_city_nodes is not None:
            result['Ipv6IspCityNodes'] = self.ipv_6isp_city_nodes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4IspCityNodes') is not None:
            temp_model = main_models.ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodes()
            self.ipv_4isp_city_nodes = temp_model.from_map(m.get('Ipv4IspCityNodes'))

        if m.get('Ipv6IspCityNodes') is not None:
            temp_model = main_models.ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodes()
            self.ipv_6isp_city_nodes = temp_model.from_map(m.get('Ipv6IspCityNodes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodes(DaraModel):
    def __init__(
        self,
        ipv_6isp_city_node: List[main_models.ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodesIpv6IspCityNode] = None,
    ):
        self.ipv_6isp_city_node = ipv_6isp_city_node

    def validate(self):
        if self.ipv_6isp_city_node:
            for v1 in self.ipv_6isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6IspCityNode'] = []
        if self.ipv_6isp_city_node is not None:
            for k1 in self.ipv_6isp_city_node:
                result['Ipv6IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6isp_city_node = []
        if m.get('Ipv6IspCityNode') is not None:
            for k1 in m.get('Ipv6IspCityNode'):
                temp_model = main_models.ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodesIpv6IspCityNode()
                self.ipv_6isp_city_node.append(temp_model.from_map(k1))

        return self

class ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodesIpv6IspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        country_code: str = None,
        country_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        ips: main_models.ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodesIpv6IspCityNodeIps = None,
        isp_code: str = None,
        isp_name: str = None,
        node_id: str = None,
    ):
        # City code.
        self.city_code = city_code
        # City name.
        self.city_name = city_name
        # Country code.
        self.country_code = country_code
        # Country name.
        self.country_name = country_name
        # Monitor node default selection:
        # - true: Selected by default
        # - false: Not selected by default
        self.default_selected = default_selected
        # Monitoring probe group name.
        self.group_name = group_name
        # Monitoring node group type, currently supported:
        # - BGP: BGP node
        # - OVERSEAS: International node
        # - ISP: Carrier node
        self.group_type = group_type
        # List of node IP addresses.
        self.ips = ips
        # Operator code.
        self.isp_code = isp_code
        # Operator name.
        self.isp_name = isp_name
        # Unique identifier ID of the probe node.
        self.node_id = node_id

    def validate(self):
        if self.ips:
            self.ips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.ips is not None:
            result['Ips'] = self.ips.to_map()

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Ips') is not None:
            temp_model = main_models.ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodesIpv6IspCityNodeIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class ListCloudGtmMonitorNodesResponseBodyIpv6IspCityNodesIpv6IspCityNodeIps(DaraModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodes(DaraModel):
    def __init__(
        self,
        ipv_4isp_city_node: List[main_models.ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodesIpv4IspCityNode] = None,
    ):
        self.ipv_4isp_city_node = ipv_4isp_city_node

    def validate(self):
        if self.ipv_4isp_city_node:
            for v1 in self.ipv_4isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv4IspCityNode'] = []
        if self.ipv_4isp_city_node is not None:
            for k1 in self.ipv_4isp_city_node:
                result['Ipv4IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4isp_city_node = []
        if m.get('Ipv4IspCityNode') is not None:
            for k1 in m.get('Ipv4IspCityNode'):
                temp_model = main_models.ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodesIpv4IspCityNode()
                self.ipv_4isp_city_node.append(temp_model.from_map(k1))

        return self

class ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodesIpv4IspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        country_code: str = None,
        country_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        ips: main_models.ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodesIpv4IspCityNodeIps = None,
        isp_code: str = None,
        isp_name: str = None,
        node_id: str = None,
    ):
        # City code.
        self.city_code = city_code
        # City name.
        self.city_name = city_name
        # Country code.
        self.country_code = country_code
        # Country name.
        self.country_name = country_name
        # Monitor node default selection:
        # - true: Selected by default
        # - false: Not selected by default
        self.default_selected = default_selected
        # Monitor probe group name.
        self.group_name = group_name
        # Monitoring node group type, currently supported:
        # - BGP: BGP node
        # - OVERSEAS: International node
        # - ISP: Carrier node
        self.group_type = group_type
        # List of node IP addresses.
        self.ips = ips
        # Operator code.
        self.isp_code = isp_code
        # Operator name.
        self.isp_name = isp_name
        # Unique identifier ID of the probe node.
        self.node_id = node_id

    def validate(self):
        if self.ips:
            self.ips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.ips is not None:
            result['Ips'] = self.ips.to_map()

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Ips') is not None:
            temp_model = main_models.ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodesIpv4IspCityNodeIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class ListCloudGtmMonitorNodesResponseBodyIpv4IspCityNodesIpv4IspCityNodeIps(DaraModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

