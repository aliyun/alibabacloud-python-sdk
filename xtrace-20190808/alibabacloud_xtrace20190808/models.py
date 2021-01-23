# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class GetTagKeyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_name: str = None,
        span_name: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.region_id = region_id
        self.service_name = service_name
        self.span_name = span_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class GetTagKeyResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_key: List[str] = None,
    ):
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class GetTagKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_keys: GetTagKeyResponseBodyTagKeys = None,
    ):
        self.request_id = request_id
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            self.tag_keys.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            temp_model = GetTagKeyResponseBodyTagKeys()
            self.tag_keys = temp_model.from_map(m['TagKeys'])
        return self


class GetTagKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTagKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTagKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagValRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_name: str = None,
        span_name: str = None,
        tag_key: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.region_id = region_id
        self.service_name = service_name
        self.span_name = span_name
        self.tag_key = tag_key
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class GetTagValResponseBodyTagValues(TeaModel):
    def __init__(
        self,
        tag_value: List[str] = None,
    ):
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetTagValResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_values: GetTagValResponseBodyTagValues = None,
    ):
        self.request_id = request_id
        self.tag_values = tag_values

    def validate(self):
        if self.tag_values:
            self.tag_values.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            temp_model = GetTagValResponseBodyTagValues()
            self.tag_values = temp_model.from_map(m['TagValues'])
        return self


class GetTagValResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTagValResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTagValResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        app_type: str = None,
        proxy_user_id: str = None,
        is_force: bool = None,
    ):
        self.region_id = region_id
        self.app_type = app_type
        self.proxy_user_id = proxy_user_id
        self.is_force = is_force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.is_force is not None:
            result['IsForce'] = self.is_force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('IsForce') is not None:
            self.is_force = m.get('IsForce')
        return self


class GetTokenResponseBodyToken(TeaModel):
    def __init__(
        self,
        domain: str = None,
        license_key: str = None,
        internal_domain: str = None,
        pid: str = None,
    ):
        self.domain = domain
        self.license_key = license_key
        self.internal_domain = internal_domain
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.internal_domain is not None:
            result['InternalDomain'] = self.internal_domain
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('InternalDomain') is not None:
            self.internal_domain = m.get('InternalDomain')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: GetTokenResponseBodyToken = None,
    ):
        self.request_id = request_id
        self.token = token

    def validate(self):
        if self.token:
            self.token.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            temp_model = GetTokenResponseBodyToken()
            self.token = temp_model.from_map(m['Token'])
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(
        self,
        trace_id: str = None,
        app_type: str = None,
        region_id: str = None,
    ):
        self.trace_id = trace_id
        self.app_type = app_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceResponseBodySpansSpanTagEntryListTagEntry(TeaModel):
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


