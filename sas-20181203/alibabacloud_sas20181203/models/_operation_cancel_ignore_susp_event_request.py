# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperationCancelIgnoreSuspEventRequest(DaraModel):
    def __init__(
        self,
        remark: str = None,
        security_event_ids: List[int] = None,
    ):
        # The remarks.
        self.remark = remark
        # The IDs of alert events.
        # 
        # This parameter is required.
        self.security_event_ids = security_event_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remark is not None:
            result['Remark'] = self.remark

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        return self

