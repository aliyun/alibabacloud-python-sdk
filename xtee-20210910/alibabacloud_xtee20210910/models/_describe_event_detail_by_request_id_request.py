# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventDetailByRequestIdRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        event_code: str = None,
        event_time: int = None,
        reg_id: str = None,
        s_request_id: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Event code
        self.event_code = event_code
        # Event execution time
        self.event_time = event_time
        # Region code
        # 
        # This parameter is required.
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

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_time is not None:
            result['eventTime'] = self.event_time

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.s_request_id is not None:
            result['sRequestId'] = self.s_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sRequestId') is not None:
            self.s_request_id = m.get('sRequestId')

        return self

