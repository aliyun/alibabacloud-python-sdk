# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobDebuggerConfig(DaraModel):
    def __init__(
        self,
        debugger_config_content: str = None,
        debugger_config_id: str = None,
        gmt_create_time: str = None,
        job_id: str = None,
    ):
        self.debugger_config_content = debugger_config_content
        self.debugger_config_id = debugger_config_id
        self.gmt_create_time = gmt_create_time
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content

        if self.debugger_config_id is not None:
            result['DebuggerConfigId'] = self.debugger_config_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')

        if m.get('DebuggerConfigId') is not None:
            self.debugger_config_id = m.get('DebuggerConfigId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

