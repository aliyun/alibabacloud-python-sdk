# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsoleFuncGrayStatusRequest(DaraModel):
    def __init__(
        self,
        condition: str = None,
        lang: str = None,
    ):
        # Name of the function module.
        self.condition = condition
        # Set the language type for request and response messages. Default value: **zh**. Values:
        # 
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
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

