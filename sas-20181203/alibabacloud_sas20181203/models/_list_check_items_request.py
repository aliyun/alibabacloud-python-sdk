# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckItemsRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_show_name: str = None,
        check_types: List[str] = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        statuses: List[str] = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The name of the custom check item.
        self.check_show_name = check_show_name
        # The source type of the situational awareness check item.
        self.check_types = check_types
        # Specifies the page number to display when performing a paginated query. The starting value is **1**, and the default value is **1**.
        self.current_page = current_page
        # The language type for requests and responses. The default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Specifies the maximum number of data entries to display per page when performing a paginated query. The default number of data entries displayed per page is 20, and if the PageSize parameter is empty, it will default to returning 20 data entries.
        # > It is recommended that the PageSize value is not left empty.
        self.page_size = page_size
        # The status of the check item.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_show_name is not None:
            result['CheckShowName'] = self.check_show_name

        if self.check_types is not None:
            result['CheckTypes'] = self.check_types

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckShowName') is not None:
            self.check_show_name = m.get('CheckShowName')

        if m.get('CheckTypes') is not None:
            self.check_types = m.get('CheckTypes')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

