# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBgpPeerRequest(DaraModel):
    def __init__(
        self,
        bfd_multi_hop: int = None,
        bgp_group_id: str = None,
        client_token: str = None,
        enable_bfd: bool = None,
        ip_version: str = None,
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
        # 
        # > If you use BFD in a multi-cloud environment or a fiber-optic direct connection network without any bridge device, you need to change the default BFD hop count from **255** to **1**.
        self.bfd_multi_hop = bfd_multi_hop
        # The ID of the BGP group.
        # 
        # This parameter is required.
        self.bgp_group_id = bgp_group_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not set this parameter, the system uses the value of **RequestId** as **ClientToken**. The value of **RequestId** for each API request is different.
        self.client_token = client_token
        # Specifies whether to enable the Bidirectional Forwarding Detection (BFD) feature. Valid values:
        # 
        # *   **true**: enables BFD.
        # *   **false**: disables BFD.
        self.enable_bfd = enable_bfd
        # The IP version. Valid values:
        # 
        # *   **IPv4**: This is the default value.
        # *   **IPv6**: IPv6 is supported only if the VBR for which you want to create the BGP group has IPv6 enabled.
        self.ip_version = ip_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IP address of the BGP peer.
        self.peer_ip_address = peer_ip_address
        # The ID of the region to which the BGP group belongs.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_bfd is not None:
            result['EnableBfd'] = self.enable_bfd

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableBfd') is not None:
            self.enable_bfd = m.get('EnableBfd')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

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

