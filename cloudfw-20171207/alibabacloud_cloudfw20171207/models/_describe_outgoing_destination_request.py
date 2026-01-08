# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOutgoingDestinationRequest(DaraModel):
    def __init__(
        self,
        acl_coverage: str = None,
        application_name: str = None,
        category_id: str = None,
        current_page: str = None,
        dst_ip: str = None,
        end_time: str = None,
        is_aitraffic: str = None,
        lang: str = None,
        order: str = None,
        page_size: str = None,
        port: str = None,
        private_ip: str = None,
        public_ip: str = None,
        security_suggest: str = None,
        sort: str = None,
        source_ip: str = None,
        start_time: str = None,
        tag_id: str = None,
    ):
        self.acl_coverage = acl_coverage
        self.application_name = application_name
        self.category_id = category_id
        self.current_page = current_page
        self.dst_ip = dst_ip
        # This parameter is required.
        self.end_time = end_time
        self.is_aitraffic = is_aitraffic
        self.lang = lang
        self.order = order
        self.page_size = page_size
        self.port = port
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.security_suggest = security_suggest
        self.sort = sort
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_coverage is not None:
            result['AclCoverage'] = self.acl_coverage

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_aitraffic is not None:
            result['IsAITraffic'] = self.is_aitraffic

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.security_suggest is not None:
            result['SecuritySuggest'] = self.security_suggest

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclCoverage') is not None:
            self.acl_coverage = m.get('AclCoverage')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsAITraffic') is not None:
            self.is_aitraffic = m.get('IsAITraffic')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('SecuritySuggest') is not None:
            self.security_suggest = m.get('SecuritySuggest')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

