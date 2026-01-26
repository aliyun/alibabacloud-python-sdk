# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomHostnamesRequest(DaraModel):
    def __init__(
        self,
        hostname: str = None,
        name_match_type: str = None,
        page_number: int = None,
        page_size: int = None,
        record_id: int = None,
        site_id: int = None,
        status: str = None,
    ):
        self.hostname = hostname
        self.name_match_type = name_match_type
        self.page_number = page_number
        self.page_size = page_size
        self.record_id = record_id
        # This parameter is required.
        self.site_id = site_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.name_match_type is not None:
            result['NameMatchType'] = self.name_match_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('NameMatchType') is not None:
            self.name_match_type = m.get('NameMatchType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

