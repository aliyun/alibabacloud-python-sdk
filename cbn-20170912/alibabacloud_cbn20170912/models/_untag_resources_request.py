# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
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
        # Specifies whether to remove all tags. Valid values:
        # - **true**: yes.
        # - **false** (default): no.
        # 
        # > This parameter takes effect only when **TagKey.N** is left empty.
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the resource.
        # 
        # This parameter is not required when the resource type is Cen or BandwidthPackage. This parameter is required for other resource types.
        self.region_id = region_id
        # The resource ID. **N** ranges from **1** to **50**.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type. Valid values:
        # 
        # **Cen**: Cloud Enterprise Network (CEN) instance.
        # 
        # **BandwidthPackage**: bandwidth plan instance.
        # 
        # **TransitRouter**: transit router instance.
        # 
        # **TransitRouterVpcAttachment**: VPC connection instance.
        # 
        # **TransitRouterVbrAttachment**: VBR connection instance.
        # 
        # **TransitRouterPeerAttachment**: cross-region connection instance.
        # 
        # **TransitRouterVpnAttachment**: VPN connection instance.
        # 
        # **TransitRouterRouteTable**: route table instance.
        # 
        # **Flowlog**: flow log instance.
        # 
        # **TransitRouterMulticastDomain**: multicast domain instance.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag key.
        # 
        # A tag key can be up to 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # If you specify multiple tag keys, they are evaluated by using the **OR** logical operator. **N** ranges from **1** to **20**.
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

