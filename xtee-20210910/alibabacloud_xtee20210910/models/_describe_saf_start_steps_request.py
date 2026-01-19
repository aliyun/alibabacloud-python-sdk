# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSafStartStepsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        aliyun_server: bool = None,
        device_types_str: str = None,
        event_code: str = None,
        language: str = None,
        reg_id: str = None,
        server_region: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Whether the server is an Alibaba Cloud server
        # 
        # true or false
        self.aliyun_server = aliyun_server
        # Used to receive a collection of strings from the frontend that POP cannot accept
        #      
        # Device type
        self.device_types_str = device_types_str
        # Event code
        self.event_code = event_code
        # Language, parameters can be passed
        # - zh-CN: Chinese (default)
        # - en-US: English
        self.language = language
        # Region code
        self.reg_id = reg_id
        # Server region
        self.server_region = server_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.aliyun_server is not None:
            result['aliyunServer'] = self.aliyun_server

        if self.device_types_str is not None:
            result['deviceTypesStr'] = self.device_types_str

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.language is not None:
            result['language'] = self.language

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.server_region is not None:
            result['serverRegion'] = self.server_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('aliyunServer') is not None:
            self.aliyun_server = m.get('aliyunServer')

        if m.get('deviceTypesStr') is not None:
            self.device_types_str = m.get('deviceTypesStr')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('serverRegion') is not None:
            self.server_region = m.get('serverRegion')

        return self

