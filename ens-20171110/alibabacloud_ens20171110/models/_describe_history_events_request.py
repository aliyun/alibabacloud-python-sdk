# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeHistoryEventsRequest(DaraModel):
    def __init__(
        self,
        event_levels: List[str] = None,
        event_status: List[str] = None,
        event_types: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        resource_ids: List[str] = None,
    ):
        # The levels of the event-triggered alerts.
        self.event_levels = event_levels
        # Event status list.
        self.event_status = event_status
        # The list of event types.
        # 
        # This parameter is required.
        self.event_types = event_types
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The IDs of resources.
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_levels is not None:
            result['EventLevels'] = self.event_levels

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_types is not None:
            result['EventTypes'] = self.event_types

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventLevels') is not None:
            self.event_levels = m.get('EventLevels')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        return self

