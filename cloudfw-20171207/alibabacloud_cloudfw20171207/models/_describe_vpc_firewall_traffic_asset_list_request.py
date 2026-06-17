# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallTrafficAssetListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        domain: str = None,
        end_time: str = None,
        ip: str = None,
        is_aitraffic: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        sort: str = None,
        start_time: str = None,
        vpc_id: str = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The domain name.
        self.domain = domain
        # The end time. The value is a Unix timestamp that is accurate to the second.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The IP address of the asset.
        self.ip = ip
        # Specifies whether to count only the traffic that is used to access AI services.
        self.is_aitraffic = is_aitraffic
        # The language of the content within the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The field to sort by.
        # 
        # Default value: TotalBytes.
        # 
        # Valid values:
        # 
        # TotalBytes: Sorts by total traffic.
        # 
        # SessionCount: Sorts by the number of sessions.
        self.order = order
        # The number of entries to return on each page.
        self.page_size = page_size
        # The sort order. Valid values: \\`asc\\`, \\`desc\\`.
        self.sort = sort
        # The start time. The value is a Unix timestamp that is accurate to the second.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The VPC where the asset resides.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip is not None:
            result['IP'] = self.ip

        if self.is_aitraffic is not None:
            result['IsAITraffic'] = self.is_aitraffic

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IsAITraffic') is not None:
            self.is_aitraffic = m.get('IsAITraffic')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

