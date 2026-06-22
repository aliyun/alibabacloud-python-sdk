# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HandleUnknownThreatDetectEventRequest(DaraModel):
    def __init__(
        self,
        event_id_list: List[str] = None,
        status: int = None,
    ):
        # The list of event IDs.
        self.event_id_list = event_id_list
        # The event handling status. Valid values:
        # 
        # - **1**: Unhandled.
        # - **2**: Blocked.
        # - **3**: Ignored.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id_list is not None:
            result['EventIdList'] = self.event_id_list

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventIdList') is not None:
            self.event_id_list = m.get('EventIdList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

