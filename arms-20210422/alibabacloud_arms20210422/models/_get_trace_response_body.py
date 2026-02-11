# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class GetTraceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        spans: List[main_models.GetTraceResponseBodySpans] = None,
    ):
        self.request_id = request_id
        self.spans = spans

    def validate(self):
        if self.spans:
            for v1 in self.spans:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Spans'] = []
        if self.spans is not None:
            for k1 in self.spans:
                result['Spans'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.spans = []
        if m.get('Spans') is not None:
            for k1 in m.get('Spans'):
                temp_model = main_models.GetTraceResponseBodySpans()
                self.spans.append(temp_model.from_map(k1))

        return self

class GetTraceResponseBodySpans(DaraModel):
    def __init__(
        self,
        duration: int = None,
        have_stack: bool = None,
        log_event_list: List[main_models.GetTraceResponseBodySpansLogEventList] = None,
        operation_name: str = None,
        parent_span_id: str = None,
        result_code: str = None,
        rpc_id: str = None,
        rpc_type: int = None,
        service_ip: str = None,
        service_name: str = None,
        span_id: str = None,
        tag_entry_list: List[main_models.GetTraceResponseBodySpansTagEntryList] = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.duration = duration
        self.have_stack = have_stack
        self.log_event_list = log_event_list
        self.operation_name = operation_name
        self.parent_span_id = parent_span_id
        self.result_code = result_code
        self.rpc_id = rpc_id
        self.rpc_type = rpc_type
        self.service_ip = service_ip
        self.service_name = service_name
        self.span_id = span_id
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp
        self.trace_id = trace_id

    def validate(self):
        if self.log_event_list:
            for v1 in self.log_event_list:
                 if v1:
                    v1.validate()
        if self.tag_entry_list:
            for v1 in self.tag_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack

        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k1 in self.log_event_list:
                result['LogEventList'].append(k1.to_map() if k1 else None)

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id

        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type

        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.span_id is not None:
            result['SpanId'] = self.span_id

        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k1 in self.tag_entry_list:
                result['TagEntryList'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['TraceID'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')

        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k1 in m.get('LogEventList'):
                temp_model = main_models.GetTraceResponseBodySpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k1))

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')

        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')

        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')

        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k1 in m.get('TagEntryList'):
                temp_model = main_models.GetTraceResponseBodySpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k1))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')

        return self

class GetTraceResponseBodySpansTagEntryList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTraceResponseBodySpansLogEventList(DaraModel):
    def __init__(
        self,
        tag_entry_list: List[main_models.GetTraceResponseBodySpansLogEventListTagEntryList] = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            for v1 in self.tag_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k1 in self.tag_entry_list:
                result['TagEntryList'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k1 in m.get('TagEntryList'):
                temp_model = main_models.GetTraceResponseBodySpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k1))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class GetTraceResponseBodySpansLogEventListTagEntryList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