class GetTraceResponseBodySpansSpanTagEntryList(TeaModel):
    def __init__(
        self,
        tag_entry: List[GetTraceResponseBodySpansSpanTagEntryListTagEntry] = None,
    ):
        self.tag_entry = tag_entry

    def validate(self):
        if self.tag_entry:
            for k in self.tag_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagEntry'] = []
        if self.tag_entry is not None:
            for k in self.tag_entry:
                result['TagEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry = []
        if m.get('TagEntry') is not None:
            for k in m.get('TagEntry'):
                temp_model = GetTraceResponseBodySpansSpanTagEntryListTagEntry()
                self.tag_entry.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry(TeaModel):
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


class GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList(TeaModel):
    def __init__(
        self,
        tag_entry: List[GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry] = None,
    ):
        self.tag_entry = tag_entry

    def validate(self):
        if self.tag_entry:
            for k in self.tag_entry:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagEntry'] = []
        if self.tag_entry is not None:
            for k in self.tag_entry:
                result['TagEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry = []
        if m.get('TagEntry') is not None:
            for k in m.get('TagEntry'):
                temp_model = GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryListTagEntry()
                self.tag_entry.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodySpansSpanLogEventListLogEvent(TeaModel):
    def __init__(
        self,
        tag_entry_list: GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            self.tag_entry_list.validate()

    def to_map(self):
        result = dict()
        if self.tag_entry_list is not None:
            result['TagEntryList'] = self.tag_entry_list.to_map()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagEntryList') is not None:
            temp_model = GetTraceResponseBodySpansSpanLogEventListLogEventTagEntryList()
            self.tag_entry_list = temp_model.from_map(m['TagEntryList'])
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpansSpanLogEventList(TeaModel):
    def __init__(
        self,
        log_event: List[GetTraceResponseBodySpansSpanLogEventListLogEvent] = None,
    ):
        self.log_event = log_event

    def validate(self):
        if self.log_event:
            for k in self.log_event:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LogEvent'] = []
        if self.log_event is not None:
            for k in self.log_event:
                result['LogEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_event = []
        if m.get('LogEvent') is not None:
            for k in m.get('LogEvent'):
                temp_model = GetTraceResponseBodySpansSpanLogEventListLogEvent()
                self.log_event.append(temp_model.from_map(k))
        return self


class GetTraceResponseBodySpansSpan(TeaModel):
    def __init__(
        self,
        span_id: str = None,
        operation_name: str = None,
        result_code: str = None,
        timestamp: int = None,
        tag_entry_list: GetTraceResponseBodySpansSpanTagEntryList = None,
        log_event_list: GetTraceResponseBodySpansSpanLogEventList = None,
        have_stack: bool = None,
        service_ip: str = None,
        parent_span_id: str = None,
        duration: int = None,
        rpc_id: str = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.span_id = span_id
        self.operation_name = operation_name
        self.result_code = result_code
        self.timestamp = timestamp
        self.tag_entry_list = tag_entry_list
        self.log_event_list = log_event_list
        self.have_stack = have_stack
        self.service_ip = service_ip
        self.parent_span_id = parent_span_id
        self.duration = duration
        self.rpc_id = rpc_id
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        if self.tag_entry_list:
            self.tag_entry_list.validate()
        if self.log_event_list:
            self.log_event_list.validate()

    def to_map(self):
        result = dict()
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.tag_entry_list is not None:
            result['TagEntryList'] = self.tag_entry_list.to_map()
        if self.log_event_list is not None:
            result['LogEventList'] = self.log_event_list.to_map()
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.parent_span_id is not None:
            result['ParentSpanId'] = self.parent_span_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TagEntryList') is not None:
            temp_model = GetTraceResponseBodySpansSpanTagEntryList()
            self.tag_entry_list = temp_model.from_map(m['TagEntryList'])
        if m.get('LogEventList') is not None:
            temp_model = GetTraceResponseBodySpansSpanLogEventList()
            self.log_event_list = temp_model.from_map(m['LogEventList'])
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('ParentSpanId') is not None:
            self.parent_span_id = m.get('ParentSpanId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBodySpans(TeaModel):
    def __init__(
        self,
        span: List[GetTraceResponseBodySpansSpan] = None,
    ):
        self.span = span

    def validate(self):
        if self.span:
            for k in self.span:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Span'] = []
        if self.span is not None:
            for k in self.span:
                result['Span'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.span = []
        if m.get('Span') is not None:
            for k in m.get('Span'):
                temp_model = GetTraceResponseBodySpansSpan()
                self.span.append(temp_model.from_map(k))
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spans: GetTraceResponseBodySpans = None,
    ):
        self.request_id = request_id
        self.spans = spans

    def validate(self):
        if self.spans:
            self.spans.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.spans is not None:
            result['Spans'] = self.spans.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Spans') is not None:
            temp_model = GetTraceResponseBodySpans()
            self.spans = temp_model.from_map(m['Spans'])
        return self


class GetTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTraceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceAnalysisRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        api: str = None,
        query: str = None,
        proxy_user_id: str = None,
    ):
        self.region_id = region_id
        self.api = api
        self.query = query
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.api is not None:
            result['Api'] = self.api
        if self.query is not None:
            result['Query'] = self.query
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class GetTraceAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetTraceAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTraceAnalysisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTraceAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpOrHostsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_name: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.region_id = region_id
        self.service_name = service_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListIpOrHostsResponseBodyIpNames(TeaModel):
    def __init__(
        self,
        ip_name: List[str] = None,
    ):
        self.ip_name = ip_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip_name is not None:
            result['IpName'] = self.ip_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpName') is not None:
            self.ip_name = m.get('IpName')
        return self


class ListIpOrHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_names: ListIpOrHostsResponseBodyIpNames = None,
    ):
        self.request_id = request_id
        self.ip_names = ip_names

    def validate(self):
        if self.ip_names:
            self.ip_names.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_names is not None:
            result['IpNames'] = self.ip_names.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpNames') is not None:
            temp_model = ListIpOrHostsResponseBodyIpNames()
            self.ip_names = temp_model.from_map(m['IpNames'])
        return self


class ListIpOrHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIpOrHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIpOrHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        app_type: str = None,
    ):
        self.region_id = region_id
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class ListServicesResponseBodyServicesService(TeaModel):
    def __init__(
        self,
        pid: str = None,
        service_name: str = None,
        region_id: str = None,
    ):
        self.pid = pid
        self.service_name = service_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        service: List[ListServicesResponseBodyServicesService] = None,
    ):
        self.service = service

    def validate(self):
        if self.service:
            for k in self.service:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Service'] = []
        if self.service is not None:
            for k in self.service:
                result['Service'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service = []
        if m.get('Service') is not None:
            for k in m.get('Service'):
                temp_model = ListServicesResponseBodyServicesService()
                self.service.append(temp_model.from_map(k))
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        services: ListServicesResponseBodyServices = None,
        request_id: str = None,
    ):
        self.services = services
        self.request_id = request_id

    def validate(self):
        if self.services:
            self.services.validate()

    def to_map(self):
        result = dict()
        if self.services is not None:
            result['Services'] = self.services.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            temp_model = ListServicesResponseBodyServices()
            self.services = temp_model.from_map(m['Services'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpanNamesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_name: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.region_id = region_id
        self.service_name = service_name
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListSpanNamesResponseBodySpanNames(TeaModel):
    def __init__(
        self,
        span_name: List[str] = None,
    ):
        self.span_name = span_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.span_name is not None:
            result['SpanName'] = self.span_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpanName') is not None:
            self.span_name = m.get('SpanName')
        return self


class ListSpanNamesResponseBody(TeaModel):
    def __init__(
        self,
        span_names: ListSpanNamesResponseBodySpanNames = None,
        request_id: str = None,
    ):
        self.span_names = span_names
        self.request_id = request_id

    def validate(self):
        if self.span_names:
            self.span_names.validate()

    def to_map(self):
        result = dict()
        if self.span_names is not None:
            result['SpanNames'] = self.span_names.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpanNames') is not None:
            temp_model = ListSpanNamesResponseBodySpanNames()
            self.span_names = temp_model.from_map(m['SpanNames'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSpanNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSpanNamesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSpanNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricRequestFilters(TeaModel):
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


class QueryMetricRequest(TeaModel):
    def __init__(
        self,
        interval_in_sec: int = None,
        start_time: int = None,
        end_time: int = None,
        order_by: str = None,
        limit: int = None,
        metric: str = None,
        order: str = None,
        proxy_user_id: str = None,
        filters: List[QueryMetricRequestFilters] = None,
        dimensions: List[str] = None,
        measures: List[str] = None,
    ):
        self.interval_in_sec = interval_in_sec
        self.start_time = start_time
        self.end_time = end_time
        self.order_by = order_by
        self.limit = limit
        self.metric = metric
        self.order = order
        self.proxy_user_id = proxy_user_id
        self.filters = filters
        self.dimensions = dimensions
        self.measures = measures

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.measures is not None:
            result['Measures'] = self.measures
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        return self


class QueryMetricResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequestTag(TeaModel):
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


class SearchTracesRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        region_id: str = None,
        service_name: str = None,
        operation_name: str = None,
        min_duration: int = None,
        app_type: str = None,
        page_number: int = None,
        page_size: int = None,
        reverse: bool = None,
        service_ip: str = None,
        tag: List[SearchTracesRequestTag] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.region_id = region_id
        self.service_name = service_name
        self.operation_name = operation_name
        self.min_duration = min_duration
        self.app_type = app_type
        self.page_number = page_number
        self.page_size = page_size
        self.reverse = reverse
        self.service_ip = service_ip
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = SearchTracesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyPageBeanTraceInfosTraceInfo(TeaModel):
    def __init__(
        self,
        operation_name: str = None,
        service_ip: str = None,
        duration: int = None,
        timestamp: int = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.operation_name = operation_name
        self.service_ip = service_ip
        self.duration = duration
        self.timestamp = timestamp
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBodyPageBeanTraceInfos(TeaModel):
    def __init__(
        self,
        trace_info: List[SearchTracesResponseBodyPageBeanTraceInfosTraceInfo] = None,
    ):
        self.trace_info = trace_info

    def validate(self):
        if self.trace_info:
            for k in self.trace_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TraceInfo'] = []
        if self.trace_info is not None:
            for k in self.trace_info:
                result['TraceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_info = []
        if m.get('TraceInfo') is not None:
            for k in m.get('TraceInfo'):
                temp_model = SearchTracesResponseBodyPageBeanTraceInfosTraceInfo()
                self.trace_info.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        trace_infos: SearchTracesResponseBodyPageBeanTraceInfos = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.trace_infos = trace_infos
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.trace_infos:
            self.trace_infos.validate()

    def to_map(self):
        result = dict()
        if self.trace_infos is not None:
            result['TraceInfos'] = self.trace_infos.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceInfos') is not None:
            temp_model = SearchTracesResponseBodyPageBeanTraceInfos()
            self.trace_infos = temp_model.from_map(m['TraceInfos'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchTracesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTracesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTracesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


