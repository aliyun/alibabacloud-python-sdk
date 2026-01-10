# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ActivateTemplateMCPRequest(DaraModel):
    def __init__(
        self,
        enabled_tools: List[str] = None,
        transport: str = None,
    ):
        self.enabled_tools = enabled_tools
        self.transport = transport

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled_tools is not None:
            result['enabledTools'] = self.enabled_tools

        if self.transport is not None:
            result['transport'] = self.transport

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabledTools') is not None:
            self.enabled_tools = m.get('enabledTools')

        if m.get('transport') is not None:
            self.transport = m.get('transport')

        return self

