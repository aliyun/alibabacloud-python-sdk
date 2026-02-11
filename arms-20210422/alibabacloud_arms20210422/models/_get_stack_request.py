# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        pid: str = None,
        region_id: str = None,
        rpc_id: str = None,
        start_time: int = None,
        trace_id: str = None,
    ):
        self.end_time = end_time
        self.pid = pid
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.rpc_id = rpc_id
        self.start_time = start_time
        # This parameter is required.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rpc_id is not None:
            result['RpcID'] = self.rpc_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.trace_id is not None:
            result['TraceID'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RpcID') is not None:
            self.rpc_id = m.get('RpcID')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')

        return self

