# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInterfacesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ipv_6address: List[str] = None,
        max_results: int = None,
        network_interface_id: List[str] = None,
        network_interface_name: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        primary_ip_address: str = None,
        private_ip_address: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        service_managed: bool = None,
        status: str = None,
        tag: List[main_models.DescribeNetworkInterfacesRequestTag] = None,
        type: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The instance ID of the instance to which the network interface controller (NIC) is attached.
        self.instance_id = instance_id
        # The IPv6 address of the network interface controller (NIC). N indicates that you can configure multiple IPv6 addresses. Valid values of N: 1 to 100.
        self.ipv_6address = ipv_6address
        # The maximum number of entries per page for paging query. Valid values: 10 to 500.
        self.max_results = max_results
        # The network interface controller (NIC) ID. Valid values of N: 1 to 100.
        self.network_interface_id = network_interface_id
        # The name of the network interface controller (NIC). The name must be 2 to 128 characters in length and can contain characters under the Unicode letter categorization (including English letters, Chinese characters, and digits). It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.network_interface_name = network_interface_name
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # **[Deprecated]** Use MaxResults or NextToken for pagination instead.
        self.page_number = page_number
        # **[Deprecated]** Use MaxResults or NextToken for pagination instead.
        self.page_size = page_size
        # The primary private IP address of the network interface controller (NIC).
        self.primary_ip_address = primary_ip_address
        # The secondary private IP address of the network interface controller (NIC). Valid values of N: 1 to 100.
        self.private_ip_address = private_ip_address
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. When you use this parameter to filter resources, the resource count cannot exceed 1000.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The security group ID associated with the secondary ENI.
        self.security_group_id = security_group_id
        # Specifies whether the user of the network interface controller (NIC) is an Alibaba Cloud service or a Virtual Network Operator (VNO).
        self.service_managed = service_managed
        # The status of the network interface controller (NIC). Valid values:
        self.status = status
        # The tags.
        self.tag = tag
        # The type of the network interface controller (NIC). Valid values:
        self.type = type
        # The vSwitch ID of the network interface controller (NIC).
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID of the network interface controller (NIC).
        self.vpc_id = vpc_id

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeNetworkInterfacesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeNetworkInterfacesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the network interface controller (NIC). Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the network interface controller (NIC). Valid values of N: 1 to 20.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

