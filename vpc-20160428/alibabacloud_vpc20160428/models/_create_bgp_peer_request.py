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
        # This parameter is required when BFD is enabled.
        # Specify the BFD hop count, which is the maximum number of devices that data passes through from the source to the destination. You can configure different hop counts based on actual physical link factors.
        # 
        # > When you use BFD in a multi-cloud environment or a fiber direct connect network without any bridging devices in between, you need to change the default BFD hop count from **255** to **1**.
        self.bfd_multi_hop = bfd_multi_hop
        # The ID of the BGP group.
        # 
        # This parameter is required.
        self.bgp_group_id = bgp_group_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # The client generates the value of this parameter. Make sure that the value is unique among different requests. The maximum length is 64 ASCII characters.
        # 
        # > If you do not specify this parameter, the system uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to enable Bidirectional Forwarding Detection (BFD). Valid values:
        # 
        # - **true**: enables BFD.
        # 
        # - **false**: disables BFD.
        self.enable_bfd = enable_bfd
        # The IP version. Valid values:
        # 
        # - **IPv4** (default): IPv4.
        # - **IPv6**: IPv6. IPv6 is supported only when the VBR on which the BGP group is created has IPv6 enabled.
        self.ip_version = ip_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IP address of the BGP peer.
        self.peer_ip_address = peer_ip_address
        # The region ID of the BGP group.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) API to obtain the region ID.
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

