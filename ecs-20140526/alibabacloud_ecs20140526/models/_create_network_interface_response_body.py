# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateNetworkInterfaceResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        ipv_4prefix_sets: main_models.CreateNetworkInterfaceResponseBodyIpv4PrefixSets = None,
        ipv_6prefix_sets: main_models.CreateNetworkInterfaceResponseBodyIpv6PrefixSets = None,
        ipv_6sets: main_models.CreateNetworkInterfaceResponseBodyIpv6Sets = None,
        mac_address: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        owner_id: str = None,
        private_ip_address: str = None,
        private_ip_sets: main_models.CreateNetworkInterfaceResponseBodyPrivateIpSets = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_ids: main_models.CreateNetworkInterfaceResponseBodySecurityGroupIds = None,
        service_id: int = None,
        service_managed: bool = None,
        source_dest_check: bool = None,
        status: str = None,
        tags: main_models.CreateNetworkInterfaceResponseBodyTags = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The description of the ENI.
        self.description = description
        # The IPv4 prefixes assigned to the ENI.
        self.ipv_4prefix_sets = ipv_4prefix_sets
        # The IPv6 prefixes assigned to the ENI.
        self.ipv_6prefix_sets = ipv_6prefix_sets
        # The IPv6 addresses assigned to the ENI.
        self.ipv_6sets = ipv_6sets
        # The media access control (MAC) address of the ENI.
        self.mac_address = mac_address
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The name of the ENI.
        self.network_interface_name = network_interface_name
        # The ID of the account to which the ENI belongs.
        self.owner_id = owner_id
        # The private IP address of the ENI.
        self.private_ip_address = private_ip_address
        # The private IP addresses.
        self.private_ip_sets = private_ip_sets
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the ENI belongs.
        self.resource_group_id = resource_group_id
        # The IDs of the security groups to which the ENI belongs.
        self.security_group_ids = security_group_ids
        # The ID of the distributor to which the ENI belongs.
        self.service_id = service_id
        # Indicates whether the user of the ENI is an Alibaba Cloud service or a distributor.
        self.service_managed = service_managed
        # >  This parameter is in invitational preview and is not publicly available.
        self.source_dest_check = source_dest_check
        # The state of the ENI.
        self.status = status
        # The tags of the ENI.
        self.tags = tags
        # The type of the ENI.
        self.type = type
        # The ID of the vSwitch to which the ENI is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the ENI belongs.
        self.vpc_id = vpc_id
        # The zone ID of the ENI.
        self.zone_id = zone_id

    def validate(self):
        if self.ipv_4prefix_sets:
            self.ipv_4prefix_sets.validate()
        if self.ipv_6prefix_sets:
            self.ipv_6prefix_sets.validate()
        if self.ipv_6sets:
            self.ipv_6sets.validate()
        if self.private_ip_sets:
            self.private_ip_sets.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ipv_4prefix_sets is not None:
            result['Ipv4PrefixSets'] = self.ipv_4prefix_sets.to_map()

        if self.ipv_6prefix_sets is not None:
            result['Ipv6PrefixSets'] = self.ipv_6prefix_sets.to_map()

        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.private_ip_sets is not None:
            result['PrivateIpSets'] = self.private_ip_sets.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.service_id is not None:
            result['ServiceID'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.source_dest_check is not None:
            result['SourceDestCheck'] = self.source_dest_check

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Ipv4PrefixSets') is not None:
            temp_model = main_models.CreateNetworkInterfaceResponseBodyIpv4PrefixSets()
            self.ipv_4prefix_sets = temp_model.from_map(m.get('Ipv4PrefixSets'))

        if m.get('Ipv6PrefixSets') is not None:
            temp_model = main_models.CreateNetworkInterfaceResponseBodyIpv6PrefixSets()
            self.ipv_6prefix_sets = temp_model.from_map(m.get('Ipv6PrefixSets'))

        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.CreateNetworkInterfaceResponseBodyIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PrivateIpSets') is not None:
            temp_model = main_models.CreateNetworkInterfaceResponseBodyPrivateIpSets()
            self.private_ip_sets = temp_model.from_map(m.get('PrivateIpSets'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.CreateNetworkInterfaceResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('ServiceID') is not None:
            self.service_id = m.get('ServiceID')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('SourceDestCheck') is not None:
            self.source_dest_check = m.get('SourceDestCheck')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.CreateNetworkInterfaceResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateNetworkInterfaceResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.CreateNetworkInterfaceResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNetworkInterfaceResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateNetworkInterfaceResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

class CreateNetworkInterfaceResponseBodySecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class CreateNetworkInterfaceResponseBodyPrivateIpSets(DaraModel):
    def __init__(
        self,
        private_ip_set: List[main_models.CreateNetworkInterfaceResponseBodyPrivateIpSetsPrivateIpSet] = None,
    ):
        self.private_ip_set = private_ip_set

    def validate(self):
        if self.private_ip_set:
            for v1 in self.private_ip_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateIpSet'] = []
        if self.private_ip_set is not None:
            for k1 in self.private_ip_set:
                result['PrivateIpSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_ip_set = []
        if m.get('PrivateIpSet') is not None:
            for k1 in m.get('PrivateIpSet'):
                temp_model = main_models.CreateNetworkInterfaceResponseBodyPrivateIpSetsPrivateIpSet()
                self.private_ip_set.append(temp_model.from_map(k1))

        return self

class CreateNetworkInterfaceResponseBodyPrivateIpSetsPrivateIpSet(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        private_ip_address: str = None,
    ):
        # Indicates whether the private IP address is the primary private IP address.
        self.primary = primary
        # The private IP address of the instance.
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

class CreateNetworkInterfaceResponseBodyIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6set: List[main_models.CreateNetworkInterfaceResponseBodyIpv6SetsIpv6Set] = None,
    ):
        self.ipv_6set = ipv_6set

    def validate(self):
        if self.ipv_6set:
            for v1 in self.ipv_6set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6Set'] = []
        if self.ipv_6set is not None:
            for k1 in self.ipv_6set:
                result['Ipv6Set'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6set = []
        if m.get('Ipv6Set') is not None:
            for k1 in m.get('Ipv6Set'):
                temp_model = main_models.CreateNetworkInterfaceResponseBodyIpv6SetsIpv6Set()
                self.ipv_6set.append(temp_model.from_map(k1))

        return self

class CreateNetworkInterfaceResponseBodyIpv6SetsIpv6Set(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        # The IPv6 address assigned to the ENI.
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

class CreateNetworkInterfaceResponseBodyIpv6PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_6prefix_set: List[main_models.CreateNetworkInterfaceResponseBodyIpv6PrefixSetsIpv6PrefixSet] = None,
    ):
        self.ipv_6prefix_set = ipv_6prefix_set

    def validate(self):
        if self.ipv_6prefix_set:
            for v1 in self.ipv_6prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6PrefixSet'] = []
        if self.ipv_6prefix_set is not None:
            for k1 in self.ipv_6prefix_set:
                result['Ipv6PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6prefix_set = []
        if m.get('Ipv6PrefixSet') is not None:
            for k1 in m.get('Ipv6PrefixSet'):
                temp_model = main_models.CreateNetworkInterfaceResponseBodyIpv6PrefixSetsIpv6PrefixSet()
                self.ipv_6prefix_set.append(temp_model.from_map(k1))

        return self

class CreateNetworkInterfaceResponseBodyIpv6PrefixSetsIpv6PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_6prefix: str = None,
    ):
        # The IPv6 prefix assigned to the ENI.
        self.ipv_6prefix = ipv_6prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6prefix is not None:
            result['Ipv6Prefix'] = self.ipv_6prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6Prefix') is not None:
            self.ipv_6prefix = m.get('Ipv6Prefix')

        return self

class CreateNetworkInterfaceResponseBodyIpv4PrefixSets(DaraModel):
    def __init__(
        self,
        ipv_4prefix_set: List[main_models.CreateNetworkInterfaceResponseBodyIpv4PrefixSetsIpv4PrefixSet] = None,
    ):
        self.ipv_4prefix_set = ipv_4prefix_set

    def validate(self):
        if self.ipv_4prefix_set:
            for v1 in self.ipv_4prefix_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv4PrefixSet'] = []
        if self.ipv_4prefix_set is not None:
            for k1 in self.ipv_4prefix_set:
                result['Ipv4PrefixSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4prefix_set = []
        if m.get('Ipv4PrefixSet') is not None:
            for k1 in m.get('Ipv4PrefixSet'):
                temp_model = main_models.CreateNetworkInterfaceResponseBodyIpv4PrefixSetsIpv4PrefixSet()
                self.ipv_4prefix_set.append(temp_model.from_map(k1))

        return self

class CreateNetworkInterfaceResponseBodyIpv4PrefixSetsIpv4PrefixSet(DaraModel):
    def __init__(
        self,
        ipv_4prefix: str = None,
    ):
        # The IPv4 prefix assigned to the ENI.
        self.ipv_4prefix = ipv_4prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        return self

