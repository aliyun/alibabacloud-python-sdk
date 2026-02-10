# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBaselineCheckWhiteRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        check_ids_shrink: str = None,
        check_item_fuzzy: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        record_ids_shrink: str = None,
        source: str = None,
    ):
        # The IDs of check items.
        self.check_ids_shrink = check_ids_shrink
        # The name of the check item. Fuzzy match is supported.
        self.check_item_fuzzy = check_item_fuzzy
        # The page number. Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size
        # The IDs of the whitelist rules.
        self.record_ids_shrink = record_ids_shrink
        # The data source. If you leave this parameter empty, the default value is used. Valid values:
        # 
        # *   **default**: server
        # *   **agentless**: agentless detection
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids_shrink is not None:
            result['CheckIds'] = self.check_ids_shrink

        if self.check_item_fuzzy is not None:
            result['CheckItemFuzzy'] = self.check_item_fuzzy

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_ids_shrink is not None:
            result['RecordIds'] = self.record_ids_shrink

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids_shrink = m.get('CheckIds')

        if m.get('CheckItemFuzzy') is not None:
            self.check_item_fuzzy = m.get('CheckItemFuzzy')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordIds') is not None:
            self.record_ids_shrink = m.get('RecordIds')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

