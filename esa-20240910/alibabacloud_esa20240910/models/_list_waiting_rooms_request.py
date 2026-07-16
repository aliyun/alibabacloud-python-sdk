# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWaitingRoomsRequest(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        waiting_room_id: str = None,
    ):
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The waiting room ID. Specify this parameter to query the details of a specific waiting room.
        self.waiting_room_id = waiting_room_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.waiting_room_id is not None:
            result['WaitingRoomId'] = self.waiting_room_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('WaitingRoomId') is not None:
            self.waiting_room_id = m.get('WaitingRoomId')

        return self

