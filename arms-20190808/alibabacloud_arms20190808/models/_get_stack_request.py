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
        span_id: str = None,
        start_time: int = None,
        trace_id: str = None,
    ):
        # The exit timestamp of the method call. Unit: milliseconds.
        self.end_time = end_time
        # The process identifier (PID) of the application. For more information about how to obtain the PID, see [Obtain the PID of an application](https://www.alibabacloud.com/help/zh/doc-detail/186100.htm?spm=a2cdw.13409063.0.0.7a72281f0bkTfx#title-imy-7gj-qhr).
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the remote procedure call (RPC) mode. You can obtain the ID by calling the **GetTrace** operation.
        # 
        # This parameter is required.
        self.rpc_id = rpc_id
        # The span ID of the trace. It is displayed on the Trace Explorer page in the ARMS console.
        self.span_id = span_id
        # The entry timestamp of the method call. Unit: milliseconds.
        self.start_time = start_time
        # The trace ID. It is displayed on the **Trace Explorer** page in the Application Real-Time Monitoring Service (ARMS) console.
        # 
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

        if self.span_id is not None:
            result['SpanID'] = self.span_id

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

        if m.get('SpanID') is not None:
            self.span_id = m.get('SpanID')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')

        return self

