# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWaitingRoomEventRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_event_id: int = None,
    ):
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
        self.waiting_room_event_id = waiting_room_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.waiting_room_event_id is not None:
            result['WaitingRoomEventId'] = self.waiting_room_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('WaitingRoomEventId') is not None:
            self.waiting_room_event_id = m.get('WaitingRoomEventId')

        return self

