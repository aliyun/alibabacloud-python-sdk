# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSDKDownloadListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        device_type: str = None,
        list_type: str = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Device type.
        self.device_type = device_type
        # Download type
        self.list_type = list_type
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

        if self.device_type is not None:
            result['deviceType'] = self.device_type

        if self.list_type is not None:
            result['listType'] = self.list_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')

        if m.get('listType') is not None:
            self.list_type = m.get('listType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

