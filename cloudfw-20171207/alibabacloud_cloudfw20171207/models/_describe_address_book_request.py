# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddressBookRequest(DaraModel):
    def __init__(
        self,
        contain_port: str = None,
        current_page: str = None,
        group_type: str = None,
        group_uuid: str = None,
        lang: str = None,
        page_size: str = None,
        query: str = None,
    ):
        # Filters the query to return only address books that contain the specified port. This parameter is valid only when **GroupType** is set to **port**.
        self.contain_port = contain_port
        # The page number for a paginated query.
        # 
        # Default value: 1.
        self.current_page = current_page
        # The type of the address book.
        # 
        # > If this parameter is not specified, the query returns both IPv4 and ECS tag address books.
        self.group_type = group_type
        # The unique identifier of the address book.
        self.group_uuid = group_uuid
        # The language of the content in the response.
        self.lang = lang
        # The number of address books per page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The search keyword for address books.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

