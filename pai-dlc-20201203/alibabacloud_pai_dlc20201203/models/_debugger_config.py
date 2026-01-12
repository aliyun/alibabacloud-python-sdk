# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DebuggerConfig(DaraModel):
    def __init__(
        self,
        content: str = None,
        debugger_config_id: str = None,
        description: str = None,
        display_name: str = None,
        gmt_create_time: str = None,
        gmt_modify_time: str = None,
    ):
        self.content = content
        self.debugger_config_id = debugger_config_id
        self.description = description
        self.display_name = display_name
        self.gmt_create_time = gmt_create_time
        self.gmt_modify_time = gmt_modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.debugger_config_id is not None:
            result['DebuggerConfigId'] = self.debugger_config_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DebuggerConfigId') is not None:
            self.debugger_config_id = m.get('DebuggerConfigId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        return self

