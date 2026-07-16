# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfiguredDestinationIPRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        destination_ip: str = None,
        destination_isp: str = None,
        destination_region: str = None,
        direction: str = None,
        group_name: str = None,
        lang: str = None,
        page_size: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The destination IP address.
        self.destination_ip = destination_ip
        # The destination ISP.
        self.destination_isp = destination_isp
        # The destination region.
        self.destination_region = destination_region
        # The traffic direction.
        # 
        # This parameter is required.
        self.direction = direction
        # The group name.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The language of the response.
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # The trace code.
        # 
        # This parameter is required.
        self.source_code = source_code
        # The source IP address of the visitor.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.destination_ip is not None:
            result['DestinationIP'] = self.destination_ip

        if self.destination_isp is not None:
            result['DestinationISP'] = self.destination_isp

        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DestinationIP') is not None:
            self.destination_ip = m.get('DestinationIP')

        if m.get('DestinationISP') is not None:
            self.destination_isp = m.get('DestinationISP')

        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

