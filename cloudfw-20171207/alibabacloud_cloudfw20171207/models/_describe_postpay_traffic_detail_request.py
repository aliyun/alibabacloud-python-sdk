# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePostpayTrafficDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: int = None,
        region_no: str = None,
        search_item: str = None,
        start_time: str = None,
        traffic_type: str = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The end of the time range to query. Specify a value in the YYYYMMDD format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The field based on which you want to sort the query results. Valid values:
        # 
        # *   **resourceId**
        # *   **trafficDay**
        self.order = order
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The region ID.
        self.region_no = region_no
        # The instance ID or the IP address of the asset.
        self.search_item = search_item
        # The beginning of the time range to query. Specify a value in the YYYYMMDD format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The traffic type. This parameter is required. Valid values:
        # 
        # *   **EIP_TRAFFIC**: traffic for the Internet firewall.
        # *   **NatGateway_TRAFFIC**: traffic for NAT firewalls.
        # *   **VPC_TRAFFIC**: traffic for virtual private cloud (VPC) firewalls.
        # 
        # This parameter is required.
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.search_item is not None:
            result['SearchItem'] = self.search_item

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('SearchItem') is not None:
            self.search_item = m.get('SearchItem')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self

