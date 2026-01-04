# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBgpPeerAttributeRequest(DaraModel):
    def __init__(
        self,
        bfd_multi_hop: int = None,
        bgp_group_id: str = None,
        bgp_peer_id: str = None,
        client_token: str = None,
        enable_bfd: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_ip_address: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The BFD hop count. Valid values: **1** to **255**.
        # 
        # This parameter is required only if you enable BFD. The parameter specifies the maximum number of network devices that a packet can traverse from the source to the destination. Set a value based on your network topology.
        self.bfd_multi_hop = bfd_multi_hop
        # The ID of the BGP group to which the BGP peer that you want to modify belongs.
        self.bgp_group_id = bgp_group_id
        # The ID of the BGP peer that you want to modify.
        # 
        # This parameter is required.
        self.bgp_peer_id = bgp_peer_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable the Bidirectional Forwarding Detection (BFD) feature. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.enable_bfd = enable_bfd
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IP address of the BGP peer that you want to modify.
        self.peer_ip_address = peer_ip_address
        # The region ID of the BGP group to which the BGP peer that you want to modify belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.bfd_multi_hop is not None:
            result['BfdMultiHop'] = self.bfd_multi_hop

        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id

        if self.bgp_peer_id is not None:
            result['BgpPeerId'] = self.bgp_peer_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_bfd is not None:
            result['EnableBfd'] = self.enable_bfd

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_ip_address is not None:
            result['PeerIpAddress'] = self.peer_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BfdMultiHop') is not None:
            self.bfd_multi_hop = m.get('BfdMultiHop')

        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')

        if m.get('BgpPeerId') is not None:
            self.bgp_peer_id = m.get('BgpPeerId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableBfd') is not None:
            self.enable_bfd = m.get('EnableBfd')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerIpAddress') is not None:
            self.peer_ip_address = m.get('PeerIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

