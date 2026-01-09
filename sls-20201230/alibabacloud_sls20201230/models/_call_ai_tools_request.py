# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CallAiToolsRequest(DaraModel):
    def __init__(
        self,
        params: Dict[str, str] = None,
        region_id: str = None,
        tool_name: str = None,
    ):
        self.params = params
        self.region_id = region_id
        # This parameter is required.
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params is not None:
            result['params'] = self.params

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        return self

