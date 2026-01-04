# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeBgpPeersResponseBody(DaraModel):
    def __init__(
        self,
        bgp_peers: main_models.DescribeBgpPeersResponseBodyBgpPeers = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the BGP peer.
        self.bgp_peers = bgp_peers
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.bgp_peers:
            self.bgp_peers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bgp_peers is not None:
            result['BgpPeers'] = self.bgp_peers.to_map()

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
        if m.get('BgpPeers') is not None:
            temp_model = main_models.DescribeBgpPeersResponseBodyBgpPeers()
            self.bgp_peers = temp_model.from_map(m.get('BgpPeers'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBgpPeersResponseBodyBgpPeers(DaraModel):
    def __init__(
        self,
        bgp_peer: List[main_models.DescribeBgpPeersResponseBodyBgpPeersBgpPeer] = None,
    ):
        self.bgp_peer = bgp_peer

    def validate(self):
        if self.bgp_peer:
            for v1 in self.bgp_peer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BgpPeer'] = []
        if self.bgp_peer is not None:
            for k1 in self.bgp_peer:
                result['BgpPeer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bgp_peer = []
        if m.get('BgpPeer') is not None:
            for k1 in m.get('BgpPeer'):
                temp_model = main_models.DescribeBgpPeersResponseBodyBgpPeersBgpPeer()
                self.bgp_peer.append(temp_model.from_map(k1))

        return self

class DescribeBgpPeersResponseBodyBgpPeersBgpPeer(DaraModel):
    def __init__(
        self,
        advertised_route_count: int = None,
        auth_key: str = None,
        bfd_multi_hop: int = None,
        bgp_group_id: str = None,
        bgp_peer_id: str = None,
        bgp_status: str = None,
        description: str = None,
        enable_bfd: bool = None,
        gmt_modified: str = None,
        hold: str = None,
        ip_version: str = None,
        is_fake: bool = None,
        keepalive: str = None,
        local_asn: str = None,
        name: str = None,
        peer_asn: str = None,
        peer_ip_address: str = None,
        received_route_count: int = None,
        region_id: str = None,
        route_limit: str = None,
        router_id: str = None,
        status: str = None,
    ):
        # The number of advertised routes.
        self.advertised_route_count = advertised_route_count
        # The authentication key of the BGP group.
        self.auth_key = auth_key
        # The Bidirectional Forwarding Detection (BFD) hop count.
        self.bfd_multi_hop = bfd_multi_hop
        # The ID of the BGP group.
        self.bgp_group_id = bgp_group_id
        # The ID of the BGP peer.
        self.bgp_peer_id = bgp_peer_id
        # The status of the BGP connection. Valid values:
        # 
        # *   **Idle**: The BGP connection is not used.
        # *   **Connect**: The BGP connection is used.
        # *   **Active**: The BGP connection is available.
        # *   **Established**: The BGP connection is established.
        # *   **Down**: The BGP connection is unavailable.
        self.bgp_status = bgp_status
        # The description of the BGP group.
        self.description = description
        # Indicates whether BFD is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_bfd = enable_bfd
        # The time when the BGP peer is modified.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified = gmt_modified
        # The hold time.
        self.hold = hold
        # The version of the IP address.
        self.ip_version = ip_version
        # Indicates whether a fake autonomous system number (ASN) is used. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_fake = is_fake
        # The Keepalive interval.
        self.keepalive = keepalive
        # The ASN of the device on the Alibaba Cloud side.
        self.local_asn = local_asn
        # The name of the BGP peer.
        self.name = name
        # The autonomous system number (ASN)of the BGP peer.
        self.peer_asn = peer_asn
        # The IP address of the BGP peer.
        self.peer_ip_address = peer_ip_address
        # The number of received routes.
        self.received_route_count = received_route_count
        # The ID of the region to which the BGP group belongs.
        self.region_id = region_id
        # The maximum number of routes.
        self.route_limit = route_limit
        # The Router ID.
        self.router_id = router_id
        # The status of the BGP peer. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Modifying**
        # *   **Deleting**
        # *   **Deleted**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advertised_route_count is not None:
            result['AdvertisedRouteCount'] = self.advertised_route_count

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.bfd_multi_hop is not None:
            result['BfdMultiHop'] = self.bfd_multi_hop

        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id

        if self.bgp_peer_id is not None:
            result['BgpPeerId'] = self.bgp_peer_id

        if self.bgp_status is not None:
            result['BgpStatus'] = self.bgp_status

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_bfd is not None:
            result['EnableBfd'] = self.enable_bfd

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.hold is not None:
            result['Hold'] = self.hold

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.is_fake is not None:
            result['IsFake'] = self.is_fake

        if self.keepalive is not None:
            result['Keepalive'] = self.keepalive

        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.name is not None:
            result['Name'] = self.name

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.peer_ip_address is not None:
            result['PeerIpAddress'] = self.peer_ip_address

        if self.received_route_count is not None:
            result['ReceivedRouteCount'] = self.received_route_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_limit is not None:
            result['RouteLimit'] = self.route_limit

        if self.router_id is not None:
            result['RouterId'] = self.router_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvertisedRouteCount') is not None:
            self.advertised_route_count = m.get('AdvertisedRouteCount')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('BfdMultiHop') is not None:
            self.bfd_multi_hop = m.get('BfdMultiHop')

        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')

        if m.get('BgpPeerId') is not None:
            self.bgp_peer_id = m.get('BgpPeerId')

        if m.get('BgpStatus') is not None:
            self.bgp_status = m.get('BgpStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableBfd') is not None:
            self.enable_bfd = m.get('EnableBfd')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Hold') is not None:
            self.hold = m.get('Hold')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IsFake') is not None:
            self.is_fake = m.get('IsFake')

        if m.get('Keepalive') is not None:
            self.keepalive = m.get('Keepalive')

        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('PeerIpAddress') is not None:
            self.peer_ip_address = m.get('PeerIpAddress')

        if m.get('ReceivedRouteCount') is not None:
            self.received_route_count = m.get('ReceivedRouteCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteLimit') is not None:
            self.route_limit = m.get('RouteLimit')

        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

