# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInterfacesResponseBody(DaraModel):
    def __init__(
        self,
        network_interface_sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the ENIs.
        self.network_interface_sets = network_interface_sets
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the list.
        self.total_count = total_count

    def validate(self):
        if self.network_interface_sets:
            self.network_interface_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_sets is not None:
            result['NetworkInterfaceSets'] = self.network_interface_sets.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceSets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets()
            self.network_interface_sets = temp_model.from_map(m.get('NetworkInterfaceSets'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSets(DaraModel):
    def __init__(
        self,
        network_interface_set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet] = None,
    ):
        self.network_interface_set = network_interface_set

    def validate(self):
        if self.network_interface_set:
            for v1 in self.network_interface_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterfaceSet'] = []
        if self.network_interface_set is not None:
            for k1 in self.network_interface_set:
                result['NetworkInterfaceSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_set = []
        if m.get('NetworkInterfaceSet') is not None:
            for k1 in m.get('NetworkInterfaceSet'):
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet()
                self.network_interface_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSet(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        ipv_6sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6Sets = None,
        mac_address: str = None,
        network_id: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        primary_ip: str = None,
        primary_ip_type: str = None,
        private_ip_sets: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSets = None,
        security_group_ids: main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetSecurityGroupIds = None,
        status: str = None,
        type: str = None,
        v_switch_id: str = None,
    ):
        # The time when the ENI was created. Specify the time in the ISO 8601 standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of ENI.
        self.description = description
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The ID of the instance to which the ENI is bound.
        self.instance_id = instance_id
        # The IPv6 addresses of the ENIs.
        self.ipv_6sets = ipv_6sets
        # The MAC address of the ENI.
        self.mac_address = mac_address
        # The ID of the network.
        self.network_id = network_id
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The ENI name.
        self.network_interface_name = network_interface_name
        # The private IP address of the server.
        self.primary_ip = primary_ip
        # The primary private IP address. Valid values:
        # 
        # *   **Public**: public IP address.
        # *   **Private**: internal IP address.
        self.primary_ip_type = primary_ip_type
        # Details about the private IP address.
        self.private_ip_sets = private_ip_sets
        # The ID of the security group.
        self.security_group_ids = security_group_ids
        # The status of the ENI. Valid values:
        # 
        # *   Available: The ENI is available.
        # *   Attaching: The ENI is being attached to an instance.
        # *   InUse: The ENI is attached to an instance.
        # *   Detaching: The ENI is being detached from an instance.
        # *   Deleting: The ENI is being deleted.
        self.status = status
        # The type of the ENI. Valid values:
        # 
        # *   Primary
        # *   Secondary
        self.type = type
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.ipv_6sets:
            self.ipv_6sets.validate()
        if self.private_ip_sets:
            self.private_ip_sets.validate()
        if self.security_group_ids:
            self.security_group_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_6sets is not None:
            result['Ipv6Sets'] = self.ipv_6sets.to_map()

        if self.mac_address is not None:
            result['MacAddress'] = self.mac_address

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.primary_ip is not None:
            result['PrimaryIp'] = self.primary_ip

        if self.primary_ip_type is not None:
            result['PrimaryIpType'] = self.primary_ip_type

        if self.private_ip_sets is not None:
            result['PrivateIpSets'] = self.private_ip_sets.to_map()

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv6Sets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6Sets()
            self.ipv_6sets = temp_model.from_map(m.get('Ipv6Sets'))

        if m.get('MacAddress') is not None:
            self.mac_address = m.get('MacAddress')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('PrimaryIp') is not None:
            self.primary_ip = m.get('PrimaryIp')

        if m.get('PrimaryIpType') is not None:
            self.primary_ip_type = m.get('PrimaryIpType')

        if m.get('PrivateIpSets') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSets()
            self.private_ip_sets = temp_model.from_map(m.get('PrivateIpSets'))

        if m.get('SecurityGroupIds') is not None:
            temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m.get('SecurityGroupIds'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetSecurityGroupIds(DaraModel):
    def __init__(
        self,
        security_group: List[str] = None,
    ):
        self.security_group = security_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSets(DaraModel):
    def __init__(
        self,
        private_ip_set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSet] = None,
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
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSet()
                self.private_ip_set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetPrivateIpSetsPrivateIpSet(DaraModel):
    def __init__(
        self,
        primary: bool = None,
        private_ip_address: str = None,
        private_ip_status: str = None,
    ):
        # Specifies whether the private IP address is the primary private IP address. Valid values:
        # 
        # *   true
        # *   false
        self.primary = primary
        # The private IP address.
        self.private_ip_address = private_ip_address
        self.private_ip_status = private_ip_status

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

        if self.private_ip_status is not None:
            result['PrivateIpStatus'] = self.private_ip_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PrivateIpStatus') is not None:
            self.private_ip_status = m.get('PrivateIpStatus')

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6Sets(DaraModel):
    def __init__(
        self,
        ipv_6set: List[main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6SetsIpv6Set] = None,
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
                temp_model = main_models.DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6SetsIpv6Set()
                self.ipv_6set.append(temp_model.from_map(k1))

        return self

class DescribeNetworkInterfacesResponseBodyNetworkInterfaceSetsNetworkInterfaceSetIpv6SetsIpv6Set(DaraModel):
    def __init__(
        self,
        ipv_6address: str = None,
    ):
        # The IPv6 address of the ENI.
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

