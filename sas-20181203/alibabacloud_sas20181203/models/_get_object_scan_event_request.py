# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetObjectScanEventRequest(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        lang: str = None,
    ):
        # The ID of the alert event.
        self.event_id = event_id
        # The language of the content in the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

