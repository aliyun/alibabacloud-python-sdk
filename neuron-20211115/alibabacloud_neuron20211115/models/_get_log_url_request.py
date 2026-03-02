# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogUrlRequest(DaraModel):
    def __init__(
        self,
        ip: str = None,
        order_by: str = None,
        order_direction: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        service_group_id: int = None,
        source_type: str = None,
        to: int = None,
    ):
        # ip
        self.ip = ip
        self.order_by = order_by
        self.order_direction = order_direction
        self.page_number = page_number
        self.page_size = page_size
        self.query = query
        # This parameter is required.
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
        if self.ip is not None:
            result['ip'] = self.ip

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_direction is not None:
            result['orderDirection'] = self.order_direction

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
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDirection') is not None:
            self.order_direction = m.get('orderDirection')

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

