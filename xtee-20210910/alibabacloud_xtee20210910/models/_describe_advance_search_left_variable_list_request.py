# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAdvanceSearchLeftVariableListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_codes: str = None,
        reg_id: str = None,
        scene: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event code.
        # 
        # This parameter is required.
        self.event_codes = event_codes
        # Region code
        self.reg_id = reg_id
        # Scene
        # 
        # This parameter is required.
        self.scene = scene

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

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.scene is not None:
            result['scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCodes') is not None:
            self.event_codes = m.get('eventCodes')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        return self

