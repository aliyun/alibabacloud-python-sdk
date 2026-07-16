# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMatchedMaliciousNamesRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        levels: str = None,
    ):
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The risk levels of the malicious samples in images to query. You can specify multiple values. Separate multiple values with commas (,). Valid values:
        # - **serious**: urgent
        # - **suspicious**: suspicious
        # - **remind**: reminder.
        self.levels = levels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.levels is not None:
            result['Levels'] = self.levels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

        return self

