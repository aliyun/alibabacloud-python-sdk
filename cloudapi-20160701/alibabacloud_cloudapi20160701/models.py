# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AbolishApiRequest(TeaModel):
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
            temp_model = AbolishApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBlackListRequest(TeaModel):
    def __init__(
        self,
        black_content: str = None,
        black_type: str = None,
        description: str = None,
        security_token: str = None,
    ):
        self.black_content = black_content
        self.black_type = black_type
        self.description = description
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = AddBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIpControlPolicyItemRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
        ip_control_id: str = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.cidr_ip = cidr_ip
        self.ip_control_id = ip_control_id
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
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class AddIpControlPolicyItemResponseBody(TeaModel):
    def __init__(
        self,
        policy_item_id: str = None,
        request_id: str = None,
    ):
        self.policy_item_id = policy_item_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddIpControlPolicyItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddIpControlPolicyItemResponseBody = None,
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
            temp_model = AddIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddTrafficSpecialControlRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        special_key: str = None,
        special_type: str = None,
        traffic_control_id: str = None,
        traffic_value: int = None,
    ):
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = AddTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiRequest(TeaModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: str = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        open_id_connect_config: str = None,
        request_config: str = None,
        request_paramters: str = None,
        result_body_model: str = None,
        result_descriptions: str = None,
        result_sample: str = None,
        result_type: str = None,
        security_token: str = None,
        service_config: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_name = api_name
        self.app_code_auth_type = app_code_auth_type
        self.auth_type = auth_type
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.open_id_connect_config = open_id_connect_config
        self.request_config = request_config
        self.request_paramters = request_paramters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.security_token = security_token
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.visibility = visibility
        self.web_socket_api_type = web_socket_api_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config
        if self.request_paramters is not None:
            result['RequestParamters'] = self.request_paramters
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.web_socket_api_type is not None:
            result['WebSocketApiType'] = self.web_socket_api_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AppCodeAuthType') is not None:
            self.app_code_auth_type = m.get('AppCodeAuthType')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            self.error_code_samples = m.get('ErrorCodeSamples')
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OpenIdConnectConfig') is not None:
            self.open_id_connect_config = m.get('OpenIdConnectConfig')
        if m.get('RequestConfig') is not None:
            self.request_config = m.get('RequestConfig')
        if m.get('RequestParamters') is not None:
            self.request_paramters = m.get('RequestParamters')
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            self.result_descriptions = m.get('ResultDescriptions')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
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
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_name: str = None,
        instance_id: str = None,
        security_token: str = None,
    ):
        self.description = description
        self.group_name = group_name
        self.instance_id = instance_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.instance_type = instance_type
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
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
            temp_model = CreateApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiStageVariableRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
        stage_route_model: str = None,
        support_route: bool = None,
        variable_name: str = None,
        variable_value: str = None,
    ):
        self.group_id = group_id
        self.security_token = security_token
        self.stage_id = stage_id
        self.stage_route_model = stage_route_model
        self.support_route = support_route
        self.variable_name = variable_name
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_route_model is not None:
            result['StageRouteModel'] = self.stage_route_model
        if self.support_route is not None:
            result['SupportRoute'] = self.support_route
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageRouteModel') is not None:
            self.stage_route_model = m.get('StageRouteModel')
        if m.get('SupportRoute') is not None:
            self.support_route = m.get('SupportRoute')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class CreateApiStageVariableResponseBody(TeaModel):
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


class CreateApiStageVariableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApiStageVariableResponseBody = None,
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
            temp_model = CreateApiStageVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        security_token: str = None,
    ):
        self.app_name = app_name
        self.description = description
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedInfoRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        csharp_demo: str = None,
        curl_demo: str = None,
        group_id: str = None,
        java_demo: str = None,
        objectc_demo: str = None,
        php_demo: str = None,
        python_demo: str = None,
        security_token: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.csharp_demo = csharp_demo
        self.curl_demo = curl_demo
        self.group_id = group_id
        self.java_demo = java_demo
        self.objectc_demo = objectc_demo
        self.php_demo = php_demo
        self.python_demo = python_demo
        self.security_token = security_token
        self.stage_id = stage_id
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
        if self.csharp_demo is not None:
            result['CsharpDemo'] = self.csharp_demo
        if self.curl_demo is not None:
            result['CurlDemo'] = self.curl_demo
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.java_demo is not None:
            result['JavaDemo'] = self.java_demo
        if self.objectc_demo is not None:
            result['ObjectcDemo'] = self.objectc_demo
        if self.php_demo is not None:
            result['PhpDemo'] = self.php_demo
        if self.python_demo is not None:
            result['PythonDemo'] = self.python_demo
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CsharpDemo') is not None:
            self.csharp_demo = m.get('CsharpDemo')
        if m.get('CurlDemo') is not None:
            self.curl_demo = m.get('CurlDemo')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JavaDemo') is not None:
            self.java_demo = m.get('JavaDemo')
        if m.get('ObjectcDemo') is not None:
            self.objectc_demo = m.get('ObjectcDemo')
        if m.get('PhpDemo') is not None:
            self.php_demo = m.get('PhpDemo')
        if m.get('PythonDemo') is not None:
            self.python_demo = m.get('PythonDemo')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class CreateCustomizedInfoResponseBody(TeaModel):
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


class CreateCustomizedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomizedInfoResponseBody = None,
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
            temp_model = CreateCustomizedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        account_quantity: int = None,
        expired_on: str = None,
        security_token: str = None,
        sku_id: str = None,
        token: str = None,
    ):
        self.account_quantity = account_quantity
        self.expired_on = expired_on
        self.security_token = security_token
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
        if self.expired_on is not None:
            result['ExpiredOn'] = self.expired_on
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountQuantity') is not None:
            self.account_quantity = m.get('AccountQuantity')
        if m.get('ExpiredOn') is not None:
            self.expired_on = m.get('ExpiredOn')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntranetDomainRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
    ):
        self.group_id = group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateIntranetDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        request_id: str = None,
    ):
        self.domain_name = domain_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIntranetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIntranetDomainResponseBody = None,
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
            temp_model = CreateIntranetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpControlRequestIpControlPolicys(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        ip: str = None,
    ):
        self.app_id = app_id
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.ip is not None:
            result['IP'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class CreateIpControlRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        ip_control_name: str = None,
        ip_control_policys: List[CreateIpControlRequestIpControlPolicys] = None,
        ip_control_type: str = None,
        security_token: str = None,
    ):
        self.description = description
        self.ip_control_name = ip_control_name
        self.ip_control_policys = ip_control_policys
        self.ip_control_type = ip_control_type
        self.security_token = security_token

    def validate(self):
        if self.ip_control_policys:
            for k in self.ip_control_policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        result['IpControlPolicys'] = []
        if self.ip_control_policys is not None:
            for k in self.ip_control_policys:
                result['IpControlPolicys'].append(k.to_map() if k else None)
        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        self.ip_control_policys = []
        if m.get('IpControlPolicys') is not None:
            for k in m.get('IpControlPolicys'):
                temp_model = CreateIpControlRequestIpControlPolicys()
                self.ip_control_policys.append(temp_model.from_map(k))
        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateIpControlResponseBody(TeaModel):
    def __init__(
        self,
        ip_control_id: str = None,
        request_id: str = None,
    ):
        self.ip_control_id = ip_control_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpControlResponseBody = None,
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
            temp_model = CreateIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogConfigRequest(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        security_token: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
    ):
        self.log_type = log_type
        self.security_token = security_token
        self.sls_log_store = sls_log_store
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class CreateLogConfigResponseBody(TeaModel):
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


class CreateLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogConfigResponseBody = None,
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
            temp_model = CreateLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRaceWorkForInnerRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        group_id: str = None,
        keywords: str = None,
        logo_url: str = None,
        security_token: str = None,
        short_description: str = None,
        work_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.group_id = group_id
        self.keywords = keywords
        self.logo_url = logo_url
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = CreateRaceWorkForInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretKeyRequest(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
        secret_key_name: str = None,
        secret_value: str = None,
        security_token: str = None,
    ):
        self.secret_key = secret_key
        self.secret_key_name = secret_key_name
        self.secret_value = secret_value
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('SecretKeyName') is not None:
            self.secret_key_name = m.get('SecretKeyName')
        if m.get('SecretValue') is not None:
            self.secret_value = m.get('SecretValue')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = CreateSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrafficControlRequest(TeaModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        description: str = None,
        security_token: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        self.api_default = api_default
        self.app_default = app_default
        self.description = description
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = CreateTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAllTrafficSpecialControlRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        traffic_control_id: str = None,
    ):
        self.security_token = security_token
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteAllTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.security_token = security_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
    ):
        self.group_id = group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiStageVariableRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
        variable_name: str = None,
    ):
        self.group_id = group_id
        self.security_token = security_token
        self.stage_id = stage_id
        self.variable_name = variable_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        return self


class DeleteApiStageVariableResponseBody(TeaModel):
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


class DeleteApiStageVariableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApiStageVariableResponseBody = None,
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
            temp_model = DeleteApiStageVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.certificate_id = certificate_id
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpControlRequest(TeaModel):
    def __init__(
        self,
        ip_control_id: str = None,
        security_token: str = None,
    ):
        self.ip_control_id = ip_control_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteIpControlResponseBody(TeaModel):
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


class DeleteIpControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpControlResponseBody = None,
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
            temp_model = DeleteIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLogConfigRequest(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        security_token: str = None,
    ):
        self.log_type = log_type
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteLogConfigResponseBody(TeaModel):
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


class DeleteLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLogConfigResponseBody = None,
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
            temp_model = DeleteLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretKeyRequest(TeaModel):
    def __init__(
        self,
        secret_key_id: str = None,
        security_token: str = None,
    ):
        self.secret_key_id = secret_key_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_key_id is not None:
            result['SecretKeyId'] = self.secret_key_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretKeyId') is not None:
            self.secret_key_id = m.get('SecretKeyId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteSecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficControlRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        traffic_control_id: str = None,
    ):
        self.security_token = security_token
        self.traffic_control_id = traffic_control_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTrafficSpecialControlRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        special_key: str = None,
        special_type: str = None,
        traffic_control_id: str = None,
    ):
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.special_key is not None:
            result['SpecialKey'] = self.special_key
        if self.special_type is not None:
            result['SpecialType'] = self.special_type
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DeleteTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        support_mock: str = None,
    ):
        self.api_id = api_id
        self.description = description
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name
        self.support_mock = support_mock

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.support_mock is not None:
            result['SupportMock'] = self.support_mock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('SupportMock') is not None:
            self.support_mock = m.get('SupportMock')
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
            temp_model = DeployApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.security_token = security_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        body_model: str = None,
        post_body_description: str = None,
        request_http_method: str = None,
        request_mode: str = None,
        request_path: str = None,
        request_protocol: str = None,
    ):
        self.body_format = body_format
        self.body_model = body_model
        self.post_body_description = post_body_description
        self.request_http_method = request_http_method
        self.request_mode = request_mode
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
        if self.body_model is not None:
            result['BodyModel'] = self.body_model
        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description
        if self.request_http_method is not None:
            result['RequestHttpMethod'] = self.request_http_method
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
        if self.request_path is not None:
            result['RequestPath'] = self.request_path
        if self.request_protocol is not None:
            result['RequestProtocol'] = self.request_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')
        if m.get('BodyModel') is not None:
            self.body_model = m.get('BodyModel')
        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')
        if m.get('RequestHttpMethod') is not None:
            self.request_http_method = m.get('RequestHttpMethod')
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
        if m.get('RequestPath') is not None:
            self.request_path = m.get('RequestPath')
        if m.get('RequestProtocol') is not None:
            self.request_protocol = m.get('RequestProtocol')
        return self


