# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIdentifyTaskStatusRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
    ):
        # Task ID, obtained from the ID field in the response after calling CreateScanTask or ScanOssObjectV1.
        # 
        # This parameter is required.
        self.id = id
        # Language type for request and response messages, default is **zh_cn**. Values:
        # - **zh_cn**: Chinese (Simplified)
        # - **en_us**: English (United States)
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

