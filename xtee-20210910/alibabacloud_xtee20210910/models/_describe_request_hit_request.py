# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRequestHitRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        s_request_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region code
        self.reg_id = reg_id
        # Request ID.
        # 
        # This parameter is required.
        self.s_request_id = s_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.s_request_id is not None:
            result['sRequestId'] = self.s_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sRequestId') is not None:
            self.s_request_id = m.get('sRequestId')

        return self