class DescribeApiResponseBodyRequestParametersObjectRequestParam(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        qualifier: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.fc_region_id = fc_region_id
        self.function_name = function_name
        self.qualifier = qualifier
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
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
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
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeApiResponseBodyServiceConfigMockHeadersMockHeader(TeaModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        self.header_name = header_name
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        if self.header_value is not None:
            result['HeaderValue'] = self.header_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')
        return self


class DescribeApiResponseBodyServiceConfigMockHeaders(TeaModel):
    def __init__(
        self,
        mock_header: List[DescribeApiResponseBodyServiceConfigMockHeadersMockHeader] = None,
    ):
        self.mock_header = mock_header

    def validate(self):
        if self.mock_header:
            for k in self.mock_header:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MockHeader'] = []
        if self.mock_header is not None:
            for k in self.mock_header:
                result['MockHeader'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mock_header = []
        if m.get('MockHeader') is not None:
            for k in m.get('MockHeader'):
                temp_model = DescribeApiResponseBodyServiceConfigMockHeadersMockHeader()
                self.mock_header.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyServiceConfigVpcConfig(TeaModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
        vpc_scheme: str = None,
    ):
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.port = port
        self.vpc_id = vpc_id
        self.vpc_scheme = vpc_scheme

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
        if self.vpc_scheme is not None:
            result['VpcScheme'] = self.vpc_scheme
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
        if m.get('VpcScheme') is not None:
            self.vpc_scheme = m.get('VpcScheme')
        return self


class DescribeApiResponseBodyServiceConfig(TeaModel):
    def __init__(
        self,
        aone_app_name: str = None,
        content_type_catagory: str = None,
        content_type_value: str = None,
        function_compute_config: DescribeApiResponseBodyServiceConfigFunctionComputeConfig = None,
        inner_service_info: str = None,
        inner_service_type: str = None,
        mock: str = None,
        mock_headers: DescribeApiResponseBodyServiceConfigMockHeaders = None,
        mock_result: str = None,
        mock_status_code: int = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: str = None,
        service_vpc_enable: str = None,
        vpc_config: DescribeApiResponseBodyServiceConfigVpcConfig = None,
    ):
        self.aone_app_name = aone_app_name
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.function_compute_config = function_compute_config
        self.inner_service_info = inner_service_info
        self.inner_service_type = inner_service_type
        self.mock = mock
        self.mock_headers = mock_headers
        self.mock_result = mock_result
        self.mock_status_code = mock_status_code
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
        if self.mock_headers:
            self.mock_headers.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aone_app_name is not None:
            result['AoneAppName'] = self.aone_app_name
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory
        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
        if self.inner_service_info is not None:
            result['InnerServiceInfo'] = self.inner_service_info
        if self.inner_service_type is not None:
            result['InnerServiceType'] = self.inner_service_type
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_headers is not None:
            result['MockHeaders'] = self.mock_headers.to_map()
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.mock_status_code is not None:
            result['MockStatusCode'] = self.mock_status_code
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
        if m.get('AoneAppName') is not None:
            self.aone_app_name = m.get('AoneAppName')
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('InnerServiceInfo') is not None:
            self.inner_service_info = m.get('InnerServiceInfo')
        if m.get('InnerServiceType') is not None:
            self.inner_service_type = m.get('InnerServiceType')
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockHeaders') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigMockHeaders()
            self.mock_headers = temp_model.from_map(m['MockHeaders'])
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')
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
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        constant_parameters: DescribeApiResponseBodyConstantParameters = None,
        created_time: str = None,
        custom_system_parameters: DescribeApiResponseBodyCustomSystemParameters = None,
        deployed_infos: DescribeApiResponseBodyDeployedInfos = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: DescribeApiResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
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
        result_body_model: str = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: DescribeApiResponseBodyServiceConfig = None,
        service_parameters_object: DescribeApiResponseBodyServiceParametersObject = None,
        system_parameters: DescribeApiResponseBodySystemParameters = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_id = api_id
        self.api_name = api_name
        self.app_code_auth_type = app_code_auth_type
        self.auth_type = auth_type
        self.constant_parameters = constant_parameters
        self.created_time = created_time
        self.custom_system_parameters = custom_system_parameters
        self.deployed_infos = deployed_infos
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
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
        self.result_body_model = result_body_model
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters_object = service_parameters_object
        self.system_parameters = system_parameters
        self.visibility = visibility
        self.web_socket_api_type = web_socket_api_type

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
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type
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
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
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
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
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
        if self.web_socket_api_type is not None:
            result['WebSocketApiType'] = self.web_socket_api_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AppCodeAuthType') is not None:
            self.app_code_auth_type = m.get('AppCodeAuthType')
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
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
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
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
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
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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


class DescribeApiDocResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        body_format: str = None,
        deployed_time: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: DescribeApiDocResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        http_method: str = None,
        http_protocol: str = None,
        mock: str = None,
        mock_result: str = None,
        origin_result_description: str = None,
        path: str = None,
        path_parameters: DescribeApiDocResponseBodyPathParameters = None,
        post_body_description: str = None,
        post_body_type: str = None,
        region_id: str = None,
        request_body: DescribeApiDocResponseBodyRequestBody = None,
        request_headers: DescribeApiDocResponseBodyRequestHeaders = None,
        request_id: str = None,
        request_mode: str = None,
        request_queries: DescribeApiDocResponseBodyRequestQueries = None,
        result_sample: str = None,
        result_type: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        stage_name: str = None,
        vpc_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.body_format = body_format
        self.deployed_time = deployed_time
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.group_name = group_name
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
        self.request_mode = request_mode
        self.request_queries = request_queries
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_timeout = service_timeout
        self.service_vpc_enable = service_vpc_enable
        self.stage_name = stage_name
        self.vpc_name = vpc_name

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
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
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
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
        if self.request_queries is not None:
            result['RequestQueries'] = self.request_queries.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout
        if self.service_vpc_enable is not None:
            result['ServiceVpcEnable'] = self.service_vpc_enable
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
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
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiDocResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
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
        if m.get('OriginResultDescription') is not None:
            self.origin_result_description = m.get('OriginResultDescription')
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
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
        if m.get('RequestQueries') is not None:
            temp_model = DescribeApiDocResponseBodyRequestQueries()
            self.request_queries = temp_model.from_map(m['RequestQueries'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')
        if m.get('ServiceVpcEnable') is not None:
            self.service_vpc_enable = m.get('ServiceVpcEnable')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
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
            temp_model = DescribeApiDocsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiErrorRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeApiErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
    ):
        self.group_id = group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApiGroupDetailResponseBodyDomainItemsDomainItem(TeaModel):
    def __init__(
        self,
        bind_stage_name: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        domain_binding_status: str = None,
        domain_legal_status: str = None,
        domain_name: str = None,
        domain_name_resolution: str = None,
        domain_remark: str = None,
        domain_web_socket_status: str = None,
        wildcard_domain_patterns: str = None,
    ):
        self.bind_stage_name = bind_stage_name
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.domain_binding_status = domain_binding_status
        self.domain_legal_status = domain_legal_status
        self.domain_name = domain_name
        self.domain_name_resolution = domain_name_resolution
        self.domain_remark = domain_remark
        self.domain_web_socket_status = domain_web_socket_status
        self.wildcard_domain_patterns = wildcard_domain_patterns

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_stage_name is not None:
            result['BindStageName'] = self.bind_stage_name
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_remark is not None:
            result['DomainRemark'] = self.domain_remark
        if self.domain_web_socket_status is not None:
            result['DomainWebSocketStatus'] = self.domain_web_socket_status
        if self.wildcard_domain_patterns is not None:
            result['WildcardDomainPatterns'] = self.wildcard_domain_patterns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStageName') is not None:
            self.bind_stage_name = m.get('BindStageName')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
        if m.get('WildcardDomainPatterns') is not None:
            self.wildcard_domain_patterns = m.get('WildcardDomainPatterns')
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


class DescribeApiGroupDetailResponseBodyStageItemsStageInfo(TeaModel):
    def __init__(
        self,
        description: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        self.description = description
        self.stage_id = stage_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeApiGroupDetailResponseBodyStageItems(TeaModel):
    def __init__(
        self,
        stage_info: List[DescribeApiGroupDetailResponseBodyStageItemsStageInfo] = None,
    ):
        self.stage_info = stage_info

    def validate(self):
        if self.stage_info:
            for k in self.stage_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StageInfo'] = []
        if self.stage_info is not None:
            for k in self.stage_info:
                result['StageInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stage_info = []
        if m.get('StageInfo') is not None:
            for k in m.get('StageInfo'):
                temp_model = DescribeApiGroupDetailResponseBodyStageItemsStageInfo()
                self.stage_info.append(temp_model.from_map(k))
        return self


class DescribeApiGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        billing_status: str = None,
        classic_vpc_sub_domain: str = None,
        compatible_flags: str = None,
        created_time: str = None,
        custom_trace_config: str = None,
        default_domain: str = None,
        description: str = None,
        domain_items: DescribeApiGroupDetailResponseBodyDomainItems = None,
        group_id: str = None,
        group_name: str = None,
        https_policy: str = None,
        illegal_status: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        instance_vip_list: str = None,
        ipv_6status: str = None,
        modified_time: str = None,
        passthrough_headers: str = None,
        region_id: str = None,
        request_id: str = None,
        rpc_pattern: str = None,
        stage_items: DescribeApiGroupDetailResponseBodyStageItems = None,
        status: str = None,
        sub_domain: str = None,
        traffic_limit: int = None,
        user_log_config: str = None,
        vpc_domain: str = None,
    ):
        self.billing_status = billing_status
        self.classic_vpc_sub_domain = classic_vpc_sub_domain
        self.compatible_flags = compatible_flags
        self.created_time = created_time
        self.custom_trace_config = custom_trace_config
        self.default_domain = default_domain
        self.description = description
        self.domain_items = domain_items
        self.group_id = group_id
        self.group_name = group_name
        self.https_policy = https_policy
        self.illegal_status = illegal_status
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.instance_vip_list = instance_vip_list
        self.ipv_6status = ipv_6status
        self.modified_time = modified_time
        self.passthrough_headers = passthrough_headers
        self.region_id = region_id
        self.request_id = request_id
        self.rpc_pattern = rpc_pattern
        self.stage_items = stage_items
        self.status = status
        self.sub_domain = sub_domain
        self.traffic_limit = traffic_limit
        self.user_log_config = user_log_config
        self.vpc_domain = vpc_domain

    def validate(self):
        if self.domain_items:
            self.domain_items.validate()
        if self.stage_items:
            self.stage_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.classic_vpc_sub_domain is not None:
            result['ClassicVpcSubDomain'] = self.classic_vpc_sub_domain
        if self.compatible_flags is not None:
            result['CompatibleFlags'] = self.compatible_flags
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.custom_trace_config is not None:
            result['CustomTraceConfig'] = self.custom_trace_config
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_items is not None:
            result['DomainItems'] = self.domain_items.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_vip_list is not None:
            result['InstanceVipList'] = self.instance_vip_list
        if self.ipv_6status is not None:
            result['Ipv6Status'] = self.ipv_6status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.passthrough_headers is not None:
            result['PassthroughHeaders'] = self.passthrough_headers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rpc_pattern is not None:
            result['RpcPattern'] = self.rpc_pattern
        if self.stage_items is not None:
            result['StageItems'] = self.stage_items.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        if self.user_log_config is not None:
            result['UserLogConfig'] = self.user_log_config
        if self.vpc_domain is not None:
            result['VpcDomain'] = self.vpc_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('ClassicVpcSubDomain') is not None:
            self.classic_vpc_sub_domain = m.get('ClassicVpcSubDomain')
        if m.get('CompatibleFlags') is not None:
            self.compatible_flags = m.get('CompatibleFlags')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CustomTraceConfig') is not None:
            self.custom_trace_config = m.get('CustomTraceConfig')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainItems') is not None:
            temp_model = DescribeApiGroupDetailResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceVipList') is not None:
            self.instance_vip_list = m.get('InstanceVipList')
        if m.get('Ipv6Status') is not None:
            self.ipv_6status = m.get('Ipv6Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PassthroughHeaders') is not None:
            self.passthrough_headers = m.get('PassthroughHeaders')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RpcPattern') is not None:
            self.rpc_pattern = m.get('RpcPattern')
        if m.get('StageItems') is not None:
            temp_model = DescribeApiGroupDetailResponseBodyStageItems()
            self.stage_items = temp_model.from_map(m['StageItems'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('TrafficLimit') is not None:
            self.traffic_limit = m.get('TrafficLimit')
        if m.get('UserLogConfig') is not None:
            self.user_log_config = m.get('UserLogConfig')
        if m.get('VpcDomain') is not None:
            self.vpc_domain = m.get('VpcDomain')
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
            temp_model = DescribeApiGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupDetailForConsumerRequest(TeaModel):
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


class DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem(TeaModel):
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


class DescribeApiGroupDetailForConsumerResponseBodyDomainItems(TeaModel):
    def __init__(
        self,
        domain_item: List[DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem] = None,
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
                temp_model = DescribeApiGroupDetailForConsumerResponseBodyDomainItemsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribeApiGroupDetailForConsumerResponseBody(TeaModel):
    def __init__(
        self,
        billing_status: str = None,
        created_time: str = None,
        description: str = None,
        domain_items: DescribeApiGroupDetailForConsumerResponseBodyDomainItems = None,
        group_id: str = None,
        group_name: str = None,
        illegal_status: str = None,
        modified_time: str = None,
        purchased: str = None,
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
        self.purchased = purchased
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
        if self.purchased is not None:
            result['Purchased'] = self.purchased
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
            temp_model = DescribeApiGroupDetailForConsumerResponseBodyDomainItems()
            self.domain_items = temp_model.from_map(m['DomainItems'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Purchased') is not None:
            self.purchased = m.get('Purchased')
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


class DescribeApiGroupDetailForConsumerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiGroupDetailForConsumerResponseBody = None,
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
            temp_model = DescribeApiGroupDetailForConsumerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupsRequestTag(TeaModel):
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


class DescribeApiGroupsRequest(TeaModel):
    def __init__(
        self,
        enable_tag_auth: bool = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        not_classic: bool = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        tag: List[DescribeApiGroupsRequestTag] = None,
    ):
        self.enable_tag_auth = enable_tag_auth
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.not_classic = not_classic
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.tag = tag

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
        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.not_classic is not None:
            result['NotClassic'] = self.not_classic
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NotClassic') is not None:
            self.not_classic = m.get('NotClassic')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeApiGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute(TeaModel):
    def __init__(
        self,
        billing_status: str = None,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        https_policy: str = None,
        illegal_status: str = None,
        instance_id: str = None,
        instance_type: str = None,
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
        self.https_policy = https_policy
        self.illegal_status = illegal_status
        self.instance_id = instance_id
        self.instance_type = instance_type
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
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.illegal_status is not None:
            result['IllegalStatus'] = self.illegal_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
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
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('IllegalStatus') is not None:
            self.illegal_status = m.get('IllegalStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
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
            temp_model = DescribeApiGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiIpControlsRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
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
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
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
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
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


class DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        ip_control_id: str = None,
        ip_control_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.bound_time = bound_time
        self.ip_control_id = ip_control_id
        self.ip_control_name = ip_control_name

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
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        return self


class DescribeApiIpControlsResponseBodyApiIpControls(TeaModel):
    def __init__(
        self,
        api_ip_control_item: List[DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem] = None,
    ):
        self.api_ip_control_item = api_ip_control_item

    def validate(self):
        if self.api_ip_control_item:
            for k in self.api_ip_control_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiIpControlItem'] = []
        if self.api_ip_control_item is not None:
            for k in self.api_ip_control_item:
                result['ApiIpControlItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_ip_control_item = []
        if m.get('ApiIpControlItem') is not None:
            for k in m.get('ApiIpControlItem'):
                temp_model = DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem()
                self.api_ip_control_item.append(temp_model.from_map(k))
        return self


class DescribeApiIpControlsResponseBody(TeaModel):
    def __init__(
        self,
        api_ip_controls: DescribeApiIpControlsResponseBodyApiIpControls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_ip_controls = api_ip_controls
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_ip_controls:
            self.api_ip_controls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ip_controls is not None:
            result['ApiIpControls'] = self.api_ip_controls.to_map()
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
        if m.get('ApiIpControls') is not None:
            temp_model = DescribeApiIpControlsResponseBodyApiIpControls()
            self.api_ip_controls = temp_model.from_map(m['ApiIpControls'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiIpControlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiIpControlsResponseBody = None,
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
            temp_model = DescribeApiIpControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiLatencyRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeApiLatencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiQpsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeApiQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiRulesRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_type: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.rule_type = rule_type
        self.security_token = security_token
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
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeApiRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiStageDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
    ):
        self.group_id = group_id
        self.security_token = security_token
        self.stage_id = stage_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem(TeaModel):
    def __init__(
        self,
        condition_value: str = None,
        max_value: int = None,
        min_value: int = None,
        result_value: str = None,
    ):
        self.condition_value = condition_value
        self.max_value = max_value
        self.min_value = min_value
        self.result_value = result_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition_value is not None:
            result['ConditionValue'] = self.condition_value
        if self.max_value is not None:
            result['MaxValue'] = self.max_value
        if self.min_value is not None:
            result['MinValue'] = self.min_value
        if self.result_value is not None:
            result['ResultValue'] = self.result_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionValue') is not None:
            self.condition_value = m.get('ConditionValue')
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')
        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')
        if m.get('ResultValue') is not None:
            self.result_value = m.get('ResultValue')
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules(TeaModel):
    def __init__(
        self,
        route_rule_item: List[DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem] = None,
    ):
        self.route_rule_item = route_rule_item

    def validate(self):
        if self.route_rule_item:
            for k in self.route_rule_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteRuleItem'] = []
        if self.route_rule_item is not None:
            for k in self.route_rule_item:
                result['RouteRuleItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_rule_item = []
        if m.get('RouteRuleItem') is not None:
            for k in m.get('RouteRuleItem'):
                temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRulesRouteRuleItem()
                self.route_rule_item.append(temp_model.from_map(k))
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel(TeaModel):
    def __init__(
        self,
        location: str = None,
        parameter_catalog: str = None,
        parameter_type: str = None,
        route_match_symbol: str = None,
        route_rules: DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules = None,
        service_parameter_name: str = None,
    ):
        self.location = location
        self.parameter_catalog = parameter_catalog
        self.parameter_type = parameter_type
        self.route_match_symbol = route_match_symbol
        self.route_rules = route_rules
        self.service_parameter_name = service_parameter_name

    def validate(self):
        if self.route_rules:
            self.route_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_catalog is not None:
            result['ParameterCatalog'] = self.parameter_catalog
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.route_match_symbol is not None:
            result['RouteMatchSymbol'] = self.route_match_symbol
        if self.route_rules is not None:
            result['RouteRules'] = self.route_rules.to_map()
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterCatalog') is not None:
            self.parameter_catalog = m.get('ParameterCatalog')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('RouteMatchSymbol') is not None:
            self.route_match_symbol = m.get('RouteMatchSymbol')
        if m.get('RouteRules') is not None:
            temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModelRouteRules()
            self.route_rules = temp_model.from_map(m['RouteRules'])
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiStageDetailResponseBodyVariablesVariableItem(TeaModel):
    def __init__(
        self,
        stage_route_model: DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel = None,
        support_route: bool = None,
        variable_name: str = None,
        variable_value: str = None,
    ):
        self.stage_route_model = stage_route_model
        self.support_route = support_route
        self.variable_name = variable_name
        self.variable_value = variable_value

    def validate(self):
        if self.stage_route_model:
            self.stage_route_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stage_route_model is not None:
            result['StageRouteModel'] = self.stage_route_model.to_map()
        if self.support_route is not None:
            result['SupportRoute'] = self.support_route
        if self.variable_name is not None:
            result['VariableName'] = self.variable_name
        if self.variable_value is not None:
            result['VariableValue'] = self.variable_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StageRouteModel') is not None:
            temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItemStageRouteModel()
            self.stage_route_model = temp_model.from_map(m['StageRouteModel'])
        if m.get('SupportRoute') is not None:
            self.support_route = m.get('SupportRoute')
        if m.get('VariableName') is not None:
            self.variable_name = m.get('VariableName')
        if m.get('VariableValue') is not None:
            self.variable_value = m.get('VariableValue')
        return self


class DescribeApiStageDetailResponseBodyVariables(TeaModel):
    def __init__(
        self,
        variable_item: List[DescribeApiStageDetailResponseBodyVariablesVariableItem] = None,
    ):
        self.variable_item = variable_item

    def validate(self):
        if self.variable_item:
            for k in self.variable_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VariableItem'] = []
        if self.variable_item is not None:
            for k in self.variable_item:
                result['VariableItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.variable_item = []
        if m.get('VariableItem') is not None:
            for k in m.get('VariableItem'):
                temp_model = DescribeApiStageDetailResponseBodyVariablesVariableItem()
                self.variable_item.append(temp_model.from_map(k))
        return self


class DescribeApiStageDetailResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        modified_time: str = None,
        request_id: str = None,
        stage_id: str = None,
        stage_name: str = None,
        variables: DescribeApiStageDetailResponseBodyVariables = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.modified_time = modified_time
        self.request_id = request_id
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.variables = variables

    def validate(self):
        if self.variables:
            self.variables.validate()

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
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.variables is not None:
            result['Variables'] = self.variables.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Variables') is not None:
            temp_model = DescribeApiStageDetailResponseBodyVariables()
            self.variables = temp_model.from_map(m['Variables'])
        return self


class DescribeApiStageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApiStageDetailResponseBody = None,
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
            temp_model = DescribeApiStageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiTrafficRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        security_token: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.app_id = app_id
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApisByAppResponseBodyAppApiRelationInfosAppApiRelationInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_vaild_time: str = None,
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
        self.auth_vaild_time = auth_vaild_time
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
        if self.auth_vaild_time is not None:
            result['AuthVaildTime'] = self.auth_vaild_time
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
        if m.get('AuthVaildTime') is not None:
            self.auth_vaild_time = m.get('AuthVaildTime')
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
            temp_model = DescribeApisByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByIpControlRequest(TeaModel):
    def __init__(
        self,
        ip_control_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.ip_control_id = ip_control_id
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
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeApisByIpControlResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.bound_time = bound_time
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
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time
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
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
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


class DescribeApisByIpControlResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApisByIpControlResponseBodyApiInfosApiInfo] = None,
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
                temp_model = DescribeApisByIpControlResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisByIpControlResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApisByIpControlResponseBodyApiInfos = None,
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
            temp_model = DescribeApisByIpControlResponseBodyApiInfos()
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


class DescribeApisByIpControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApisByIpControlResponseBody = None,
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
            temp_model = DescribeApisByIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByRuleRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rule_id: str = None,
        rule_type: str = None,
        security_token: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        security_token: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeApisForConsoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppRequest(TeaModel):
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
            temp_model = DescribeAppSecuritiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecurityRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        security_token: str = None,
    ):
        self.app_key = app_key
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppSecurityResponseBody(TeaModel):
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
            temp_model = DescribeAppSecurityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequestTag(TeaModel):
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


class DescribeAppsRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        enable_tag_auth: bool = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        tag: List[DescribeAppsRequestTag] = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.enable_tag_auth = enable_tag_auth
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.tag = tag

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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeAppsRequestTag()
                self.tag.append(temp_model.from_map(k))
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
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsByApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_id: int = None,
        app_name: str = None,
        app_owner_id: int = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_id = app_id
        self.app_name = app_name
        self.app_owner_id = app_owner_id
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_owner_id is not None:
            result['AppOwnerId'] = self.app_owner_id
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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppOwnerId') is not None:
            self.app_owner_id = m.get('AppOwnerId')
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


class DescribeAppsByApiResponseBodyAppApiRelationInfosAppApiRelationInfo(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        auth_vaild_time: str = None,
        authorization_source: str = None,
        created_time: str = None,
        description: str = None,
        operator: str = None,
        stage_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.auth_vaild_time = auth_vaild_time
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
        if self.auth_vaild_time is not None:
            result['AuthVaildTime'] = self.auth_vaild_time
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
        if m.get('AuthVaildTime') is not None:
            self.auth_vaild_time = m.get('AuthVaildTime')
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
            temp_model = DescribeAppsByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsForProviderRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.app_owner_id = app_owner_id
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
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_owner_id is not None:
            result['AppOwnerId'] = self.app_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppOwnerId') is not None:
            self.app_owner_id = m.get('AppOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeAppsForProviderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBlackListsRequest(TeaModel):
    def __init__(
        self,
        black_type: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.black_type = black_type
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
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeBlackListsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployedApiRequest(TeaModel):
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        disable_internet: bool = None,
        error_code_samples: DescribeDeployedApiResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
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
        request_mode: str = None,
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
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
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
        self.request_mode = request_mode
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
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
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
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
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
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeDeployedApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
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
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
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
            temp_model = DescribeDeployedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDomainResponseBody(TeaModel):
    def __init__(
        self,
        certificate_body: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        domain_binding_status: str = None,
        domain_legal_status: str = None,
        domain_name: str = None,
        domain_name_resolution: str = None,
        domain_remark: str = None,
        domain_web_socket_status: str = None,
        group_id: str = None,
        private_key: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.certificate_body = certificate_body
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.domain_binding_status = domain_binding_status
        self.domain_legal_status = domain_legal_status
        self.domain_name = domain_name
        self.domain_name_resolution = domain_name_resolution
        self.domain_remark = domain_remark
        self.domain_web_socket_status = domain_web_socket_status
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
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_name_resolution is not None:
            result['DomainNameResolution'] = self.domain_name_resolution
        if self.domain_remark is not None:
            result['DomainRemark'] = self.domain_remark
        if self.domain_web_socket_status is not None:
            result['DomainWebSocketStatus'] = self.domain_web_socket_status
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
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainNameResolution') is not None:
            self.domain_name_resolution = m.get('DomainNameResolution')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
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
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainResolutionRequest(TeaModel):
    def __init__(
        self,
        domain_names: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.domain_names = domain_names
        self.group_id = group_id
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeDomainResolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
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
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
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
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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


class DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter(TeaModel):
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


class DescribeHistoryApiResponseBodyCustomSystemParameters(TeaModel):
    def __init__(
        self,
        custom_system_parameter: List[DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter] = None,
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
                temp_model = DescribeHistoryApiResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k))
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


class DescribeHistoryApiResponseBodyOpenIdConnectConfig(TeaModel):
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        array_items_type: str = None,
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
        self.array_items_type = array_items_type
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
        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type
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
        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')
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
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        body_format: str = None,
        constant_parameters: DescribeHistoryApiResponseBodyConstantParameters = None,
        custom_system_parameters: DescribeHistoryApiResponseBodyCustomSystemParameters = None,
        deployed_time: str = None,
        description: str = None,
        error_code_samples: DescribeHistoryApiResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        function_compute_config: DescribeHistoryApiResponseBodyFunctionComputeConfig = None,
        group_id: str = None,
        group_name: str = None,
        history_version: str = None,
        http_method: str = None,
        http_protocol: str = None,
        mock: str = None,
        mock_result: str = None,
        open_id_connect_config: DescribeHistoryApiResponseBodyOpenIdConnectConfig = None,
        origin_result_description: str = None,
        path: str = None,
        path_parameters: DescribeHistoryApiResponseBodyPathParameters = None,
        post_body_description: str = None,
        post_body_type: str = None,
        region_id: str = None,
        request_body: DescribeHistoryApiResponseBodyRequestBody = None,
        request_headers: DescribeHistoryApiResponseBodyRequestHeaders = None,
        request_id: str = None,
        request_mode: str = None,
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
        self.allow_signature_method = allow_signature_method
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.body_format = body_format
        self.constant_parameters = constant_parameters
        self.custom_system_parameters = custom_system_parameters
        self.deployed_time = deployed_time
        self.description = description
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.function_compute_config = function_compute_config
        self.group_id = group_id
        self.group_name = group_name
        self.history_version = history_version
        self.http_method = http_method
        self.http_protocol = http_protocol
        self.mock = mock
        self.mock_result = mock_result
        self.open_id_connect_config = open_id_connect_config
        self.origin_result_description = origin_result_description
        self.path = path
        self.path_parameters = path_parameters
        self.post_body_description = post_body_description
        self.post_body_type = post_body_type
        self.region_id = region_id
        self.request_body = request_body
        self.request_headers = request_headers
        self.request_id = request_id
        self.request_mode = request_mode
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
        if self.custom_system_parameters:
            self.custom_system_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.open_id_connect_config:
            self.open_id_connect_config.validate()
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
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
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
        if self.custom_system_parameters is not None:
            result['CustomSystemParameters'] = self.custom_system_parameters.to_map()
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
        if self.description is not None:
            result['Description'] = self.description
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
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
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config.to_map()
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
        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode
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
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
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
        if m.get('CustomSystemParameters') is not None:
            temp_model = DescribeHistoryApiResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m['CustomSystemParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeHistoryApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
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
        if m.get('OpenIdConnectConfig') is not None:
            temp_model = DescribeHistoryApiResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m['OpenIdConnectConfig'])
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
        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')
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
            temp_model = DescribeHistoryApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpControlPolicyItemsRequest(TeaModel):
    def __init__(
        self,
        ip_control_id: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_item_id: str = None,
        security_token: str = None,
    ):
        self.ip_control_id = ip_control_id
        self.page_number = page_number
        self.page_size = page_size
        self.policy_item_id = policy_item_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
        create_time: str = None,
        modified_time: str = None,
        policy_item_id: str = None,
    ):
        self.app_id = app_id
        self.cidr_ip = cidr_ip
        self.create_time = create_time
        self.modified_time = modified_time
        self.policy_item_id = policy_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        return self


class DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems(TeaModel):
    def __init__(
        self,
        ip_control_policy_item: List[DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem] = None,
    ):
        self.ip_control_policy_item = ip_control_policy_item

    def validate(self):
        if self.ip_control_policy_item:
            for k in self.ip_control_policy_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpControlPolicyItem'] = []
        if self.ip_control_policy_item is not None:
            for k in self.ip_control_policy_item:
                result['IpControlPolicyItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_control_policy_item = []
        if m.get('IpControlPolicyItem') is not None:
            for k in m.get('IpControlPolicyItem'):
                temp_model = DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem()
                self.ip_control_policy_item.append(temp_model.from_map(k))
        return self


class DescribeIpControlPolicyItemsResponseBody(TeaModel):
    def __init__(
        self,
        ip_control_policy_items: DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ip_control_policy_items = ip_control_policy_items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ip_control_policy_items:
            self.ip_control_policy_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_policy_items is not None:
            result['IpControlPolicyItems'] = self.ip_control_policy_items.to_map()
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
        if m.get('IpControlPolicyItems') is not None:
            temp_model = DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems()
            self.ip_control_policy_items = temp_model.from_map(m['IpControlPolicyItems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeIpControlPolicyItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpControlPolicyItemsResponseBody = None,
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
            temp_model = DescribeIpControlPolicyItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpControlsRequest(TeaModel):
    def __init__(
        self,
        ip_control_id: str = None,
        ip_control_name: str = None,
        ip_control_type: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.ip_control_id = ip_control_id
        self.ip_control_name = ip_control_name
        self.ip_control_type = ip_control_type
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
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeIpControlsResponseBodyIpControlInfosIpControlInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        ip_control_id: str = None,
        ip_control_name: str = None,
        ip_control_type: str = None,
        modified_time: str = None,
        region_id: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.ip_control_id = ip_control_id
        self.ip_control_name = ip_control_name
        self.ip_control_type = ip_control_type
        self.modified_time = modified_time
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeIpControlsResponseBodyIpControlInfos(TeaModel):
    def __init__(
        self,
        ip_control_info: List[DescribeIpControlsResponseBodyIpControlInfosIpControlInfo] = None,
    ):
        self.ip_control_info = ip_control_info

    def validate(self):
        if self.ip_control_info:
            for k in self.ip_control_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpControlInfo'] = []
        if self.ip_control_info is not None:
            for k in self.ip_control_info:
                result['IpControlInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_control_info = []
        if m.get('IpControlInfo') is not None:
            for k in m.get('IpControlInfo'):
                temp_model = DescribeIpControlsResponseBodyIpControlInfosIpControlInfo()
                self.ip_control_info.append(temp_model.from_map(k))
        return self


class DescribeIpControlsResponseBody(TeaModel):
    def __init__(
        self,
        ip_control_infos: DescribeIpControlsResponseBodyIpControlInfos = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ip_control_infos = ip_control_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ip_control_infos:
            self.ip_control_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_infos is not None:
            result['IpControlInfos'] = self.ip_control_infos.to_map()
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
        if m.get('IpControlInfos') is not None:
            temp_model = DescribeIpControlsResponseBodyIpControlInfos()
            self.ip_control_infos = temp_model.from_map(m['IpControlInfos'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeIpControlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpControlsResponseBody = None,
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
            temp_model = DescribeIpControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogConfigRequest(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        security_token: str = None,
    ):
        self.log_type = log_type
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeLogConfigResponseBodyLogInfosLogInfo(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        region_id: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
    ):
        self.log_type = log_type
        self.region_id = region_id
        self.sls_log_store = sls_log_store
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class DescribeLogConfigResponseBodyLogInfos(TeaModel):
    def __init__(
        self,
        log_info: List[DescribeLogConfigResponseBodyLogInfosLogInfo] = None,
    ):
        self.log_info = log_info

    def validate(self):
        if self.log_info:
            for k in self.log_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogInfo'] = []
        if self.log_info is not None:
            for k in self.log_info:
                result['LogInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_info = []
        if m.get('LogInfo') is not None:
            for k in m.get('LogInfo'):
                temp_model = DescribeLogConfigResponseBodyLogInfosLogInfo()
                self.log_info.append(temp_model.from_map(k))
        return self


class DescribeLogConfigResponseBody(TeaModel):
    def __init__(
        self,
        log_infos: DescribeLogConfigResponseBodyLogInfos = None,
        request_id: str = None,
    ):
        self.log_infos = log_infos
        self.request_id = request_id

    def validate(self):
        if self.log_infos:
            self.log_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_infos is not None:
            result['LogInfos'] = self.log_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogInfos') is not None:
            temp_model = DescribeLogConfigResponseBodyLogInfos()
            self.log_infos = temp_model.from_map(m['LogInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogConfigResponseBody = None,
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
            temp_model = DescribeLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.security_token = security_token

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribePurchasedApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
    ):
        self.group_id = group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribePurchasedApiGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        security_token: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
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
        return self


class DescribePurchasedApisResponseBodyApiInfosApiInfo(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
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
        self.deployed_time = deployed_time
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
        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time
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
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
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
            temp_model = DescribePurchasedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRaceWorkForInnerRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
    ):
        self.group_id = group_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeRaceWorkForInnerResponseBody()
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
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRulesByApiRequest(TeaModel):
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
        security_token: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        security_token: str = None,
        stage_name: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
    ):
        self.api_uid = api_uid
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = DescribeTrafficControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportSwaggerRequest(TeaModel):
    def __init__(
        self,
        api_uid: str = None,
        data_format: str = None,
    ):
        self.api_uid = api_uid
        self.data_format = data_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        return self


class ExportSwaggerResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportSwaggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportSwaggerResponseBody = None,
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
            temp_model = ExportSwaggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApiMethodsRequest(TeaModel):
    def __init__(
        self,
        api_path: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_path = api_path
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
        if self.api_path is not None:
            result['ApiPath'] = self.api_path
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiPath') is not None:
            self.api_path = m.get('ApiPath')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class GetApiMethodsResponseBody(TeaModel):
    def __init__(
        self,
        methods: List[str] = None,
        request_id: str = None,
    ):
        self.methods = methods
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.methods is not None:
            result['Methods'] = self.methods
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Methods') is not None:
            self.methods = m.get('Methods')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApiMethodsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApiMethodsResponseBody = None,
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
            temp_model = GetApiMethodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomizedInfoRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.security_token = security_token
        self.stage_id = stage_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class GetCustomizedInfoResponseBodySdkDemosSdkDemo(TeaModel):
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


class GetCustomizedInfoResponseBodySdkDemos(TeaModel):
    def __init__(
        self,
        sdk_demo: List[GetCustomizedInfoResponseBodySdkDemosSdkDemo] = None,
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
                temp_model = GetCustomizedInfoResponseBodySdkDemosSdkDemo()
                self.sdk_demo.append(temp_model.from_map(k))
        return self


class GetCustomizedInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_demos: GetCustomizedInfoResponseBodySdkDemos = None,
    ):
        self.request_id = request_id
        self.sdk_demos = sdk_demos

    def validate(self):
        if self.sdk_demos:
            self.sdk_demos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_demos is not None:
            result['SdkDemos'] = self.sdk_demos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkDemos') is not None:
            temp_model = GetCustomizedInfoResponseBodySdkDemos()
            self.sdk_demos = temp_model.from_map(m['SdkDemos'])
        return self


class GetCustomizedInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomizedInfoResponseBody = None,
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
            temp_model = GetCustomizedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSwaggerRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        data_format: str = None,
        dry_run: bool = None,
        group_id: str = None,
        overwrite: bool = None,
    ):
        self.data = data
        self.data_format = data_format
        self.dry_run = dry_run
        self.group_id = group_id
        self.overwrite = overwrite

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        return self


class ImportSwaggerResponseBodyFailedApiImportSwaggerFailed(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        http_method: str = None,
        path: str = None,
    ):
        self.error_msg = error_msg
        self.http_method = http_method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ImportSwaggerResponseBodyFailed(TeaModel):
    def __init__(
        self,
        api_import_swagger_failed: List[ImportSwaggerResponseBodyFailedApiImportSwaggerFailed] = None,
    ):
        self.api_import_swagger_failed = api_import_swagger_failed

    def validate(self):
        if self.api_import_swagger_failed:
            for k in self.api_import_swagger_failed:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportSwaggerFailed'] = []
        if self.api_import_swagger_failed is not None:
            for k in self.api_import_swagger_failed:
                result['ApiImportSwaggerFailed'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_swagger_failed = []
        if m.get('ApiImportSwaggerFailed') is not None:
            for k in m.get('ApiImportSwaggerFailed'):
                temp_model = ImportSwaggerResponseBodyFailedApiImportSwaggerFailed()
                self.api_import_swagger_failed.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBodyModelFailedApiImportModelFailed(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        group_id: str = None,
        model_name: str = None,
    ):
        self.error_msg = error_msg
        self.group_id = group_id
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class ImportSwaggerResponseBodyModelFailed(TeaModel):
    def __init__(
        self,
        api_import_model_failed: List[ImportSwaggerResponseBodyModelFailedApiImportModelFailed] = None,
    ):
        self.api_import_model_failed = api_import_model_failed

    def validate(self):
        if self.api_import_model_failed:
            for k in self.api_import_model_failed:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportModelFailed'] = []
        if self.api_import_model_failed is not None:
            for k in self.api_import_model_failed:
                result['ApiImportModelFailed'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_model_failed = []
        if m.get('ApiImportModelFailed') is not None:
            for k in m.get('ApiImportModelFailed'):
                temp_model = ImportSwaggerResponseBodyModelFailedApiImportModelFailed()
                self.api_import_model_failed.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        model_name: str = None,
        model_operation: str = None,
        model_uid: str = None,
    ):
        self.group_id = group_id
        self.model_name = model_name
        self.model_operation = model_operation
        self.model_uid = model_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_operation is not None:
            result['ModelOperation'] = self.model_operation
        if self.model_uid is not None:
            result['ModelUid'] = self.model_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelOperation') is not None:
            self.model_operation = m.get('ModelOperation')
        if m.get('ModelUid') is not None:
            self.model_uid = m.get('ModelUid')
        return self


class ImportSwaggerResponseBodyModelSuccess(TeaModel):
    def __init__(
        self,
        api_import_model_success: List[ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess] = None,
    ):
        self.api_import_model_success = api_import_model_success

    def validate(self):
        if self.api_import_model_success:
            for k in self.api_import_model_success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportModelSuccess'] = []
        if self.api_import_model_success is not None:
            for k in self.api_import_model_success:
                result['ApiImportModelSuccess'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_model_success = []
        if m.get('ApiImportModelSuccess') is not None:
            for k in m.get('ApiImportModelSuccess'):
                temp_model = ImportSwaggerResponseBodyModelSuccessApiImportModelSuccess()
                self.api_import_model_success.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess(TeaModel):
    def __init__(
        self,
        api_operation: str = None,
        api_uid: str = None,
        http_method: str = None,
        path: str = None,
    ):
        self.api_operation = api_operation
        self.api_uid = api_uid
        self.http_method = http_method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_operation is not None:
            result['ApiOperation'] = self.api_operation
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.http_method is not None:
            result['HttpMethod'] = self.http_method
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiOperation') is not None:
            self.api_operation = m.get('ApiOperation')
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class ImportSwaggerResponseBodySuccess(TeaModel):
    def __init__(
        self,
        api_import_swagger_success: List[ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess] = None,
    ):
        self.api_import_swagger_success = api_import_swagger_success

    def validate(self):
        if self.api_import_swagger_success:
            for k in self.api_import_swagger_success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiImportSwaggerSuccess'] = []
        if self.api_import_swagger_success is not None:
            for k in self.api_import_swagger_success:
                result['ApiImportSwaggerSuccess'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_swagger_success = []
        if m.get('ApiImportSwaggerSuccess') is not None:
            for k in m.get('ApiImportSwaggerSuccess'):
                temp_model = ImportSwaggerResponseBodySuccessApiImportSwaggerSuccess()
                self.api_import_swagger_success.append(temp_model.from_map(k))
        return self


class ImportSwaggerResponseBody(TeaModel):
    def __init__(
        self,
        failed: ImportSwaggerResponseBodyFailed = None,
        model_failed: ImportSwaggerResponseBodyModelFailed = None,
        model_success: ImportSwaggerResponseBodyModelSuccess = None,
        request_id: str = None,
        success: ImportSwaggerResponseBodySuccess = None,
    ):
        self.failed = failed
        self.model_failed = model_failed
        self.model_success = model_success
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.failed:
            self.failed.validate()
        if self.model_failed:
            self.model_failed.validate()
        if self.model_success:
            self.model_success.validate()
        if self.success:
            self.success.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed.to_map()
        if self.model_failed is not None:
            result['ModelFailed'] = self.model_failed.to_map()
        if self.model_success is not None:
            result['ModelSuccess'] = self.model_success.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            temp_model = ImportSwaggerResponseBodyFailed()
            self.failed = temp_model.from_map(m['Failed'])
        if m.get('ModelFailed') is not None:
            temp_model = ImportSwaggerResponseBodyModelFailed()
            self.model_failed = temp_model.from_map(m['ModelFailed'])
        if m.get('ModelSuccess') is not None:
            temp_model = ImportSwaggerResponseBodyModelSuccess()
            self.model_success = temp_model.from_map(m['ModelSuccess'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            temp_model = ImportSwaggerResponseBodySuccess()
            self.success = temp_model.from_map(m['Success'])
        return self


class ImportSwaggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportSwaggerResponseBody = None,
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
            temp_model = ImportSwaggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiRequest(TeaModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: str = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        open_id_connect_config: str = None,
        request_config: str = None,
        request_paramters: str = None,
        result_body_model: str = None,
        result_descriptions: str = None,
        result_sample: str = None,
        result_type: str = None,
        security_token: str = None,
        service_config: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_id = api_id
        self.api_name = api_name
        self.app_code_auth_type = app_code_auth_type
        self.auth_type = auth_type
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.open_id_connect_config = open_id_connect_config
        self.request_config = request_config
        self.request_paramters = request_paramters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.security_token = security_token
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.visibility = visibility
        self.web_socket_api_type = web_socket_api_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet
        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples
        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample
        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config
        if self.request_paramters is not None:
            result['RequestParamters'] = self.request_paramters
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.web_socket_api_type is not None:
            result['WebSocketApiType'] = self.web_socket_api_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSignatureMethod') is not None:
            self.allow_signature_method = m.get('AllowSignatureMethod')
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AppCodeAuthType') is not None:
            self.app_code_auth_type = m.get('AppCodeAuthType')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            self.error_code_samples = m.get('ErrorCodeSamples')
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OpenIdConnectConfig') is not None:
            self.open_id_connect_config = m.get('OpenIdConnectConfig')
        if m.get('RequestConfig') is not None:
            self.request_config = m.get('RequestConfig')
        if m.get('RequestParamters') is not None:
            self.request_paramters = m.get('RequestParamters')
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            self.result_descriptions = m.get('ResultDescriptions')
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
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
            temp_model = ModifyApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiGroupRequest(TeaModel):
    def __init__(
        self,
        compatible_flags: str = None,
        custom_trace_config: str = None,
        default_domain: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        passthrough_headers: str = None,
        rpc_pattern: str = None,
        security_token: str = None,
        user_log_config: str = None,
    ):
        self.compatible_flags = compatible_flags
        self.custom_trace_config = custom_trace_config
        self.default_domain = default_domain
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.passthrough_headers = passthrough_headers
        self.rpc_pattern = rpc_pattern
        self.security_token = security_token
        self.user_log_config = user_log_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compatible_flags is not None:
            result['CompatibleFlags'] = self.compatible_flags
        if self.custom_trace_config is not None:
            result['CustomTraceConfig'] = self.custom_trace_config
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.passthrough_headers is not None:
            result['PassthroughHeaders'] = self.passthrough_headers
        if self.rpc_pattern is not None:
            result['RpcPattern'] = self.rpc_pattern
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.user_log_config is not None:
            result['UserLogConfig'] = self.user_log_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompatibleFlags') is not None:
            self.compatible_flags = m.get('CompatibleFlags')
        if m.get('CustomTraceConfig') is not None:
            self.custom_trace_config = m.get('CustomTraceConfig')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PassthroughHeaders') is not None:
            self.passthrough_headers = m.get('PassthroughHeaders')
        if m.get('RpcPattern') is not None:
            self.rpc_pattern = m.get('RpcPattern')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('UserLogConfig') is not None:
            self.user_log_config = m.get('UserLogConfig')
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
            temp_model = ModifyApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.description = description
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
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        https_policy: str = None,
        instance_id: str = None,
        instance_name: str = None,
        token: str = None,
    ):
        self.https_policy = https_policy
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceAttributeResponseBody = None,
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
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVpcAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.token = token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ModifyInstanceVpcAttributeResponseBody(TeaModel):
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


class ModifyInstanceVpcAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceVpcAttributeResponseBody = None,
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
            temp_model = ModifyInstanceVpcAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpControlRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        ip_control_id: str = None,
        ip_control_name: str = None,
        security_token: str = None,
    ):
        self.description = description
        self.ip_control_id = ip_control_id
        self.ip_control_name = ip_control_name
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
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyIpControlResponseBody(TeaModel):
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


class ModifyIpControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIpControlResponseBody = None,
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
            temp_model = ModifyIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpControlPolicyItemRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
        ip_control_id: str = None,
        policy_item_id: str = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.cidr_ip = cidr_ip
        self.ip_control_id = ip_control_id
        self.policy_item_id = policy_item_id
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
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyIpControlPolicyItemResponseBody(TeaModel):
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


class ModifyIpControlPolicyItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIpControlPolicyItemResponseBody = None,
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
            temp_model = ModifyIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogConfigRequest(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        security_token: str = None,
        sls_log_store: str = None,
        sls_project: str = None,
    ):
        self.log_type = log_type
        self.security_token = security_token
        self.sls_log_store = sls_log_store
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        return self


class ModifyLogConfigResponseBody(TeaModel):
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


class ModifyLogConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyLogConfigResponseBody = None,
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
            temp_model = ModifyLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecretKeyRequest(TeaModel):
    def __init__(
        self,
        secret_key: str = None,
        secret_key_id: str = None,
        secret_key_name: str = None,
        secret_value: str = None,
        security_token: str = None,
    ):
        self.secret_key = secret_key
        self.secret_key_id = secret_key_id
        self.secret_key_name = secret_key_name
        self.secret_value = secret_value
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = ModifySecretKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTrafficControlRequest(TeaModel):
    def __init__(
        self,
        api_default: int = None,
        app_default: int = None,
        description: str = None,
        security_token: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
        traffic_control_unit: str = None,
        user_default: int = None,
    ):
        self.api_default = api_default
        self.app_default = app_default
        self.description = description
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = ModifyTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReactivateDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReactivateDomainResponseBody(TeaModel):
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


class ReactivateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReactivateDomainResponseBody = None,
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
            temp_model = ReactivateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverApiFromHistoricalRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
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
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
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
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RecoverApiFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryApiDefineFromHistoricalRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
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
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
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
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RecoveryApiDefineFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryApiFromHistoricalRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        history_version: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.history_version = history_version
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
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
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
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RecoveryApiFromHistoricalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDomainRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.app_id = app_id
        self.description = description
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
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RemoveAccessPermissionByApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAccessPermissionByAppsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_ids: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_ids = app_ids
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
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
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
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RemoveAccessPermissionByAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAllBlackListRequest(TeaModel):
    def __init__(
        self,
        black_type: str = None,
        security_token: str = None,
    ):
        self.black_type = black_type
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RemoveApiRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBlackListRequest(TeaModel):
    def __init__(
        self,
        black_content: str = None,
        black_type: str = None,
        security_token: str = None,
    ):
        self.black_content = black_content
        self.black_type = black_type
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackContent') is not None:
            self.black_content = m.get('BlackContent')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = RemoveBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveIpControlApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        ip_control_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.ip_control_id = ip_control_id
        self.security_token = security_token
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
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveIpControlApisResponseBody(TeaModel):
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


class RemoveIpControlApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveIpControlApisResponseBody = None,
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
            temp_model = RemoveIpControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveIpControlPolicyItemRequest(TeaModel):
    def __init__(
        self,
        ip_control_id: str = None,
        policy_item_ids: str = None,
        security_token: str = None,
    ):
        self.ip_control_id = ip_control_id
        self.policy_item_ids = policy_item_ids
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.policy_item_ids is not None:
            result['PolicyItemIds'] = self.policy_item_ids
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('PolicyItemIds') is not None:
            self.policy_item_ids = m.get('PolicyItemIds')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RemoveIpControlPolicyItemResponseBody(TeaModel):
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


class RemoveIpControlPolicyItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveIpControlPolicyItemResponseBody = None,
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
            temp_model = RemoveIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppKeySecretRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        security_token: str = None,
    ):
        self.app_key = app_key
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = ResetAppKeySecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetCustomizedRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.group_id = group_id
        self.security_token = security_token
        self.stage_id = stage_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class ResetCustomizedResponseBodySdkDemosSdkDemo(TeaModel):
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


class ResetCustomizedResponseBodySdkDemos(TeaModel):
    def __init__(
        self,
        sdk_demo: List[ResetCustomizedResponseBodySdkDemosSdkDemo] = None,
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
                temp_model = ResetCustomizedResponseBodySdkDemosSdkDemo()
                self.sdk_demo.append(temp_model.from_map(k))
        return self


class ResetCustomizedResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_demos: ResetCustomizedResponseBodySdkDemos = None,
    ):
        self.request_id = request_id
        self.sdk_demos = sdk_demos

    def validate(self):
        if self.sdk_demos:
            self.sdk_demos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_demos is not None:
            result['SdkDemos'] = self.sdk_demos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkDemos') is not None:
            temp_model = ResetCustomizedResponseBodySdkDemos()
            self.sdk_demos = temp_model.from_map(m['SdkDemos'])
        return self


class ResetCustomizedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetCustomizedResponseBody = None,
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
            temp_model = ResetCustomizedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGenerateRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        group_id: str = None,
        language: str = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.group_id = group_id
        self.language = language
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SdkGenerateResponseBody(TeaModel):
    def __init__(
        self,
        download_link: str = None,
        request_id: str = None,
    ):
        self.download_link = download_link
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SdkGenerateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SdkGenerateResponseBody = None,
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
            temp_model = SdkGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGenerateByAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        language: str = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.language = language
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
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SdkGenerateByAppResponseBody(TeaModel):
    def __init__(
        self,
        download_link: str = None,
        request_id: str = None,
    ):
        self.download_link = download_link
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SdkGenerateByAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SdkGenerateByAppResponseBody = None,
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
            temp_model = SdkGenerateByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SdkGenerateByGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        language: str = None,
        security_token: str = None,
    ):
        self.group_id = group_id
        self.language = language
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
        if self.language is not None:
            result['Language'] = self.language
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SdkGenerateByGroupResponseBody(TeaModel):
    def __init__(
        self,
        download_link: str = None,
        request_id: str = None,
    ):
        self.download_link = download_link
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SdkGenerateByGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SdkGenerateByGroupResponseBody = None,
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
            temp_model = SdkGenerateByGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionByApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        app_id: int = None,
        auth_valid_time: str = None,
        description: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.app_id = app_id
        self.auth_valid_time = auth_valid_time
        self.description = description
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
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auth_valid_time is not None:
            result['AuthValidTime'] = self.auth_valid_time
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AuthValidTime') is not None:
            self.auth_valid_time = m.get('AuthValidTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = SetAccessPermissionByApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAccessPermissionsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_ids: str = None,
        description: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_ids = app_ids
        self.description = description
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
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.description is not None:
            result['Description'] = self.description
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
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = SetAccessPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApiRuleRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        rule_id: str = None,
        rule_type: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.security_token = security_token
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = SetApiRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainRequest(TeaModel):
    def __init__(
        self,
        bind_stage_name: str = None,
        certificate_body: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        group_id: str = None,
        is_force: bool = None,
        private_key: str = None,
        security_token: str = None,
    ):
        self.bind_stage_name = bind_stage_name
        self.certificate_body = certificate_body
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.group_id = group_id
        self.is_force = is_force
        self.private_key = private_key
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_stage_name is not None:
            result['BindStageName'] = self.bind_stage_name
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_force is not None:
            result['IsForce'] = self.is_force
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStageName') is not None:
            self.bind_stage_name = m.get('BindStageName')
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsForce') is not None:
            self.is_force = m.get('IsForce')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDomainResponseBody(TeaModel):
    def __init__(
        self,
        domain_binding_status: str = None,
        domain_legal_status: str = None,
        domain_name: str = None,
        domain_remark: str = None,
        domain_web_socket_status: str = None,
        group_id: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.domain_binding_status = domain_binding_status
        self.domain_legal_status = domain_legal_status
        self.domain_name = domain_name
        self.domain_remark = domain_remark
        self.domain_web_socket_status = domain_web_socket_status
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
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_remark is not None:
            result['DomainRemark'] = self.domain_remark
        if self.domain_web_socket_status is not None:
            result['DomainWebSocketStatus'] = self.domain_web_socket_status
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
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
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
            temp_model = SetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        ca_certificate_body: str = None,
        certificate_body: str = None,
        certificate_name: str = None,
        domain_name: str = None,
        group_id: str = None,
        private_key: str = None,
        security_token: str = None,
    ):
        self.ca_certificate_body = ca_certificate_body
        self.certificate_body = certificate_body
        self.certificate_name = certificate_name
        self.domain_name = domain_name
        self.group_id = group_id
        self.private_key = private_key
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_certificate_body is not None:
            result['CaCertificateBody'] = self.ca_certificate_body
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertificateBody') is not None:
            self.ca_certificate_body = m.get('CaCertificateBody')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = SetDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainWebSocketStatusRequest(TeaModel):
    def __init__(
        self,
        action_value: str = None,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.action_value = action_value
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_value is not None:
            result['ActionValue'] = self.action_value
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionValue') is not None:
            self.action_value = m.get('ActionValue')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class SetDomainWebSocketStatusResponseBody(TeaModel):
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


class SetDomainWebSocketStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDomainWebSocketStatusResponseBody = None,
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
            temp_model = SetDomainWebSocketStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIpControlApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        ip_control_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.ip_control_id = ip_control_id
        self.security_token = security_token
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
        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetIpControlApisResponseBody(TeaModel):
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


class SetIpControlApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetIpControlApisResponseBody = None,
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
            temp_model = SetIpControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMockIntegrationRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        mock: str = None,
        mock_result: str = None,
        security_token: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.mock = mock
        self.mock_result = mock_result
        self.security_token = security_token

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = SetMockIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetWildcardDomainPatternsRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
        wildcard_domain_patterns: str = None,
    ):
        self.domain_name = domain_name
        self.group_id = group_id
        self.security_token = security_token
        self.wildcard_domain_patterns = wildcard_domain_patterns

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.wildcard_domain_patterns is not None:
            result['WildcardDomainPatterns'] = self.wildcard_domain_patterns
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('WildcardDomainPatterns') is not None:
            self.wildcard_domain_patterns = m.get('WildcardDomainPatterns')
        return self


class SetWildcardDomainPatternsResponseBody(TeaModel):
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


class SetWildcardDomainPatternsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetWildcardDomainPatternsResponseBody = None,
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
            temp_model = SetWildcardDomainPatternsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchApiRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        history_version: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.description = description
        self.group_id = group_id
        self.history_version = history_version
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
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
            temp_model = SwitchApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcDescribeAccessesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_port: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.instance_port = instance_port
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        id: str = None,
        instance_id: str = None,
        modified_time: str = None,
        name: str = None,
        port: str = None,
        region_id: str = None,
        status: str = None,
        user_id: str = None,
        vpc_id: str = None,
    ):
        self.created_time = created_time
        self.id = id
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.name = name
        self.port = port
        self.region_id = region_id
        self.status = status
        self.user_id = user_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcDescribeAccessesResponseBodyVpcAccessAttributes(TeaModel):
    def __init__(
        self,
        vpc_access_attribute: List[VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute] = None,
    ):
        self.vpc_access_attribute = vpc_access_attribute

    def validate(self):
        if self.vpc_access_attribute:
            for k in self.vpc_access_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VpcAccessAttribute'] = []
        if self.vpc_access_attribute is not None:
            for k in self.vpc_access_attribute:
                result['VpcAccessAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_access_attribute = []
        if m.get('VpcAccessAttribute') is not None:
            for k in m.get('VpcAccessAttribute'):
                temp_model = VpcDescribeAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute()
                self.vpc_access_attribute.append(temp_model.from_map(k))
        return self


class VpcDescribeAccessesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_access_attributes: VpcDescribeAccessesResponseBodyVpcAccessAttributes = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_access_attributes = vpc_access_attributes

    def validate(self):
        if self.vpc_access_attributes:
            self.vpc_access_attributes.validate()

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
        if self.vpc_access_attributes is not None:
            result['VpcAccessAttributes'] = self.vpc_access_attributes.to_map()
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
        if m.get('VpcAccessAttributes') is not None:
            temp_model = VpcDescribeAccessesResponseBodyVpcAccessAttributes()
            self.vpc_access_attributes = temp_model.from_map(m['VpcAccessAttributes'])
        return self


class VpcDescribeAccessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcDescribeAccessesResponseBody = None,
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
            temp_model = VpcDescribeAccessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcGrantAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_port: str = None,
        name: str = None,
        security_token: str = None,
        token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.instance_port = instance_port
        self.name = name
        self.security_token = security_token
        self.token = token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.name is not None:
            result['Name'] = self.name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcGrantAccessResponseBody(TeaModel):
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


class VpcGrantAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcGrantAccessResponseBody = None,
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
            temp_model = VpcGrantAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcModifyAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_port: str = None,
        security_token: str = None,
        token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.instance_port = instance_port
        self.security_token = security_token
        self.token = token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcModifyAccessResponseBody(TeaModel):
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


class VpcModifyAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcModifyAccessResponseBody = None,
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
            temp_model = VpcModifyAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VpcRevokeAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_port: str = None,
        security_token: str = None,
        token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.instance_port = instance_port
        self.security_token = security_token
        self.token = token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.token is not None:
            result['Token'] = self.token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class VpcRevokeAccessResponseBody(TeaModel):
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


class VpcRevokeAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VpcRevokeAccessResponseBody = None,
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
            temp_model = VpcRevokeAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


