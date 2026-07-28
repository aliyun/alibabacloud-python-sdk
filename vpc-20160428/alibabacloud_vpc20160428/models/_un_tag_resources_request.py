# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnTagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to unbind all tags from the resources. Valid values:
        # - **true**: Unbinds all tags from the resources.
        # - **false** (default): Does not unbind all tags from the resources.
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resources.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # - **VPC**: virtual private cloud (VPC) instance.
        # - **VSWITCH**: vSwitch instance.
        # - **ROUTETABLE**: route table instance.
        # - **EIP**: elastic IP address (EIP) instance.
        # - **VPNGATEWAY**: VPN gateway instance.
        # - **NATGATEWAY**: NAT gateway instance.
        # - **COMMONBANDWIDTHPACKAGE**: Internet Shared Bandwidth instance.
        # - **PREFIXLIST**: prefix list instance.
        # - **PUBLICIPADDRESSPOOL**: IP address pool instance.
        # - **IPV4GATEWAY**: IPv4 gateway instance.
        # - **IPV6GATEWAY**: IPv6 gateway instance.
        # - **NETWORKACL**: network ACL instance.
        # - **TRAFFICMIRRORFILTER**: traffic mirror filter instance.
        # - **TRAFFICMIRRORSESSION**: traffic mirror session instance.
        # - **FLOWLOG**: flow log instance.
        # - **HAVIP**: high-availability virtual IP address (HaVip) instance.
        # - **DHCPOPTIONSSET**: DHCP options set instance.
        # - **GATEWAYENDPOINT**: gateway endpoint instance.
        # - **IPV6ADDRESS**: IPv6 address instance.
        # 
        # > The resource type value is case-insensitive.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys to unbind. You can specify up to 20 tag keys.
        # 
        # Each tag key can be up to 128 characters in length, can be an empty string, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

