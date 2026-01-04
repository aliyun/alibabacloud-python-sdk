# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHistoryEventsShrinkRequest(DaraModel):
    def __init__(
        self,
        event_levels_shrink: str = None,
        event_status_shrink: str = None,
        event_types_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_ids_shrink: str = None,
    ):
        # The levels of the event-triggered alerts.
        self.event_levels_shrink = event_levels_shrink
        # Event status list.
        self.event_status_shrink = event_status_shrink
        # The list of event types.
        # 
        # This parameter is required.
        self.event_types_shrink = event_types_shrink
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The IDs of resources.
        self.resource_ids_shrink = resource_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_levels_shrink is not None:
            result['EventLevels'] = self.event_levels_shrink

        if self.event_status_shrink is not None:
            result['EventStatus'] = self.event_status_shrink

        if self.event_types_shrink is not None:
            result['EventTypes'] = self.event_types_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventLevels') is not None:
            self.event_levels_shrink = m.get('EventLevels')

        if m.get('EventStatus') is not None:
            self.event_status_shrink = m.get('EventStatus')

        if m.get('EventTypes') is not None:
            self.event_types_shrink = m.get('EventTypes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')

        return self

