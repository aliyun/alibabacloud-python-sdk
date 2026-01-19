# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class QueryRequestLogsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        request_logs: main_models.QueryRequestLogsResponseBodyRequestLogs = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The request logs.
        self.request_logs = request_logs

    def validate(self):
        if self.request_logs:
            self.request_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_logs is not None:
            result['RequestLogs'] = self.request_logs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestLogs') is not None:
            temp_model = main_models.QueryRequestLogsResponseBodyRequestLogs()
            self.request_logs = temp_model.from_map(m.get('RequestLogs'))

        return self

class QueryRequestLogsResponseBodyRequestLogs(DaraModel):
    def __init__(
        self,
        request_log: List[main_models.QueryRequestLogsResponseBodyRequestLogsRequestLog] = None,
    ):
        self.request_log = request_log

    def validate(self):
        if self.request_log:
            for v1 in self.request_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RequestLog'] = []
        if self.request_log is not None:
            for k1 in self.request_log:
                result['RequestLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_log = []
        if m.get('RequestLog') is not None:
            for k1 in m.get('RequestLog'):
                temp_model = main_models.QueryRequestLogsResponseBodyRequestLogsRequestLog()
                self.request_log.append(temp_model.from_map(k1))

        return self

class QueryRequestLogsResponseBodyRequestLogsRequestLog(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        app_name: str = None,
        backend_request_end: int = None,
        backend_request_start: int = None,
        backend_response_end: int = None,
        backend_response_start: int = None,
        client_ip: str = None,
        client_nonce: str = None,
        consumer_app_id: str = None,
        consumer_app_key: str = None,
        custom_trace_id: str = None,
        domain: str = None,
        error_code: str = None,
        error_message: str = None,
        exception: str = None,
        front_request_end: int = None,
        front_request_start: int = None,
        front_response_end: int = None,
        front_response_start: int = None,
        group_id: str = None,
        group_name: str = None,
        http_method: str = None,
        http_path: str = None,
        initial_request_id: str = None,
        instance_id: str = None,
        jwt_claims: str = None,
        region: str = None,
        request_body: str = None,
        request_headers: str = None,
        request_id: str = None,
        request_protocol: str = None,
        request_query_string: str = None,
        request_size: str = None,
        request_time: str = None,
        response_body: str = None,
        response_headers: str = None,
        response_size: str = None,
        service_latency: str = None,
        stage_id: str = None,
        stage_name: str = None,
        status_code: str = None,
        total_latency: str = None,
        plugin: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The application name.
        self.app_name = app_name
        # The time when API Gateway finished forwarding the request to the backend service.
        self.backend_request_end = backend_request_end
        # The time when API Gateway started to forward the request to the backend service.
        self.backend_request_start = backend_request_start
        # The time when API Gateway finished receiving the response from the backend service.
        self.backend_response_end = backend_response_end
        # The time when API Gateway started to receive the response from the backend service.
        self.backend_response_start = backend_response_start
        # The IP address of the client that sends the request.
        self.client_ip = client_ip
        # The X-Ca-Nonce header included in the request from the client.
        self.client_nonce = client_nonce
        # The application ID that is used by the caller.
        self.consumer_app_id = consumer_app_id
        # The App Key that is used by the caller.
        self.consumer_app_key = consumer_app_key
        # The custom trace ID.
        self.custom_trace_id = custom_trace_id
        # The requested domain name in the request.
        self.domain = domain
        # The error code that is returned.
        self.error_code = error_code
        # The error message returned if the call fails.
        self.error_message = error_message
        # The specific error message returned by the backend service.
        self.exception = exception
        # The time when API Gateway finished receiving the request.
        self.front_request_end = front_request_end
        # The time when API Gateway started to receive the request.
        self.front_request_start = front_request_start
        # The time when API Gateway finished forwarding the response to the client.
        self.front_response_end = front_response_end
        # The time when API Gateway started to forward the response to the client.
        self.front_response_start = front_response_start
        # The ID of the API group to which the API belongs.
        self.group_id = group_id
        # The name of the API group to which the API belongs.
        self.group_name = group_name
        # The HTTP method that is used to send the request.
        self.http_method = http_method
        # The path of the request.
        self.http_path = http_path
        # The initial request ID when API Gateway calls an API. For example, if API-1 calls API-2, the initialRequestId parameter in the log of API-2 indicates the ID of the request from API-1.
        self.initial_request_id = initial_request_id
        # The ID of the API Gateway instance to which the API belongs.
        self.instance_id = instance_id
        # The JSON web token (JWT) claims. The claims can be configured at the group level.
        self.jwt_claims = jwt_claims
        # The region in which the instance resides.
        self.region = region
        # The request body. A request body cannot exceed 1,024 bytes in size.
        self.request_body = request_body
        # The request headers.
        self.request_headers = request_headers
        # The request ID.
        self.request_id = request_id
        # The protocol used by the client to send the request. Valid values: HTTP, HTTPS, and WS.
        self.request_protocol = request_protocol
        # The query string for the request.
        self.request_query_string = request_query_string
        # The size of the request. Unit: bytes.
        self.request_size = request_size
        # The request time, in UTC.
        self.request_time = request_time
        # The response body. A response body cannot exceed 1,024 bytes in size.
        self.response_body = response_body
        # The headers in the API response.
        self.response_headers = response_headers
        # The size of returned data. Unit: bytes.
        self.response_size = response_size
        # The total time consumed to access the backend resources. The total time includes the time consumed to request a connection to the resources, the time consumed to establish the connection, and the time consumed to call the backend service. Unit: milliseconds.
        self.service_latency = service_latency
        # The ID of the API environment.
        self.stage_id = stage_id
        # The name of the API environment.
        self.stage_name = stage_name
        # The status code returned.
        self.status_code = status_code
        # The total time consumed by the request. Unit: milliseconds.
        self.total_latency = total_latency
        # The plug-in hit by the request and the relevant context.
        self.plugin = plugin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.backend_request_end is not None:
            result['BackendRequestEnd'] = self.backend_request_end

        if self.backend_request_start is not None:
            result['BackendRequestStart'] = self.backend_request_start

        if self.backend_response_end is not None:
            result['BackendResponseEnd'] = self.backend_response_end

        if self.backend_response_start is not None:
            result['BackendResponseStart'] = self.backend_response_start

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_nonce is not None:
            result['ClientNonce'] = self.client_nonce

        if self.consumer_app_id is not None:
            result['ConsumerAppId'] = self.consumer_app_id

        if self.consumer_app_key is not None:
            result['ConsumerAppKey'] = self.consumer_app_key

        if self.custom_trace_id is not None:
            result['CustomTraceId'] = self.custom_trace_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.exception is not None:
            result['Exception'] = self.exception

        if self.front_request_end is not None:
            result['FrontRequestEnd'] = self.front_request_end

        if self.front_request_start is not None:
            result['FrontRequestStart'] = self.front_request_start

        if self.front_response_end is not None:
            result['FrontResponseEnd'] = self.front_response_end

        if self.front_response_start is not None:
            result['FrontResponseStart'] = self.front_response_start

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.http_path is not None:
            result['HttpPath'] = self.http_path

        if self.initial_request_id is not None:
            result['InitialRequestId'] = self.initial_request_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.jwt_claims is not None:
            result['JwtClaims'] = self.jwt_claims

        if self.region is not None:
            result['Region'] = self.region

        if self.request_body is not None:
            result['RequestBody'] = self.request_body

        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_protocol is not None:
            result['RequestProtocol'] = self.request_protocol

        if self.request_query_string is not None:
            result['RequestQueryString'] = self.request_query_string

        if self.request_size is not None:
            result['RequestSize'] = self.request_size

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        if self.response_body is not None:
            result['ResponseBody'] = self.response_body

        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers

        if self.response_size is not None:
            result['ResponseSize'] = self.response_size

        if self.service_latency is not None:
            result['ServiceLatency'] = self.service_latency

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.total_latency is not None:
            result['TotalLatency'] = self.total_latency

        if self.plugin is not None:
            result['plugin'] = self.plugin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BackendRequestEnd') is not None:
            self.backend_request_end = m.get('BackendRequestEnd')

        if m.get('BackendRequestStart') is not None:
            self.backend_request_start = m.get('BackendRequestStart')

        if m.get('BackendResponseEnd') is not None:
            self.backend_response_end = m.get('BackendResponseEnd')

        if m.get('BackendResponseStart') is not None:
            self.backend_response_start = m.get('BackendResponseStart')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientNonce') is not None:
            self.client_nonce = m.get('ClientNonce')

        if m.get('ConsumerAppId') is not None:
            self.consumer_app_id = m.get('ConsumerAppId')

        if m.get('ConsumerAppKey') is not None:
            self.consumer_app_key = m.get('ConsumerAppKey')

        if m.get('CustomTraceId') is not None:
            self.custom_trace_id = m.get('CustomTraceId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Exception') is not None:
            self.exception = m.get('Exception')

        if m.get('FrontRequestEnd') is not None:
            self.front_request_end = m.get('FrontRequestEnd')

        if m.get('FrontRequestStart') is not None:
            self.front_request_start = m.get('FrontRequestStart')

        if m.get('FrontResponseEnd') is not None:
            self.front_response_end = m.get('FrontResponseEnd')

        if m.get('FrontResponseStart') is not None:
            self.front_response_start = m.get('FrontResponseStart')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('HttpPath') is not None:
            self.http_path = m.get('HttpPath')

        if m.get('InitialRequestId') is not None:
            self.initial_request_id = m.get('InitialRequestId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JwtClaims') is not None:
            self.jwt_claims = m.get('JwtClaims')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestBody') is not None:
            self.request_body = m.get('RequestBody')

        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestProtocol') is not None:
            self.request_protocol = m.get('RequestProtocol')

        if m.get('RequestQueryString') is not None:
            self.request_query_string = m.get('RequestQueryString')

        if m.get('RequestSize') is not None:
            self.request_size = m.get('RequestSize')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        if m.get('ResponseBody') is not None:
            self.response_body = m.get('ResponseBody')

        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')

        if m.get('ResponseSize') is not None:
            self.response_size = m.get('ResponseSize')

        if m.get('ServiceLatency') is not None:
            self.service_latency = m.get('ServiceLatency')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TotalLatency') is not None:
            self.total_latency = m.get('TotalLatency')

        if m.get('plugin') is not None:
            self.plugin = m.get('plugin')

        return self

