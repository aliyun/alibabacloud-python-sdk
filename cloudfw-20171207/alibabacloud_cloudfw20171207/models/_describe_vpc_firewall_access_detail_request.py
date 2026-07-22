# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallAccessDetailRequest(DaraModel):
    def __init__(
        self,
        asset_ip: str = None,
        current_page: str = None,
        direction: str = None,
        end_time: str = None,
        ipprotocol: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        peer_asset_ip: str = None,
        peer_asset_instance_id: str = None,
        peer_asset_instance_name: str = None,
        peer_vpc_id: str = None,
        port: str = None,
        risk_level: str = None,
        sort: str = None,
        start_time: str = None,
        vpc_id: str = None,
    ):
        # The IP address of the local asset. You must specify at least one of AssetIP and Port. If both are left empty, the API returns a 400 error.
        self.asset_ip = asset_ip
        # The page number in a paging query. Settings this parameter to specify the current page for paging.
        self.current_page = current_page
        # The traffic direction. Valid values:
        # - **in**: inbound.
        # - **out**: outbound.
        # 
        # >If this parameter is not specified in Settings, traffic in all directions is queried.
        self.direction = direction
        # The end time of the query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The protocol type. Valid values:
        # - **tcp**: TCP protocol.
        # - **udp**: UDP protocol.
        self.ipprotocol = ipprotocol
        # The language type. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The sort order. Valid values:
        # 
        # - **asc**: ascending order.
        # -  **desc** (default): descending order.
        self.order = order
        # The number of entries per page in a paging query.
        self.page_size = page_size
        # The source IP address of the peer.
        self.peer_asset_ip = peer_asset_ip
        # The instance ID of the peer asset.
        self.peer_asset_instance_id = peer_asset_instance_id
        # The instance name of the peer asset.
        self.peer_asset_instance_name = peer_asset_instance_name
        # The instance ID of the peer VPC.
        self.peer_vpc_id = peer_vpc_id
        # The port number. You must specify at least one of AssetIP and Port. If both are left empty, the API returns a 400 error.
        self.port = port
        # The risk assessment level.
        self.risk_level = risk_level
        # The sort field. Valid values:
        # 
        #  - **InBytes**
        # 
        # - **OutBytes**
        # 
        # - **TotalBytes**
        # 
        # - **InPackets**
        # 
        # - **OutPackets**
        # 
        # - **SessionCount**
        self.sort = sort
        # The start time of the query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The VPC-connected instance ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ipprotocol is not None:
            result['IPProtocol'] = self.ipprotocol

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.peer_asset_ip is not None:
            result['PeerAssetIP'] = self.peer_asset_ip

        if self.peer_asset_instance_id is not None:
            result['PeerAssetInstanceId'] = self.peer_asset_instance_id

        if self.peer_asset_instance_name is not None:
            result['PeerAssetInstanceName'] = self.peer_asset_instance_name

        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id

        if self.port is not None:
            result['Port'] = self.port

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IPProtocol') is not None:
            self.ipprotocol = m.get('IPProtocol')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PeerAssetIP') is not None:
            self.peer_asset_ip = m.get('PeerAssetIP')

        if m.get('PeerAssetInstanceId') is not None:
            self.peer_asset_instance_id = m.get('PeerAssetInstanceId')

        if m.get('PeerAssetInstanceName') is not None:
            self.peer_asset_instance_name = m.get('PeerAssetInstanceName')

        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

