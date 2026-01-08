# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallAssetListRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        asset_ip: str = None,
        current_page: str = None,
        direction: str = None,
        ecs_instance_id: str = None,
        ecs_instance_name: str = None,
        end_time: str = None,
        ipprotocol: str = None,
        is_aitraffic: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        peer_vpc_id: str = None,
        port: str = None,
        risk_level: str = None,
        sort: str = None,
        start_time: str = None,
        vpc_id: str = None,
    ):
        self.app_name = app_name
        self.asset_ip = asset_ip
        self.current_page = current_page
        self.direction = direction
        self.ecs_instance_id = ecs_instance_id
        self.ecs_instance_name = ecs_instance_name
        # This parameter is required.
        self.end_time = end_time
        self.ipprotocol = ipprotocol
        self.is_aitraffic = is_aitraffic
        self.lang = lang
        self.order = order
        self.page_size = page_size
        self.peer_vpc_id = peer_vpc_id
        self.port = port
        self.risk_level = risk_level
        self.sort = sort
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.asset_ip is not None:
            result['AssetIP'] = self.asset_ip

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_instance_name is not None:
            result['EcsInstanceName'] = self.ecs_instance_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ipprotocol is not None:
            result['IPProtocol'] = self.ipprotocol

        if self.is_aitraffic is not None:
            result['IsAITraffic'] = self.is_aitraffic

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AssetIP') is not None:
            self.asset_ip = m.get('AssetIP')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsInstanceName') is not None:
            self.ecs_instance_name = m.get('EcsInstanceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IPProtocol') is not None:
            self.ipprotocol = m.get('IPProtocol')

        if m.get('IsAITraffic') is not None:
            self.is_aitraffic = m.get('IsAITraffic')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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

