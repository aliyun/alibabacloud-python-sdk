# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEduRoomRequest(DaraModel):
    def __init__(
        self,
        edu_room_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.edu_room_id = edu_room_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edu_room_id is not None:
            result['EduRoomId'] = self.edu_room_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EduRoomId') is not None:
            self.edu_room_id = m.get('EduRoomId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

