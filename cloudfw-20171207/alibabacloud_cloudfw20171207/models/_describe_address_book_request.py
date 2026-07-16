# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAddressBookRequest(DaraModel):
    def __init__(
        self,
        asset_member_uids: List[int] = None,
        contain_port: str = None,
        current_page: str = None,
        group_type: str = None,
        group_uuid: str = None,
        lang: str = None,
        page_size: str = None,
        query: str = None,
    ):
        # The list of member accounts for the asset address book.
        self.asset_member_uids = asset_member_uids
        # Queries address books that contain the specified port. This parameter takes effect only when the **GroupType** parameter is set to **port**.
        self.contain_port = contain_port
        # The page number in a paged query.
        # 
        # Default value: 1, which indicates that the first page of data is returned.
        self.current_page = current_page
        # The type of the address book.
        # 
        # > If you do not set this parameter, IP address books and ECS tag-based address books are queried.
        self.group_type = group_type
        # The unique ID of the address book.
        self.group_uuid = group_uuid
        # The language type for the address book description. Valid values:
        # - **en**: English.
        # - **zh**: Chinese (default).
        self.lang = lang
        # The number of address books on each page in a paged query.
        # 
        # Default value: 10, which indicates that each page contains 10 results. Maximum value: 50.
        self.page_size = page_size
        # The search condition. Enter the address book information that you want to query.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_member_uids is not None:
            result['AssetMemberUids'] = self.asset_member_uids

        if self.contain_port is not None:
            result['ContainPort'] = self.contain_port

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetMemberUids') is not None:
            self.asset_member_uids = m.get('AssetMemberUids')

        if m.get('ContainPort') is not None:
            self.contain_port = m.get('ContainPort')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

