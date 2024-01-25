# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AbolishApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class AbolishApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbolishApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbolishApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AbolishApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbolishApiForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class AbolishApiForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbolishApiForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbolishApiForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AbolishApiForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBlackListRequest(TeaModel):
    def __init__(
        self,
        black_content: str = None,
        black_type: str = None,
        description: str = None,
    ):
        self.black_content = black_content
        self.black_type = black_type
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_content is not None:
            result['BlackContent'] = self.black_content
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class AddBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddBlackListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTrafficSpecialControlRequest(TeaModel):
    def __init__(
        self,
        special_key: str = None,
        special_type: str = None,
        traffic_control_id: str = None,
        traffic_value: int = None,
    ):
        self.special_key = special_key
        self.special_type = special_type
        self.traffic_control_id = traffic_control_id
        self.traffic_value = traffic_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        return self


class AddTrafficSpecialControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddTrafficSpecialControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddTrafficSpecialControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccountForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
    ):
        self.ali_uid = ali_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        return self


class CheckAccountForInnerResponseBody(TeaModel):
    def __init__(
        self,
        check_result: bool = None,
        request_id: str = None,
    ):
        self.check_result = check_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckAccountForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAccountForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckAccountForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAoneAppAuditRequest(TeaModel):
    def __init__(
        self,
        aone_app_name: str = None,
    ):
        self.aone_app_name = aone_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aone_app_name is not None:
            result['AoneAppName'] = self.aone_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AoneAppName') is not None:
            self.aone_app_name = m.get('AoneAppName')
        return self


class CheckAoneAppAuditResponseBody(TeaModel):
    def __init__(
        self,
        check_result: bool = None,
        request_id: str = None,
    ):
        self.check_result = check_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckAoneAppAuditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAoneAppAuditResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckAoneAppAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyConsumerOpenForInnerRequest(TeaModel):
    def __init__(
        self,
        copy_list: str = None,
    ):
        self.copy_list = copy_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy_list is not None:
            result['CopyList'] = self.copy_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyList') is not None:
            self.copy_list = m.get('CopyList')
        return self


class CopyConsumerOpenForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyConsumerOpenForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyConsumerOpenForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CopyConsumerOpenForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        auth_type: str = None,
        body_format: str = None,
        constant_parameters: str = None,
        description: str = None,
        group_id: str = None,
        http_method: str = None,
        http_protocol: str = None,
        path: str = None,
        path_parameters: str = None,
        post_body_description: str = None,
        post_body_type: str = None,
        request_body: str = None,
        request_headers: str = None,
        request_queries: str = None,
        result_sample: str = None,
        result_type: str = None,
        service_address: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        system_parameters: str = None,
        visibility: str = None,
    ):
        self.api_name = api_name
        self.auth_type = auth_type
        self.body_format = body_format
        self.constant_parameters = constant_parameters
        self.description = description
        self.group_id = group_id
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_queries = request_queries
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_address = service_address
        self.service_protocol = service_protocol
        self.service_timeout = service_timeout
        self.system_parameters = system_parameters
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.request_body is not None:
            result['RequestBody'] = self.request_body
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('ConstantParameters') is not None:
            self.constant_parameters = m.get('ConstantParameters')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            self.path_parameters = m.get('PathParameters')
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RequestBody') is not None:
            self.request_body = m.get('RequestBody')
        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')
        if m.get('RequestQueries') is not None:
            self.request_queries = m.get('RequestQueries')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('SystemParameters') is not None:
            self.system_parameters = m.get('SystemParameters')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateApiResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        request_id: str = None,
    ):
        self.api_id = api_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_name: str = None,
        auth_type: str = None,
        description: str = None,
        group_id: str = None,
        request_config: str = None,
        request_paramters: str = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        visibility: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_name = api_name
        self.auth_type = auth_type
        self.description = description
        self.group_id = group_id
        self.request_config = request_config
        self.request_paramters = request_paramters
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config
        if self.request_paramters is not None:
            result['RequestParamters'] = self.request_paramters
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestConfig') is not None:
            self.request_config = m.get('RequestConfig')
        if m.get('RequestParamters') is not None:
            self.request_paramters = m.get('RequestParamters')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class CreateApiForInnerResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        request_id: str = None,
    ):
        self.api_id = api_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApiForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateApiForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_name: str = None,
        security_token: str = None,
    ):
        self.description = description
        self.group_name = group_name
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class CreateApiGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiGroupForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        group_name: str = None,
        source: str = None,
    ):
        self.ali_uid = ali_uid
        self.description = description
        self.group_name = group_name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateApiGroupForInnerResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class CreateApiGroupForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiGroupForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateApiGroupForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
    ):
        self.app_name = app_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppForBackendRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_name: str = None,
        description: str = None,
        source: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_name = app_name
        self.description = description
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateAppForBackendResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppForBackendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppForBackendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateAppForBackendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_code: str = None,
        app_key: str = None,
        app_name: str = None,
        app_secret: str = None,
        description: str = None,
        extend: str = None,
        source: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_code = app_code
        self.app_key = app_key
        self.app_name = app_name
        self.app_secret = app_secret
        self.description = description
        self.extend = extend
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreateAppForInnerResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateAppForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        account_quantity: int = None,
        alarm_quota: int = None,
        ali_uid: int = None,
        app_id: int = None,
        billing_type: str = None,
        cloud_market_instance_id: str = None,
        expired_on: str = None,
        instance_attributes: str = None,
        sku_id: str = None,
        token: str = None,
    ):
        self.account_quantity = account_quantity
        self.alarm_quota = alarm_quota
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.billing_type = billing_type
        self.cloud_market_instance_id = cloud_market_instance_id
        self.expired_on = expired_on
        self.instance_attributes = instance_attributes
        self.sku_id = sku_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_quantity is not None:
            result['AccountQuantity'] = self.account_quantity
        if self.alarm_quota is not None:
            result['AlarmQuota'] = self.alarm_quota
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cloud_market_instance_id is not None:
            result['CloudMarketInstanceId'] = self.cloud_market_instance_id
        if self.expired_on is not None:
            result['ExpiredOn'] = self.expired_on
        if self.instance_attributes is not None:
            result['InstanceAttributes'] = self.instance_attributes
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('AlarmQuota') is not None:
            self.alarm_quota = m.get('AlarmQuota')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CloudMarketInstanceId') is not None:
            self.cloud_market_instance_id = m.get('CloudMarketInstanceId')
        if m.get('ExpiredOn') is not None:
            self.expired_on = m.get('ExpiredOn')
        if m.get('InstanceAttributes') is not None:
            self.instance_attributes = m.get('InstanceAttributes')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRaceWorkForInnerRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        group_id: str = None,
        keywords: str = None,
        logo_url: str = None,
        short_description: str = None,
        work_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.group_id = group_id
        self.keywords = keywords
        self.logo_url = logo_url
        self.short_description = short_description
        self.work_name = work_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class CreateRaceWorkForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRaceWorkForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRaceWorkForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateRaceWorkForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretKeyRequest(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
        secret_key_name: str = None,
        secret_value: str = None,
    ):
        self.secret_key = secret_key
        self.secret_key_name = secret_key_name
        self.secret_value = secret_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.secret_value is not None:
            result['SecretValue'] = self.secret_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretValue') is not None:
            self.secret_value = m.get('SecretValue')
        return self


class CreateSecretKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_key_id: str = None,
        secret_key_name: str = None,
    ):
        self.request_id = request_id
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        return self


class CreateSecretKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecretKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrafficControlRequest(TeaModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        description: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        self.api_default = api_default
        self.app_default = app_default
        self.description = description
        self.traffic_control_name = traffic_control_name
        self.traffic_control_unit = traffic_control_unit
        self.user_default = user_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default
        if self.app_default is not None:
            result['AppDefault'] = self.app_default
        if self.description is not None:
            result['Description'] = self.description
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit
        if self.user_default is not None:
            result['UserDefault'] = self.user_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')
        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')
        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')
        return self


class CreateTrafficControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_id: str = None,
    ):
        self.request_id = request_id
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class CreateTrafficControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserWhiteListRequest(TeaModel):
    def __init__(
        self,
        aone_id: str = None,
        description: str = None,
        entity_id: str = None,
        limit_count: int = None,
        type: str = None,
        uid: int = None,
        value: str = None,
    ):
        self.aone_id = aone_id
        self.description = description
        self.entity_id = entity_id
        self.limit_count = limit_count
        self.type = type
        self.uid = uid
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aone_id is not None:
            result['AoneId'] = self.aone_id
        if self.description is not None:
            result['Description'] = self.description
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AoneId') is not None:
            self.aone_id = m.get('AoneId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('LimitCount') is not None:
            self.limit_count = m.get('LimitCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateUserWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateUserWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAllTrafficSpecialControlRequest(TeaModel):
    def __init__(
        self,
        traffic_control_id: str = None,
    ):
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DeleteAllTrafficSpecialControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAllTrafficSpecialControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAllTrafficSpecialControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteAllTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        group_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteApiForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApiForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApiForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteApiForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApiGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: int = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteAppForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.certificate_id = certificate_id
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DeleteDomainCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDomainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretKeyRequest(TeaModel):
    def __init__(
        self,
        secret_key_id: str = None,
    ):
        self.secret_key_id = secret_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        return self


class DeleteSecretKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecretKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecretKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficControlRequest(TeaModel):
    def __init__(
        self,
        traffic_control_id: str = None,
    ):
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DeleteTrafficControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrafficControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficSpecialControlRequest(TeaModel):
    def __init__(
        self,
        special_key: str = None,
        special_type: str = None,
        traffic_control_id: str = None,
    ):
        self.special_key = special_key
        self.special_type = special_type
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DeleteTrafficSpecialControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTrafficSpecialControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTrafficSpecialControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserWhiteListByTypeRequest(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        type: str = None,
        uid: int = None,
    ):
        self.entity_id = entity_id
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DeleteUserWhiteListByTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserWhiteListByTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserWhiteListByTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteUserWhiteListByTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.description = description
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DeployApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeployApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApiForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.description = description
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DeployApiForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployApiForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployApiForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeployApiForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeApiResponseBodyConstantParametersConstantParameter(TeaModel):
    def __init__(
        self,
        constant_value: str = None,
        description: str = None,
        location: str = None,
        service_parameter_name: str = None,
    ):
        self.constant_value = constant_value
        self.description = description
        self.location = location
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constant_value is not None:
            result['ConstantValue'] = self.constant_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstantValue') is not None:
            self.constant_value = m.get('ConstantValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyConstantParameters(TeaModel):
    def __init__(
        self,
        constant_parameter: List[DescribeApiResponseBodyConstantParametersConstantParameter] = None,
    ):
        self.constant_parameter = constant_parameter

    def validate(self):
        if self.constant_parameter:
            for k in self.constant_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k in self.constant_parameter:
                result['ConstantParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k in m.get('ConstantParameter'):
                temp_model = DescribeApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter(TeaModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        self.demo_value = demo_value
        self.description = description
        self.location = location
        self.parameter_name = parameter_name
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyCustomSystemParameters(TeaModel):
    def __init__(
        self,
        custom_system_parameter: List[DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter] = None,
    ):
        self.custom_system_parameter = custom_system_parameter

    def validate(self):
        if self.custom_system_parameter:
            for k in self.custom_system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomSystemParameter'] = []
        if self.custom_system_parameter is not None:
            for k in self.custom_system_parameter:
                result['CustomSystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_system_parameter = []
        if m.get('CustomSystemParameter') is not None:
            for k in m.get('CustomSystemParameter'):
                temp_model = DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyDeployedInfosDeployedInfo(TeaModel):
    def __init__(
        self,
        deployed_status: str = None,
        effective_version: str = None,
        stage_name: str = None,
    ):
        self.deployed_status = deployed_status
        self.effective_version = effective_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status
        if self.effective_version is not None:
            result['EffectiveVersion'] = self.effective_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')
        if m.get('EffectiveVersion') is not None:
            self.effective_version = m.get('EffectiveVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiResponseBodyDeployedInfos(TeaModel):
    def __init__(
        self,
        deployed_info: List[DescribeApiResponseBodyDeployedInfosDeployedInfo] = None,
    ):
        self.deployed_info = deployed_info

    def validate(self):
        if self.deployed_info:
            for k in self.deployed_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeployedInfo'] = []
        if self.deployed_info is not None:
            for k in self.deployed_info:
                result['DeployedInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_info = []
        if m.get('DeployedInfo') is not None:
            for k in m.get('DeployedInfo'):
                temp_model = DescribeApiResponseBodyDeployedInfosDeployedInfo()
                self.deployed_info.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
        model: str = None,
    ):
        self.code = code
        self.description = description
        self.message = message
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class DescribeApiResponseBodyErrorCodeSamples(TeaModel):
    def __init__(
        self,
        error_code_sample: List[DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample] = None,
    ):
        self.error_code_sample = error_code_sample

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyOpenIdConnectConfig(TeaModel):
    def __init__(
        self,
        id_token_param_name: str = None,
        open_id_api_type: str = None,
        public_key: str = None,
        public_key_id: str = None,
    ):
        self.id_token_param_name = id_token_param_name
        self.open_id_api_type = open_id_api_type
        self.public_key = public_key
        self.public_key_id = public_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id_token_param_name is not None:
            result['IdTokenParamName'] = self.id_token_param_name
        if self.open_id_api_type is not None:
            result['OpenIdApiType'] = self.open_id_api_type
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdTokenParamName') is not None:
            self.id_token_param_name = m.get('IdTokenParamName')
        if m.get('OpenIdApiType') is not None:
            self.open_id_api_type = m.get('OpenIdApiType')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        return self


class DescribeApiResponseBodyParametersMapObjectServiceParameterMap(TeaModel):
    def __init__(
        self,
        request_parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        self.request_parameter_name = request_parameter_name
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_parameter_name is not None:
            result['RequestParameterName'] = self.request_parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestParameterName') is not None:
            self.request_parameter_name = m.get('RequestParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyParametersMapObject(TeaModel):
    def __init__(
        self,
        service_parameter_map: List[DescribeApiResponseBodyParametersMapObjectServiceParameterMap] = None,
    ):
        self.service_parameter_map = service_parameter_map

    def validate(self):
        if self.service_parameter_map:
            for k in self.service_parameter_map:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParameterMap'] = []
        if self.service_parameter_map is not None:
            for k in self.service_parameter_map:
                result['ServiceParameterMap'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_parameter_map = []
        if m.get('ServiceParameterMap') is not None:
            for k in m.get('ServiceParameterMap'):
                temp_model = DescribeApiResponseBodyParametersMapObjectServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyRequestConfig(TeaModel):
    def __init__(
        self,
        body_format: str = None,
        post_body_description: str = None,
        request_http_method: str = None,
        request_path: str = None,
        request_protocol: str = None,
    ):
        self.body_format = body_format
        self.post_body_description = post_body_description
        self.request_http_method = request_http_method
        self.request_path = request_path
        self.request_protocol = request_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.request_http_method is not None:
            result['RequestHttpMethod'] = self.request_http_method
        if self.request_path is not None:
            result['RequestPath'] = self.request_path
        if self.request_protocol is not None:
            result['RequestProtocol'] = self.request_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('RequestHttpMethod') is not None:
            self.request_http_method = m.get('RequestHttpMethod')
        if m.get('RequestPath') is not None:
            self.request_path = m.get('RequestPath')
        if m.get('RequestProtocol') is not None:
            self.request_protocol = m.get('RequestProtocol')
        return self


class DescribeApiResponseBodyRequestParametersObjectRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        location: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.location = location
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.location is not None:
            result['Location'] = self.location
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiResponseBodyRequestParametersObject(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeApiResponseBodyRequestParametersObjectRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiResponseBodyRequestParametersObjectRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyServiceConfigFunctionComputeConfig(TeaModel):
    def __init__(
        self,
        fc_region_id: str = None,
        function_name: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.fc_region_id = fc_region_id
        self.function_name = function_name
        self.role_arn = role_arn
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeApiResponseBodyServiceConfigVpcConfig(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
    ):
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.port = port
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeApiResponseBodyServiceConfig(TeaModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        function_compute_config: DescribeApiResponseBodyServiceConfigFunctionComputeConfig = None,
        mock: str = None,
        mock_result: str = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: str = None,
        service_vpc_enable: str = None,
        vpc_config: DescribeApiResponseBodyServiceConfigVpcConfig = None,
    ):
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.function_compute_config = function_compute_config
        self.mock = mock
        self.mock_result = mock_result
        self.service_address = service_address
        self.service_http_method = service_http_method
        self.service_path = service_path
        self.service_protocol = service_protocol
        self.service_timeout = service_timeout
        self.service_vpc_enable = service_vpc_enable
        self.vpc_config = vpc_config

    def validate(self):
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory
        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_http_method is not None:
            result['ServiceHttpMethod'] = self.service_http_method
        if self.service_path is not None:
            result['ServicePath'] = self.service_path
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.vpc_config is not None:
            result['VpcConfig'] = self.vpc_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceHttpMethod') is not None:
            self.service_http_method = m.get('ServiceHttpMethod')
        if m.get('ServicePath') is not None:
            self.service_path = m.get('ServicePath')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('VpcConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m['VpcConfig'])
        return self


class DescribeApiResponseBodyServiceParametersObjectServiceParam(TeaModel):
    def __init__(
        self,
        location: str = None,
        service_parameter_name: str = None,
        type: str = None,
    ):
        self.location = location
        self.service_parameter_name = service_parameter_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApiResponseBodyServiceParametersObject(TeaModel):
    def __init__(
        self,
        service_param: List[DescribeApiResponseBodyServiceParametersObjectServiceParam] = None,
    ):
        self.service_param = service_param

    def validate(self):
        if self.service_param:
            for k in self.service_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParam'] = []
        if self.service_param is not None:
            for k in self.service_param:
                result['ServiceParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_param = []
        if m.get('ServiceParam') is not None:
            for k in m.get('ServiceParam'):
                temp_model = DescribeApiResponseBodyServiceParametersObjectServiceParam()
                self.service_param.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        self.demo_value = demo_value
        self.description = description
        self.location = location
        self.parameter_name = parameter_name
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodySystemParameters(TeaModel):
    def __init__(
        self,
        system_parameter: List[DescribeApiResponseBodySystemParametersSystemParameter] = None,
    ):
        self.system_parameter = system_parameter

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        constant_parameters: DescribeApiResponseBodyConstantParameters = None,
        created_time: str = None,
        custom_system_parameters: DescribeApiResponseBodyCustomSystemParameters = None,
        deployed_infos: DescribeApiResponseBodyDeployedInfos = None,
        description: str = None,
        error_code_samples: DescribeApiResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        group_id: str = None,
        group_name: str = None,
        mock: str = None,
        mock_result: str = None,
        modified_time: str = None,
        open_id_connect_config: DescribeApiResponseBodyOpenIdConnectConfig = None,
        origin_result_description: str = None,
        parameters_map_object: DescribeApiResponseBodyParametersMapObject = None,
        region_id: str = None,
        request_config: DescribeApiResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters_object: DescribeApiResponseBodyRequestParametersObject = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: DescribeApiResponseBodyServiceConfig = None,
        service_parameters_object: DescribeApiResponseBodyServiceParametersObject = None,
        system_parameters: DescribeApiResponseBodySystemParameters = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.constant_parameters = constant_parameters
        self.created_time = created_time
        self.custom_system_parameters = custom_system_parameters
        self.deployed_infos = deployed_infos
        self.description = description
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.group_id = group_id
        self.group_name = group_name
        self.mock = mock
        self.mock_result = mock_result
        self.modified_time = modified_time
        self.open_id_connect_config = open_id_connect_config
        self.origin_result_description = origin_result_description
        self.parameters_map_object = parameters_map_object
        self.region_id = region_id
        self.request_config = request_config
        self.request_id = request_id
        self.request_parameters_object = request_parameters_object
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters_object = service_parameters_object
        self.system_parameters = system_parameters
        self.visibility = visibility

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.custom_system_parameters:
            self.custom_system_parameters.validate()
        if self.deployed_infos:
            self.deployed_infos.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.open_id_connect_config:
            self.open_id_connect_config.validate()
        if self.parameters_map_object:
            self.parameters_map_object.validate()
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters_object:
            self.request_parameters_object.validate()
        if self.service_config:
            self.service_config.validate()
        if self.service_parameters_object:
            self.service_parameters_object.validate()
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.custom_system_parameters is not None:
            result['CustomSystemParameters'] = self.custom_system_parameters.to_map()
        if self.deployed_infos is not None:
            result['DeployedInfos'] = self.deployed_infos.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config.to_map()
        if self.origin_result_description is not None:
            result['OriginResultDescription'] = self.origin_result_description
        if self.parameters_map_object is not None:
            result['ParametersMapObject'] = self.parameters_map_object.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_parameters_object is not None:
            result['RequestParametersObject'] = self.request_parameters_object.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()
        if self.service_parameters_object is not None:
            result['ServiceParametersObject'] = self.service_parameters_object.to_map()
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CustomSystemParameters') is not None:
            temp_model = DescribeApiResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m['CustomSystemParameters'])
        if m.get('DeployedInfos') is not None:
            temp_model = DescribeApiResponseBodyDeployedInfos()
            self.deployed_infos = temp_model.from_map(m['DeployedInfos'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('OpenIdConnectConfig') is not None:
            temp_model = DescribeApiResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m['OpenIdConnectConfig'])
        if m.get('OriginResultDescription') is not None:
            self.origin_result_description = m.get('OriginResultDescription')
        if m.get('ParametersMapObject') is not None:
            temp_model = DescribeApiResponseBodyParametersMapObject()
            self.parameters_map_object = temp_model.from_map(m['ParametersMapObject'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestConfig') is not None:
            temp_model = DescribeApiResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m['RequestConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestParametersObject') is not None:
            temp_model = DescribeApiResponseBodyRequestParametersObject()
            self.request_parameters_object = temp_model.from_map(m['RequestParametersObject'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m['ServiceConfig'])
        if m.get('ServiceParametersObject') is not None:
            temp_model = DescribeApiResponseBodyServiceParametersObject()
            self.service_parameters_object = temp_model.from_map(m['ServiceParametersObject'])
        if m.get('SystemParameters') is not None:
            temp_model = DescribeApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiDocRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
    ):
        self.code = code
        self.description = description
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeApiDocResponseBodyErrorCodeSamples(TeaModel):
    def __init__(
        self,
        error_code_sample: List[DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample] = None,
    ):
        self.error_code_sample = error_code_sample

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        demo_value: str = None,
        description: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.demo_value = demo_value
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribeApiDocResponseBodyPathParameters(TeaModel):
    def __init__(
        self,
        path_parameter: List[DescribeApiDocResponseBodyPathParametersPathParameter] = None,
    ):
        self.path_parameter = path_parameter

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribeApiDocResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiDocResponseBodyRequestBody(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeApiDocResponseBodyRequestBodyRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiDocResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiDocResponseBodyRequestHeaders(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeApiDocResponseBodyRequestHeadersRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiDocResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeApiDocResponseBodyRequestQueries(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeApiDocResponseBodyRequestQueriesRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeApiDocResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodyResultDescriptionsResultDescription(TeaModel):
    def __init__(
        self,
        description: str = None,
        has_child: bool = None,
        id: str = None,
        key: str = None,
        mandatory: bool = None,
        name: str = None,
        pid: str = None,
        type: str = None,
    ):
        self.description = description
        self.has_child = has_child
        self.id = id
        self.key = key
        self.mandatory = mandatory
        self.name = name
        self.pid = pid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.has_child is not None:
            result['HasChild'] = self.has_child
        if self.id is not None:
            result['Id'] = self.id
        if self.key is not None:
            result['Key'] = self.key
        if self.mandatory is not None:
            result['Mandatory'] = self.mandatory
        if self.name is not None:
            result['Name'] = self.name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasChild') is not None:
            self.has_child = m.get('HasChild')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Mandatory') is not None:
            self.mandatory = m.get('Mandatory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApiDocResponseBodyResultDescriptions(TeaModel):
    def __init__(
        self,
        result_description: List[DescribeApiDocResponseBodyResultDescriptionsResultDescription] = None,
    ):
        self.result_description = result_description

    def validate(self):
        if self.result_description:
            for k in self.result_description:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultDescription'] = []
        if self.result_description is not None:
            for k in self.result_description:
                result['ResultDescription'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_description = []
        if m.get('ResultDescription') is not None:
            for k in m.get('ResultDescription'):
                temp_model = DescribeApiDocResponseBodyResultDescriptionsResultDescription()
                self.result_description.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBodySdkDemosSdkDemo(TeaModel):
    def __init__(
        self,
        call_demo: str = None,
        ide_key: str = None,
    ):
        self.call_demo = call_demo
        self.ide_key = ide_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_demo is not None:
            result['CallDemo'] = self.call_demo
        if self.ide_key is not None:
            result['IdeKey'] = self.ide_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallDemo') is not None:
            self.call_demo = m.get('CallDemo')
        if m.get('IdeKey') is not None:
            self.ide_key = m.get('IdeKey')
        return self


class DescribeApiDocResponseBodySdkDemos(TeaModel):
    def __init__(
        self,
        sdk_demo: List[DescribeApiDocResponseBodySdkDemosSdkDemo] = None,
    ):
        self.sdk_demo = sdk_demo

    def validate(self):
        if self.sdk_demo:
            for k in self.sdk_demo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SdkDemo'] = []
        if self.sdk_demo is not None:
            for k in self.sdk_demo:
                result['SdkDemo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sdk_demo = []
        if m.get('SdkDemo') is not None:
            for k in m.get('SdkDemo'):
                temp_model = DescribeApiDocResponseBodySdkDemosSdkDemo()
                self.sdk_demo.append(temp_model.from_map(k))
        return self


class DescribeApiDocResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        body_format: str = None,
        deployed_time: str = None,
        description: str = None,
        error_code_samples: DescribeApiDocResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        group_id: str = None,
        group_name: str = None,
        http_method: str = None,
        http_protocol: str = None,
        path: str = None,
        path_parameters: DescribeApiDocResponseBodyPathParameters = None,
        post_body_description: str = None,
        post_body_type: str = None,
        region_id: str = None,
        request_body: DescribeApiDocResponseBodyRequestBody = None,
        request_headers: DescribeApiDocResponseBodyRequestHeaders = None,
        request_id: str = None,
        request_queries: DescribeApiDocResponseBodyRequestQueries = None,
        result_descriptions: DescribeApiDocResponseBodyResultDescriptions = None,
        result_sample: str = None,
        result_type: str = None,
        sdk_demos: DescribeApiDocResponseBodySdkDemos = None,
        service_timeout: int = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.body_format = body_format
        self.deployed_time = deployed_time
        self.description = description
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.group_id = group_id
        self.group_name = group_name
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.region_id = region_id
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_id = request_id
        self.request_queries = request_queries
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.sdk_demos = sdk_demos
        self.service_timeout = service_timeout
        self.stage_name = stage_name

    def validate(self):
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()
        if self.result_descriptions:
            self.result_descriptions.validate()
        if self.sdk_demos:
            self.sdk_demos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.sdk_demos is not None:
            result['SdkDemos'] = self.sdk_demos.to_map()
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiDocResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribeApiDocResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribeApiDocResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribeApiDocResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeApiDocResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultDescriptions') is not None:
            temp_model = DescribeApiDocResponseBodyResultDescriptions()
            self.result_descriptions = temp_model.from_map(m['ResultDescriptions'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SdkDemos') is not None:
            temp_model = DescribeApiDocResponseBodySdkDemos()
            self.sdk_demos = temp_model.from_map(m['SdkDemos'])
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiDocResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiDocsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocsResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
        description: str = None,
        group_description: str = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.deployed_time = deployed_time
        self.description = description
        self.group_description = group_description
        self.group_id = group_id
        self.group_name = group_name
        self.region_id = region_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_description is not None:
            result['GroupDescription'] = self.group_description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupDescription') is not None:
            self.group_description = m.get('GroupDescription')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocsResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApiDocsResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApiDocsResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApiDocsResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApiDocsResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApiDocsResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiDocsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiDocsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiDocsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiDocsForBackendRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocsForBackendResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
        description: str = None,
        group_description: str = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.deployed_time = deployed_time
        self.description = description
        self.group_description = group_description
        self.group_id = group_id
        self.group_name = group_name
        self.region_id = region_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_description is not None:
            result['GroupDescription'] = self.group_description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupDescription') is not None:
            self.group_description = m.get('GroupDescription')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiDocsForBackendResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApiDocsForBackendResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApiDocsForBackendResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApiDocsForBackendResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApiDocsForBackendResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApiDocsForBackendResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiDocsForBackendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiDocsForBackendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiDocsForBackendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiErrorRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiErrorResponseBodyClientErrorsClientError(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiErrorResponseBodyClientErrors(TeaModel):
    def __init__(
        self,
        client_error: List[DescribeApiErrorResponseBodyClientErrorsClientError] = None,
    ):
        self.client_error = client_error

    def validate(self):
        if self.client_error:
            for k in self.client_error:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClientError'] = []
        if self.client_error is not None:
            for k in self.client_error:
                result['ClientError'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_error = []
        if m.get('ClientError') is not None:
            for k in m.get('ClientError'):
                temp_model = DescribeApiErrorResponseBodyClientErrorsClientError()
                self.client_error.append(temp_model.from_map(k))
        return self


class DescribeApiErrorResponseBodyServerErrorsServerError(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiErrorResponseBodyServerErrors(TeaModel):
    def __init__(
        self,
        server_error: List[DescribeApiErrorResponseBodyServerErrorsServerError] = None,
    ):
        self.server_error = server_error

    def validate(self):
        if self.server_error:
            for k in self.server_error:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerError'] = []
        if self.server_error is not None:
            for k in self.server_error:
                result['ServerError'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_error = []
        if m.get('ServerError') is not None:
            for k in m.get('ServerError'):
                temp_model = DescribeApiErrorResponseBodyServerErrorsServerError()
                self.server_error.append(temp_model.from_map(k))
        return self


class DescribeApiErrorResponseBody(TeaModel):
    def __init__(
        self,
        client_errors: DescribeApiErrorResponseBodyClientErrors = None,
        request_id: str = None,
        server_errors: DescribeApiErrorResponseBodyServerErrors = None,
    ):
        self.client_errors = client_errors
        self.request_id = request_id
        self.server_errors = server_errors

    def validate(self):
        if self.client_errors:
            self.client_errors.validate()
        if self.server_errors:
            self.server_errors.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_errors is not None:
            result['ClientErrors'] = self.client_errors.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_errors is not None:
            result['ServerErrors'] = self.server_errors.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientErrors') is not None:
            temp_model = DescribeApiErrorResponseBodyClientErrors()
            self.client_errors = temp_model.from_map(m['ClientErrors'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerErrors') is not None:
            temp_model = DescribeApiErrorResponseBodyServerErrors()
            self.server_errors = temp_model.from_map(m['ServerErrors'])
        return self


class DescribeApiErrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiErrorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeApiGroupDetailResponseBodyDomainItemsDomainItem(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        domain_name_resolution: str = None,
        domain_status: str = None,
    ):
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.domain_name_resolution = domain_name_resolution
        self.domain_status = domain_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        return self


class DescribeApiGroupDetailResponseBodyDomainItems(TeaModel):
    def __init__(
        self,
        domain_item: List[DescribeApiGroupDetailResponseBodyDomainItemsDomainItem] = None,
    ):
        self.domain_item = domain_item

    def validate(self):
        if self.domain_item:
            for k in self.domain_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainItem'] = []
        if self.domain_item is not None:
            for k in self.domain_item:
                result['DomainItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k in m.get('DomainItem'):
                temp_model = DescribeApiGroupDetailResponseBodyDomainItemsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribeApiGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        billing_status: str = None,
        created_time: str = None,
        description: str = None,
        domain_items: DescribeApiGroupDetailResponseBodyDomainItems = None,
        group_id: str = None,
        group_name: str = None,
        illegal_status: str = None,
        modified_time: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        sub_domain: str = None,
        traffic_limit: int = None,
    ):
        self.billing_status = billing_status
        self.created_time = created_time
        self.description = description
        self.domain_items = domain_items
        self.group_id = group_id
        self.group_name = group_name
        self.illegal_status = illegal_status
        self.modified_time = modified_time
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.sub_domain = sub_domain
        self.traffic_limit = traffic_limit

    def validate(self):
        if self.domain_items:
            self.domain_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainItems') is not None:
            temp_model = DescribeApiGroupDetailResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('TrafficLimit') is not None:
            self.traffic_limit = m.get('TrafficLimit')
        return self


class DescribeApiGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiGroupDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute(TeaModel):
    def __init__(
        self,
        billing_status: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        illegal_status: str = None,
        modified_time: str = None,
        region_id: str = None,
        sub_domain: str = None,
        traffic_limit: int = None,
    ):
        self.billing_status = billing_status
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.illegal_status = illegal_status
        self.modified_time = modified_time
        self.region_id = region_id
        self.sub_domain = sub_domain
        self.traffic_limit = traffic_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('TrafficLimit') is not None:
            self.traffic_limit = m.get('TrafficLimit')
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributes(TeaModel):
    def __init__(
        self,
        api_group_attribute: List[DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute] = None,
    ):
        self.api_group_attribute = api_group_attribute

    def validate(self):
        if self.api_group_attribute:
            for k in self.api_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiGroupAttribute'] = []
        if self.api_group_attribute is not None:
            for k in self.api_group_attribute:
                result['ApiGroupAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_group_attribute = []
        if m.get('ApiGroupAttribute') is not None:
            for k in m.get('ApiGroupAttribute'):
                temp_model = DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute()
                self.api_group_attribute.append(temp_model.from_map(k))
        return self


class DescribeApiGroupsResponseBody(TeaModel):
    def __init__(
        self,
        api_group_attributes: DescribeApiGroupsResponseBodyApiGroupAttributes = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_group_attributes = api_group_attributes
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_group_attributes:
            self.api_group_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group_attributes is not None:
            result['ApiGroupAttributes'] = self.api_group_attributes.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiGroupAttributes') is not None:
            temp_model = DescribeApiGroupsResponseBodyApiGroupAttributes()
            self.api_group_attributes = temp_model.from_map(m['ApiGroupAttributes'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiLatencyRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiLatencyResponseBodyLatencysLatency(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiLatencyResponseBodyLatencys(TeaModel):
    def __init__(
        self,
        latency: List[DescribeApiLatencyResponseBodyLatencysLatency] = None,
    ):
        self.latency = latency

    def validate(self):
        if self.latency:
            for k in self.latency:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Latency'] = []
        if self.latency is not None:
            for k in self.latency:
                result['Latency'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.latency = []
        if m.get('Latency') is not None:
            for k in m.get('Latency'):
                temp_model = DescribeApiLatencyResponseBodyLatencysLatency()
                self.latency.append(temp_model.from_map(k))
        return self


class DescribeApiLatencyResponseBody(TeaModel):
    def __init__(
        self,
        latencys: DescribeApiLatencyResponseBodyLatencys = None,
        request_id: str = None,
    ):
        self.latencys = latencys
        self.request_id = request_id

    def validate(self):
        if self.latencys:
            self.latencys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.latencys is not None:
            result['Latencys'] = self.latencys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Latencys') is not None:
            temp_model = DescribeApiLatencyResponseBodyLatencys()
            self.latencys = temp_model.from_map(m['Latencys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiLatencyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiLatencyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiLatencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiMarketInstanceRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        group_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeApiMarketInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_attributes: str = None,
        request_id: str = None,
    ):
        self.instance_attributes = instance_attributes
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_attributes is not None:
            result['InstanceAttributes'] = self.instance_attributes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceAttributes') is not None:
            self.instance_attributes = m.get('InstanceAttributes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiMarketInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiMarketInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiMarketInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiQpsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiQpsResponseBodyFailsFail(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiQpsResponseBodyFails(TeaModel):
    def __init__(
        self,
        fail: List[DescribeApiQpsResponseBodyFailsFail] = None,
    ):
        self.fail = fail

    def validate(self):
        if self.fail:
            for k in self.fail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fail'] = []
        if self.fail is not None:
            for k in self.fail:
                result['Fail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail = []
        if m.get('Fail') is not None:
            for k in m.get('Fail'):
                temp_model = DescribeApiQpsResponseBodyFailsFail()
                self.fail.append(temp_model.from_map(k))
        return self


class DescribeApiQpsResponseBodySuccessesSuccess(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiQpsResponseBodySuccesses(TeaModel):
    def __init__(
        self,
        success: List[DescribeApiQpsResponseBodySuccessesSuccess] = None,
    ):
        self.success = success

    def validate(self):
        if self.success:
            for k in self.success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Success'] = []
        if self.success is not None:
            for k in self.success:
                result['Success'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.success = []
        if m.get('Success') is not None:
            for k in m.get('Success'):
                temp_model = DescribeApiQpsResponseBodySuccessesSuccess()
                self.success.append(temp_model.from_map(k))
        return self


class DescribeApiQpsResponseBody(TeaModel):
    def __init__(
        self,
        fails: DescribeApiQpsResponseBodyFails = None,
        request_id: str = None,
        successes: DescribeApiQpsResponseBodySuccesses = None,
    ):
        self.fails = fails
        self.request_id = request_id
        self.successes = successes

    def validate(self):
        if self.fails:
            self.fails.validate()
        if self.successes:
            self.successes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fails is not None:
            result['Fails'] = self.fails.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.successes is not None:
            result['Successes'] = self.successes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fails') is not None:
            temp_model = DescribeApiQpsResponseBodyFails()
            self.fails = temp_model.from_map(m['Fails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Successes') is not None:
            temp_model = DescribeApiQpsResponseBodySuccesses()
            self.successes = temp_model.from_map(m['Successes'])
        return self


class DescribeApiQpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiQpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiRulesRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_type: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.rule_type = rule_type
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiRulesResponseBodyApiRulesApiRule(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        created_time: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.created_time = created_time
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeApiRulesResponseBodyApiRules(TeaModel):
    def __init__(
        self,
        api_rule: List[DescribeApiRulesResponseBodyApiRulesApiRule] = None,
    ):
        self.api_rule = api_rule

    def validate(self):
        if self.api_rule:
            for k in self.api_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiRule'] = []
        if self.api_rule is not None:
            for k in self.api_rule:
                result['ApiRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_rule = []
        if m.get('ApiRule') is not None:
            for k in m.get('ApiRule'):
                temp_model = DescribeApiRulesResponseBodyApiRulesApiRule()
                self.api_rule.append(temp_model.from_map(k))
        return self


class DescribeApiRulesResponseBody(TeaModel):
    def __init__(
        self,
        api_rules: DescribeApiRulesResponseBodyApiRules = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_rules = api_rules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_rules:
            self.api_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_rules is not None:
            result['ApiRules'] = self.api_rules.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiRules') is not None:
            temp_model = DescribeApiRulesResponseBodyApiRules()
            self.api_rules = temp_model.from_map(m['ApiRules'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiTrafficRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiTrafficResponseBodyDownloadsDownload(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiTrafficResponseBodyDownloads(TeaModel):
    def __init__(
        self,
        download: List[DescribeApiTrafficResponseBodyDownloadsDownload] = None,
    ):
        self.download = download

    def validate(self):
        if self.download:
            for k in self.download:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Download'] = []
        if self.download is not None:
            for k in self.download:
                result['Download'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.download = []
        if m.get('Download') is not None:
            for k in m.get('Download'):
                temp_model = DescribeApiTrafficResponseBodyDownloadsDownload()
                self.download.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficResponseBodyUploadsUpload(TeaModel):
    def __init__(
        self,
        time: str = None,
        value: str = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApiTrafficResponseBodyUploads(TeaModel):
    def __init__(
        self,
        upload: List[DescribeApiTrafficResponseBodyUploadsUpload] = None,
    ):
        self.upload = upload

    def validate(self):
        if self.upload:
            for k in self.upload:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Upload'] = []
        if self.upload is not None:
            for k in self.upload:
                result['Upload'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.upload = []
        if m.get('Upload') is not None:
            for k in m.get('Upload'):
                temp_model = DescribeApiTrafficResponseBodyUploadsUpload()
                self.upload.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficResponseBody(TeaModel):
    def __init__(
        self,
        downloads: DescribeApiTrafficResponseBodyDownloads = None,
        request_id: str = None,
        uploads: DescribeApiTrafficResponseBodyUploads = None,
    ):
        self.downloads = downloads
        self.request_id = request_id
        self.uploads = uploads

    def validate(self):
        if self.downloads:
            self.downloads.validate()
        if self.uploads:
            self.uploads.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.downloads is not None:
            result['Downloads'] = self.downloads.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uploads is not None:
            result['Uploads'] = self.uploads.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Downloads') is not None:
            temp_model = DescribeApiTrafficResponseBodyDownloads()
            self.downloads = temp_model.from_map(m['Downloads'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uploads') is not None:
            temp_model = DescribeApiTrafficResponseBodyUploads()
            self.uploads = temp_model.from_map(m['Uploads'])
        return self


class DescribeApiTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiTrafficResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApiTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        region_id: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.modified_time = modified_time
        self.region_id = region_id
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApisResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApisResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        authorization_source: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        operator: str = None,
        region_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.authorization_source = authorization_source
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.operator = operator
        self.region_id = region_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.authorization_source is not None:
            result['AuthorizationSource'] = self.authorization_source
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthorizationSource') is not None:
            self.authorization_source = m.get('AuthorizationSource')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApisByAppResponseBodyAppApiRelationInfos(TeaModel):
    def __init__(
        self,
        app_api_relation_info: List[DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo] = None,
    ):
        self.app_api_relation_info = app_api_relation_info

    def validate(self):
        if self.app_api_relation_info:
            for k in self.app_api_relation_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppApiRelationInfo'] = []
        if self.app_api_relation_info is not None:
            for k in self.app_api_relation_info:
                result['AppApiRelationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_api_relation_info = []
        if m.get('AppApiRelationInfo') is not None:
            for k in m.get('AppApiRelationInfo'):
                temp_model = DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo()
                self.app_api_relation_info.append(temp_model.from_map(k))
        return self


class DescribeApisByAppResponseBody(TeaModel):
    def __init__(
        self,
        app_api_relation_infos: DescribeApisByAppResponseBodyAppApiRelationInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_api_relation_infos = app_api_relation_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_api_relation_infos:
            self.app_api_relation_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_api_relation_infos is not None:
            result['AppApiRelationInfos'] = self.app_api_relation_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppApiRelationInfos') is not None:
            temp_model = DescribeApisByAppResponseBodyAppApiRelationInfos()
            self.app_api_relation_infos = temp_model.from_map(m['AppApiRelationInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisByAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApisByAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApisByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByRuleRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rule_id: str = None,
        rule_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.rule_id = rule_id
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeApisByRuleResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        region_id: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.modified_time = modified_time
        self.region_id = region_id
        self.stage_name = stage_name
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisByRuleResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApisByRuleResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisByRuleResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisByRuleResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApisByRuleResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisByRuleResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisByRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApisByRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApisByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisForConsoleRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo(TeaModel):
    def __init__(
        self,
        deployed_status: str = None,
        effective_version: str = None,
        stage_name: str = None,
    ):
        self.deployed_status = deployed_status
        self.effective_version = effective_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status
        if self.effective_version is not None:
            result['EffectiveVersion'] = self.effective_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')
        if m.get('EffectiveVersion') is not None:
            self.effective_version = m.get('EffectiveVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos(TeaModel):
    def __init__(
        self,
        deployed_info: List[DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo] = None,
    ):
        self.deployed_info = deployed_info

    def validate(self):
        if self.deployed_info:
            for k in self.deployed_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeployedInfo'] = []
        if self.deployed_info is not None:
            for k in self.deployed_info:
                result['DeployedInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_info = []
        if m.get('DeployedInfo') is not None:
            for k in m.get('DeployedInfo'):
                temp_model = DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfosDeployedInfo()
                self.deployed_info.append(temp_model.from_map(k))
        return self


class DescribeApisForConsoleResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        created_time: str = None,
        deployed_infos: DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        region_id: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.created_time = created_time
        self.deployed_infos = deployed_infos
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.modified_time = modified_time
        self.region_id = region_id
        self.visibility = visibility

    def validate(self):
        if self.deployed_infos:
            self.deployed_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.deployed_infos is not None:
            result['DeployedInfos'] = self.deployed_infos.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DeployedInfos') is not None:
            temp_model = DescribeApisForConsoleResponseBodyApiInfosApiInfoDeployedInfos()
            self.deployed_infos = temp_model.from_map(m['DeployedInfos'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisForConsoleResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApisForConsoleResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeApisForConsoleResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisForConsoleResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApisForConsoleResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeApisForConsoleResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApisForConsoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApisForConsoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApisForConsoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecuritiesRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_key: str = None,
        app_secret: str = None,
        created_time: str = None,
        modified_time: str = None,
    ):
        self.app_code = app_code
        self.app_key = app_key
        self.app_secret = app_secret
        self.created_time = created_time
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeAppSecuritiesResponseBodyAppSecuritys(TeaModel):
    def __init__(
        self,
        app_security: List[DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity] = None,
    ):
        self.app_security = app_security

    def validate(self):
        if self.app_security:
            for k in self.app_security:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSecurity'] = []
        if self.app_security is not None:
            for k in self.app_security:
                result['AppSecurity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_security = []
        if m.get('AppSecurity') is not None:
            for k in m.get('AppSecurity'):
                temp_model = DescribeAppSecuritiesResponseBodyAppSecuritysAppSecurity()
                self.app_security.append(temp_model.from_map(k))
        return self


class DescribeAppSecuritiesResponseBody(TeaModel):
    def __init__(
        self,
        app_securitys: DescribeAppSecuritiesResponseBodyAppSecuritys = None,
        request_id: str = None,
    ):
        self.app_securitys = app_securitys
        self.request_id = request_id

    def validate(self):
        if self.app_securitys:
            self.app_securitys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_securitys is not None:
            result['AppSecuritys'] = self.app_securitys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppSecuritys') is not None:
            temp_model = DescribeAppSecuritiesResponseBodyAppSecuritys()
            self.app_securitys = temp_model.from_map(m['AppSecuritys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppSecuritiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppSecuritiesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppSecuritiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecurityRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
    ):
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class DescribeAppSecurityResponseBody(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
        created_time: str = None,
        modified_time: str = None,
        request_id: str = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret
        self.created_time = created_time
        self.modified_time = modified_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppSecurityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppSecurityResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppSecurityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecurityForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: int = None,
        security_token: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppSecurityForInnerResponseBody(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_key: str = None,
        app_secret: str = None,
        created_time: str = None,
        modified_time: str = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_key = app_key
        self.app_secret = app_secret
        self.created_time = created_time
        self.modified_time = modified_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAppSecurityForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppSecurityForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppSecurityForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAppsResponseBodyAppsApp(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeAppsResponseBodyApps(TeaModel):
    def __init__(
        self,
        app: List[DescribeAppsResponseBodyAppsApp] = None,
    ):
        self.app = app

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = DescribeAppsResponseBodyAppsApp()
                self.app.append(temp_model.from_map(k))
        return self


class DescribeAppsResponseBody(TeaModel):
    def __init__(
        self,
        apps: DescribeAppsResponseBodyApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.apps = apps
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.apps:
            self.apps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['Apps'] = self.apps.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apps') is not None:
            temp_model = DescribeAppsResponseBodyApps()
            self.apps = temp_model.from_map(m['Apps'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsByApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        authorization_source: str = None,
        created_time: str = None,
        description: str = None,
        operator: str = None,
        stage_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.authorization_source = authorization_source
        self.created_time = created_time
        self.description = description
        self.operator = operator
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.authorization_source is not None:
            result['AuthorizationSource'] = self.authorization_source
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthorizationSource') is not None:
            self.authorization_source = m.get('AuthorizationSource')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeAppsByApiResponseBodyAppApiRelationInfos(TeaModel):
    def __init__(
        self,
        app_api_relation_info: List[DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo] = None,
    ):
        self.app_api_relation_info = app_api_relation_info

    def validate(self):
        if self.app_api_relation_info:
            for k in self.app_api_relation_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppApiRelationInfo'] = []
        if self.app_api_relation_info is not None:
            for k in self.app_api_relation_info:
                result['AppApiRelationInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_api_relation_info = []
        if m.get('AppApiRelationInfo') is not None:
            for k in m.get('AppApiRelationInfo'):
                temp_model = DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo()
                self.app_api_relation_info.append(temp_model.from_map(k))
        return self


class DescribeAppsByApiResponseBody(TeaModel):
    def __init__(
        self,
        app_api_relation_infos: DescribeAppsByApiResponseBodyAppApiRelationInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_api_relation_infos = app_api_relation_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_api_relation_infos:
            self.app_api_relation_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_api_relation_infos is not None:
            result['AppApiRelationInfos'] = self.app_api_relation_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppApiRelationInfos') is not None:
            temp_model = DescribeAppsByApiResponseBodyAppApiRelationInfos()
            self.app_api_relation_infos = temp_model.from_map(m['AppApiRelationInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsByApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppsByApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppsByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsForProviderRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_owner: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_id = app_id
        self.app_owner = app_owner
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_owner is not None:
            result['AppOwner'] = self.app_owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppOwner') is not None:
            self.app_owner = m.get('AppOwner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAppsForProviderResponseBodyAppsApp(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeAppsForProviderResponseBodyApps(TeaModel):
    def __init__(
        self,
        app: List[DescribeAppsForProviderResponseBodyAppsApp] = None,
    ):
        self.app = app

    def validate(self):
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app = []
        if m.get('App') is not None:
            for k in m.get('App'):
                temp_model = DescribeAppsForProviderResponseBodyAppsApp()
                self.app.append(temp_model.from_map(k))
        return self


class DescribeAppsForProviderResponseBody(TeaModel):
    def __init__(
        self,
        apps: DescribeAppsForProviderResponseBodyApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.apps = apps
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.apps:
            self.apps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apps is not None:
            result['Apps'] = self.apps.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apps') is not None:
            temp_model = DescribeAppsForProviderResponseBodyApps()
            self.apps = temp_model.from_map(m['Apps'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppsForProviderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppsForProviderResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAppsForProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableVipsRequest(TeaModel):
    def __init__(
        self,
        vip: str = None,
    ):
        self.vip = vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vip is not None:
            result['Vip'] = self.vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vip') is not None:
            self.vip = m.get('Vip')
        return self


class DescribeAvailableVipsResponseBodyAvailableVips(TeaModel):
    def __init__(
        self,
        available_vip: List[str] = None,
    ):
        self.available_vip = available_vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_vip is not None:
            result['AvailableVip'] = self.available_vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableVip') is not None:
            self.available_vip = m.get('AvailableVip')
        return self


class DescribeAvailableVipsResponseBody(TeaModel):
    def __init__(
        self,
        available_vips: DescribeAvailableVipsResponseBodyAvailableVips = None,
    ):
        self.available_vips = available_vips

    def validate(self):
        if self.available_vips:
            self.available_vips.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_vips is not None:
            result['AvailableVips'] = self.available_vips.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableVips') is not None:
            temp_model = DescribeAvailableVipsResponseBodyAvailableVips()
            self.available_vips = temp_model.from_map(m['AvailableVips'])
        return self


class DescribeAvailableVipsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableVipsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAvailableVipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBidByUserIdForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        security_token: str = None,
    ):
        self.ali_uid = ali_uid
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeBidByUserIdForInnerResponseBody(TeaModel):
    def __init__(
        self,
        bid: str = None,
        request_id: str = None,
    ):
        self.bid = bid
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBidByUserIdForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBidByUserIdForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeBidByUserIdForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackListsRequest(TeaModel):
    def __init__(
        self,
        black_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.black_type = black_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBlackListsResponseBodyBlackListsBlackList(TeaModel):
    def __init__(
        self,
        black_content: str = None,
        black_type: str = None,
        create_time: str = None,
        description: str = None,
        modified_time: str = None,
    ):
        self.black_content = black_content
        self.black_type = black_type
        self.create_time = create_time
        self.description = description
        self.modified_time = modified_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_content is not None:
            result['BlackContent'] = self.black_content
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class DescribeBlackListsResponseBodyBlackLists(TeaModel):
    def __init__(
        self,
        black_list: List[DescribeBlackListsResponseBodyBlackListsBlackList] = None,
    ):
        self.black_list = black_list

    def validate(self):
        if self.black_list:
            for k in self.black_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlackList'] = []
        if self.black_list is not None:
            for k in self.black_list:
                result['BlackList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.black_list = []
        if m.get('BlackList') is not None:
            for k in m.get('BlackList'):
                temp_model = DescribeBlackListsResponseBodyBlackListsBlackList()
                self.black_list.append(temp_model.from_map(k))
        return self


class DescribeBlackListsResponseBody(TeaModel):
    def __init__(
        self,
        black_lists: DescribeBlackListsResponseBodyBlackLists = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.black_lists = black_lists
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.black_lists:
            self.black_lists.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_lists is not None:
            result['BlackLists'] = self.black_lists.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackLists') is not None:
            temp_model = DescribeBlackListsResponseBodyBlackLists()
            self.black_lists = temp_model.from_map(m['BlackLists'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBlackListsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBlackListsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeBlackListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployedApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeDeployedApiResponseBodyConstantParametersConstantParameter(TeaModel):
    def __init__(
        self,
        constant_value: str = None,
        description: str = None,
        location: str = None,
        service_parameter_name: str = None,
    ):
        self.constant_value = constant_value
        self.description = description
        self.location = location
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constant_value is not None:
            result['ConstantValue'] = self.constant_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstantValue') is not None:
            self.constant_value = m.get('ConstantValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyConstantParameters(TeaModel):
    def __init__(
        self,
        constant_parameter: List[DescribeDeployedApiResponseBodyConstantParametersConstantParameter] = None,
    ):
        self.constant_parameter = constant_parameter

    def validate(self):
        if self.constant_parameter:
            for k in self.constant_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k in self.constant_parameter:
                result['ConstantParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k in m.get('ConstantParameter'):
                temp_model = DescribeDeployedApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
    ):
        self.code = code
        self.description = description
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeDeployedApiResponseBodyErrorCodeSamples(TeaModel):
    def __init__(
        self,
        error_code_sample: List[DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample] = None,
    ):
        self.error_code_sample = error_code_sample

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeDeployedApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyFunctionComputeConfig(TeaModel):
    def __init__(
        self,
        fc_region_id: str = None,
        function_name: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.fc_region_id = fc_region_id
        self.function_name = function_name
        self.role_arn = role_arn
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeDeployedApiResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        demo_value: str = None,
        description: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.demo_value = demo_value
        self.description = description
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyPathParameters(TeaModel):
    def __init__(
        self,
        path_parameter: List[DescribeDeployedApiResponseBodyPathParametersPathParameter] = None,
    ):
        self.path_parameter = path_parameter

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribeDeployedApiResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyRequestBody(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeDeployedApiResponseBodyRequestBodyRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeDeployedApiResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyRequestHeaders(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeDeployedApiResponseBodyRequestHeadersRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeDeployedApiResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyRequestQueries(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeDeployedApiResponseBodyRequestQueriesRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeDeployedApiResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        self.demo_value = demo_value
        self.description = description
        self.location = location
        self.parameter_name = parameter_name
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodySystemParameters(TeaModel):
    def __init__(
        self,
        system_parameter: List[DescribeDeployedApiResponseBodySystemParametersSystemParameter] = None,
    ):
        self.system_parameter = system_parameter

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeDeployedApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        body_format: str = None,
        constant_parameters: DescribeDeployedApiResponseBodyConstantParameters = None,
        deployed_time: str = None,
        error_code_samples: DescribeDeployedApiResponseBodyErrorCodeSamples = None,
        function_compute_config: DescribeDeployedApiResponseBodyFunctionComputeConfig = None,
        group_id: str = None,
        group_name: str = None,
        http_method: str = None,
        http_protocol: str = None,
        path: str = None,
        path_parameters: DescribeDeployedApiResponseBodyPathParameters = None,
        post_body_description: str = None,
        post_body_type: str = None,
        region_id: str = None,
        request_body: DescribeDeployedApiResponseBodyRequestBody = None,
        request_headers: DescribeDeployedApiResponseBodyRequestHeaders = None,
        request_id: str = None,
        request_queries: DescribeDeployedApiResponseBodyRequestQueries = None,
        result_sample: str = None,
        result_type: str = None,
        service_address: str = None,
        service_fcenable: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        stage_name: str = None,
        system_parameters: DescribeDeployedApiResponseBodySystemParameters = None,
        visibility: str = None,
        vpc_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.body_format = body_format
        self.constant_parameters = constant_parameters
        self.deployed_time = deployed_time
        self.error_code_samples = error_code_samples
        self.function_compute_config = function_compute_config
        self.group_id = group_id
        self.group_name = group_name
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.region_id = region_id
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_id = request_id
        self.request_queries = request_queries
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_address = service_address
        self.service_fcenable = service_fcenable
        self.service_protocol = service_protocol
        self.service_timeout = service_timeout
        self.service_vpc_enable = service_vpc_enable
        self.stage_name = stage_name
        self.system_parameters = system_parameters
        self.visibility = visibility
        self.vpc_name = vpc_name

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_fcenable is not None:
            result['ServiceFCEnable'] = self.service_fcenable
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeDeployedApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeDeployedApiResponseBodyFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceFCEnable') is not None:
            self.service_fcenable = m.get('ServiceFCEnable')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeDeployedApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeployedApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDeployedApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployedApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeDeployedApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.deployed_time = deployed_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.region_id = region_id
        self.stage_name = stage_name
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeDeployedApisResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeDeployedApisResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeDeployedApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeDeployedApisResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeDeployedApisResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeDeployedApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDeployedApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDeployedApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDeployedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeDomainResponseBody(TeaModel):
    def __init__(
        self,
        certificate_body: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        domain_name_resolution: str = None,
        domain_status: str = None,
        group_id: str = None,
        private_key: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.certificate_body = certificate_body
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.domain_name_resolution = domain_name_resolution
        self.domain_status = domain_status
        self.group_id = group_id
        self.private_key = private_key
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class DescribeDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResolutionRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        group_id: str = None,
    ):
        self.domain_names = domain_names
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_name_resolution: str = None,
    ):
        self.domain_name = domain_name
        self.domain_name_resolution = domain_name_resolution

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        return self


class DescribeDomainResolutionResponseBodyDomainResolutions(TeaModel):
    def __init__(
        self,
        domain_resolution: List[DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution] = None,
    ):
        self.domain_resolution = domain_resolution

    def validate(self):
        if self.domain_resolution:
            for k in self.domain_resolution:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainResolution'] = []
        if self.domain_resolution is not None:
            for k in self.domain_resolution:
                result['DomainResolution'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_resolution = []
        if m.get('DomainResolution') is not None:
            for k in m.get('DomainResolution'):
                temp_model = DescribeDomainResolutionResponseBodyDomainResolutionsDomainResolution()
                self.domain_resolution.append(temp_model.from_map(k))
        return self


class DescribeDomainResolutionResponseBody(TeaModel):
    def __init__(
        self,
        domain_resolutions: DescribeDomainResolutionResponseBodyDomainResolutions = None,
        group_id: str = None,
        request_id: str = None,
    ):
        self.domain_resolutions = domain_resolutions
        self.group_id = group_id
        self.request_id = request_id

    def validate(self):
        if self.domain_resolutions:
            self.domain_resolutions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_resolutions is not None:
            result['DomainResolutions'] = self.domain_resolutions.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainResolutions') is not None:
            temp_model = DescribeDomainResolutionResponseBodyDomainResolutions()
            self.domain_resolutions = temp_model.from_map(m['DomainResolutions'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainResolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainResolutionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDomainResolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeHistoryApiResponseBodyConstantParametersConstantParameter(TeaModel):
    def __init__(
        self,
        constant_value: str = None,
        description: str = None,
        location: str = None,
        service_parameter_name: str = None,
    ):
        self.constant_value = constant_value
        self.description = description
        self.location = location
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constant_value is not None:
            result['ConstantValue'] = self.constant_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstantValue') is not None:
            self.constant_value = m.get('ConstantValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyConstantParameters(TeaModel):
    def __init__(
        self,
        constant_parameter: List[DescribeHistoryApiResponseBodyConstantParametersConstantParameter] = None,
    ):
        self.constant_parameter = constant_parameter

    def validate(self):
        if self.constant_parameter:
            for k in self.constant_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k in self.constant_parameter:
                result['ConstantParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k in m.get('ConstantParameter'):
                temp_model = DescribeHistoryApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
    ):
        self.code = code
        self.description = description
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeHistoryApiResponseBodyErrorCodeSamples(TeaModel):
    def __init__(
        self,
        error_code_sample: List[DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample] = None,
    ):
        self.error_code_sample = error_code_sample

    def validate(self):
        if self.error_code_sample:
            for k in self.error_code_sample:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k in self.error_code_sample:
                result['ErrorCodeSample'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k in m.get('ErrorCodeSample'):
                temp_model = DescribeHistoryApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyFunctionComputeConfig(TeaModel):
    def __init__(
        self,
        fc_region_id: str = None,
        function_name: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.fc_region_id = fc_region_id
        self.function_name = function_name
        self.role_arn = role_arn
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fc_region_id is not None:
            result['FcRegionId'] = self.fc_region_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FcRegionId') is not None:
            self.fc_region_id = m.get('FcRegionId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeHistoryApiResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        demo_value: str = None,
        description: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.demo_value = demo_value
        self.description = description
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyPathParameters(TeaModel):
    def __init__(
        self,
        path_parameter: List[DescribeHistoryApiResponseBodyPathParametersPathParameter] = None,
    ):
        self.path_parameter = path_parameter

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribeHistoryApiResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyRequestBody(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeHistoryApiResponseBodyRequestBodyRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeHistoryApiResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyRequestHeaders(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeHistoryApiResponseBodyRequestHeadersRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeHistoryApiResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
        service_parameter_name: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodyRequestQueries(TeaModel):
    def __init__(
        self,
        request_param: List[DescribeHistoryApiResponseBodyRequestQueriesRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribeHistoryApiResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        self.demo_value = demo_value
        self.description = description
        self.location = location
        self.parameter_name = parameter_name
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeHistoryApiResponseBodySystemParameters(TeaModel):
    def __init__(
        self,
        system_parameter: List[DescribeHistoryApiResponseBodySystemParametersSystemParameter] = None,
    ):
        self.system_parameter = system_parameter

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeHistoryApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeHistoryApiResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        body_format: str = None,
        constant_parameters: DescribeHistoryApiResponseBodyConstantParameters = None,
        deployed_time: str = None,
        description: str = None,
        error_code_samples: DescribeHistoryApiResponseBodyErrorCodeSamples = None,
        function_compute_config: DescribeHistoryApiResponseBodyFunctionComputeConfig = None,
        group_id: str = None,
        group_name: str = None,
        history_version: str = None,
        http_method: str = None,
        http_protocol: str = None,
        mock: str = None,
        mock_result: str = None,
        origin_result_description: str = None,
        path: str = None,
        path_parameters: DescribeHistoryApiResponseBodyPathParameters = None,
        post_body_description: str = None,
        post_body_type: str = None,
        region_id: str = None,
        request_body: DescribeHistoryApiResponseBodyRequestBody = None,
        request_headers: DescribeHistoryApiResponseBodyRequestHeaders = None,
        request_id: str = None,
        request_queries: DescribeHistoryApiResponseBodyRequestQueries = None,
        result_sample: str = None,
        result_type: str = None,
        service_address: str = None,
        service_fcenable: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        status: str = None,
        system_parameters: DescribeHistoryApiResponseBodySystemParameters = None,
        visibility: str = None,
        vpc_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.body_format = body_format
        self.constant_parameters = constant_parameters
        self.deployed_time = deployed_time
        self.description = description
        self.error_code_samples = error_code_samples
        self.function_compute_config = function_compute_config
        self.group_id = group_id
        self.group_name = group_name
        self.history_version = history_version
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.mock = mock
        self.mock_result = mock_result
        self.origin_result_description = origin_result_description
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.region_id = region_id
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_id = request_id
        self.request_queries = request_queries
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_address = service_address
        self.service_fcenable = service_fcenable
        self.service_protocol = service_protocol
        self.service_timeout = service_timeout
        self.service_vpc_enable = service_vpc_enable
        self.status = status
        self.system_parameters = system_parameters
        self.visibility = visibility
        self.vpc_name = vpc_name

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.origin_result_description is not None:
            result['OriginResultDescription'] = self.origin_result_description
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_fcenable is not None:
            result['ServiceFCEnable'] = self.service_fcenable
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.status is not None:
            result['Status'] = self.status
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeHistoryApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeHistoryApiResponseBodyFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('OriginResultDescription') is not None:
            self.origin_result_description = m.get('OriginResultDescription')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribeHistoryApiResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribeHistoryApiResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeHistoryApiResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceFCEnable') is not None:
            self.service_fcenable = m.get('ServiceFCEnable')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeHistoryApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHistoryApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeHistoryApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeHistoryApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        history_version: str = None,
        region_id: str = None,
        stage_name: str = None,
        status: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.deployed_time = deployed_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.history_version = history_version
        self.region_id = region_id
        self.stage_name = stage_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHistoryApisResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeHistoryApisResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribeHistoryApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeHistoryApisResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeHistoryApisResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribeHistoryApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeHistoryApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHistoryApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeHistoryApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModelsForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.ali_uid = ali_uid
        self.group_id = group_id
        self.model_id = model_id
        self.model_name = model_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeModelsForInnerResponseBodyModelDetailsModelDetail(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        model_name: str = None,
        model_ref: str = None,
        modified_time: str = None,
        schema: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.model_name = model_name
        self.model_ref = model_ref
        self.modified_time = modified_time
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_ref is not None:
            result['ModelRef'] = self.model_ref
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelRef') is not None:
            self.model_ref = m.get('ModelRef')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class DescribeModelsForInnerResponseBodyModelDetails(TeaModel):
    def __init__(
        self,
        model_detail: List[DescribeModelsForInnerResponseBodyModelDetailsModelDetail] = None,
    ):
        self.model_detail = model_detail

    def validate(self):
        if self.model_detail:
            for k in self.model_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModelDetail'] = []
        if self.model_detail is not None:
            for k in self.model_detail:
                result['ModelDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_detail = []
        if m.get('ModelDetail') is not None:
            for k in m.get('ModelDetail'):
                temp_model = DescribeModelsForInnerResponseBodyModelDetailsModelDetail()
                self.model_detail.append(temp_model.from_map(k))
        return self


class DescribeModelsForInnerResponseBody(TeaModel):
    def __init__(
        self,
        model_details: DescribeModelsForInnerResponseBodyModelDetails = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.model_details = model_details
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.model_details:
            self.model_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_details is not None:
            result['ModelDetails'] = self.model_details.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelDetails') is not None:
            temp_model = DescribeModelsForInnerResponseBodyModelDetails()
            self.model_details = temp_model.from_map(m['ModelDetails'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeModelsForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeModelsForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeModelsForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribePurchasedApiResponseBodyPathParametersPathParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        demo_value: str = None,
        description: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.demo_value = demo_value
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribePurchasedApiResponseBodyPathParameters(TeaModel):
    def __init__(
        self,
        path_parameter: List[DescribePurchasedApiResponseBodyPathParametersPathParameter] = None,
    ):
        self.path_parameter = path_parameter

    def validate(self):
        if self.path_parameter:
            for k in self.path_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PathParameter'] = []
        if self.path_parameter is not None:
            for k in self.path_parameter:
                result['PathParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.path_parameter = []
        if m.get('PathParameter') is not None:
            for k in m.get('PathParameter'):
                temp_model = DescribePurchasedApiResponseBodyPathParametersPathParameter()
                self.path_parameter.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBodyRequestBodyRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: str = None,
        min_length: int = None,
        min_value: str = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribePurchasedApiResponseBodyRequestBody(TeaModel):
    def __init__(
        self,
        request_param: List[DescribePurchasedApiResponseBodyRequestBodyRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribePurchasedApiResponseBodyRequestBodyRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBodyRequestHeadersRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribePurchasedApiResponseBodyRequestHeaders(TeaModel):
    def __init__(
        self,
        request_param: List[DescribePurchasedApiResponseBodyRequestHeadersRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribePurchasedApiResponseBodyRequestHeadersRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBodyRequestQueriesRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: str = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        max_length: int = None,
        max_value: str = None,
        min_length: int = None,
        min_value: str = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        self.api_parameter_name = api_parameter_name
        self.default_value = default_value
        self.demo_value = demo_value
        self.description = description
        self.doc_order = doc_order
        self.doc_show = doc_show
        self.enum_value = enum_value
        self.json_scheme = json_scheme
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.parameter_type = parameter_type
        self.regular_expression = regular_expression
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order
        if self.doc_show is not None:
            result['DocShow'] = self.doc_show
        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value
        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_length is not None:
            result['MinLength'] = self.min_length
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')
        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')
        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')
        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribePurchasedApiResponseBodyRequestQueries(TeaModel):
    def __init__(
        self,
        request_param: List[DescribePurchasedApiResponseBodyRequestQueriesRequestParam] = None,
    ):
        self.request_param = request_param

    def validate(self):
        if self.request_param:
            for k in self.request_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParam'] = []
        if self.request_param is not None:
            for k in self.request_param:
                result['RequestParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_param = []
        if m.get('RequestParam') is not None:
            for k in m.get('RequestParam'):
                temp_model = DescribePurchasedApiResponseBodyRequestQueriesRequestParam()
                self.request_param.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        body_format: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        http_method: str = None,
        http_protocol: str = None,
        mock: str = None,
        mock_result: str = None,
        modified_time: str = None,
        path: str = None,
        path_parameters: DescribePurchasedApiResponseBodyPathParameters = None,
        post_body_description: str = None,
        post_body_type: str = None,
        region_id: str = None,
        request_body: DescribePurchasedApiResponseBodyRequestBody = None,
        request_headers: DescribePurchasedApiResponseBodyRequestHeaders = None,
        request_id: str = None,
        request_queries: DescribePurchasedApiResponseBodyRequestQueries = None,
        result_sample: str = None,
        result_type: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.body_format = body_format
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.mock = mock
        self.mock_result = mock_result
        self.modified_time = modified_time
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.region_id = region_id
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_id = request_id
        self.request_queries = request_queries
        self.result_sample = result_sample
        self.result_type = result_type
        self.visibility = visibility

    def validate(self):
        if self.path_parameters:
            self.path_parameters.validate()
        if self.request_body:
            self.request_body.validate()
        if self.request_headers:
            self.request_headers.validate()
        if self.request_queries:
            self.request_queries.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters.to_map()
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            temp_model = DescribePurchasedApiResponseBodyPathParameters()
            self.path_parameters = temp_model.from_map(m['PathParameters'])
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestBody') is not None:
            temp_model = DescribePurchasedApiResponseBodyRequestBody()
            self.request_body = temp_model.from_map(m['RequestBody'])
        if m.get('RequestHeaders') is not None:
            temp_model = DescribePurchasedApiResponseBodyRequestHeaders()
            self.request_headers = temp_model.from_map(m['RequestHeaders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestQueries') is not None:
            temp_model = DescribePurchasedApiResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribePurchasedApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePurchasedApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePurchasedApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
    ):
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DescribePurchasedApiGroupDetailResponseBodyDomainItems(TeaModel):
    def __init__(
        self,
        domain_item: List[DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem] = None,
    ):
        self.domain_item = domain_item

    def validate(self):
        if self.domain_item:
            for k in self.domain_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainItem'] = []
        if self.domain_item is not None:
            for k in self.domain_item:
                result['DomainItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_item = []
        if m.get('DomainItem') is not None:
            for k in m.get('DomainItem'):
                temp_model = DescribePurchasedApiGroupDetailResponseBodyDomainItemsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        domain_items: DescribePurchasedApiGroupDetailResponseBodyDomainItems = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.domain_items = domain_items
        self.group_id = group_id
        self.group_name = group_name
        self.modified_time = modified_time
        self.region_id = region_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.domain_items:
            self.domain_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainItems') is not None:
            temp_model = DescribePurchasedApiGroupDetailResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePurchasedApiGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePurchasedApiGroupDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePurchasedApiGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupsRequest(TeaModel):
    def __init__(
        self,
        group_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.group_ids = group_ids
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute(TeaModel):
    def __init__(
        self,
        billing_type: str = None,
        created_time: str = None,
        expire_time: str = None,
        group_description: str = None,
        group_id: str = None,
        group_name: str = None,
        invoke_times_max: int = None,
        invoke_times_now: int = None,
        modified_time: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.billing_type = billing_type
        self.created_time = created_time
        self.expire_time = expire_time
        self.group_description = group_description
        self.group_id = group_id
        self.group_name = group_name
        self.invoke_times_max = invoke_times_max
        self.invoke_times_now = invoke_times_now
        self.modified_time = modified_time
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.group_description is not None:
            result['GroupDescription'] = self.group_description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.invoke_times_max is not None:
            result['InvokeTimesMax'] = self.invoke_times_max
        if self.invoke_times_now is not None:
            result['InvokeTimesNow'] = self.invoke_times_now
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GroupDescription') is not None:
            self.group_description = m.get('GroupDescription')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InvokeTimesMax') is not None:
            self.invoke_times_max = m.get('InvokeTimesMax')
        if m.get('InvokeTimesNow') is not None:
            self.invoke_times_now = m.get('InvokeTimesNow')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes(TeaModel):
    def __init__(
        self,
        purchased_api_group_attribute: List[DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute] = None,
    ):
        self.purchased_api_group_attribute = purchased_api_group_attribute

    def validate(self):
        if self.purchased_api_group_attribute:
            for k in self.purchased_api_group_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PurchasedApiGroupAttribute'] = []
        if self.purchased_api_group_attribute is not None:
            for k in self.purchased_api_group_attribute:
                result['PurchasedApiGroupAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.purchased_api_group_attribute = []
        if m.get('PurchasedApiGroupAttribute') is not None:
            for k in m.get('PurchasedApiGroupAttribute'):
                temp_model = DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributesPurchasedApiGroupAttribute()
                self.purchased_api_group_attribute.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiGroupsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        purchased_api_group_attributes: DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.purchased_api_group_attributes = purchased_api_group_attributes
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.purchased_api_group_attributes:
            self.purchased_api_group_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.purchased_api_group_attributes is not None:
            result['PurchasedApiGroupAttributes'] = self.purchased_api_group_attributes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PurchasedApiGroupAttributes') is not None:
            temp_model = DescribePurchasedApiGroupsResponseBodyPurchasedApiGroupAttributes()
            self.purchased_api_group_attributes = temp_model.from_map(m['PurchasedApiGroupAttributes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurchasedApiGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePurchasedApiGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePurchasedApiGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribePurchasedApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        region_id: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.modified_time = modified_time
        self.region_id = region_id
        self.stage_name = stage_name
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribePurchasedApisResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribePurchasedApisResponseBodyApiInfosApiInfo] = None,
    ):
        self.api_info = api_info

    def validate(self):
        if self.api_info:
            for k in self.api_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiInfo'] = []
        if self.api_info is not None:
            for k in self.api_info:
                result['ApiInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_info = []
        if m.get('ApiInfo') is not None:
            for k in m.get('ApiInfo'):
                temp_model = DescribePurchasedApisResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribePurchasedApisResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribePurchasedApisResponseBodyApiInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_infos = api_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_infos:
            self.api_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_infos is not None:
            result['ApiInfos'] = self.api_infos.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiInfos') is not None:
            temp_model = DescribePurchasedApisResponseBodyApiInfos()
            self.api_infos = temp_model.from_map(m['ApiInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurchasedApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePurchasedApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePurchasedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRaceWorkForInnerRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeRaceWorkForInnerResponseBody(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        group_id: str = None,
        keywords: str = None,
        logo_url: str = None,
        modified_time: str = None,
        request_id: str = None,
        short_description: str = None,
        work_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.group_id = group_id
        self.keywords = keywords
        self.logo_url = logo_url
        self.modified_time = modified_time
        self.request_id = request_id
        self.short_description = short_description
        self.work_name = work_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class DescribeRaceWorkForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRaceWorkForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeRaceWorkForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRaceWorksForInnerRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRaceWorksForInnerResponseBodyApiWorksApiWork(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        group_id: str = None,
        keywords: str = None,
        logo_url: str = None,
        modified_time: str = None,
        short_description: str = None,
        work_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.create_time = create_time
        self.group_id = group_id
        self.keywords = keywords
        self.logo_url = logo_url
        self.modified_time = modified_time
        self.short_description = short_description
        self.work_name = work_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logo_url is not None:
            result['LogoUrl'] = self.logo_url
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.work_name is not None:
            result['WorkName'] = self.work_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogoUrl') is not None:
            self.logo_url = m.get('LogoUrl')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('WorkName') is not None:
            self.work_name = m.get('WorkName')
        return self


class DescribeRaceWorksForInnerResponseBodyApiWorks(TeaModel):
    def __init__(
        self,
        api_work: List[DescribeRaceWorksForInnerResponseBodyApiWorksApiWork] = None,
    ):
        self.api_work = api_work

    def validate(self):
        if self.api_work:
            for k in self.api_work:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiWork'] = []
        if self.api_work is not None:
            for k in self.api_work:
                result['ApiWork'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_work = []
        if m.get('ApiWork') is not None:
            for k in m.get('ApiWork'):
                temp_model = DescribeRaceWorksForInnerResponseBodyApiWorksApiWork()
                self.api_work.append(temp_model.from_map(k))
        return self


class DescribeRaceWorksForInnerResponseBody(TeaModel):
    def __init__(
        self,
        api_works: DescribeRaceWorksForInnerResponseBodyApiWorks = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_works = api_works
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_works:
            self.api_works.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_works is not None:
            result['ApiWorks'] = self.api_works.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiWorks') is not None:
            temp_model = DescribeRaceWorksForInnerResponseBodyApiWorks()
            self.api_works = temp_model.from_map(m['ApiWorks'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRaceWorksForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRaceWorksForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeRaceWorksForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        security_token: str = None,
    ):
        self.language = language
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        end_point: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        self.end_point = end_point
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesByApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeRulesByApiResponseBodyRulesRule(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
    ):
        self.created_time = created_time
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DescribeRulesByApiResponseBodyRules(TeaModel):
    def __init__(
        self,
        rule: List[DescribeRulesByApiResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = DescribeRulesByApiResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k))
        return self


class DescribeRulesByApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rules: DescribeRulesByApiResponseBodyRules = None,
    ):
        self.request_id = request_id
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rules') is not None:
            temp_model = DescribeRulesByApiResponseBodyRules()
            self.rules = temp_model.from_map(m['Rules'])
        return self


class DescribeRulesByApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRulesByApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeRulesByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecretKeysRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        secret_key_id: str = None,
        secret_key_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        return self


class DescribeSecretKeysResponseBodySecretKeysSecretKey(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        modified_time: str = None,
        region_id: str = None,
        secret_key: str = None,
        secret_key_id: str = None,
        secret_key_name: str = None,
        secret_key_value: str = None,
    ):
        self.created_time = created_time
        self.modified_time = modified_time
        self.region_id = region_id
        self.secret_key = secret_key
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name
        self.secret_key_value = secret_key_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.secret_key_value is not None:
            result['SecretKeyValue'] = self.secret_key_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretKeyValue') is not None:
            self.secret_key_value = m.get('SecretKeyValue')
        return self


class DescribeSecretKeysResponseBodySecretKeys(TeaModel):
    def __init__(
        self,
        secret_key: List[DescribeSecretKeysResponseBodySecretKeysSecretKey] = None,
    ):
        self.secret_key = secret_key

    def validate(self):
        if self.secret_key:
            for k in self.secret_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecretKey'] = []
        if self.secret_key is not None:
            for k in self.secret_key:
                result['SecretKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secret_key = []
        if m.get('SecretKey') is not None:
            for k in m.get('SecretKey'):
                temp_model = DescribeSecretKeysResponseBodySecretKeysSecretKey()
                self.secret_key.append(temp_model.from_map(k))
        return self


class DescribeSecretKeysResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        secret_keys: DescribeSecretKeysResponseBodySecretKeys = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.secret_keys = secret_keys
        self.total_count = total_count

    def validate(self):
        if self.secret_keys:
            self.secret_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_keys is not None:
            result['SecretKeys'] = self.secret_keys.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKeys') is not None:
            temp_model = DescribeSecretKeysResponseBodySecretKeys()
            self.secret_keys = temp_model.from_map(m['SecretKeys'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSecretKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecretKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeSecretKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSystemParametersRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSystemParametersResponseBodySystemParametersSystemParameter(TeaModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        param_name: str = None,
        param_type: str = None,
    ):
        self.demo_value = demo_value
        self.description = description
        self.param_name = param_name
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class DescribeSystemParametersResponseBodySystemParameters(TeaModel):
    def __init__(
        self,
        system_parameter: List[DescribeSystemParametersResponseBodySystemParametersSystemParameter] = None,
    ):
        self.system_parameter = system_parameter

    def validate(self):
        if self.system_parameter:
            for k in self.system_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k in self.system_parameter:
                result['SystemParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k in m.get('SystemParameter'):
                temp_model = DescribeSystemParametersResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeSystemParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        system_parameters: DescribeSystemParametersResponseBodySystemParameters = None,
    ):
        self.request_id = request_id
        self.system_parameters = system_parameters

    def validate(self):
        if self.system_parameters:
            self.system_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeSystemParametersResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        return self


class DescribeSystemParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSystemParametersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeSystemParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSystemParamsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSystemParamsResponseBodySystemParamsSystemParam(TeaModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        param_name: str = None,
        param_type: str = None,
    ):
        self.demo_value = demo_value
        self.description = description
        self.param_name = param_name
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value
        if self.description is not None:
            result['Description'] = self.description
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_type is not None:
            result['ParamType'] = self.param_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')
        return self


class DescribeSystemParamsResponseBodySystemParams(TeaModel):
    def __init__(
        self,
        system_param: List[DescribeSystemParamsResponseBodySystemParamsSystemParam] = None,
    ):
        self.system_param = system_param

    def validate(self):
        if self.system_param:
            for k in self.system_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParam'] = []
        if self.system_param is not None:
            for k in self.system_param:
                result['SystemParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_param = []
        if m.get('SystemParam') is not None:
            for k in m.get('SystemParam'):
                temp_model = DescribeSystemParamsResponseBodySystemParamsSystemParam()
                self.system_param.append(temp_model.from_map(k))
        return self


class DescribeSystemParamsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        system_params: DescribeSystemParamsResponseBodySystemParams = None,
    ):
        self.request_id = request_id
        self.system_params = system_params

    def validate(self):
        if self.system_params:
            self.system_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.system_params is not None:
            result['SystemParams'] = self.system_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SystemParams') is not None:
            temp_model = DescribeSystemParamsResponseBodySystemParams()
            self.system_params = temp_model.from_map(m['SystemParams'])
        return self


class DescribeSystemParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSystemParamsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeSystemParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficControlsRequest(TeaModel):
    def __init__(
        self,
        api_uid: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        stage_name: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
    ):
        self.api_uid = api_uid
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.stage_name = stage_name
        self.traffic_control_id = traffic_control_id
        self.traffic_control_name = traffic_control_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial(TeaModel):
    def __init__(
        self,
        special_key: str = None,
        traffic_value: int = None,
    ):
        self.special_key = special_key
        self.traffic_value = traffic_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialKey') is not None:
            self.special_key = m.get('SpecialKey')
        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials(TeaModel):
    def __init__(
        self,
        special: List[DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial] = None,
    ):
        self.special = special

    def validate(self):
        if self.special:
            for k in self.special:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Special'] = []
        if self.special is not None:
            for k in self.special:
                result['Special'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.special = []
        if m.get('Special') is not None:
            for k in m.get('Special'):
                temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecialsSpecial()
                self.special.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy(TeaModel):
    def __init__(
        self,
        special_type: str = None,
        specials: DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials = None,
    ):
        self.special_type = special_type
        self.specials = specials

    def validate(self):
        if self.specials:
            self.specials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.specials is not None:
            result['Specials'] = self.specials.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecialType') is not None:
            self.special_type = m.get('SpecialType')
        if m.get('Specials') is not None:
            temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicySpecials()
            self.specials = temp_model.from_map(m['Specials'])
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies(TeaModel):
    def __init__(
        self,
        special_policy: List[DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy] = None,
    ):
        self.special_policy = special_policy

    def validate(self):
        if self.special_policy:
            for k in self.special_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SpecialPolicy'] = []
        if self.special_policy is not None:
            for k in self.special_policy:
                result['SpecialPolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.special_policy = []
        if m.get('SpecialPolicy') is not None:
            for k in m.get('SpecialPolicy'):
                temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPoliciesSpecialPolicy()
                self.special_policy.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl(TeaModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        special_policies: DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        self.api_default = api_default
        self.app_default = app_default
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time
        self.special_policies = special_policies
        self.traffic_control_id = traffic_control_id
        self.traffic_control_name = traffic_control_name
        self.traffic_control_unit = traffic_control_unit
        self.user_default = user_default

    def validate(self):
        if self.special_policies:
            self.special_policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default
        if self.app_default is not None:
            result['AppDefault'] = self.app_default
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.special_policies is not None:
            result['SpecialPolicies'] = self.special_policies.to_map()
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit
        if self.user_default is not None:
            result['UserDefault'] = self.user_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')
        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SpecialPolicies') is not None:
            temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControlSpecialPolicies()
            self.special_policies = temp_model.from_map(m['SpecialPolicies'])
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')
        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')
        return self


class DescribeTrafficControlsResponseBodyTrafficControls(TeaModel):
    def __init__(
        self,
        traffic_control: List[DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl] = None,
    ):
        self.traffic_control = traffic_control

    def validate(self):
        if self.traffic_control:
            for k in self.traffic_control:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficControl'] = []
        if self.traffic_control is not None:
            for k in self.traffic_control:
                result['TrafficControl'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_control = []
        if m.get('TrafficControl') is not None:
            for k in m.get('TrafficControl'):
                temp_model = DescribeTrafficControlsResponseBodyTrafficControlsTrafficControl()
                self.traffic_control.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        traffic_controls: DescribeTrafficControlsResponseBodyTrafficControls = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.traffic_controls = traffic_controls

    def validate(self):
        if self.traffic_controls:
            self.traffic_controls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.traffic_controls is not None:
            result['TrafficControls'] = self.traffic_controls.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TrafficControls') is not None:
            temp_model = DescribeTrafficControlsResponseBodyTrafficControls()
            self.traffic_controls = temp_model.from_map(m['TrafficControls'])
        return self


class DescribeTrafficControlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTrafficControlsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeTrafficControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserWhiteListsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
        uid: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.type = type
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeUserWhiteListsResponseBodyUserWhiteListInfosUserWhiteListInfo(TeaModel):
    def __init__(
        self,
        aone_id: str = None,
        create_time: str = None,
        description: str = None,
        id: int = None,
        modified_time: str = None,
        type: str = None,
        uid: int = None,
        value: str = None,
    ):
        self.aone_id = aone_id
        self.create_time = create_time
        self.description = description
        self.id = id
        self.modified_time = modified_time
        self.type = type
        self.uid = uid
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aone_id is not None:
            result['AoneId'] = self.aone_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AoneId') is not None:
            self.aone_id = m.get('AoneId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeUserWhiteListsResponseBodyUserWhiteListInfos(TeaModel):
    def __init__(
        self,
        user_white_list_info: List[DescribeUserWhiteListsResponseBodyUserWhiteListInfosUserWhiteListInfo] = None,
    ):
        self.user_white_list_info = user_white_list_info

    def validate(self):
        if self.user_white_list_info:
            for k in self.user_white_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserWhiteListInfo'] = []
        if self.user_white_list_info is not None:
            for k in self.user_white_list_info:
                result['UserWhiteListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_white_list_info = []
        if m.get('UserWhiteListInfo') is not None:
            for k in m.get('UserWhiteListInfo'):
                temp_model = DescribeUserWhiteListsResponseBodyUserWhiteListInfosUserWhiteListInfo()
                self.user_white_list_info.append(temp_model.from_map(k))
        return self


class DescribeUserWhiteListsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        user_white_list_infos: DescribeUserWhiteListsResponseBodyUserWhiteListInfos = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.user_white_list_infos = user_white_list_infos

    def validate(self):
        if self.user_white_list_infos:
            self.user_white_list_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_white_list_infos is not None:
            result['UserWhiteListInfos'] = self.user_white_list_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserWhiteListInfos') is not None:
            temp_model = DescribeUserWhiteListsResponseBodyUserWhiteListInfos()
            self.user_white_list_infos = temp_model.from_map(m['UserWhiteListInfos'])
        return self


class DescribeUserWhiteListsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserWhiteListsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeUserWhiteListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsIncludedByUserWhitelistRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class IsIncludedByUserWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        is_included: bool = None,
        request_id: str = None,
    ):
        self.is_included = is_included
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_included is not None:
            result['IsIncluded'] = self.is_included
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsIncluded') is not None:
            self.is_included = m.get('IsIncluded')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IsIncludedByUserWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IsIncludedByUserWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = IsIncludedByUserWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        body_format: str = None,
        constant_parameters: str = None,
        description: str = None,
        group_id: str = None,
        http_method: str = None,
        http_protocol: str = None,
        path: str = None,
        path_parameters: str = None,
        post_body_description: str = None,
        post_body_type: str = None,
        request_body: str = None,
        request_headers: str = None,
        request_queries: str = None,
        result_sample: str = None,
        result_type: str = None,
        service_address: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        system_parameters: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.body_format = body_format
        self.constant_parameters = constant_parameters
        self.description = description
        self.group_id = group_id
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_queries = request_queries
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_address = service_address
        self.service_protocol = service_protocol
        self.service_timeout = service_timeout
        self.system_parameters = system_parameters
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.http_protocol is not None:
            result['HttpProtocol'] = self.http_protocol
        if self.path is not None:
            result['Path'] = self.path
        if self.path_parameters is not None:
            result['PathParameters'] = self.path_parameters
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.post_body_type is not None:
            result['PostBodyType'] = self.post_body_type
        if self.request_body is not None:
            result['RequestBody'] = self.request_body
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_address is not None:
            result['ServiceAddress'] = self.service_address
        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('ConstantParameters') is not None:
            self.constant_parameters = m.get('ConstantParameters')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('HttpProtocol') is not None:
            self.http_protocol = m.get('HttpProtocol')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('PathParameters') is not None:
            self.path_parameters = m.get('PathParameters')
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('PostBodyType') is not None:
            self.post_body_type = m.get('PostBodyType')
        if m.get('RequestBody') is not None:
            self.request_body = m.get('RequestBody')
        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')
        if m.get('RequestQueries') is not None:
            self.request_queries = m.get('RequestQueries')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceAddress') is not None:
            self.service_address = m.get('ServiceAddress')
        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('SystemParameters') is not None:
            self.system_parameters = m.get('SystemParameters')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class ModifyApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        description: str = None,
        group_id: str = None,
        request_config: str = None,
        request_paramters: str = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        visibility: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.description = description
        self.group_id = group_id
        self.request_config = request_config
        self.request_paramters = request_paramters
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config
        if self.request_paramters is not None:
            result['RequestParamters'] = self.request_paramters
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestConfig') is not None:
            self.request_config = m.get('RequestConfig')
        if m.get('RequestParamters') is not None:
            self.request_paramters = m.get('RequestParamters')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class ModifyApiForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyApiForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApiForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyApiForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ModifyApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class ModifyApiGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiMarketInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        group_id: str = None,
        instance_attributes: str = None,
    ):
        self.ali_uid = ali_uid
        self.group_id = group_id
        self.instance_attributes = instance_attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_attributes is not None:
            result['InstanceAttributes'] = self.instance_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceAttributes') is not None:
            self.instance_attributes = m.get('InstanceAttributes')
        return self


class ModifyApiMarketInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyApiMarketInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApiMarketInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyApiMarketInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
        extend: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_id = app_id
        self.app_name = app_name
        self.description = description
        self.extend = extend

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.extend is not None:
            result['Extend'] = self.extend
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        return self


class ModifyAppForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAppForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyAppForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGroupAuthAppCodeForBackendRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        auth_app_code: str = None,
        group_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.auth_app_code = auth_app_code
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.auth_app_code is not None:
            result['AuthAppCode'] = self.auth_app_code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AuthAppCode') is not None:
            self.auth_app_code = m.get('AuthAppCode')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ModifyGroupAuthAppCodeForBackendResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyGroupAuthAppCodeForBackendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGroupAuthAppCodeForBackendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyGroupAuthAppCodeForBackendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecretKeyRequest(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
        secret_key_id: str = None,
        secret_key_name: str = None,
        secret_value: str = None,
    ):
        self.secret_key = secret_key
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name
        self.secret_value = secret_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        if self.secret_value is not None:
            result['SecretValue'] = self.secret_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretValue') is not None:
            self.secret_value = m.get('SecretValue')
        return self


class ModifySecretKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_key_id: str = None,
        secret_key_name: str = None,
    ):
        self.request_id = request_id
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.secret_key_name is not None:
            result['SecretKeyName'] = self.secret_key_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        return self


class ModifySecretKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecretKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifySecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrafficControlRequest(TeaModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        description: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        self.api_default = api_default
        self.app_default = app_default
        self.description = description
        self.traffic_control_id = traffic_control_id
        self.traffic_control_name = traffic_control_name
        self.traffic_control_unit = traffic_control_unit
        self.user_default = user_default

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_default is not None:
            result['ApiDefault'] = self.api_default
        if self.app_default is not None:
            result['AppDefault'] = self.app_default
        if self.description is not None:
            result['Description'] = self.description
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        if self.traffic_control_unit is not None:
            result['TrafficControlUnit'] = self.traffic_control_unit
        if self.user_default is not None:
            result['UserDefault'] = self.user_default
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDefault') is not None:
            self.api_default = m.get('ApiDefault')
        if m.get('AppDefault') is not None:
            self.app_default = m.get('AppDefault')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        if m.get('TrafficControlUnit') is not None:
            self.traffic_control_unit = m.get('TrafficControlUnit')
        if m.get('UserDefault') is not None:
            self.user_default = m.get('UserDefault')
        return self


class ModifyTrafficControlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTrafficControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserWhiteListValueByTypeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        type: str = None,
        uid: int = None,
        value: str = None,
    ):
        self.description = description
        self.type = type
        self.uid = uid
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyUserWhiteListValueByTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserWhiteListValueByTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserWhiteListValueByTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyUserWhiteListValueByTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReactivateDomainForBackendRequest(TeaModel):
    def __init__(
        self,
        aliuid: int = None,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.aliuid = aliuid
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class ReactivateDomainForBackendResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReactivateDomainForBackendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReactivateDomainForBackendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReactivateDomainForBackendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverApiFromHistoricalRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RecoverApiFromHistoricalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecoverApiFromHistoricalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoverApiFromHistoricalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecoverApiFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryApiDefineFromHistoricalRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RecoveryApiDefineFromHistoricalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecoveryApiDefineFromHistoricalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoveryApiDefineFromHistoricalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecoveryApiDefineFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryApiFromHistoricalRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RecoveryApiFromHistoricalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecoveryApiFromHistoricalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoveryApiFromHistoricalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecoveryApiFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class RefreshDomainResponseBody(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        domain_name_resolution: str = None,
        domain_status: str = None,
        group_id: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.domain_name_resolution = domain_name_resolution
        self.domain_status = domain_status
        self.group_id = group_id
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class RefreshDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RefreshDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessPermissionByApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        app_id: int = None,
        description: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.app_id = app_id
        self.description = description
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveAccessPermissionByApisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAccessPermissionByApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAccessPermissionByApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveAccessPermissionByApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessPermissionByAppsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_ids: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_ids = app_ids
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveAccessPermissionByAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAccessPermissionByAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAccessPermissionByAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveAccessPermissionByAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessPermissionByAppsForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        app_ids: str = None,
        group_id: str = None,
        source: str = None,
        stage_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.app_ids = app_ids
        self.group_id = group_id
        self.source = source
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveAccessPermissionByAppsForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAccessPermissionByAppsForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAccessPermissionByAppsForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveAccessPermissionByAppsForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAllBlackListRequest(TeaModel):
    def __init__(
        self,
        black_type: str = None,
    ):
        self.black_type = black_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        return self


class RemoveAllBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAllBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAllBlackListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveAllBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveApiRuleRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        rule_id: str = None,
        rule_type: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveApiRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveApiRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveApiRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveApiRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppsFromApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_ids: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_ids = app_ids
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveAppsFromApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAppsFromApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveAppsFromApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveAppsFromApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBlackListRequest(TeaModel):
    def __init__(
        self,
        black_content: str = None,
        black_type: str = None,
    ):
        self.black_content = black_content
        self.black_type = black_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_content is not None:
            result['BlackContent'] = self.black_content
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        return self


class RemoveBlackListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveBlackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveBlackListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppCodeRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
    ):
        self.app_code = app_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        return self


class ResetAppCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAppCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAppCodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ResetAppCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppCodeForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_code: str = None,
        new_app_code: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_code = app_code
        self.new_app_code = new_app_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.new_app_code is not None:
            result['NewAppCode'] = self.new_app_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('NewAppCode') is not None:
            self.new_app_code = m.get('NewAppCode')
        return self


class ResetAppCodeForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAppCodeForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAppCodeForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ResetAppCodeForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppKeySecretRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
    ):
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ResetAppKeySecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetAppKeySecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAppKeySecretResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ResetAppKeySecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSecretByAppKeyForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_key: str = None,
        new_app_key: str = None,
        new_app_secret: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_key = app_key
        self.new_app_key = new_app_key
        self.new_app_secret = new_app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.new_app_key is not None:
            result['NewAppKey'] = self.new_app_key
        if self.new_app_secret is not None:
            result['NewAppSecret'] = self.new_app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('NewAppKey') is not None:
            self.new_app_key = m.get('NewAppKey')
        if m.get('NewAppSecret') is not None:
            self.new_app_secret = m.get('NewAppSecret')
        return self


class ResetSecretByAppKeyForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetSecretByAppKeyForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetSecretByAppKeyForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ResetSecretByAppKeyForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionByApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        app_id: int = None,
        description: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.app_id = app_id
        self.description = description
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetAccessPermissionByApisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAccessPermissionByApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAccessPermissionByApisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetAccessPermissionByApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionByGroupForBackendRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        group_id: str = None,
    ):
        self.app_id = app_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class SetAccessPermissionByGroupForBackendResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAccessPermissionByGroupForBackendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAccessPermissionByGroupForBackendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetAccessPermissionByGroupForBackendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_ids: str = None,
        description: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_ids = app_ids
        self.description = description
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetAccessPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAccessPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAccessPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetAccessPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionsForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_id: str = None,
        app_ids: str = None,
        description: str = None,
        group_id: str = None,
        source: str = None,
        stage_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_id = api_id
        self.app_ids = app_ids
        self.description = description
        self.group_id = group_id
        self.source = source
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetAccessPermissionsForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetAccessPermissionsForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAccessPermissionsForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetAccessPermissionsForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApiRuleRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        rule_id: str = None,
        rule_type: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetApiRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetApiRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetApiRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetApiRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainRequest(TeaModel):
    def __init__(
        self,
        certificate_body: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        group_id: str = None,
        private_key: str = None,
    ):
        self.certificate_body = certificate_body
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.group_id = group_id
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        return self


class SetDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        domain_status: str = None,
        group_id: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.domain_name = domain_name
        self.domain_status = domain_status
        self.group_id = group_id
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class SetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDomainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_body: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        group_id: str = None,
        private_key: str = None,
    ):
        self.certificate_body = certificate_body
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.group_id = group_id
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        return self


class SetDomainCertificateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDomainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainForBackendRequest(TeaModel):
    def __init__(
        self,
        certificate_body: str = None,
        certificate_name: str = None,
        certificate_private_key: str = None,
        domain_name: str = None,
        group_id: str = None,
    ):
        self.certificate_body = certificate_body
        self.certificate_name = certificate_name
        self.certificate_private_key = certificate_private_key
        self.domain_name = domain_name
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.certificate_private_key is not None:
            result['CertificatePrivateKey'] = self.certificate_private_key
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CertificatePrivateKey') is not None:
            self.certificate_private_key = m.get('CertificatePrivateKey')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class SetDomainForBackendResponseBody(TeaModel):
    def __init__(
        self,
        domain_binding_status: str = None,
        domain_name: str = None,
        group_id: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.domain_binding_status = domain_binding_status
        self.domain_name = domain_name
        self.group_id = group_id
        self.request_id = request_id
        self.sub_domain = sub_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        return self


class SetDomainForBackendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDomainForBackendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetDomainForBackendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMockIntegrationRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        mock: str = None,
        mock_result: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.mock = mock
        self.mock_result = mock_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        return self


class SetMockIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetMockIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetMockIntegrationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetMockIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetPurchasedApiGroupStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        billing_status: str = None,
        close_order: bool = None,
        group_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.billing_status = billing_status
        self.close_order = close_order
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.close_order is not None:
            result['CloseOrder'] = self.close_order
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('CloseOrder') is not None:
            self.close_order = m.get('CloseOrder')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class SetPurchasedApiGroupStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetPurchasedApiGroupStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetPurchasedApiGroupStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SetPurchasedApiGroupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        history_version: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.description = description
        self.group_id = group_id
        self.history_version = history_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SwitchApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchApiResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SwitchApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchApiForInnerRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        history_version: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.description = description
        self.group_id = group_id
        self.history_version = history_version
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SwitchApiForInnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchApiForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchApiForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SwitchApiForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SynCreateAppForInnerRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_key: int = None,
        app_name: str = None,
        app_secret: str = None,
        description: str = None,
        source: str = None,
    ):
        self.ali_uid = ali_uid
        self.app_key = app_key
        self.app_name = app_name
        self.app_secret = app_secret
        self.description = description
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.description is not None:
            result['Description'] = self.description
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SynCreateAppForInnerResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SynCreateAppForInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SynCreateAppForInnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SynCreateAppForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesSystemTagsRequestTag(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class TagResourcesSystemTagsRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        scope: str = None,
        security_token: str = None,
        tag: List[TagResourcesSystemTagsRequestTag] = None,
        tag_owner_bid: str = None,
        tag_owner_uid: int = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.scope = scope
        self.security_token = security_token
        self.tag = tag
        self.tag_owner_bid = tag_owner_bid
        self.tag_owner_uid = tag_owner_uid

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid
        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesSystemTagsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')
        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')
        return self


class TagResourcesSystemTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesSystemTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesSystemTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = TagResourcesSystemTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesSystemTagsRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
        tag_owner_bid: str = None,
        tag_owner_uid: int = None,
    ):
        self.all = all
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag_key = tag_key
        self.tag_owner_bid = tag_owner_bid
        self.tag_owner_uid = tag_owner_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid
        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')
        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')
        return self


class UntagResourcesSystemTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesSystemTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesSystemTagsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UntagResourcesSystemTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VipMigrationRequest(TeaModel):
    def __init__(
        self,
        new_vip: str = None,
        original_vip: str = None,
    ):
        self.new_vip = new_vip
        self.original_vip = original_vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_vip is not None:
            result['NewVip'] = self.new_vip
        if self.original_vip is not None:
            result['OriginalVip'] = self.original_vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewVip') is not None:
            self.new_vip = m.get('NewVip')
        if m.get('OriginalVip') is not None:
            self.original_vip = m.get('OriginalVip')
        return self


class VipMigrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class VipMigrationByUidRequest(TeaModel):
    def __init__(
        self,
        new_vip: str = None,
        original_vip: str = None,
    ):
        self.new_vip = new_vip
        self.original_vip = original_vip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_vip is not None:
            result['NewVip'] = self.new_vip
        if self.original_vip is not None:
            result['OriginalVip'] = self.original_vip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewVip') is not None:
            self.new_vip = m.get('NewVip')
        if m.get('OriginalVip') is not None:
            self.original_vip = m.get('OriginalVip')
        return self


class VipMigrationByUidResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VipMigrationByUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VipMigrationByUidResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = VipMigrationByUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcAddAppServerRequest(TeaModel):
    def __init__(
        self,
        address_pool_id: str = None,
        app_id: str = None,
        server_ip: str = None,
        token: str = None,
    ):
        self.address_pool_id = address_pool_id
        self.app_id = app_id
        self.server_ip = server_ip
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class VpcAddAppServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VpcAddAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcAddAppServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = VpcAddAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcCreateAddressPoolRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        name: str = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.description = description
        self.name = name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class VpcCreateAddressPoolResponseBody(TeaModel):
    def __init__(
        self,
        address_pool_id: str = None,
        request_id: str = None,
    ):
        self.address_pool_id = address_pool_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VpcCreateAddressPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcCreateAddressPoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = VpcCreateAddressPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcQueryAppServersRequest(TeaModel):
    def __init__(
        self,
        address_pool_id: str = None,
        app_id: str = None,
        server_ip: str = None,
    ):
        self.address_pool_id = address_pool_id
        self.app_id = app_id
        self.server_ip = server_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        return self


class VpcQueryAppServersResponseBodyAppServerInfosAppServerInfo(TeaModel):
    def __init__(
        self,
        address_pool_id: str = None,
        app_id: str = None,
        server_ip: str = None,
        server_mapping_ip: str = None,
        server_type: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.address_pool_id = address_pool_id
        self.app_id = app_id
        self.server_ip = server_ip
        self.server_mapping_ip = server_mapping_ip
        self.server_type = server_type
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_pool_id is not None:
            result['AddressPoolId'] = self.address_pool_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_mapping_ip is not None:
            result['ServerMappingIp'] = self.server_mapping_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPoolId') is not None:
            self.address_pool_id = m.get('AddressPoolId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerMappingIp') is not None:
            self.server_mapping_ip = m.get('ServerMappingIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcQueryAppServersResponseBodyAppServerInfos(TeaModel):
    def __init__(
        self,
        app_server_info: List[VpcQueryAppServersResponseBodyAppServerInfosAppServerInfo] = None,
    ):
        self.app_server_info = app_server_info

    def validate(self):
        if self.app_server_info:
            for k in self.app_server_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppServerInfo'] = []
        if self.app_server_info is not None:
            for k in self.app_server_info:
                result['AppServerInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_server_info = []
        if m.get('AppServerInfo') is not None:
            for k in m.get('AppServerInfo'):
                temp_model = VpcQueryAppServersResponseBodyAppServerInfosAppServerInfo()
                self.app_server_info.append(temp_model.from_map(k))
        return self


class VpcQueryAppServersResponseBody(TeaModel):
    def __init__(
        self,
        app_server_infos: VpcQueryAppServersResponseBodyAppServerInfos = None,
        request_id: str = None,
    ):
        self.app_server_infos = app_server_infos
        self.request_id = request_id

    def validate(self):
        if self.app_server_infos:
            self.app_server_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_server_infos is not None:
            result['AppServerInfos'] = self.app_server_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppServerInfos') is not None:
            temp_model = VpcQueryAppServersResponseBodyAppServerInfos()
            self.app_server_infos = temp_model.from_map(m['AppServerInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VpcQueryAppServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcQueryAppServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = VpcQueryAppServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcRegisterAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        name: str = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.description = description
        self.name = name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class VpcRegisterAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_id: str = None,
    ):
        self.app_id = app_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VpcRegisterAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcRegisterAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = VpcRegisterAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcRemoveAppServerRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        server_ip: str = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.server_ip = server_ip
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class VpcRemoveAppServerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VpcRemoveAppServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcRemoveAppServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = VpcRemoveAppServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


