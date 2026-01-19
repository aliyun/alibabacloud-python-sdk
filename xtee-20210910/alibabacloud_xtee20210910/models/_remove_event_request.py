# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveEventRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        event_code: str = None,
        id: int = None,
        reg_id: str = None,
        template_code: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Creation type
        self.create_type = create_type
        # Event code
        self.event_code = event_code
        # Event ID
        self.id = id
        # Region code
        self.reg_id = reg_id
        # Input field template type
        self.template_code = template_code

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

        if self.id is not None:
            result['id'] = self.id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.template_code is not None:
            result['templateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('templateCode') is not None:
            self.template_code = m.get('templateCode')

        return self

