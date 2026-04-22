# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScriptTrendingReportRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        script_id: str = None,
        start_time: int = None,
        time_interval: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.script_id = script_id
        self.start_time = start_time
        self.time_interval = time_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')

        return self

