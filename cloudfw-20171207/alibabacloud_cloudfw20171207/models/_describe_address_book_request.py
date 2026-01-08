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
        lang: str = None,
        page_size: str = None,
        query: str = None,
    ):
        # The port that is included in the address book. This parameter takes effect only when the **GroupType** parameter is set to **port**.
        self.contain_port = contain_port
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The type of the address book. Valid values:
        # 
        # *   **ip**: IP address book
        # *   **domain**: domain address book
        # *   **port**: port address book
        # *   **tag**: Elastic Compute Service (ECS) tag-based address book
        # *   **allCloud**: cloud service address book
        # *   **threat**: threat intelligence address book
        # *   **ipv6**: IPv6 address book
        # >  If you do not specify a type, the domain address books and ECS tag-based address books are queried.
        self.group_type = group_type
        # The language of the content within the request. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The query condition that is used to search for the address book.
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

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

