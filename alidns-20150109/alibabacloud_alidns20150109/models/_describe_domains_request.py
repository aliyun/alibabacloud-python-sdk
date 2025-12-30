# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainsRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        key_word: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        search_mode: str = None,
        starmark: bool = None,
    ):
        # The ID of the domain name group. If you do not specify this parameter, all domain names are queried by default.
        self.group_id = group_id
        # The keyword for searches in "%KeyWord%" mode. The value is not case-sensitive.
        self.key_word = key_word
        # The language type.
        self.lang = lang
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **100**. Default value: **20**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The search mode. Valid values:
        # 
        # *   **LIKE**: fuzzy match.
        # *   **EXACT**: exact match.
        self.search_mode = search_mode
        # Specifies whether to query the starmark of the domain name.
        self.starmark = starmark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.starmark is not None:
            result['Starmark'] = self.starmark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('Starmark') is not None:
            self.starmark = m.get('Starmark')

        return self

