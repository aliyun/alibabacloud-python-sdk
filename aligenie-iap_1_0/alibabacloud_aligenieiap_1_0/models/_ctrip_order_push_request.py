# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CtripOrderPushRequest(DaraModel):
    def __init__(
        self,
        journey_id: str = None,
        schedule_item: str = None,
        uid: str = None,
    ):
        self.journey_id = journey_id
        self.schedule_item = schedule_item
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.journey_id is not None:
            result['JourneyId'] = self.journey_id

        if self.schedule_item is not None:
            result['ScheduleItem'] = self.schedule_item

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JourneyId') is not None:
            self.journey_id = m.get('JourneyId')

        if m.get('ScheduleItem') is not None:
            self.schedule_item = m.get('ScheduleItem')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

