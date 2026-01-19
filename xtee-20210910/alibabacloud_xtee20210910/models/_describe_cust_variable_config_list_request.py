# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustVariableConfigListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        biz_type: str = None,
        reg_id: str = None,
        time_type: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Configuration type
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Region code
        self.reg_id = reg_id
        # Time type
        self.time_type = time_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.time_type is not None:
            result['timeType'] = self.time_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('timeType') is not None:
            self.time_type = m.get('timeType')

        return self

