# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFieldListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        condition: str = None,
        inputs: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Query input name or title
        self.condition = condition
        # Selected fields
        self.inputs = inputs
        # Region code
        # 
        # This parameter is required.
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

        if self.condition is not None:
            result['condition'] = self.condition

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

