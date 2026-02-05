# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        scheduled_id: str = None,
    ):
        # This parameter is required.
        self.scheduled_id = scheduled_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheduled_id is not None:
            result['ScheduledId'] = self.scheduled_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduledId') is not None:
            self.scheduled_id = m.get('ScheduledId')

        return self

