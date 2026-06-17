# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeVpcFirewallDomainRelationListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        domain_list: List[str] = None,
        dst_ip: str = None,
        dst_vpc_id: str = None,
        end_time: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        sort: str = None,
        src_ip: str = None,
        src_vpc_id: str = None,
        start_time: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The list of domain names.
        self.domain_list = domain_list
        # The destination IP address to query.
        self.dst_ip = dst_ip
        # The ID of the destination VPC.
        self.dst_vpc_id = dst_vpc_id
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The order in which to sort the queried entries. Valid values:
        self.order = order
        # The number of entries to return on each page.
        self.page_size = page_size
        # The field by which to sort the queried entries. Valid values:
        # 
        # Default value: TotalBytes.
        # 
        # Valid values:
        # 
        # TotalBytes: Order by total traffic.
        # 
        # SessionCount: Order by session count.
        self.sort = sort
        # The source IP address to query.
        self.src_ip = src_ip
        # The ID of the source VPC.
        self.src_vpc_id = src_vpc_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

