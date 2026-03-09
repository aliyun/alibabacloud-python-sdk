# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCNetworkInterfacesResponseBody(DaraModel):
    def __init__(
        self,
        network_interface_sets: List[main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSets] = None,
        request_id: str = None,
    ):
        self.network_interface_sets = network_interface_sets
        self.request_id = request_id

    def validate(self):
        if self.network_interface_sets:
            for v1 in self.network_interface_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterfaceSets'] = []
        if self.network_interface_sets is not None:
            for k1 in self.network_interface_sets:
                result['NetworkInterfaceSets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_sets = []
        if m.get('NetworkInterfaceSets') is not None:
            for k1 in m.get('NetworkInterfaceSets'):
                temp_model = main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSets()
                self.network_interface_sets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSets(DaraModel):
    def __init__(
        self,
        associated_public_ip: main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsAssociatedPublicIp = None,
        creation_time: str = None,
        description: str = None,
        instance_id: str = None,
        ipv_6sets: List[main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsIpv6Sets] = None,
        mac_address: str = None,
        network_interface_id: str = None,
        private_ip_sets: List[main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsPrivateIpSets] = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        status: str = None,
        tags: List[main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsTags] = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.associated_public_ip = associated_public_ip
        self.creation_time = creation_time
        self.description = description
        self.instance_id = instance_id
        self.ipv_6sets = ipv_6sets
        self.mac_address = mac_address
        self.network_interface_id = network_interface_id
        self.private_ip_sets = private_ip_sets
        self.resource_group_id = resource_group_id
        self.security_group_ids = security_group_ids
        self.status = status
        self.tags = tags
        self.type = type
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.associated_public_ip:
            self.associated_public_ip.validate()
        if self.ipv_6sets:
            for v1 in self.ipv_6sets:
                 if v1:
                    v1.validate()
        if self.private_ip_sets:
            for v1 in self.private_ip_sets:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_public_ip is not None:
            result['AssociatedPublicIp'] = self.associated_public_ip.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Ipv6Sets'] = []
        if self.ipv_6sets is not None:
            for k1 in self.ipv_6sets:
                result['Ipv6Sets'].append(k1.to_map() if k1 else None)

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        result['PrivateIpSets'] = []
        if self.private_ip_sets is not None:
            for k1 in self.private_ip_sets:
                result['PrivateIpSets'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedPublicIp') is not None:
            temp_model = main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsAssociatedPublicIp()
            self.associated_public_ip = temp_model.from_map(m.get('AssociatedPublicIp'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.ipv_6sets = []
        if m.get('Ipv6Sets') is not None:
            for k1 in m.get('Ipv6Sets'):
                temp_model = main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsIpv6Sets()
                self.ipv_6sets.append(temp_model.from_map(k1))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        self.private_ip_sets = []
        if m.get('PrivateIpSets') is not None:
            for k1 in m.get('PrivateIpSets'):
                temp_model = main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsPrivateIpSets()
                self.private_ip_sets.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsPrivateIpSets(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        private_ip_address: str = None,
    ):
        self.primary = primary
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary is not None:
            result['Primary'] = self.primary

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        return self

class DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        self.ipv_6address = ipv_6address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        return self

class DescribeRCNetworkInterfacesResponseBodyNetworkInterfaceSetsAssociatedPublicIp(DaraModel):
    def __init__(
        self,
        public_ip_address: str = None,
    ):
        self.public_ip_address = public_ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        return self

