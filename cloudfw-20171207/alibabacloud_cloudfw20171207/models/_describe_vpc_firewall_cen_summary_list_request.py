# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallCenSummaryListRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        lang: str = None,
        member_uid: str = None,
        page_size: str = None,
        transit_router_type: str = None,
    ):
        # The page number for a paged query. The default value is 1.
        self.current_page = current_page
        # The language of the content. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the member account.
        self.member_uid = member_uid
        # The number of entries to return on each page.
        self.page_size = page_size
        # The type of the CEN transit router. Valid values:
        # 
        # **Basic**: Basic Edition
        # 
        # **Enterprise**: Enterprise Edition
        self.transit_router_type = transit_router_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')

        return self

