# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateTrailRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        role_name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_key_prefix = oss_key_prefix
        self.role_name = role_name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class CreateTrailResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        param: str = None,
        result: str = None,
        role_name: str = None,
    ):
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_key_prefix = oss_key_prefix
        self.param = param
        self.result = result
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrailRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DeleteTrailResponseBody(TeaModel):
    def __init__(
        self,
        param: str = None,
        result: str = None,
    ):
        self.param = param
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrailsRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeTrailsResponseBody(TeaModel):
    def __init__(
        self,
        param: str = None,
        result: str = None,
        trail_list: str = None,
    ):
        self.param = param
        self.result = result
        self.trail_list = trail_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        if self.trail_list is not None:
            result['TrailList'] = self.trail_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TrailList') is not None:
            self.trail_list = m.get('TrailList')
        return self


class DescribeTrailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTrailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EchoRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        format: str = None,
        help: str = None,
        is_logging: str = None,
        key_prefix: str = None,
        latest_delivery_error: str = None,
        latest_delivery_time: str = None,
        name: str = None,
        start_logging_time: str = None,
        status: str = None,
        stop_logging_time: str = None,
        type: str = None,
        version: str = None,
    ):
        self.bucket_name = bucket_name
        self.format = format
        self.help = help
        self.is_logging = is_logging
        self.key_prefix = key_prefix
        self.latest_delivery_error = latest_delivery_error
        self.latest_delivery_time = latest_delivery_time
        self.name = name
        self.start_logging_time = start_logging_time
        self.status = status
        self.stop_logging_time = stop_logging_time
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.is_logging is not None:
            result['IsLogging'] = self.is_logging
        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix
        if self.latest_delivery_error is not None:
            result['LatestDeliveryError'] = self.latest_delivery_error
        if self.latest_delivery_time is not None:
            result['LatestDeliveryTime'] = self.latest_delivery_time
        if self.name is not None:
            result['Name'] = self.name
        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('IsLogging') is not None:
            self.is_logging = m.get('IsLogging')
        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')
        if m.get('LatestDeliveryError') is not None:
            self.latest_delivery_error = m.get('LatestDeliveryError')
        if m.get('LatestDeliveryTime') is not None:
            self.latest_delivery_time = m.get('LatestDeliveryTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class EchoResponseBody(TeaModel):
    def __init__(
        self,
        param: str = None,
        result: str = None,
        request_id: str = None,
    ):
        self.param = param
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EchoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EchoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EchoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrailStatusRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTrailStatusResponseBody(TeaModel):
    def __init__(
        self,
        is_logging: bool = None,
        latest_delivery_error: str = None,
        latest_delivery_time: str = None,
        param: str = None,
        result: str = None,
        start_logging_time: str = None,
        stop_logging_time: str = None,
    ):
        self.is_logging = is_logging
        self.latest_delivery_error = latest_delivery_error
        self.latest_delivery_time = latest_delivery_time
        self.param = param
        self.result = result
        self.start_logging_time = start_logging_time
        self.stop_logging_time = stop_logging_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_logging is not None:
            result['IsLogging'] = self.is_logging
        if self.latest_delivery_error is not None:
            result['LatestDeliveryError'] = self.latest_delivery_error
        if self.latest_delivery_time is not None:
            result['LatestDeliveryTime'] = self.latest_delivery_time
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        if self.start_logging_time is not None:
            result['StartLoggingTime'] = self.start_logging_time
        if self.stop_logging_time is not None:
            result['StopLoggingTime'] = self.stop_logging_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsLogging') is not None:
            self.is_logging = m.get('IsLogging')
        if m.get('LatestDeliveryError') is not None:
            self.latest_delivery_error = m.get('LatestDeliveryError')
        if m.get('LatestDeliveryTime') is not None:
            self.latest_delivery_time = m.get('LatestDeliveryTime')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StartLoggingTime') is not None:
            self.start_logging_time = m.get('StartLoggingTime')
        if m.get('StopLoggingTime') is not None:
            self.stop_logging_time = m.get('StopLoggingTime')
        return self


class GetTrailStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrailStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrailStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HelpRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class HelpResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        param: str = None,
        result: str = None,
    ):
        self.action = action
        self.param = param
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class HelpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HelpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HelpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LookupEventsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event: str = None,
        event_access_key_id: str = None,
        event_name: str = None,
        event_rw: str = None,
        event_type: str = None,
        format: str = None,
        help: str = None,
        max_results: str = None,
        next_token: str = None,
        request: str = None,
        resource_name: str = None,
        resource_type: str = None,
        service_name: str = None,
        start_time: str = None,
        type: str = None,
        user: str = None,
        version: str = None,
    ):
        self.end_time = end_time
        self.event = event
        self.event_access_key_id = event_access_key_id
        self.event_name = event_name
        self.event_rw = event_rw
        self.event_type = event_type
        self.format = format
        self.help = help
        self.max_results = max_results
        self.next_token = next_token
        self.request = request
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.service_name = service_name
        self.start_time = start_time
        self.type = type
        self.user = user
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event is not None:
            result['Event'] = self.event
        if self.event_access_key_id is not None:
            result['EventAccessKeyId'] = self.event_access_key_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_rw is not None:
            result['EventRW'] = self.event_rw
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request is not None:
            result['Request'] = self.request
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.user is not None:
            result['User'] = self.user
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventAccessKeyId') is not None:
            self.event_access_key_id = m.get('EventAccessKeyId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventRW') is not None:
            self.event_rw = m.get('EventRW')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class LookupEventsResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        events: str = None,
        next_token: str = None,
        param: str = None,
        request_id: str = None,
        result: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.events = events
        self.next_token = next_token
        self.param = param
        self.request_id = request_id
        self.result = result
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.events is not None:
            result['Events'] = self.events
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.param is not None:
            result['Param'] = self.param
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class LookupEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LookupEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LookupEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartLoggingRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class StartLoggingResponseBody(TeaModel):
    def __init__(
        self,
        param: str = None,
        result: str = None,
    ):
        self.param = param
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StartLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartLoggingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLoggingRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class StopLoggingResponseBody(TeaModel):
    def __init__(
        self,
        param: str = None,
        result: str = None,
    ):
        self.param = param
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class StopLoggingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopLoggingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopLoggingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTrailRequest(TeaModel):
    def __init__(
        self,
        format: str = None,
        help: str = None,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        role_name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.format = format
        self.help = help
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_key_prefix = oss_key_prefix
        self.role_name = role_name
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format is not None:
            result['Format'] = self.format
        if self.help is not None:
            result['Help'] = self.help
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Help') is not None:
            self.help = m.get('Help')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateTrailResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss_bucket_name: str = None,
        oss_key_prefix: str = None,
        param: str = None,
        result: str = None,
        role_name: str = None,
    ):
        self.name = name
        self.oss_bucket_name = oss_bucket_name
        self.oss_key_prefix = oss_key_prefix
        self.param = param
        self.result = result
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_key_prefix is not None:
            result['OssKeyPrefix'] = self.oss_key_prefix
        if self.param is not None:
            result['Param'] = self.param
        if self.result is not None:
            result['Result'] = self.result
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssKeyPrefix') is not None:
            self.oss_key_prefix = m.get('OssKeyPrefix')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class UpdateTrailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTrailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTrailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


