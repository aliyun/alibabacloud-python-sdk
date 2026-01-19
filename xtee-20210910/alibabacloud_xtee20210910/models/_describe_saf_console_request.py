# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSafConsoleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        content: str = None,
        service: str = None,
    ):
        # Set the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Query content.
        self.content = content
        # Service to be called.
        # 
        # This parameter is required.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.content is not None:
            result['content'] = self.content

        if self.service is not None:
            result['service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('service') is not None:
            self.service = m.get('service')

        return self

