# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEventStatusRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        event_code: str = None,
        from_event_satus: str = None,
        reg_id: str = None,
        to_event_satus: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Creation type
        self.create_type = create_type
        # Event code
        self.event_code = event_code
        # Initial event status, to avoid duplicate submissions or historical replays
        self.from_event_satus = from_event_satus
        # Region code
        self.reg_id = reg_id
        # Updated event status
        self.to_event_satus = to_event_satus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.from_event_satus is not None:
            result['fromEventSatus'] = self.from_event_satus

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.to_event_satus is not None:
            result['toEventSatus'] = self.to_event_satus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('fromEventSatus') is not None:
            self.from_event_satus = m.get('fromEventSatus')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('toEventSatus') is not None:
            self.to_event_satus = m.get('toEventSatus')

        return self

