# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledInstancesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        scheduled_id: str = None,
    ):
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of records on each page. Default value: 20. Maximum value: 100.
        self.page_size = page_size
        # The ID of the scheduled inspection configuration.
        # 
        # This parameter is required.
        self.scheduled_id = scheduled_id

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

        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        return self

