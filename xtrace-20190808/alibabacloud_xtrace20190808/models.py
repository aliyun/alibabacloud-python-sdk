# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        service_name: str = None,
        spiregion_id: str = None,
        deletion_task_id: str = None,
        region_id: str = None,
    ):
        self.role_arn = role_arn
        self.service_name = service_name
        self.spiregion_id = spiregion_id
        self.deletion_task_id = deletion_task_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: List[str] = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeletingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        deletable: bool = None,
        role_usages: List[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages] = None,
    ):
        self.request_id = request_id
        self.deletable = deletable
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckServiceLinkedRoleForDeletingResponseBody = None,
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
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSamplingRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        proxy_user_id: str = None,
    ):
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class GetSamplingResponseBody(TeaModel):
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


class GetSamplingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSamplingResponseBody = None,
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
            temp_model = GetSamplingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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


class GetTagKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        self.request_id = request_id
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
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


class GetTagValResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_values: List[str] = None,
    ):
        self.request_id = request_id
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
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
    ):
        self.region_id = region_id
        self.app_type = app_type
        self.proxy_user_id = proxy_user_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
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


class GetTraceResponseBodySpansTagEntryList(TeaModel):
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


class GetTraceResponseBodySpansLogEventListTagEntryList(TeaModel):
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


class GetTraceResponseBodySpansLogEventList(TeaModel):
    def __init__(
        self,
        tag_entry_list: List[GetTraceResponseBodySpansLogEventListTagEntryList] = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpans(TeaModel):
    def __init__(
        self,
        tag_entry_list: List[GetTraceResponseBodySpansTagEntryList] = None,
        log_event_list: List[GetTraceResponseBodySpansLogEventList] = None,
        have_stack: bool = None,
        service_ip: str = None,
        operation_name: str = None,
        result_code: str = None,
        duration: int = None,
        rpc_id: str = None,
        timestamp: int = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.log_event_list = log_event_list
        self.have_stack = have_stack
        self.service_ip = service_ip
        self.operation_name = operation_name
        self.result_code = result_code
        self.duration = duration
        self.rpc_id = rpc_id
        self.timestamp = timestamp
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetTraceResponseBodySpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spans: List[GetTraceResponseBodySpans] = None,
    ):
        self.request_id = request_id
        self.spans = spans

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetTraceResponseBodySpans()
                self.spans.append(temp_model.from_map(k))
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


class ListIpOrHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_names: List[str] = None,
    ):
        self.request_id = request_id
        self.ip_names = ip_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_names is not None:
            result['IpNames'] = self.ip_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpNames') is not None:
            self.ip_names = m.get('IpNames')
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


class ListServicesResponseBodyServices(TeaModel):
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


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        services: List[ListServicesResponseBodyServices] = None,
        request_id: str = None,
    ):
        self.services = services
        self.request_id = request_id

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
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


class ListSpanNamesResponseBody(TeaModel):
    def __init__(
        self,
        span_names: List[str] = None,
        request_id: str = None,
    ):
        self.span_names = span_names
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.span_names is not None:
            result['SpanNames'] = self.span_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpanNames') is not None:
            self.span_names = m.get('SpanNames')
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


class OpenXtraceServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class OpenXtraceServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenXtraceServiceResponseBody = None,
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
            temp_model = OpenXtraceServiceResponseBody()
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


class SearchTracesResponseBodyPageBeanTraceInfos(TeaModel):
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


class SearchTracesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        trace_infos: List[SearchTracesResponseBodyPageBeanTraceInfos] = None,
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
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesResponseBodyPageBeanTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
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


class UpdateSamplingRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        proxy_user_id: str = None,
        sampling: str = None,
    ):
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.sampling = sampling

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.sampling is not None:
            result['Sampling'] = self.sampling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('Sampling') is not None:
            self.sampling = m.get('Sampling')
        return self


class UpdateSamplingResponseBody(TeaModel):
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


class UpdateSamplingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSamplingResponseBody = None,
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
            temp_model = UpdateSamplingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


