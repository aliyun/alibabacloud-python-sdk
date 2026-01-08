# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingAssetListRequest(DaraModel):
    def __init__(
        self,
        assets_region: str = None,
        current_page: str = None,
        end_time: str = None,
        group_name: str = None,
        iptype: str = None,
        lang: str = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        order: str = None,
        page_size: str = None,
        private_ip: str = None,
        public_ip: str = None,
        resource_type: str = None,
        security_risk: str = None,
        sort: str = None,
        start_time: str = None,
    ):
        self.assets_region = assets_region
        self.current_page = current_page
        # This parameter is required.
        self.end_time = end_time
        self.group_name = group_name
        self.iptype = iptype
        self.lang = lang
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.order = order
        self.page_size = page_size
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.resource_type = resource_type
        self.security_risk = security_risk
        self.sort = sort
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_region is not None:
            result['AssetsRegion'] = self.assets_region

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.iptype is not None:
            result['IPType'] = self.iptype

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.security_risk is not None:
            result['SecurityRisk'] = self.security_risk

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsRegion') is not None:
            self.assets_region = m.get('AssetsRegion')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IPType') is not None:
            self.iptype = m.get('IPType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SecurityRisk') is not None:
            self.security_risk = m.get('SecurityRisk')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

