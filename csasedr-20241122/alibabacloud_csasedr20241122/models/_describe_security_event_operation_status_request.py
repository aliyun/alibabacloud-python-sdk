# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSecurityEventOperationStatusRequest(DaraModel):
    def __init__(
        self,
        security_event_ids: List[int] = None,
        task_id: int = None,
    ):
        # The IDs of the security alert events.
        # > You must specify either TaskId or SecurityEventIds. The API call succeeds only if one of these parameters is specified.
        # 
        # This parameter is required.
        self.security_event_ids = security_event_ids
        # The ID of the task that processes the security alert event.
        # 
        # > You must specify either TaskId or SecurityEventIds. The API call succeeds only if one of these parameters is specified.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

