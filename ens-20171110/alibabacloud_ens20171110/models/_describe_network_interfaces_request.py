# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNetworkInterfacesRequest(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        instance_id: str = None,
        ipv_6address: List[str] = None,
        network_id: str = None,
        network_interface_id: str = None,
        network_interface_ids: List[str] = None,
        network_interface_name: str = None,
        page_number: str = None,
        page_size: str = None,
        primary_ip_address: str = None,
        security_group_id: str = None,
        status: str = None,
        type: str = None,
        v_switch_id: str = None,
    ):
        # The region ID of the instance.
        self.ens_region_id = ens_region_id
        # The IDs of edge nodes. N indicates the number of edge node IDs that you can specify at the same time. Valid values of N: 1 to 100.
        self.ens_region_ids = ens_region_ids
        # The ID of the instance.
        self.instance_id = instance_id
        # IPv6 addresses N of the ENI. You can specify multiple IPv6 addresses. Valid values of N: 1 to 100.
        self.ipv_6address = ipv_6address
        # The ID of the network.
        self.network_id = network_id
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The IDs of the elastic network interfaces (ENIs). N indicates the number of ENI IDs that you can specify at the same time. Valid values of N: 1 to 100.
        self.network_interface_ids = network_interface_ids
        # The name of the ENI.
        self.network_interface_name = network_interface_name
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 50.
        self.page_size = page_size
        # The primary IP address of the ENI.
        self.primary_ip_address = primary_ip_address
        # The ID of the security group to which the secondary ENI belongs. To query the details of secondary ENIs based on the ID of a security group, specify this parameter.
        self.security_group_id = security_group_id
        # The status of the ENI. Valid values:
        # 
        # *   Available: The ENI is available.
        # *   Attaching: The ENI is being attached to an instance.
        # *   InUse: The ENI is attached to an instance.
        # *   Detaching: The ENI is being detached from an instance.
        # *   Deleting: The ENI is being deleted.
        # 
        # This parameter is empty by default, which indicates that ENIs in all states are queried.
        self.status = status
        # The type of the ENI. Valid values:
        # 
        # *   Primary: the primary ENI.
        # *   Secondary: the secondary ENI.
        # 
        # This parameter is empty by default, which indicates that both primary and secondary ENIs are queried.
        self.type = type
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids = m.get('NetworkInterfaceIds')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

