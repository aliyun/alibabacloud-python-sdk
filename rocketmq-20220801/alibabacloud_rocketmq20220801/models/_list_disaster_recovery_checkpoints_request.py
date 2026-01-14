# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDisasterRecoveryCheckpointsRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Filter Condition
        self.filter = filter
        # Source Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Current page number, starting from 1.
        self.page_number = page_number
        # Page size, the maximum number of results returned per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

