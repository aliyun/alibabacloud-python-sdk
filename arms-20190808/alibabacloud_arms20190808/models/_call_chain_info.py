# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CallChainInfo(DaraModel):
    def __init__(
        self,
        additional_info: str = None,
        app_name: str = None,
        app_type: str = None,
        children: List[main_models.CallChainInfo] = None,
        have_span: bool = None,
        log_map: Dict[str, dict] = None,
        log_time: int = None,
        parent_span_id: str = None,
        pid: str = None,
        region_id: str = None,
        result_code: str = None,
        rpc: str = None,
        rpc_id: str = None,
        rpc_type: int = None,
        server_ip: str = None,
        span: int = None,
        span_id: str = None,
        tag_map: Dict[str, str] = None,
        trace_id: str = None,
    ):
        self.additional_info = additional_info
        self.app_name = app_name
        self.app_type = app_type
        self.children = children
        self.have_span = have_span
        self.log_map = log_map
        self.log_time = log_time
        self.parent_span_id = parent_span_id
        self.pid = pid
        self.region_id = region_id
        self.result_code = result_code
        self.rpc = rpc
        self.rpc_id = rpc_id
        self.rpc_type = rpc_type
        self.server_ip = server_ip
        self.span = span
        self.span_id = span_id
        self.tag_map = tag_map
        self.trace_id = trace_id

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_info is not None:
            result['AdditionalInfo'] = self.additional_info

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.have_span is not None:
            result['HaveSpan'] = self.have_span

        if self.log_map is not None:
            result['LogMap'] = self.log_map

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.rpc is not None:
            result['Rpc'] = self.rpc

        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id

        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.span is not None:
            result['Span'] = self.span

        if self.span_id is not None:
            result['SpanId'] = self.span_id

        if self.tag_map is not None:
            result['TagMap'] = self.tag_map

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalInfo') is not None:
            self.additional_info = m.get('AdditionalInfo')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.CallChainInfo()
                self.children.append(temp_model.from_map(k1))

        if m.get('HaveSpan') is not None:
            self.have_span = m.get('HaveSpan')

        if m.get('LogMap') is not None:
            self.log_map = m.get('LogMap')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('Rpc') is not None:
            self.rpc = m.get('Rpc')

        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')

        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('Span') is not None:
            self.span = m.get('Span')

        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')

        if m.get('TagMap') is not None:
            self.tag_map = m.get('TagMap')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

