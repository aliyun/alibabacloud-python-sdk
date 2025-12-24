# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssignIpv6AddressesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        ipv_6address: List[str] = None,
        ipv_6address_count: int = None,
        ipv_6prefix: List[str] = None,
        ipv_6prefix_count: int = None,
        network_interface_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.**** For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The IPv6 addresses to assign to the ENI. Valid values of N: 1 to 10.
        # 
        # Example: Ipv6Address.1=2001:db8:1234:1a00::\\*\\*\\*\\*
        # 
        # >  You must specify `Ipv6Addresses.N` or `Ipv6AddressCount`, but not both.
        self.ipv_6address = ipv_6address
        # The number of IPv6 addresses to randomly generate for the ENI. Valid values: 1 to 10.
        # 
        # >  You must specify `Ipv6Addresses.N` or `Ipv6AddressCount`, but not both.
        self.ipv_6address_count = ipv_6address_count
        # The IPv6 prefixes to assign to the ENI. Valid values of N: 1 to 10.
        # 
        # >  To assign IPv6 prefixes to the ENI, you must specify Ipv6Prefix.N or Ipv6PrefixCount, but not both.
        self.ipv_6prefix = ipv_6prefix
        # The number of IPv6 prefixes to assign to the ENI. Valid values: 1 to 10.
        # 
        # >  To assign IPv6 prefixes to the ENI, you must specify Ipv6Prefix.N or Ipv6PrefixCount, but not both.
        self.ipv_6prefix_count = ipv_6prefix_count
        # The ENI ID.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the ENI. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.ipv_6prefix is not None:
            result['Ipv6Prefix'] = self.ipv_6prefix

        if self.ipv_6prefix_count is not None:
            result['Ipv6PrefixCount'] = self.ipv_6prefix_count

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('Ipv6Prefix') is not None:
            self.ipv_6prefix = m.get('Ipv6Prefix')

        if m.get('Ipv6PrefixCount') is not None:
            self.ipv_6prefix_count = m.get('Ipv6PrefixCount')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

