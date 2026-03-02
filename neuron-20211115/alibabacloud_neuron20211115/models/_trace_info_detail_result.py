# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class TraceInfoDetailResult(DaraModel):
    def __init__(
        self,
        trace_details: List[main_models.TraceInfoDetailResultTraceDetails] = None,
    ):
        self.trace_details = trace_details

    def validate(self):
        if self.trace_details:
            for v1 in self.trace_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['traceDetails'] = []
        if self.trace_details is not None:
            for k1 in self.trace_details:
                result['traceDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_details = []
        if m.get('traceDetails') is not None:
            for k1 in m.get('traceDetails'):
                temp_model = main_models.TraceInfoDetailResultTraceDetails()
                self.trace_details.append(temp_model.from_map(k1))

        return self



class TraceInfoDetailResultTraceDetails(DaraModel):
    def __init__(
        self,
        children: List[Dict[str, Any]] = None,
        duration: int = None,
        have_stack: bool = None,
        log_event_list: List[main_models.TraceSpansLogEventList] = None,
        operation_name: str = None,
        parent_span_id: str = None,
        result_code: str = None,
        rpc_id: str = None,
        rpc_type: int = None,
        rpc_type_name: str = None,
        service_ip: str = None,
        service_name: str = None,
        span_id: str = None,
        tag_entry_list: List[main_models.TagEntry] = None,
        timestamp: int = None,
        trace_id: str = None,
    ):
        self.children = children
        self.duration = duration
        self.have_stack = have_stack
        self.log_event_list = log_event_list
        self.operation_name = operation_name
        self.parent_span_id = parent_span_id
        self.result_code = result_code
        self.rpc_id = rpc_id
        self.rpc_type = rpc_type
        self.rpc_type_name = rpc_type_name
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
        if self.children is not None:
            result['children'] = self.children

        if self.duration is not None:
            result['duration'] = self.duration

        if self.have_stack is not None:
            result['haveStack'] = self.have_stack

        result['logEventList'] = []
        if self.log_event_list is not None:
            for k1 in self.log_event_list:
                result['logEventList'].append(k1.to_map() if k1 else None)

        if self.operation_name is not None:
            result['operationName'] = self.operation_name

        if self.parent_span_id is not None:
            result['parentSpanId'] = self.parent_span_id

        if self.result_code is not None:
            result['resultCode'] = self.result_code

        if self.rpc_id is not None:
            result['rpcId'] = self.rpc_id

        if self.rpc_type is not None:
            result['rpcType'] = self.rpc_type

        if self.rpc_type_name is not None:
            result['rpcTypeName'] = self.rpc_type_name

        if self.service_ip is not None:
            result['serviceIp'] = self.service_ip

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.span_id is not None:
            result['spanId'] = self.span_id

        result['tagEntryList'] = []
        if self.tag_entry_list is not None:
            for k1 in self.tag_entry_list:
                result['tagEntryList'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('children') is not None:
            self.children = m.get('children')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('haveStack') is not None:
            self.have_stack = m.get('haveStack')

        self.log_event_list = []
        if m.get('logEventList') is not None:
            for k1 in m.get('logEventList'):
                temp_model = main_models.TraceSpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k1))

        if m.get('operationName') is not None:
            self.operation_name = m.get('operationName')

        if m.get('parentSpanId') is not None:
            self.parent_span_id = m.get('parentSpanId')

        if m.get('resultCode') is not None:
            self.result_code = m.get('resultCode')

        if m.get('rpcId') is not None:
            self.rpc_id = m.get('rpcId')

        if m.get('rpcType') is not None:
            self.rpc_type = m.get('rpcType')

        if m.get('rpcTypeName') is not None:
            self.rpc_type_name = m.get('rpcTypeName')

        if m.get('serviceIp') is not None:
            self.service_ip = m.get('serviceIp')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('spanId') is not None:
            self.span_id = m.get('spanId')

        self.tag_entry_list = []
        if m.get('tagEntryList') is not None:
            for k1 in m.get('tagEntryList'):
                temp_model = main_models.TagEntry()
                self.tag_entry_list.append(temp_model.from_map(k1))

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

