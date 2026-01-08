# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceRdAccountsRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        lang: str = None,
        member_desc: str = None,
        member_display_name: str = None,
        member_uid: str = None,
        page_size: str = None,
        source_ip: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.member_desc = member_desc
        self.member_display_name = member_display_name
        self.member_uid = member_uid
        self.page_size = page_size
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_desc is not None:
            result['MemberDesc'] = self.member_desc

        if self.member_display_name is not None:
            result['MemberDisplayName'] = self.member_display_name

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberDesc') is not None:
            self.member_desc = m.get('MemberDesc')

        if m.get('MemberDisplayName') is not None:
            self.member_display_name = m.get('MemberDisplayName')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

