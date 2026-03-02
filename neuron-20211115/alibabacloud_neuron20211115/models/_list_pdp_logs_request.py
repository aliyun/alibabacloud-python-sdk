# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPdpLogsRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        ip: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        service_group_id: int = None,
        source_type: str = None,
        to: int = None,
    ):
        self.from_ = from_
        self.ip = ip
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        self.service_group_id = service_group_id
        self.source_type = source_type
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        if self.ip is not None:
            result['ip'] = self.ip

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

