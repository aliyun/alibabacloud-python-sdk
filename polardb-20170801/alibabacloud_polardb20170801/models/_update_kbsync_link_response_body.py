# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKBSyncLinkResponseBody(DaraModel):
    def __init__(
        self,
        link_id: str = None,
        request_id: str = None,
        sync_schedule: str = None,
    ):
        self.link_id = link_id
        self.request_id = request_id
        self.sync_schedule = sync_schedule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.link_id is not None:
            result['LinkId'] = self.link_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sync_schedule is not None:
            result['SyncSchedule'] = self.sync_schedule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LinkId') is not None:
            self.link_id = m.get('LinkId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SyncSchedule') is not None:
            self.sync_schedule = m.get('SyncSchedule')

        return self

