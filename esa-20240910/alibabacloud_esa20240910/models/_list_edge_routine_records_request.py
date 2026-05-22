# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEdgeRoutineRecordsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
    ):
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: **500**.
        self.page_size = page_size
        # The match mode to filter the record names.
        # 
        # *   **fuzzy**: fuzzy match.
        # *   **prefix**: match by prefix.
        # *   **suffix**: match by suffix.
        # *   **exact** (default): exact match .
        self.record_match_type = record_match_type
        # The record name.
        self.record_name = record_name
        # The website ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_match_type is not None:
            result['RecordMatchType'] = self.record_match_type

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordMatchType') is not None:
            self.record_match_type = m.get('RecordMatchType')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

