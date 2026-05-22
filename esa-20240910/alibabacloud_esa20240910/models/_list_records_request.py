# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecordsRequest(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        page_number: int = None,
        page_size: int = None,
        proxied: bool = None,
        record_match_type: str = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        type: str = None,
    ):
        self.biz_name = biz_name
        self.page_number = page_number
        self.page_size = page_size
        self.proxied = proxied
        self.record_match_type = record_match_type
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id
        self.source_type = source_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_match_type is not None:
            result['RecordMatchType'] = self.record_match_type

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordMatchType') is not None:
            self.record_match_type = m.get('RecordMatchType')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

