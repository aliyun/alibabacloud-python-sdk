# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssignPrivateIpAddressesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        ipv_4prefix: List[str] = None,
        ipv_4prefix_count: int = None,
        network_interface_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        private_ip_address: List[str] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_private_ip_address_count: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # One or more IPv4 prefixes to allocate to the network interface controller (NIC). Valid values of N: 1 to 10.
        # > To configure IPv4 prefixes for the ENI, you must specify either the Ipv4Prefix.N parameter or the Ipv4PrefixCount parameter, but not both.
        self.ipv_4prefix = ipv_4prefix
        # The number of randomly generated IPv4 prefixes to allocate to the network interface controller (NIC). Valid values: 1 to 10.
        # > To configure IPv4 prefixes for the ENI, you must specify either the Ipv4Prefix.N parameter or the Ipv4PrefixCount parameter, but not both.
        self.ipv_4prefix_count = ipv_4prefix_count
        # The ID of the network interface controller (NIC).
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # One or more secondary private IP addresses selected from the available IP addresses of the vSwitch to which the network interface controller (NIC) belongs. Valid values of N:
        # 
        # - When the ENI is in the Available (`Available`) state: 1 to 32.
        # - When the ENI is in the `InUse` state: limited by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # When you allocate secondary private IP addresses, you cannot specify both PrivateIpAddress.N and SecondaryPrivateIpAddressCount.
        self.private_ip_address = private_ip_address
        # The region ID of the network interface controller (NIC). You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The number of private IP addresses to be automatically assigned from the available IP addresses of the vSwitch.
        # 
        # When you assign secondary private IP addresses, you cannot specify both PrivateIpAddress.N and SecondaryPrivateIpAddressCount.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ipv_4prefix is not None:
            result['Ipv4Prefix'] = self.ipv_4prefix

        if self.ipv_4prefix_count is not None:
            result['Ipv4PrefixCount'] = self.ipv_4prefix_count

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secondary_private_ip_address_count is not None:
            result['SecondaryPrivateIpAddressCount'] = self.secondary_private_ip_address_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Ipv4Prefix') is not None:
            self.ipv_4prefix = m.get('Ipv4Prefix')

        if m.get('Ipv4PrefixCount') is not None:
            self.ipv_4prefix_count = m.get('Ipv4PrefixCount')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecondaryPrivateIpAddressCount') is not None:
            self.secondary_private_ip_address_count = m.get('SecondaryPrivateIpAddressCount')

        return self

