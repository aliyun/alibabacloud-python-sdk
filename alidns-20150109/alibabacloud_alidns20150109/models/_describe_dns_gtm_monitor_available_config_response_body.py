# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmMonitorAvailableConfigResponseBody(DaraModel):
    def __init__(
        self,
        domain_ipv_4isp_city_nodes: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodes = None,
        domain_ipv_6isp_city_nodes: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodes = None,
        ipv_4isp_city_nodes: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodes = None,
        ipv_6isp_city_nodes: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodes = None,
        request_id: str = None,
    ):
        # The nodes that perform health checks on domain names that use public IPv4 addresses.
        self.domain_ipv_4isp_city_nodes = domain_ipv_4isp_city_nodes
        # The nodes that perform health checks on domain names that use public IPv6 addresses.
        self.domain_ipv_6isp_city_nodes = domain_ipv_6isp_city_nodes
        # The nodes that perform health checks on public IPv4 addresses.
        self.ipv_4isp_city_nodes = ipv_4isp_city_nodes
        # The nodes that perform health checks on public IPv6 addresses.
        self.ipv_6isp_city_nodes = ipv_6isp_city_nodes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_ipv_4isp_city_nodes:
            self.domain_ipv_4isp_city_nodes.validate()
        if self.domain_ipv_6isp_city_nodes:
            self.domain_ipv_6isp_city_nodes.validate()
        if self.ipv_4isp_city_nodes:
            self.ipv_4isp_city_nodes.validate()
        if self.ipv_6isp_city_nodes:
            self.ipv_6isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_ipv_4isp_city_nodes is not None:
            result['DomainIpv4IspCityNodes'] = self.domain_ipv_4isp_city_nodes.to_map()

        if self.domain_ipv_6isp_city_nodes is not None:
            result['DomainIpv6IspCityNodes'] = self.domain_ipv_6isp_city_nodes.to_map()

        if self.ipv_4isp_city_nodes is not None:
            result['Ipv4IspCityNodes'] = self.ipv_4isp_city_nodes.to_map()

        if self.ipv_6isp_city_nodes is not None:
            result['Ipv6IspCityNodes'] = self.ipv_6isp_city_nodes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainIpv4IspCityNodes') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodes()
            self.domain_ipv_4isp_city_nodes = temp_model.from_map(m.get('DomainIpv4IspCityNodes'))

        if m.get('DomainIpv6IspCityNodes') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodes()
            self.domain_ipv_6isp_city_nodes = temp_model.from_map(m.get('DomainIpv6IspCityNodes'))

        if m.get('Ipv4IspCityNodes') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodes()
            self.ipv_4isp_city_nodes = temp_model.from_map(m.get('Ipv4IspCityNodes'))

        if m.get('Ipv6IspCityNodes') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodes()
            self.ipv_6isp_city_nodes = temp_model.from_map(m.get('Ipv6IspCityNodes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodes(DaraModel):
    def __init__(
        self,
        ipv_6isp_city_node: List[main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodesIpv6IspCityNode] = None,
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
                temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodesIpv6IspCityNode()
                self.ipv_6isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodesIpv6IspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        ips: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodesIpv6IspCityNodeIps = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        # The city code.
        self.city_code = city_code
        # The display name of the city.
        self.city_name = city_name
        # Indicates whether the health check node is selected by default.
        self.default_selected = default_selected
        # The name of the node group.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   BGP: BGP node
        # *   OVERSEAS: node outside the Chinese mainland
        # *   ISP: ISP node
        self.group_type = group_type
        # This parameter is not returned.
        self.ips = ips
        # The ISP code.
        self.isp_code = isp_code
        # The display name of the ISP.
        self.isp_name = isp_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Ips') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodesIpv6IspCityNodeIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv6IspCityNodesIpv6IspCityNodeIps(DaraModel):
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

class DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodes(DaraModel):
    def __init__(
        self,
        ipv_4isp_city_node: List[main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodesIpv4IspCityNode] = None,
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
                temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodesIpv4IspCityNode()
                self.ipv_4isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodesIpv4IspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        ips: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodesIpv4IspCityNodeIps = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        # The city code.
        self.city_code = city_code
        # The display name of the city.
        self.city_name = city_name
        # Indicates whether the health check node is selected by default.
        self.default_selected = default_selected
        # The name of the node group.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   BGP: Border Gateway Protocol (BGP) node
        # *   OVERSEAS: node outside the Chinese mainland
        # *   ISP: ISP node
        self.group_type = group_type
        # The IP addresses of the health check nodes.
        self.ips = ips
        # The Internet service provider (ISP) code.
        self.isp_code = isp_code
        # The display name of the ISP.
        self.isp_name = isp_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Ips') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodesIpv4IspCityNodeIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyIpv4IspCityNodesIpv4IspCityNodeIps(DaraModel):
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

class DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodes(DaraModel):
    def __init__(
        self,
        domain_ipv_6isp_city_node: List[main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodesDomainIpv6IspCityNode] = None,
    ):
        self.domain_ipv_6isp_city_node = domain_ipv_6isp_city_node

    def validate(self):
        if self.domain_ipv_6isp_city_node:
            for v1 in self.domain_ipv_6isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainIpv6IspCityNode'] = []
        if self.domain_ipv_6isp_city_node is not None:
            for k1 in self.domain_ipv_6isp_city_node:
                result['DomainIpv6IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_ipv_6isp_city_node = []
        if m.get('DomainIpv6IspCityNode') is not None:
            for k1 in m.get('DomainIpv6IspCityNode'):
                temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodesDomainIpv6IspCityNode()
                self.domain_ipv_6isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodesDomainIpv6IspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        ips: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodesDomainIpv6IspCityNodeIps = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        # The city code.
        self.city_code = city_code
        # The display name of the city.
        self.city_name = city_name
        # Indicates whether the health check node is selected by default.
        self.default_selected = default_selected
        # The name of the node group.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   BGP: BGP node
        # *   OVERSEAS: node outside the Chinese mainland
        # *   ISP: ISP node
        self.group_type = group_type
        # This parameter is not returned.
        self.ips = ips
        # The ISP code.
        self.isp_code = isp_code
        # The display name of the ISP.
        self.isp_name = isp_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Ips') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodesDomainIpv6IspCityNodeIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv6IspCityNodesDomainIpv6IspCityNodeIps(DaraModel):
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
            result['ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodes(DaraModel):
    def __init__(
        self,
        domain_ipv_4isp_city_node: List[main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodesDomainIpv4IspCityNode] = None,
    ):
        self.domain_ipv_4isp_city_node = domain_ipv_4isp_city_node

    def validate(self):
        if self.domain_ipv_4isp_city_node:
            for v1 in self.domain_ipv_4isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainIpv4IspCityNode'] = []
        if self.domain_ipv_4isp_city_node is not None:
            for k1 in self.domain_ipv_4isp_city_node:
                result['DomainIpv4IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_ipv_4isp_city_node = []
        if m.get('DomainIpv4IspCityNode') is not None:
            for k1 in m.get('DomainIpv4IspCityNode'):
                temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodesDomainIpv4IspCityNode()
                self.domain_ipv_4isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodesDomainIpv4IspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        default_selected: bool = None,
        group_name: str = None,
        group_type: str = None,
        ips: main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodesDomainIpv4IspCityNodeIps = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        # The city code.
        self.city_code = city_code
        # The display name of the city.
        self.city_name = city_name
        # Indicates whether the health check node is selected by default.
        self.default_selected = default_selected
        # The name of the node group.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   BGP: BGP node
        # *   OVERSEAS: node outside the Chinese mainland
        # *   ISP: ISP node
        self.group_type = group_type
        # The IP addresses of the health check nodes.
        self.ips = ips
        # The ISP code.
        self.isp_code = isp_code
        # The display name of the ISP.
        self.isp_name = isp_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Ips') is not None:
            temp_model = main_models.DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodesDomainIpv4IspCityNodeIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

class DescribeDnsGtmMonitorAvailableConfigResponseBodyDomainIpv4IspCityNodesDomainIpv4IspCityNodeIps(DaraModel):
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

