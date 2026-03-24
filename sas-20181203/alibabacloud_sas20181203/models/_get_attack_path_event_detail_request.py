# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttackPathEventDetailRequest(DaraModel):
    def __init__(
        self,
        event_id: int = None,
        event_source: str = None,
        lang: str = None,
    ):
        # Event ID.
        # > You can call [ListAttackPathEvent](~~ListAttackPathEvent~~) to query the event ID.
        self.event_id = event_id
        # Data source. The default value is **default**. Values:
        #  - **caasm**: Attack surface
        #  - **default**: Attack path
        self.event_source = event_source
        # The language type for request and response, default is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
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

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

