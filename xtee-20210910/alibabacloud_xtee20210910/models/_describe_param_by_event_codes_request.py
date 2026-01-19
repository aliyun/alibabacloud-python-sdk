# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParamByEventCodesRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_codes: str = None,
        parma: str = None,
        reg_id: str = None,
    ):
        # Set the language type for request and response, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event code.
        # 
        # This parameter is required.
        self.event_codes = event_codes
        # Query condition
        self.parma = parma
        # Region code
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.event_codes is not None:
            result['eventCodes'] = self.event_codes

        if self.parma is not None:
            result['parma'] = self.parma

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('parma') is not None:
            self.parma = m.get('parma')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

