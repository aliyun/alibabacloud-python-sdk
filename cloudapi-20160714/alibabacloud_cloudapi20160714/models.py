# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


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
        body: AbolishApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AbolishApiResponseBody()
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
        body: AddIpControlPolicyItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: AddTrafficSpecialControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddTrafficSpecialControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachPluginRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_ids: str = None,
        group_id: str = None,
        plugin_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.api_ids = api_ids
        self.group_id = group_id
        self.plugin_id = plugin_id
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
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class AttachPluginResponseBody(TeaModel):
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


class AttachPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchAbolishApisRequestApi(TeaModel):
    def __init__(
        self,
        api_uid: str = None,
        group_id: str = None,
        stage_id: str = None,
    ):
        self.api_uid = api_uid
        self.group_id = group_id
        self.stage_id = stage_id

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
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        return self


class BatchAbolishApisRequest(TeaModel):
    def __init__(
        self,
        api: List[BatchAbolishApisRequestApi] = None,
        security_token: str = None,
    ):
        self.api = api
        self.security_token = security_token

    def validate(self):
        if self.api:
            for k in self.api:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Api'] = []
        if self.api is not None:
            for k in self.api:
                result['Api'].append(k.to_map() if k else None)
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api = []
        if m.get('Api') is not None:
            for k in m.get('Api'):
                temp_model = BatchAbolishApisRequestApi()
                self.api.append(temp_model.from_map(k))
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class BatchAbolishApisResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchAbolishApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchAbolishApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchAbolishApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeployApisRequestApi(TeaModel):
    def __init__(
        self,
        api_uid: str = None,
        group_id: str = None,
    ):
        self.api_uid = api_uid
        self.group_id = group_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class BatchDeployApisRequest(TeaModel):
    def __init__(
        self,
        api: List[BatchDeployApisRequestApi] = None,
        description: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api = api
        self.description = description
        self.security_token = security_token
        self.stage_name = stage_name

    def validate(self):
        if self.api:
            for k in self.api:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Api'] = []
        if self.api is not None:
            for k in self.api:
                result['Api'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api = []
        if m.get('Api') is not None:
            for k in m.get('Api'):
                temp_model = BatchDeployApisRequestApi()
                self.api.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class BatchDeployApisResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeployApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeployApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchDeployApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiRequest(TeaModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        constant_parameters: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: str = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        open_id_connect_config: str = None,
        request_config: str = None,
        request_parameters: str = None,
        result_body_model: str = None,
        result_descriptions: str = None,
        result_sample: str = None,
        result_type: str = None,
        security_token: str = None,
        service_config: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        system_parameters: str = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_name = api_name
        self.app_code_auth_type = app_code_auth_type
        self.auth_type = auth_type
        self.constant_parameters = constant_parameters
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.open_id_connect_config = open_id_connect_config
        self.request_config = request_config
        self.request_parameters = request_parameters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.security_token = security_token
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.system_parameters = system_parameters
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
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters
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
        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters
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
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters
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
        if m.get('ConstantParameters') is not None:
            self.constant_parameters = m.get('ConstantParameters')
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
        if m.get('RequestParameters') is not None:
            self.request_parameters = m.get('RequestParameters')
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
        if m.get('SystemParameters') is not None:
            self.system_parameters = m.get('SystemParameters')
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
        body: CreateApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApiGroupRequestTag(TeaModel):
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


class CreateApiGroupRequest(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        group_name: str = None,
        instance_id: str = None,
        security_token: str = None,
        tag: List[CreateApiGroupRequestTag] = None,
    ):
        self.base_path = base_path
        self.description = description
        self.group_name = group_name
        self.instance_id = instance_id
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
        if self.base_path is not None:
            result['BasePath'] = self.base_path
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateApiGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        request_id: str = None,
        sub_domain: str = None,
        tag_status: bool = None,
    ):
        self.base_path = base_path
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.request_id = request_id
        self.sub_domain = sub_domain
        self.tag_status = tag_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_path is not None:
            result['BasePath'] = self.base_path
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
        if self.tag_status is not None:
            result['TagStatus'] = self.tag_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')
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
        if m.get('TagStatus') is not None:
            self.tag_status = m.get('TagStatus')
        return self


class CreateApiGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateApiStageVariableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateApiStageVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequestTag(TeaModel):
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


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        security_token: str = None,
        source: str = None,
        tag: List[CreateAppRequestTag] = None,
    ):
        self.app_name = app_name
        self.description = description
        self.security_token = security_token
        self.source = source
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
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.description is not None:
            result['Description'] = self.description
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.source is not None:
            result['Source'] = self.source
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateAppRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        request_id: str = None,
        tag_status: bool = None,
    ):
        self.app_id = app_id
        self.request_id = request_id
        self.tag_status = tag_status

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
        if self.tag_status is not None:
            result['TagStatus'] = self.tag_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagStatus') is not None:
            self.tag_status = m.get('TagStatus')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        duration: int = None,
        https_policy: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        pricing_cycle: str = None,
        token: str = None,
        zone_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.charge_type = charge_type
        self.duration = duration
        self.https_policy = https_policy
        self.instance_name = instance_name
        self.instance_spec = instance_spec
        self.pricing_cycle = pricing_cycle
        self.token = token
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.token is not None:
            result['Token'] = self.token
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateIntranetDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntranetDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpControlRequestIpControlPolicys(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
    ):
        self.app_id = app_id
        self.cidr_ip = cidr_ip

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
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
        body: CreateIpControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: CreateLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        model_name: str = None,
        schema: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.model_name = model_name
        self.schema = schema

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
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class CreateModelResponseBody(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        model_ref: str = None,
        modified_time: str = None,
        region_id: str = None,
        request_id: str = None,
        schema: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.model_id = model_id
        self.model_name = model_name
        self.model_ref = model_ref
        self.modified_time = modified_time
        self.region_id = region_id
        self.request_id = request_id
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
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.model_ref is not None:
            result['ModelRef'] = self.model_ref
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelRef') is not None:
            self.model_ref = m.get('ModelRef')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class CreateModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMonitorGroupRequest(TeaModel):
    def __init__(
        self,
        auth: str = None,
        group_id: str = None,
        raw_monitor_group_id: int = None,
        security_token: str = None,
    ):
        self.auth = auth
        self.group_id = group_id
        self.raw_monitor_group_id = raw_monitor_group_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth is not None:
            result['Auth'] = self.auth
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.raw_monitor_group_id is not None:
            result['RawMonitorGroupId'] = self.raw_monitor_group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RawMonitorGroupId') is not None:
            self.raw_monitor_group_id = m.get('RawMonitorGroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class CreateMonitorGroupResponseBody(TeaModel):
    def __init__(
        self,
        monitor_group_id: int = None,
        request_id: str = None,
    ):
        self.monitor_group_id = monitor_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_group_id is not None:
            result['MonitorGroupId'] = self.monitor_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorGroupId') is not None:
            self.monitor_group_id = m.get('MonitorGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMonitorGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMonitorGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMonitorGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePluginRequestTag(TeaModel):
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


class CreatePluginRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        plugin_data: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        security_token: str = None,
        tag: List[CreatePluginRequestTag] = None,
    ):
        self.description = description
        self.plugin_data = plugin_data
        self.plugin_name = plugin_name
        self.plugin_type = plugin_type
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
        if self.description is not None:
            result['Description'] = self.description
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PluginData') is not None:
            self.plugin_data = m.get('PluginData')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreatePluginRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreatePluginResponseBody(TeaModel):
    def __init__(
        self,
        plugin_id: str = None,
        request_id: str = None,
        tag_status: bool = None,
    ):
        self.plugin_id = plugin_id
        self.request_id = request_id
        self.tag_status = tag_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_status is not None:
            result['TagStatus'] = self.tag_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagStatus') is not None:
            self.tag_status = m.get('TagStatus')
        return self


class CreatePluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSignatureRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        signature_key: str = None,
        signature_name: str = None,
        signature_secret: str = None,
    ):
        self.security_token = security_token
        self.signature_key = signature_key
        self.signature_name = signature_name
        self.signature_secret = signature_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        if self.signature_secret is not None:
            result['SignatureSecret'] = self.signature_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        if m.get('SignatureSecret') is not None:
            self.signature_secret = m.get('SignatureSecret')
        return self


class CreateSignatureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        self.request_id = request_id
        self.signature_id = signature_id
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        return self


class CreateSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSignatureResponseBody()
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
        body: CreateTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteAllTrafficSpecialControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApiGroupRequestTag(TeaModel):
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


class DeleteApiGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        tag: List[DeleteApiGroupRequestTag] = None,
    ):
        self.group_id = group_id
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DeleteApiGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        body: DeleteApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteApiStageVariableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApiStageVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequestTag(TeaModel):
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


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        security_token: str = None,
        tag: List[DeleteAppRequestTag] = None,
    ):
        self.app_id = app_id
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DeleteAppRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteDomainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequestTag(TeaModel):
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


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tag: List[DeleteInstanceRequestTag] = None,
    ):
        self.instance_id = instance_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DeleteInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DeleteInstanceResponseBody(TeaModel):
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


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
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
        body: DeleteIpControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        model_name: str = None,
    ):
        self.group_id = group_id
        self.model_name = model_name

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        return self


class DeleteModelResponseBody(TeaModel):
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


class DeleteModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePluginRequestTag(TeaModel):
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


class DeletePluginRequest(TeaModel):
    def __init__(
        self,
        plugin_id: str = None,
        security_token: str = None,
        tag: List[DeletePluginRequestTag] = None,
    ):
        self.plugin_id = plugin_id
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
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DeletePluginRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DeletePluginResponseBody(TeaModel):
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


class DeletePluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSignatureRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        signature_id: str = None,
    ):
        self.security_token = security_token
        self.signature_id = signature_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        return self


class DeleteSignatureResponseBody(TeaModel):
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


class DeleteSignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSignatureResponseBody()
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
        body: DeleteTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DeleteTrafficSpecialControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    ):
        self.api_id = api_id
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        body: DeployApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAbolishApiTaskRequest(TeaModel):
    def __init__(
        self,
        operation_uid: str = None,
        security_token: str = None,
    ):
        self.operation_uid = operation_uid
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAbolishApiTaskResponseBodyApiAbolishResultsApiAbolishResult(TeaModel):
    def __init__(
        self,
        abolish_status: str = None,
        api_name: str = None,
        api_uid: str = None,
        error_msg: str = None,
        group_id: str = None,
        group_name: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        self.abolish_status = abolish_status
        self.api_name = api_name
        self.api_uid = api_uid
        self.error_msg = error_msg
        self.group_id = group_id
        self.group_name = group_name
        self.stage_id = stage_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abolish_status is not None:
            result['AbolishStatus'] = self.abolish_status
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbolishStatus') is not None:
            self.abolish_status = m.get('AbolishStatus')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeAbolishApiTaskResponseBodyApiAbolishResults(TeaModel):
    def __init__(
        self,
        api_abolish_result: List[DescribeAbolishApiTaskResponseBodyApiAbolishResultsApiAbolishResult] = None,
    ):
        self.api_abolish_result = api_abolish_result

    def validate(self):
        if self.api_abolish_result:
            for k in self.api_abolish_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiAbolishResult'] = []
        if self.api_abolish_result is not None:
            for k in self.api_abolish_result:
                result['ApiAbolishResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_abolish_result = []
        if m.get('ApiAbolishResult') is not None:
            for k in m.get('ApiAbolishResult'):
                temp_model = DescribeAbolishApiTaskResponseBodyApiAbolishResultsApiAbolishResult()
                self.api_abolish_result.append(temp_model.from_map(k))
        return self


class DescribeAbolishApiTaskResponseBody(TeaModel):
    def __init__(
        self,
        api_abolish_results: DescribeAbolishApiTaskResponseBodyApiAbolishResults = None,
        request_id: str = None,
    ):
        self.api_abolish_results = api_abolish_results
        self.request_id = request_id

    def validate(self):
        if self.api_abolish_results:
            self.api_abolish_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_abolish_results is not None:
            result['ApiAbolishResults'] = self.api_abolish_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiAbolishResults') is not None:
            temp_model = DescribeAbolishApiTaskResponseBodyApiAbolishResults()
            self.api_abolish_results = temp_model.from_map(m['ApiAbolishResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAbolishApiTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAbolishApiTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAbolishApiTaskResponseBody()
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


class DescribeApiResponseBodyRequestParametersRequestParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        array_items_type: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: int = None,
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


class DescribeApiResponseBodyRequestParameters(TeaModel):
    def __init__(
        self,
        request_parameter: List[DescribeApiResponseBodyRequestParametersRequestParameter] = None,
    ):
        self.request_parameter = request_parameter

    def validate(self):
        if self.request_parameter:
            for k in self.request_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParameter'] = []
        if self.request_parameter is not None:
            for k in self.request_parameter:
                result['RequestParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_parameter = []
        if m.get('RequestParameter') is not None:
            for k in m.get('RequestParameter'):
                temp_model = DescribeApiResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyResultDescriptionsResultDescription(TeaModel):
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


class DescribeApiResponseBodyResultDescriptions(TeaModel):
    def __init__(
        self,
        result_description: List[DescribeApiResponseBodyResultDescriptionsResultDescription] = None,
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
                temp_model = DescribeApiResponseBodyResultDescriptionsResultDescription()
                self.result_description.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyServiceConfigFunctionComputeConfig(TeaModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        fc_base_url: str = None,
        fc_type: str = None,
        function_name: str = None,
        method: str = None,
        only_business_path: bool = None,
        path: str = None,
        qualifier: str = None,
        region_id: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.fc_base_url = fc_base_url
        self.fc_type = fc_type
        self.function_name = function_name
        self.method = method
        self.only_business_path = only_business_path
        self.path = path
        self.qualifier = qualifier
        self.region_id = region_id
        self.role_arn = role_arn
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory
        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value
        if self.fc_base_url is not None:
            result['FcBaseUrl'] = self.fc_base_url
        if self.fc_type is not None:
            result['FcType'] = self.fc_type
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.method is not None:
            result['Method'] = self.method
        if self.only_business_path is not None:
            result['OnlyBusinessPath'] = self.only_business_path
        if self.path is not None:
            result['Path'] = self.path
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FcBaseUrl') is not None:
            self.fc_base_url = m.get('FcBaseUrl')
        if m.get('FcType') is not None:
            self.fc_type = m.get('FcType')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('OnlyBusinessPath') is not None:
            self.only_business_path = m.get('OnlyBusinessPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class DescribeApiResponseBodyServiceConfigOssConfig(TeaModel):
    def __init__(
        self,
        action: str = None,
        bucket_name: str = None,
        key: str = None,
        oss_region_id: str = None,
    ):
        self.action = action
        self.bucket_name = bucket_name
        self.key = key
        self.oss_region_id = oss_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.key is not None:
            result['Key'] = self.key
        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')
        return self


class DescribeApiResponseBodyServiceConfigVpcConfig(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
        vpc_scheme: str = None,
    ):
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
        mock: str = None,
        mock_headers: DescribeApiResponseBodyServiceConfigMockHeaders = None,
        mock_result: str = None,
        mock_status_code: int = None,
        oss_config: DescribeApiResponseBodyServiceConfigOssConfig = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        vpc_config: DescribeApiResponseBodyServiceConfigVpcConfig = None,
    ):
        self.aone_app_name = aone_app_name
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.function_compute_config = function_compute_config
        self.mock = mock
        self.mock_headers = mock_headers
        self.mock_result = mock_result
        self.mock_status_code = mock_status_code
        self.oss_config = oss_config
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
        if self.oss_config:
            self.oss_config.validate()
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
        if self.mock is not None:
            result['Mock'] = self.mock
        if self.mock_headers is not None:
            result['MockHeaders'] = self.mock_headers.to_map()
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.mock_status_code is not None:
            result['MockStatusCode'] = self.mock_status_code
        if self.oss_config is not None:
            result['OssConfig'] = self.oss_config.to_map()
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
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockHeaders') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigMockHeaders()
            self.mock_headers = temp_model.from_map(m['MockHeaders'])
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')
        if m.get('OssConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfigOssConfig()
            self.oss_config = temp_model.from_map(m['OssConfig'])
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


class DescribeApiResponseBodyServiceParametersServiceParameter(TeaModel):
    def __init__(
        self,
        location: str = None,
        parameter_type: str = None,
        service_parameter_name: str = None,
    ):
        self.location = location
        self.parameter_type = parameter_type
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiResponseBodyServiceParameters(TeaModel):
    def __init__(
        self,
        service_parameter: List[DescribeApiResponseBodyServiceParametersServiceParameter] = None,
    ):
        self.service_parameter = service_parameter

    def validate(self):
        if self.service_parameter:
            for k in self.service_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParameter'] = []
        if self.service_parameter is not None:
            for k in self.service_parameter:
                result['ServiceParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_parameter = []
        if m.get('ServiceParameter') is not None:
            for k in m.get('ServiceParameter'):
                temp_model = DescribeApiResponseBodyServiceParametersServiceParameter()
                self.service_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiResponseBodyServiceParametersMapServiceParameterMap(TeaModel):
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


class DescribeApiResponseBodyServiceParametersMap(TeaModel):
    def __init__(
        self,
        service_parameter_map: List[DescribeApiResponseBodyServiceParametersMapServiceParameterMap] = None,
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
                temp_model = DescribeApiResponseBodyServiceParametersMapServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k))
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
        region_id: str = None,
        request_config: DescribeApiResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: DescribeApiResponseBodyRequestParameters = None,
        result_body_model: str = None,
        result_descriptions: DescribeApiResponseBodyResultDescriptions = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: DescribeApiResponseBodyServiceConfig = None,
        service_parameters: DescribeApiResponseBodyServiceParameters = None,
        service_parameters_map: DescribeApiResponseBodyServiceParametersMap = None,
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
        self.region_id = region_id
        self.request_config = request_config
        self.request_id = request_id
        self.request_parameters = request_parameters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
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
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters:
            self.request_parameters.validate()
        if self.result_descriptions:
            self.result_descriptions.validate()
        if self.service_config:
            self.service_config.validate()
        if self.service_parameters:
            self.service_parameters.validate()
        if self.service_parameters_map:
            self.service_parameters_map.validate()
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters.to_map()
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters.to_map()
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map.to_map()
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestConfig') is not None:
            temp_model = DescribeApiResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m['RequestConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestParameters') is not None:
            temp_model = DescribeApiResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m['RequestParameters'])
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            temp_model = DescribeApiResponseBodyResultDescriptions()
            self.result_descriptions = temp_model.from_map(m['ResultDescriptions'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            temp_model = DescribeApiResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m['ServiceConfig'])
        if m.get('ServiceParameters') is not None:
            temp_model = DescribeApiResponseBodyServiceParameters()
            self.service_parameters = temp_model.from_map(m['ServiceParameters'])
        if m.get('ServiceParametersMap') is not None:
            temp_model = DescribeApiResponseBodyServiceParametersMap()
            self.service_parameters_map = temp_model.from_map(m['ServiceParametersMap'])
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
        body: DescribeApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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


class DescribeApiDocResponseBodyRequestConfig(TeaModel):
    def __init__(
        self,
        body_format: str = None,
        post_body_description: str = None,
        request_http_method: str = None,
        request_mode: str = None,
        request_path: str = None,
        request_protocol: str = None,
    ):
        self.body_format = body_format
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


class DescribeApiDocResponseBodyRequestParametersRequestParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        array_items_type: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: int = None,
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


class DescribeApiDocResponseBodyRequestParameters(TeaModel):
    def __init__(
        self,
        request_parameter: List[DescribeApiDocResponseBodyRequestParametersRequestParameter] = None,
    ):
        self.request_parameter = request_parameter

    def validate(self):
        if self.request_parameter:
            for k in self.request_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParameter'] = []
        if self.request_parameter is not None:
            for k in self.request_parameter:
                result['RequestParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_parameter = []
        if m.get('RequestParameter') is not None:
            for k in m.get('RequestParameter'):
                temp_model = DescribeApiDocResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k))
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


class DescribeApiDocResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        deployed_time: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: DescribeApiDocResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        request_config: DescribeApiDocResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: DescribeApiDocResponseBodyRequestParameters = None,
        result_descriptions: DescribeApiDocResponseBodyResultDescriptions = None,
        result_sample: str = None,
        result_type: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.deployed_time = deployed_time
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.group_name = group_name
        self.region_id = region_id
        self.request_config = request_config
        self.request_id = request_id
        self.request_parameters = request_parameters
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.stage_name = stage_name
        self.visibility = visibility

    def validate(self):
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters:
            self.request_parameters.validate()
        if self.result_descriptions:
            self.result_descriptions.validate()

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters.to_map()
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
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
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestConfig') is not None:
            temp_model = DescribeApiDocResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m['RequestConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestParameters') is not None:
            temp_model = DescribeApiDocResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m['RequestParameters'])
        if m.get('ResultDescriptions') is not None:
            temp_model = DescribeApiDocResponseBodyResultDescriptions()
            self.result_descriptions = temp_model.from_map(m['ResultDescriptions'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApiDocResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiDocResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiDocResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupRequestTag(TeaModel):
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


class DescribeApiGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        tag: List[DescribeApiGroupRequestTag] = None,
    ):
        self.group_id = group_id
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
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeApiGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeApiGroupResponseBodyCustomDomainsDomainItem(TeaModel):
    def __init__(
        self,
        bind_stage_name: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        custom_domain_type: str = None,
        domain_binding_status: str = None,
        domain_cnamestatus: str = None,
        domain_legal_status: str = None,
        domain_name: str = None,
        domain_remark: str = None,
        domain_web_socket_status: str = None,
        wildcard_domain_patterns: str = None,
    ):
        self.bind_stage_name = bind_stage_name
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.custom_domain_type = custom_domain_type
        self.domain_binding_status = domain_binding_status
        self.domain_cnamestatus = domain_cnamestatus
        self.domain_legal_status = domain_legal_status
        self.domain_name = domain_name
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
        if self.custom_domain_type is not None:
            result['CustomDomainType'] = self.custom_domain_type
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_cnamestatus is not None:
            result['DomainCNAMEStatus'] = self.domain_cnamestatus
        if self.domain_legal_status is not None:
            result['DomainLegalStatus'] = self.domain_legal_status
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
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
        if m.get('CustomDomainType') is not None:
            self.custom_domain_type = m.get('CustomDomainType')
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainCNAMEStatus') is not None:
            self.domain_cnamestatus = m.get('DomainCNAMEStatus')
        if m.get('DomainLegalStatus') is not None:
            self.domain_legal_status = m.get('DomainLegalStatus')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainRemark') is not None:
            self.domain_remark = m.get('DomainRemark')
        if m.get('DomainWebSocketStatus') is not None:
            self.domain_web_socket_status = m.get('DomainWebSocketStatus')
        if m.get('WildcardDomainPatterns') is not None:
            self.wildcard_domain_patterns = m.get('WildcardDomainPatterns')
        return self


class DescribeApiGroupResponseBodyCustomDomains(TeaModel):
    def __init__(
        self,
        domain_item: List[DescribeApiGroupResponseBodyCustomDomainsDomainItem] = None,
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
                temp_model = DescribeApiGroupResponseBodyCustomDomainsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribeApiGroupResponseBodyStageItemsStageInfo(TeaModel):
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


class DescribeApiGroupResponseBodyStageItems(TeaModel):
    def __init__(
        self,
        stage_info: List[DescribeApiGroupResponseBodyStageItemsStageInfo] = None,
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
                temp_model = DescribeApiGroupResponseBodyStageItemsStageInfo()
                self.stage_info.append(temp_model.from_map(k))
        return self


class DescribeApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        billing_status: str = None,
        classic_vpc_sub_domain: str = None,
        cms_monitor_group: str = None,
        compatible_flags: str = None,
        created_time: str = None,
        custom_domains: DescribeApiGroupResponseBodyCustomDomains = None,
        custom_trace_config: str = None,
        customer_configs: str = None,
        default_domain: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        https_policy: str = None,
        illegal_status: str = None,
        instance_id: str = None,
        instance_type: str = None,
        instance_vip_list: str = None,
        ipv_6status: str = None,
        modified_time: str = None,
        passthrough_headers: str = None,
        region_id: str = None,
        request_id: str = None,
        rpc_pattern: str = None,
        stage_items: DescribeApiGroupResponseBodyStageItems = None,
        status: str = None,
        sub_domain: str = None,
        traffic_limit: int = None,
        user_log_config: str = None,
        vpc_domain: str = None,
        vpc_slb_intranet_domain: str = None,
    ):
        self.base_path = base_path
        self.billing_status = billing_status
        self.classic_vpc_sub_domain = classic_vpc_sub_domain
        self.cms_monitor_group = cms_monitor_group
        self.compatible_flags = compatible_flags
        self.created_time = created_time
        self.custom_domains = custom_domains
        self.custom_trace_config = custom_trace_config
        self.customer_configs = customer_configs
        self.default_domain = default_domain
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.https_policy = https_policy
        self.illegal_status = illegal_status
        self.instance_id = instance_id
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
        self.vpc_slb_intranet_domain = vpc_slb_intranet_domain

    def validate(self):
        if self.custom_domains:
            self.custom_domains.validate()
        if self.stage_items:
            self.stage_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_path is not None:
            result['BasePath'] = self.base_path
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status
        if self.classic_vpc_sub_domain is not None:
            result['ClassicVpcSubDomain'] = self.classic_vpc_sub_domain
        if self.cms_monitor_group is not None:
            result['CmsMonitorGroup'] = self.cms_monitor_group
        if self.compatible_flags is not None:
            result['CompatibleFlags'] = self.compatible_flags
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.custom_domains is not None:
            result['CustomDomains'] = self.custom_domains.to_map()
        if self.custom_trace_config is not None:
            result['CustomTraceConfig'] = self.custom_trace_config
        if self.customer_configs is not None:
            result['CustomerConfigs'] = self.customer_configs
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
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
        if self.vpc_slb_intranet_domain is not None:
            result['VpcSlbIntranetDomain'] = self.vpc_slb_intranet_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')
        if m.get('ClassicVpcSubDomain') is not None:
            self.classic_vpc_sub_domain = m.get('ClassicVpcSubDomain')
        if m.get('CmsMonitorGroup') is not None:
            self.cms_monitor_group = m.get('CmsMonitorGroup')
        if m.get('CompatibleFlags') is not None:
            self.compatible_flags = m.get('CompatibleFlags')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CustomDomains') is not None:
            temp_model = DescribeApiGroupResponseBodyCustomDomains()
            self.custom_domains = temp_model.from_map(m['CustomDomains'])
        if m.get('CustomTraceConfig') is not None:
            self.custom_trace_config = m.get('CustomTraceConfig')
        if m.get('CustomerConfigs') is not None:
            self.customer_configs = m.get('CustomerConfigs')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
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
            temp_model = DescribeApiGroupResponseBodyStageItems()
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
        if m.get('VpcSlbIntranetDomain') is not None:
            self.vpc_slb_intranet_domain = m.get('VpcSlbIntranetDomain')
        return self


class DescribeApiGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiGroupVpcWhitelistRequest(TeaModel):
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


class DescribeApiGroupVpcWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_ids: str = None,
    ):
        self.request_id = request_id
        self.vpc_ids = vpc_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        return self


class DescribeApiGroupVpcWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiGroupVpcWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiGroupVpcWhitelistResponseBody()
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
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        sort: str = None,
        tag: List[DescribeApiGroupsRequestTag] = None,
    ):
        self.enable_tag_auth = enable_tag_auth
        self.group_id = group_id
        self.group_name = group_name
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.sort = sort
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sort is not None:
            result['Sort'] = self.sort
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeApiGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttributeTagsTagInfo(TeaModel):
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


class DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttributeTags(TeaModel):
    def __init__(
        self,
        tag_info: List[DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttributeTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttribute(TeaModel):
    def __init__(
        self,
        base_path: str = None,
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
        tags: DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttributeTags = None,
        traffic_limit: int = None,
    ):
        self.base_path = base_path
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
        self.tags = tags
        self.traffic_limit = traffic_limit

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_path is not None:
            result['BasePath'] = self.base_path
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
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.traffic_limit is not None:
            result['TrafficLimit'] = self.traffic_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')
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
        if m.get('Tags') is not None:
            temp_model = DescribeApiGroupsResponseBodyApiGroupAttributesApiGroupAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
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
        body: DescribeApiGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiHistoriesRequest(TeaModel):
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


class DescribeApiHistoriesResponseBodyApiHisItemsApiHisItem(TeaModel):
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


class DescribeApiHistoriesResponseBodyApiHisItems(TeaModel):
    def __init__(
        self,
        api_his_item: List[DescribeApiHistoriesResponseBodyApiHisItemsApiHisItem] = None,
    ):
        self.api_his_item = api_his_item

    def validate(self):
        if self.api_his_item:
            for k in self.api_his_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiHisItem'] = []
        if self.api_his_item is not None:
            for k in self.api_his_item:
                result['ApiHisItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_his_item = []
        if m.get('ApiHisItem') is not None:
            for k in m.get('ApiHisItem'):
                temp_model = DescribeApiHistoriesResponseBodyApiHisItemsApiHisItem()
                self.api_his_item.append(temp_model.from_map(k))
        return self


class DescribeApiHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        api_his_items: DescribeApiHistoriesResponseBodyApiHisItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_his_items = api_his_items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_his_items:
            self.api_his_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_his_items is not None:
            result['ApiHisItems'] = self.api_his_items.to_map()
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
        if m.get('ApiHisItems') is not None:
            temp_model = DescribeApiHistoriesResponseBodyApiHisItems()
            self.api_his_items = temp_model.from_map(m['ApiHisItems'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiHistoryRequest(TeaModel):
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


class DescribeApiHistoryResponseBodyConstantParametersConstantParameter(TeaModel):
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


class DescribeApiHistoryResponseBodyConstantParameters(TeaModel):
    def __init__(
        self,
        constant_parameter: List[DescribeApiHistoryResponseBodyConstantParametersConstantParameter] = None,
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
                temp_model = DescribeApiHistoryResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyCustomSystemParametersCustomSystemParameter(TeaModel):
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


class DescribeApiHistoryResponseBodyCustomSystemParameters(TeaModel):
    def __init__(
        self,
        custom_system_parameter: List[DescribeApiHistoryResponseBodyCustomSystemParametersCustomSystemParameter] = None,
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
                temp_model = DescribeApiHistoryResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyErrorCodeSamplesErrorCodeSample(TeaModel):
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


class DescribeApiHistoryResponseBodyErrorCodeSamples(TeaModel):
    def __init__(
        self,
        error_code_sample: List[DescribeApiHistoryResponseBodyErrorCodeSamplesErrorCodeSample] = None,
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
                temp_model = DescribeApiHistoryResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyOpenIdConnectConfig(TeaModel):
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


class DescribeApiHistoryResponseBodyRequestConfig(TeaModel):
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


class DescribeApiHistoryResponseBodyRequestParametersRequestParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        array_items_type: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: int = None,
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


class DescribeApiHistoryResponseBodyRequestParameters(TeaModel):
    def __init__(
        self,
        request_parameter: List[DescribeApiHistoryResponseBodyRequestParametersRequestParameter] = None,
    ):
        self.request_parameter = request_parameter

    def validate(self):
        if self.request_parameter:
            for k in self.request_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParameter'] = []
        if self.request_parameter is not None:
            for k in self.request_parameter:
                result['RequestParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_parameter = []
        if m.get('RequestParameter') is not None:
            for k in m.get('RequestParameter'):
                temp_model = DescribeApiHistoryResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyResultDescriptionsResultDescription(TeaModel):
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


class DescribeApiHistoryResponseBodyResultDescriptions(TeaModel):
    def __init__(
        self,
        result_description: List[DescribeApiHistoryResponseBodyResultDescriptionsResultDescription] = None,
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
                temp_model = DescribeApiHistoryResponseBodyResultDescriptionsResultDescription()
                self.result_description.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyServiceConfigFunctionComputeConfig(TeaModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        fc_base_url: str = None,
        fc_type: str = None,
        function_name: str = None,
        method: str = None,
        only_business_path: bool = None,
        path: str = None,
        qualifier: str = None,
        region_id: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.fc_base_url = fc_base_url
        self.fc_type = fc_type
        self.function_name = function_name
        self.method = method
        self.only_business_path = only_business_path
        self.path = path
        self.qualifier = qualifier
        self.region_id = region_id
        self.role_arn = role_arn
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory
        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value
        if self.fc_base_url is not None:
            result['FcBaseUrl'] = self.fc_base_url
        if self.fc_type is not None:
            result['FcType'] = self.fc_type
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.method is not None:
            result['Method'] = self.method
        if self.only_business_path is not None:
            result['OnlyBusinessPath'] = self.only_business_path
        if self.path is not None:
            result['Path'] = self.path
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FcBaseUrl') is not None:
            self.fc_base_url = m.get('FcBaseUrl')
        if m.get('FcType') is not None:
            self.fc_type = m.get('FcType')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('OnlyBusinessPath') is not None:
            self.only_business_path = m.get('OnlyBusinessPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeApiHistoryResponseBodyServiceConfigMockHeadersMockHeader(TeaModel):
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


class DescribeApiHistoryResponseBodyServiceConfigMockHeaders(TeaModel):
    def __init__(
        self,
        mock_header: List[DescribeApiHistoryResponseBodyServiceConfigMockHeadersMockHeader] = None,
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
                temp_model = DescribeApiHistoryResponseBodyServiceConfigMockHeadersMockHeader()
                self.mock_header.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyServiceConfigOssConfig(TeaModel):
    def __init__(
        self,
        action: str = None,
        bucket_name: str = None,
        key: str = None,
        oss_region_id: str = None,
    ):
        self.action = action
        self.bucket_name = bucket_name
        self.key = key
        self.oss_region_id = oss_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.key is not None:
            result['Key'] = self.key
        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')
        return self


class DescribeApiHistoryResponseBodyServiceConfigVpcConfig(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
        vpc_scheme: str = None,
    ):
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


class DescribeApiHistoryResponseBodyServiceConfig(TeaModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        function_compute_config: DescribeApiHistoryResponseBodyServiceConfigFunctionComputeConfig = None,
        mock: str = None,
        mock_headers: DescribeApiHistoryResponseBodyServiceConfigMockHeaders = None,
        mock_result: str = None,
        mock_status_code: int = None,
        oss_config: DescribeApiHistoryResponseBodyServiceConfigOssConfig = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        vpc_config: DescribeApiHistoryResponseBodyServiceConfigVpcConfig = None,
        vpc_id: str = None,
    ):
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.function_compute_config = function_compute_config
        self.mock = mock
        self.mock_headers = mock_headers
        self.mock_result = mock_result
        self.mock_status_code = mock_status_code
        self.oss_config = oss_config
        self.service_address = service_address
        self.service_http_method = service_http_method
        self.service_path = service_path
        self.service_protocol = service_protocol
        self.service_timeout = service_timeout
        self.service_vpc_enable = service_vpc_enable
        self.vpc_config = vpc_config
        self.vpc_id = vpc_id

    def validate(self):
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.mock_headers:
            self.mock_headers.validate()
        if self.oss_config:
            self.oss_config.validate()
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
        if self.mock_headers is not None:
            result['MockHeaders'] = self.mock_headers.to_map()
        if self.mock_result is not None:
            result['MockResult'] = self.mock_result
        if self.mock_status_code is not None:
            result['MockStatusCode'] = self.mock_status_code
        if self.oss_config is not None:
            result['OssConfig'] = self.oss_config.to_map()
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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeApiHistoryResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockHeaders') is not None:
            temp_model = DescribeApiHistoryResponseBodyServiceConfigMockHeaders()
            self.mock_headers = temp_model.from_map(m['MockHeaders'])
        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')
        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')
        if m.get('OssConfig') is not None:
            temp_model = DescribeApiHistoryResponseBodyServiceConfigOssConfig()
            self.oss_config = temp_model.from_map(m['OssConfig'])
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
            temp_model = DescribeApiHistoryResponseBodyServiceConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m['VpcConfig'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeApiHistoryResponseBodyServiceParametersServiceParameter(TeaModel):
    def __init__(
        self,
        location: str = None,
        parameter_type: str = None,
        service_parameter_name: str = None,
    ):
        self.location = location
        self.parameter_type = parameter_type
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeApiHistoryResponseBodyServiceParameters(TeaModel):
    def __init__(
        self,
        service_parameter: List[DescribeApiHistoryResponseBodyServiceParametersServiceParameter] = None,
    ):
        self.service_parameter = service_parameter

    def validate(self):
        if self.service_parameter:
            for k in self.service_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParameter'] = []
        if self.service_parameter is not None:
            for k in self.service_parameter:
                result['ServiceParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_parameter = []
        if m.get('ServiceParameter') is not None:
            for k in m.get('ServiceParameter'):
                temp_model = DescribeApiHistoryResponseBodyServiceParametersServiceParameter()
                self.service_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodyServiceParametersMapServiceParameterMap(TeaModel):
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


class DescribeApiHistoryResponseBodyServiceParametersMap(TeaModel):
    def __init__(
        self,
        service_parameter_map: List[DescribeApiHistoryResponseBodyServiceParametersMapServiceParameterMap] = None,
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
                temp_model = DescribeApiHistoryResponseBodyServiceParametersMapServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBodySystemParametersSystemParameter(TeaModel):
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


class DescribeApiHistoryResponseBodySystemParameters(TeaModel):
    def __init__(
        self,
        system_parameter: List[DescribeApiHistoryResponseBodySystemParametersSystemParameter] = None,
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
                temp_model = DescribeApiHistoryResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k))
        return self


class DescribeApiHistoryResponseBody(TeaModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        constant_parameters: DescribeApiHistoryResponseBodyConstantParameters = None,
        custom_system_parameters: DescribeApiHistoryResponseBodyCustomSystemParameters = None,
        deployed_time: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: DescribeApiHistoryResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        history_version: str = None,
        open_id_connect_config: DescribeApiHistoryResponseBodyOpenIdConnectConfig = None,
        region_id: str = None,
        request_config: DescribeApiHistoryResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: DescribeApiHistoryResponseBodyRequestParameters = None,
        result_body_model: str = None,
        result_descriptions: DescribeApiHistoryResponseBodyResultDescriptions = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: DescribeApiHistoryResponseBodyServiceConfig = None,
        service_parameters: DescribeApiHistoryResponseBodyServiceParameters = None,
        service_parameters_map: DescribeApiHistoryResponseBodyServiceParametersMap = None,
        stage_name: str = None,
        status: str = None,
        system_parameters: DescribeApiHistoryResponseBodySystemParameters = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_id = api_id
        self.api_name = api_name
        self.app_code_auth_type = app_code_auth_type
        self.auth_type = auth_type
        self.constant_parameters = constant_parameters
        self.custom_system_parameters = custom_system_parameters
        self.deployed_time = deployed_time
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.group_name = group_name
        self.history_version = history_version
        self.open_id_connect_config = open_id_connect_config
        self.region_id = region_id
        self.request_config = request_config
        self.request_id = request_id
        self.request_parameters = request_parameters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.stage_name = stage_name
        self.status = status
        self.system_parameters = system_parameters
        self.visibility = visibility
        self.web_socket_api_type = web_socket_api_type

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.custom_system_parameters:
            self.custom_system_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.open_id_connect_config:
            self.open_id_connect_config.validate()
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters:
            self.request_parameters.validate()
        if self.result_descriptions:
            self.result_descriptions.validate()
        if self.service_config:
            self.service_config.validate()
        if self.service_parameters:
            self.service_parameters.validate()
        if self.service_parameters_map:
            self.service_parameters_map.validate()
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
        if self.custom_system_parameters is not None:
            result['CustomSystemParameters'] = self.custom_system_parameters.to_map()
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
        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters.to_map()
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters.to_map()
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map.to_map()
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.status is not None:
            result['Status'] = self.status
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
            temp_model = DescribeApiHistoryResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('CustomSystemParameters') is not None:
            temp_model = DescribeApiHistoryResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m['CustomSystemParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeApiHistoryResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')
        if m.get('OpenIdConnectConfig') is not None:
            temp_model = DescribeApiHistoryResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m['OpenIdConnectConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestConfig') is not None:
            temp_model = DescribeApiHistoryResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m['RequestConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestParameters') is not None:
            temp_model = DescribeApiHistoryResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m['RequestParameters'])
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            temp_model = DescribeApiHistoryResponseBodyResultDescriptions()
            self.result_descriptions = temp_model.from_map(m['ResultDescriptions'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            temp_model = DescribeApiHistoryResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m['ServiceConfig'])
        if m.get('ServiceParameters') is not None:
            temp_model = DescribeApiHistoryResponseBodyServiceParameters()
            self.service_parameters = temp_model.from_map(m['ServiceParameters'])
        if m.get('ServiceParametersMap') is not None:
            temp_model = DescribeApiHistoryResponseBodyServiceParametersMap()
            self.service_parameters_map = temp_model.from_map(m['ServiceParametersMap'])
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeApiHistoryResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')
        return self


class DescribeApiHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiHistoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiHistoryResponseBody()
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
        body: DescribeApiIpControlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiIpControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiLatencyDataRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name
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
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
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
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiLatencyDataResponseBodyCallLatencysMonitorItem(TeaModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        self.item_time = item_time
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_time is not None:
            result['ItemTime'] = self.item_time
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        return self


class DescribeApiLatencyDataResponseBodyCallLatencys(TeaModel):
    def __init__(
        self,
        monitor_item: List[DescribeApiLatencyDataResponseBodyCallLatencysMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for k in self.monitor_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k in self.monitor_item:
                result['MonitorItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k in m.get('MonitorItem'):
                temp_model = DescribeApiLatencyDataResponseBodyCallLatencysMonitorItem()
                self.monitor_item.append(temp_model.from_map(k))
        return self


class DescribeApiLatencyDataResponseBody(TeaModel):
    def __init__(
        self,
        call_latencys: DescribeApiLatencyDataResponseBodyCallLatencys = None,
        request_id: str = None,
    ):
        self.call_latencys = call_latencys
        self.request_id = request_id

    def validate(self):
        if self.call_latencys:
            self.call_latencys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_latencys is not None:
            result['CallLatencys'] = self.call_latencys.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallLatencys') is not None:
            temp_model = DescribeApiLatencyDataResponseBodyCallLatencys()
            self.call_latencys = temp_model.from_map(m['CallLatencys'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiLatencyDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiLatencyDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiLatencyDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiMarketAttributesRequest(TeaModel):
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


class DescribeApiMarketAttributesResponseBody(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        market_charging_mode: str = None,
        need_charging: str = None,
        request_id: str = None,
    ):
        self.api_id = api_id
        self.market_charging_mode = market_charging_mode
        self.need_charging = need_charging
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
        if self.market_charging_mode is not None:
            result['MarketChargingMode'] = self.market_charging_mode
        if self.need_charging is not None:
            result['NeedCharging'] = self.need_charging
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('MarketChargingMode') is not None:
            self.market_charging_mode = m.get('MarketChargingMode')
        if m.get('NeedCharging') is not None:
            self.need_charging = m.get('NeedCharging')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiMarketAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiMarketAttributesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiMarketAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiQpsDataRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name
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
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
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
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiQpsDataResponseBodyCallFailsMonitorItem(TeaModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        self.item_time = item_time
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_time is not None:
            result['ItemTime'] = self.item_time
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        return self


class DescribeApiQpsDataResponseBodyCallFails(TeaModel):
    def __init__(
        self,
        monitor_item: List[DescribeApiQpsDataResponseBodyCallFailsMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for k in self.monitor_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k in self.monitor_item:
                result['MonitorItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k in m.get('MonitorItem'):
                temp_model = DescribeApiQpsDataResponseBodyCallFailsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k))
        return self


class DescribeApiQpsDataResponseBodyCallSuccessesMonitorItem(TeaModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        self.item_time = item_time
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_time is not None:
            result['ItemTime'] = self.item_time
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        return self


class DescribeApiQpsDataResponseBodyCallSuccesses(TeaModel):
    def __init__(
        self,
        monitor_item: List[DescribeApiQpsDataResponseBodyCallSuccessesMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for k in self.monitor_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k in self.monitor_item:
                result['MonitorItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k in m.get('MonitorItem'):
                temp_model = DescribeApiQpsDataResponseBodyCallSuccessesMonitorItem()
                self.monitor_item.append(temp_model.from_map(k))
        return self


class DescribeApiQpsDataResponseBody(TeaModel):
    def __init__(
        self,
        call_fails: DescribeApiQpsDataResponseBodyCallFails = None,
        call_successes: DescribeApiQpsDataResponseBodyCallSuccesses = None,
        request_id: str = None,
    ):
        self.call_fails = call_fails
        self.call_successes = call_successes
        self.request_id = request_id

    def validate(self):
        if self.call_fails:
            self.call_fails.validate()
        if self.call_successes:
            self.call_successes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_fails is not None:
            result['CallFails'] = self.call_fails.to_map()
        if self.call_successes is not None:
            result['CallSuccesses'] = self.call_successes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallFails') is not None:
            temp_model = DescribeApiQpsDataResponseBodyCallFails()
            self.call_fails = temp_model.from_map(m['CallFails'])
        if m.get('CallSuccesses') is not None:
            temp_model = DescribeApiQpsDataResponseBodyCallSuccesses()
            self.call_successes = temp_model.from_map(m['CallSuccesses'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiQpsDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiQpsDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiQpsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiSignaturesRequest(TeaModel):
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


class DescribeApiSignaturesResponseBodyApiSignaturesApiSignatureItem(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.bound_time = bound_time
        self.signature_id = signature_id
        self.signature_name = signature_name

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
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        return self


class DescribeApiSignaturesResponseBodyApiSignatures(TeaModel):
    def __init__(
        self,
        api_signature_item: List[DescribeApiSignaturesResponseBodyApiSignaturesApiSignatureItem] = None,
    ):
        self.api_signature_item = api_signature_item

    def validate(self):
        if self.api_signature_item:
            for k in self.api_signature_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiSignatureItem'] = []
        if self.api_signature_item is not None:
            for k in self.api_signature_item:
                result['ApiSignatureItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_signature_item = []
        if m.get('ApiSignatureItem') is not None:
            for k in m.get('ApiSignatureItem'):
                temp_model = DescribeApiSignaturesResponseBodyApiSignaturesApiSignatureItem()
                self.api_signature_item.append(temp_model.from_map(k))
        return self


class DescribeApiSignaturesResponseBody(TeaModel):
    def __init__(
        self,
        api_signatures: DescribeApiSignaturesResponseBodyApiSignatures = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_signatures = api_signatures
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_signatures:
            self.api_signatures.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_signatures is not None:
            result['ApiSignatures'] = self.api_signatures.to_map()
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
        if m.get('ApiSignatures') is not None:
            temp_model = DescribeApiSignaturesResponseBodyApiSignatures()
            self.api_signatures = temp_model.from_map(m['ApiSignatures'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiSignaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiSignaturesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiSignaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiTrafficControlsRequest(TeaModel):
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


class DescribeApiTrafficControlsResponseBodyApiTrafficControlsApiTrafficControlItem(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.bound_time = bound_time
        self.traffic_control_id = traffic_control_id
        self.traffic_control_name = traffic_control_name

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
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')
        return self


class DescribeApiTrafficControlsResponseBodyApiTrafficControls(TeaModel):
    def __init__(
        self,
        api_traffic_control_item: List[DescribeApiTrafficControlsResponseBodyApiTrafficControlsApiTrafficControlItem] = None,
    ):
        self.api_traffic_control_item = api_traffic_control_item

    def validate(self):
        if self.api_traffic_control_item:
            for k in self.api_traffic_control_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiTrafficControlItem'] = []
        if self.api_traffic_control_item is not None:
            for k in self.api_traffic_control_item:
                result['ApiTrafficControlItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_traffic_control_item = []
        if m.get('ApiTrafficControlItem') is not None:
            for k in m.get('ApiTrafficControlItem'):
                temp_model = DescribeApiTrafficControlsResponseBodyApiTrafficControlsApiTrafficControlItem()
                self.api_traffic_control_item.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficControlsResponseBody(TeaModel):
    def __init__(
        self,
        api_traffic_controls: DescribeApiTrafficControlsResponseBodyApiTrafficControls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_traffic_controls = api_traffic_controls
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_traffic_controls:
            self.api_traffic_controls.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_traffic_controls is not None:
            result['ApiTrafficControls'] = self.api_traffic_controls.to_map()
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
        if m.get('ApiTrafficControls') is not None:
            temp_model = DescribeApiTrafficControlsResponseBodyApiTrafficControls()
            self.api_traffic_controls = temp_model.from_map(m['ApiTrafficControls'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApiTrafficControlsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiTrafficControlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiTrafficControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApiTrafficDataRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        end_time: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        start_time: str = None,
    ):
        self.api_id = api_id
        self.end_time = end_time
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name
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
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
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
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeApiTrafficDataResponseBodyCallDownloadsMonitorItem(TeaModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        self.item_time = item_time
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_time is not None:
            result['ItemTime'] = self.item_time
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        return self


class DescribeApiTrafficDataResponseBodyCallDownloads(TeaModel):
    def __init__(
        self,
        monitor_item: List[DescribeApiTrafficDataResponseBodyCallDownloadsMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for k in self.monitor_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k in self.monitor_item:
                result['MonitorItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k in m.get('MonitorItem'):
                temp_model = DescribeApiTrafficDataResponseBodyCallDownloadsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficDataResponseBodyCallUploadsMonitorItem(TeaModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        self.item_time = item_time
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_time is not None:
            result['ItemTime'] = self.item_time
        if self.item_value is not None:
            result['ItemValue'] = self.item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')
        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')
        return self


class DescribeApiTrafficDataResponseBodyCallUploads(TeaModel):
    def __init__(
        self,
        monitor_item: List[DescribeApiTrafficDataResponseBodyCallUploadsMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for k in self.monitor_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k in self.monitor_item:
                result['MonitorItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k in m.get('MonitorItem'):
                temp_model = DescribeApiTrafficDataResponseBodyCallUploadsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k))
        return self


class DescribeApiTrafficDataResponseBody(TeaModel):
    def __init__(
        self,
        call_downloads: DescribeApiTrafficDataResponseBodyCallDownloads = None,
        call_uploads: DescribeApiTrafficDataResponseBodyCallUploads = None,
        request_id: str = None,
    ):
        self.call_downloads = call_downloads
        self.call_uploads = call_uploads
        self.request_id = request_id

    def validate(self):
        if self.call_downloads:
            self.call_downloads.validate()
        if self.call_uploads:
            self.call_uploads.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_downloads is not None:
            result['CallDownloads'] = self.call_downloads.to_map()
        if self.call_uploads is not None:
            result['CallUploads'] = self.call_uploads.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallDownloads') is not None:
            temp_model = DescribeApiTrafficDataResponseBodyCallDownloads()
            self.call_downloads = temp_model.from_map(m['CallDownloads'])
        if m.get('CallUploads') is not None:
            temp_model = DescribeApiTrafficDataResponseBodyCallUploads()
            self.call_uploads = temp_model.from_map(m['CallUploads'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeApiTrafficDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApiTrafficDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApiTrafficDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisRequestTag(TeaModel):
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


class DescribeApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        catalog_id: str = None,
        enable_tag_auth: bool = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        tag: List[DescribeApisRequestTag] = None,
        visibility: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.catalog_id = catalog_id
        self.enable_tag_auth = enable_tag_auth
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.tag = tag
        self.visibility = visibility

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
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id
        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth
        if self.group_id is not None:
            result['GroupId'] = self.group_id
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
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')
        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeApisRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeApisResponseBodyApiSummarysApiSummary(TeaModel):
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


class DescribeApisResponseBodyApiSummarys(TeaModel):
    def __init__(
        self,
        api_summary: List[DescribeApisResponseBodyApiSummarysApiSummary] = None,
    ):
        self.api_summary = api_summary

    def validate(self):
        if self.api_summary:
            for k in self.api_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiSummary'] = []
        if self.api_summary is not None:
            for k in self.api_summary:
                result['ApiSummary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_summary = []
        if m.get('ApiSummary') is not None:
            for k in m.get('ApiSummary'):
                temp_model = DescribeApisResponseBodyApiSummarysApiSummary()
                self.api_summary.append(temp_model.from_map(k))
        return self


class DescribeApisResponseBody(TeaModel):
    def __init__(
        self,
        api_summarys: DescribeApisResponseBodyApiSummarys = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_summarys = api_summarys
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_summarys:
            self.api_summarys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_summarys is not None:
            result['ApiSummarys'] = self.api_summarys.to_map()
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
        if m.get('ApiSummarys') is not None:
            temp_model = DescribeApisResponseBodyApiSummarys()
            self.api_summarys = temp_model.from_map(m['ApiSummarys'])
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
        body: DescribeApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByAppRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_uid: str = None,
        app_id: int = None,
        method: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        security_token: str = None,
    ):
        # API名称
        self.api_name = api_name
        # API的ID
        self.api_uid = api_uid
        # APP的ID
        self.app_id = app_id
        # API的请求HTTP Method
        self.method = method
        # 当前页码
        self.page_number = page_number
        # 每页条目
        self.page_size = page_size
        # API请求路径
        self.path = path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.method is not None:
            result['Method'] = self.method
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
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
        method: str = None,
        operator: str = None,
        path: str = None,
        region_id: str = None,
        stage_name: str = None,
    ):
        # API的ID
        self.api_id = api_id
        # API名称
        self.api_name = api_name
        # 授权有效时间
        self.auth_vaild_time = auth_vaild_time
        # 授权来源
        self.authorization_source = authorization_source
        # 授权时间
        self.created_time = created_time
        # 描述
        self.description = description
        # 分组ID
        self.group_id = group_id
        # 分组名称
        self.group_name = group_name
        # API的请求HTTP Method
        self.method = method
        self.operator = operator
        # API的请求路径
        self.path = path
        # 地区ID
        self.region_id = region_id
        # 环境名称
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
        if self.method is not None:
            result['Method'] = self.method
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.path is not None:
            result['Path'] = self.path
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
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Path') is not None:
            self.path = m.get('Path')
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
        # 当前页码
        self.page_number = page_number
        # 每页条目
        self.page_size = page_size
        # 请求ID
        self.request_id = request_id
        # 总条目数
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
        body: DescribeApisByAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DescribeApisByIpControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApisByIpControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisBySignatureRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        signature_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.signature_id = signature_id

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
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        return self


class DescribeApisBySignatureResponseBodyApiInfosApiInfo(TeaModel):
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


class DescribeApisBySignatureResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApisBySignatureResponseBodyApiInfosApiInfo] = None,
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
                temp_model = DescribeApisBySignatureResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisBySignatureResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApisBySignatureResponseBodyApiInfos = None,
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
            temp_model = DescribeApisBySignatureResponseBodyApiInfos()
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


class DescribeApisBySignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApisBySignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApisBySignatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApisByTrafficControlRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        traffic_control_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.traffic_control_id = traffic_control_id

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
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class DescribeApisByTrafficControlResponseBodyApiInfosApiInfo(TeaModel):
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


class DescribeApisByTrafficControlResponseBodyApiInfos(TeaModel):
    def __init__(
        self,
        api_info: List[DescribeApisByTrafficControlResponseBodyApiInfosApiInfo] = None,
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
                temp_model = DescribeApisByTrafficControlResponseBodyApiInfosApiInfo()
                self.api_info.append(temp_model.from_map(k))
        return self


class DescribeApisByTrafficControlResponseBody(TeaModel):
    def __init__(
        self,
        api_infos: DescribeApisByTrafficControlResponseBodyApiInfos = None,
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
            temp_model = DescribeApisByTrafficControlResponseBodyApiInfos()
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


class DescribeApisByTrafficControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApisByTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApisByTrafficControlResponseBody()
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
        body: DescribeAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppAttributesRequestTag(TeaModel):
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


class DescribeAppAttributesRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_id: int = None,
        app_key: str = None,
        app_name: str = None,
        enable_tag_auth: bool = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        sort: str = None,
        tag: List[DescribeAppAttributesRequestTag] = None,
    ):
        self.app_code = app_code
        self.app_id = app_id
        self.app_key = app_key
        self.app_name = app_name
        self.enable_tag_auth = enable_tag_auth
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.sort = sort
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
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
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
        if self.sort is not None:
            result['Sort'] = self.sort
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
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
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeAppAttributesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeAppAttributesResponseBodyAppsAppAttributeTagsTagInfo(TeaModel):
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


class DescribeAppAttributesResponseBodyAppsAppAttributeTags(TeaModel):
    def __init__(
        self,
        tag_info: List[DescribeAppAttributesResponseBodyAppsAppAttributeTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = DescribeAppAttributesResponseBodyAppsAppAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class DescribeAppAttributesResponseBodyAppsAppAttribute(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        tags: DescribeAppAttributesResponseBodyAppsAppAttributeTags = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

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
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
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
        if m.get('Tags') is not None:
            temp_model = DescribeAppAttributesResponseBodyAppsAppAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribeAppAttributesResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_attribute: List[DescribeAppAttributesResponseBodyAppsAppAttribute] = None,
    ):
        self.app_attribute = app_attribute

    def validate(self):
        if self.app_attribute:
            for k in self.app_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppAttribute'] = []
        if self.app_attribute is not None:
            for k in self.app_attribute:
                result['AppAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_attribute = []
        if m.get('AppAttribute') is not None:
            for k in m.get('AppAttribute'):
                temp_model = DescribeAppAttributesResponseBodyAppsAppAttribute()
                self.app_attribute.append(temp_model.from_map(k))
        return self


class DescribeAppAttributesResponseBody(TeaModel):
    def __init__(
        self,
        apps: DescribeAppAttributesResponseBodyApps = None,
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
            temp_model = DescribeAppAttributesResponseBodyApps()
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


class DescribeAppAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAppAttributesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppSecurityRequestTag(TeaModel):
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


class DescribeAppSecurityRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        security_token: str = None,
        tag: List[DescribeAppSecurityRequestTag] = None,
    ):
        self.app_id = app_id
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeAppSecurityRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        body: DescribeAppSecurityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppSecurityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppsRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_owner: int = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        self.app_id = app_id
        self.app_owner = app_owner
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
        if self.app_owner is not None:
            result['AppOwner'] = self.app_owner
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
        if m.get('AppOwner') is not None:
            self.app_owner = m.get('AppOwner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeAppsResponseBodyAppsAppItem(TeaModel):
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


class DescribeAppsResponseBodyApps(TeaModel):
    def __init__(
        self,
        app_item: List[DescribeAppsResponseBodyAppsAppItem] = None,
    ):
        self.app_item = app_item

    def validate(self):
        if self.app_item:
            for k in self.app_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppItem'] = []
        if self.app_item is not None:
            for k in self.app_item:
                result['AppItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_item = []
        if m.get('AppItem') is not None:
            for k in m.get('AppItem'):
                temp_model = DescribeAppsResponseBodyAppsAppItem()
                self.app_item.append(temp_model.from_map(k))
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
        body: DescribeAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuthorizedApisRequest(TeaModel):
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


class DescribeAuthorizedApisResponseBodyAuthorizedApisAuthorizedApi(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_vaild_time: str = None,
        authorization_source: str = None,
        authorized_time: str = None,
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
        self.authorized_time = authorized_time
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
        if self.authorized_time is not None:
            result['AuthorizedTime'] = self.authorized_time
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
        if m.get('AuthorizedTime') is not None:
            self.authorized_time = m.get('AuthorizedTime')
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


class DescribeAuthorizedApisResponseBodyAuthorizedApis(TeaModel):
    def __init__(
        self,
        authorized_api: List[DescribeAuthorizedApisResponseBodyAuthorizedApisAuthorizedApi] = None,
    ):
        self.authorized_api = authorized_api

    def validate(self):
        if self.authorized_api:
            for k in self.authorized_api:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedApi'] = []
        if self.authorized_api is not None:
            for k in self.authorized_api:
                result['AuthorizedApi'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_api = []
        if m.get('AuthorizedApi') is not None:
            for k in m.get('AuthorizedApi'):
                temp_model = DescribeAuthorizedApisResponseBodyAuthorizedApisAuthorizedApi()
                self.authorized_api.append(temp_model.from_map(k))
        return self


class DescribeAuthorizedApisResponseBody(TeaModel):
    def __init__(
        self,
        authorized_apis: DescribeAuthorizedApisResponseBodyAuthorizedApis = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorized_apis = authorized_apis
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorized_apis:
            self.authorized_apis.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_apis is not None:
            result['AuthorizedApis'] = self.authorized_apis.to_map()
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
        if m.get('AuthorizedApis') is not None:
            temp_model = DescribeAuthorizedApisResponseBodyAuthorizedApis()
            self.authorized_apis = temp_model.from_map(m['AuthorizedApis'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuthorizedApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAuthorizedApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAuthorizedApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuthorizedAppsRequest(TeaModel):
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


class DescribeAuthorizedAppsResponseBodyAuthorizedAppsAuthorizedApp(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        auth_vaild_time: str = None,
        authorization_source: str = None,
        authorized_time: str = None,
        description: str = None,
        operator: str = None,
        stage_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.auth_vaild_time = auth_vaild_time
        self.authorization_source = authorization_source
        self.authorized_time = authorized_time
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
        if self.authorized_time is not None:
            result['AuthorizedTime'] = self.authorized_time
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
        if m.get('AuthorizedTime') is not None:
            self.authorized_time = m.get('AuthorizedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeAuthorizedAppsResponseBodyAuthorizedApps(TeaModel):
    def __init__(
        self,
        authorized_app: List[DescribeAuthorizedAppsResponseBodyAuthorizedAppsAuthorizedApp] = None,
    ):
        self.authorized_app = authorized_app

    def validate(self):
        if self.authorized_app:
            for k in self.authorized_app:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedApp'] = []
        if self.authorized_app is not None:
            for k in self.authorized_app:
                result['AuthorizedApp'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_app = []
        if m.get('AuthorizedApp') is not None:
            for k in m.get('AuthorizedApp'):
                temp_model = DescribeAuthorizedAppsResponseBodyAuthorizedAppsAuthorizedApp()
                self.authorized_app.append(temp_model.from_map(k))
        return self


class DescribeAuthorizedAppsResponseBody(TeaModel):
    def __init__(
        self,
        authorized_apps: DescribeAuthorizedAppsResponseBodyAuthorizedApps = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authorized_apps = authorized_apps
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authorized_apps:
            self.authorized_apps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_apps is not None:
            result['AuthorizedApps'] = self.authorized_apps.to_map()
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
        if m.get('AuthorizedApps') is not None:
            temp_model = DescribeAuthorizedAppsResponseBodyAuthorizedApps()
            self.authorized_apps = temp_model.from_map(m['AuthorizedApps'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuthorizedAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAuthorizedAppsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAuthorizedAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployApiTaskRequest(TeaModel):
    def __init__(
        self,
        operation_uid: str = None,
        security_token: str = None,
    ):
        self.operation_uid = operation_uid
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeDeployApiTaskResponseBodyDeployedResultsDeployedResult(TeaModel):
    def __init__(
        self,
        api_uid: str = None,
        deployed_status: str = None,
        error_msg: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        self.api_uid = api_uid
        self.deployed_status = deployed_status
        self.error_msg = error_msg
        self.group_id = group_id
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class DescribeDeployApiTaskResponseBodyDeployedResults(TeaModel):
    def __init__(
        self,
        deployed_result: List[DescribeDeployApiTaskResponseBodyDeployedResultsDeployedResult] = None,
    ):
        self.deployed_result = deployed_result

    def validate(self):
        if self.deployed_result:
            for k in self.deployed_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeployedResult'] = []
        if self.deployed_result is not None:
            for k in self.deployed_result:
                result['DeployedResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_result = []
        if m.get('DeployedResult') is not None:
            for k in m.get('DeployedResult'):
                temp_model = DescribeDeployApiTaskResponseBodyDeployedResultsDeployedResult()
                self.deployed_result.append(temp_model.from_map(k))
        return self


class DescribeDeployApiTaskResponseBody(TeaModel):
    def __init__(
        self,
        deployed_results: DescribeDeployApiTaskResponseBodyDeployedResults = None,
        request_id: str = None,
    ):
        self.deployed_results = deployed_results
        self.request_id = request_id

    def validate(self):
        if self.deployed_results:
            self.deployed_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_results is not None:
            result['DeployedResults'] = self.deployed_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployedResults') is not None:
            temp_model = DescribeDeployApiTaskResponseBodyDeployedResults()
            self.deployed_results = temp_model.from_map(m['DeployedResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDeployApiTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeployApiTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDeployApiTaskResponseBody()
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


class DescribeDeployedApiResponseBodyCustomSystemParametersCustomSystemParameter(TeaModel):
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


class DescribeDeployedApiResponseBodyCustomSystemParameters(TeaModel):
    def __init__(
        self,
        custom_system_parameter: List[DescribeDeployedApiResponseBodyCustomSystemParametersCustomSystemParameter] = None,
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
                temp_model = DescribeDeployedApiResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k))
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


class DescribeDeployedApiResponseBodyOpenIdConnectConfig(TeaModel):
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


class DescribeDeployedApiResponseBodyRequestConfig(TeaModel):
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


class DescribeDeployedApiResponseBodyRequestParametersRequestParameter(TeaModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        array_items_type: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: int = None,
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


class DescribeDeployedApiResponseBodyRequestParameters(TeaModel):
    def __init__(
        self,
        request_parameter: List[DescribeDeployedApiResponseBodyRequestParametersRequestParameter] = None,
    ):
        self.request_parameter = request_parameter

    def validate(self):
        if self.request_parameter:
            for k in self.request_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RequestParameter'] = []
        if self.request_parameter is not None:
            for k in self.request_parameter:
                result['RequestParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_parameter = []
        if m.get('RequestParameter') is not None:
            for k in m.get('RequestParameter'):
                temp_model = DescribeDeployedApiResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyResultDescriptionsResultDescription(TeaModel):
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


class DescribeDeployedApiResponseBodyResultDescriptions(TeaModel):
    def __init__(
        self,
        result_description: List[DescribeDeployedApiResponseBodyResultDescriptionsResultDescription] = None,
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
                temp_model = DescribeDeployedApiResponseBodyResultDescriptionsResultDescription()
                self.result_description.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyServiceConfigFunctionComputeConfig(TeaModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        fc_base_url: str = None,
        fc_type: str = None,
        function_name: str = None,
        method: str = None,
        only_business_path: bool = None,
        path: str = None,
        qualifier: str = None,
        region_id: str = None,
        role_arn: str = None,
        service_name: str = None,
    ):
        self.content_type_catagory = content_type_catagory
        self.content_type_value = content_type_value
        self.fc_base_url = fc_base_url
        self.fc_type = fc_type
        self.function_name = function_name
        self.method = method
        self.only_business_path = only_business_path
        self.path = path
        self.qualifier = qualifier
        self.region_id = region_id
        self.role_arn = role_arn
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory
        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value
        if self.fc_base_url is not None:
            result['FcBaseUrl'] = self.fc_base_url
        if self.fc_type is not None:
            result['FcType'] = self.fc_type
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.method is not None:
            result['Method'] = self.method
        if self.only_business_path is not None:
            result['OnlyBusinessPath'] = self.only_business_path
        if self.path is not None:
            result['Path'] = self.path
        if self.qualifier is not None:
            result['Qualifier'] = self.qualifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')
        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')
        if m.get('FcBaseUrl') is not None:
            self.fc_base_url = m.get('FcBaseUrl')
        if m.get('FcType') is not None:
            self.fc_type = m.get('FcType')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('OnlyBusinessPath') is not None:
            self.only_business_path = m.get('OnlyBusinessPath')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Qualifier') is not None:
            self.qualifier = m.get('Qualifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeDeployedApiResponseBodyServiceConfigMockHeadersMockHeader(TeaModel):
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


class DescribeDeployedApiResponseBodyServiceConfigMockHeaders(TeaModel):
    def __init__(
        self,
        mock_header: List[DescribeDeployedApiResponseBodyServiceConfigMockHeadersMockHeader] = None,
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
                temp_model = DescribeDeployedApiResponseBodyServiceConfigMockHeadersMockHeader()
                self.mock_header.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyServiceConfigVpcConfig(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
    ):
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDeployedApiResponseBodyServiceConfig(TeaModel):
    def __init__(
        self,
        function_compute_config: DescribeDeployedApiResponseBodyServiceConfigFunctionComputeConfig = None,
        mock: str = None,
        mock_headers: DescribeDeployedApiResponseBodyServiceConfigMockHeaders = None,
        mock_result: str = None,
        mock_status_code: int = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        vpc_config: DescribeDeployedApiResponseBodyServiceConfigVpcConfig = None,
        vpc_id: str = None,
    ):
        self.function_compute_config = function_compute_config
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
        self.vpc_id = vpc_id

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
        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config.to_map()
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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionComputeConfig') is not None:
            temp_model = DescribeDeployedApiResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m['FunctionComputeConfig'])
        if m.get('Mock') is not None:
            self.mock = m.get('Mock')
        if m.get('MockHeaders') is not None:
            temp_model = DescribeDeployedApiResponseBodyServiceConfigMockHeaders()
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
            temp_model = DescribeDeployedApiResponseBodyServiceConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m['VpcConfig'])
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDeployedApiResponseBodyServiceParametersServiceParameter(TeaModel):
    def __init__(
        self,
        location: str = None,
        parameter_type: str = None,
        service_parameter_name: str = None,
    ):
        self.location = location
        self.parameter_type = parameter_type
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location
        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type
        if self.service_parameter_name is not None:
            result['ServiceParameterName'] = self.service_parameter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')
        if m.get('ServiceParameterName') is not None:
            self.service_parameter_name = m.get('ServiceParameterName')
        return self


class DescribeDeployedApiResponseBodyServiceParameters(TeaModel):
    def __init__(
        self,
        service_parameter: List[DescribeDeployedApiResponseBodyServiceParametersServiceParameter] = None,
    ):
        self.service_parameter = service_parameter

    def validate(self):
        if self.service_parameter:
            for k in self.service_parameter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceParameter'] = []
        if self.service_parameter is not None:
            for k in self.service_parameter:
                result['ServiceParameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_parameter = []
        if m.get('ServiceParameter') is not None:
            for k in m.get('ServiceParameter'):
                temp_model = DescribeDeployedApiResponseBodyServiceParametersServiceParameter()
                self.service_parameter.append(temp_model.from_map(k))
        return self


class DescribeDeployedApiResponseBodyServiceParametersMapServiceParameterMap(TeaModel):
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


class DescribeDeployedApiResponseBodyServiceParametersMap(TeaModel):
    def __init__(
        self,
        service_parameter_map: List[DescribeDeployedApiResponseBodyServiceParametersMapServiceParameterMap] = None,
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
                temp_model = DescribeDeployedApiResponseBodyServiceParametersMapServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k))
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
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        constant_parameters: DescribeDeployedApiResponseBodyConstantParameters = None,
        custom_system_parameters: DescribeDeployedApiResponseBodyCustomSystemParameters = None,
        deployed_time: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: DescribeDeployedApiResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        open_id_connect_config: DescribeDeployedApiResponseBodyOpenIdConnectConfig = None,
        region_id: str = None,
        request_config: DescribeDeployedApiResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: DescribeDeployedApiResponseBodyRequestParameters = None,
        result_body_model: str = None,
        result_descriptions: DescribeDeployedApiResponseBodyResultDescriptions = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: DescribeDeployedApiResponseBodyServiceConfig = None,
        service_parameters: DescribeDeployedApiResponseBodyServiceParameters = None,
        service_parameters_map: DescribeDeployedApiResponseBodyServiceParametersMap = None,
        stage_name: str = None,
        system_parameters: DescribeDeployedApiResponseBodySystemParameters = None,
        visibility: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_id = api_id
        self.api_name = api_name
        self.auth_type = auth_type
        self.constant_parameters = constant_parameters
        self.custom_system_parameters = custom_system_parameters
        self.deployed_time = deployed_time
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.group_name = group_name
        self.open_id_connect_config = open_id_connect_config
        self.region_id = region_id
        self.request_config = request_config
        self.request_id = request_id
        self.request_parameters = request_parameters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.stage_name = stage_name
        self.system_parameters = system_parameters
        self.visibility = visibility

    def validate(self):
        if self.constant_parameters:
            self.constant_parameters.validate()
        if self.custom_system_parameters:
            self.custom_system_parameters.validate()
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.open_id_connect_config:
            self.open_id_connect_config.validate()
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters:
            self.request_parameters.validate()
        if self.result_descriptions:
            self.result_descriptions.validate()
        if self.service_config:
            self.service_config.validate()
        if self.service_parameters:
            self.service_parameters.validate()
        if self.service_parameters_map:
            self.service_parameters_map.validate()
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
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters.to_map()
        if self.custom_system_parameters is not None:
            result['CustomSystemParameters'] = self.custom_system_parameters.to_map()
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
        if self.open_id_connect_config is not None:
            result['OpenIdConnectConfig'] = self.open_id_connect_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters.to_map()
        if self.result_body_model is not None:
            result['ResultBodyModel'] = self.result_body_model
        if self.result_descriptions is not None:
            result['ResultDescriptions'] = self.result_descriptions.to_map()
        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config.to_map()
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters.to_map()
        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map.to_map()
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters.to_map()
        if self.visibility is not None:
            result['Visibility'] = self.visibility
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
        if m.get('ConstantParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m['ConstantParameters'])
        if m.get('CustomSystemParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m['CustomSystemParameters'])
        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')
        if m.get('ErrorCodeSamples') is not None:
            temp_model = DescribeDeployedApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m['ErrorCodeSamples'])
        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')
        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('OpenIdConnectConfig') is not None:
            temp_model = DescribeDeployedApiResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m['OpenIdConnectConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestConfig') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m['RequestConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m['RequestParameters'])
        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')
        if m.get('ResultDescriptions') is not None:
            temp_model = DescribeDeployedApiResponseBodyResultDescriptions()
            self.result_descriptions = temp_model.from_map(m['ResultDescriptions'])
        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('ServiceConfig') is not None:
            temp_model = DescribeDeployedApiResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m['ServiceConfig'])
        if m.get('ServiceParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodyServiceParameters()
            self.service_parameters = temp_model.from_map(m['ServiceParameters'])
        if m.get('ServiceParametersMap') is not None:
            temp_model = DescribeDeployedApiResponseBodyServiceParametersMap()
            self.service_parameters_map = temp_model.from_map(m['ServiceParametersMap'])
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('SystemParameters') is not None:
            temp_model = DescribeDeployedApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m['SystemParameters'])
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribeDeployedApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeployedApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDeployedApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeployedApisRequestTag(TeaModel):
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


class DescribeDeployedApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        enable_tag_auth: bool = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
        tag: List[DescribeDeployedApisRequestTag] = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.enable_tag_auth = enable_tag_auth
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.stage_name = stage_name
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.enable_tag_auth is not None:
            result['EnableTagAuth'] = self.enable_tag_auth
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('EnableTagAuth') is not None:
            self.enable_tag_auth = m.get('EnableTagAuth')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDeployedApisRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDeployedApisResponseBodyDeployedApisDeployedApiItem(TeaModel):
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


class DescribeDeployedApisResponseBodyDeployedApis(TeaModel):
    def __init__(
        self,
        deployed_api_item: List[DescribeDeployedApisResponseBodyDeployedApisDeployedApiItem] = None,
    ):
        self.deployed_api_item = deployed_api_item

    def validate(self):
        if self.deployed_api_item:
            for k in self.deployed_api_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeployedApiItem'] = []
        if self.deployed_api_item is not None:
            for k in self.deployed_api_item:
                result['DeployedApiItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_api_item = []
        if m.get('DeployedApiItem') is not None:
            for k in m.get('DeployedApiItem'):
                temp_model = DescribeDeployedApisResponseBodyDeployedApisDeployedApiItem()
                self.deployed_api_item.append(temp_model.from_map(k))
        return self


class DescribeDeployedApisResponseBody(TeaModel):
    def __init__(
        self,
        deployed_apis: DescribeDeployedApisResponseBodyDeployedApis = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.deployed_apis = deployed_apis
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.deployed_apis:
            self.deployed_apis.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployed_apis is not None:
            result['DeployedApis'] = self.deployed_apis.to_map()
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
        if m.get('DeployedApis') is not None:
            temp_model = DescribeDeployedApisResponseBodyDeployedApis()
            self.deployed_apis = temp_model.from_map(m['DeployedApis'])
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
        body: DescribeDeployedApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        certificate_private_key: str = None,
        domain_binding_status: str = None,
        domain_cnamestatus: str = None,
        domain_legal_status: str = None,
        domain_name: str = None,
        domain_remark: str = None,
        domain_web_socket_status: str = None,
        group_id: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.certificate_body = certificate_body
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.certificate_private_key = certificate_private_key
        self.domain_binding_status = domain_binding_status
        self.domain_cnamestatus = domain_cnamestatus
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
        if self.certificate_body is not None:
            result['CertificateBody'] = self.certificate_body
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.certificate_private_key is not None:
            result['CertificatePrivateKey'] = self.certificate_private_key
        if self.domain_binding_status is not None:
            result['DomainBindingStatus'] = self.domain_binding_status
        if self.domain_cnamestatus is not None:
            result['DomainCNAMEStatus'] = self.domain_cnamestatus
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
        if m.get('CertificateBody') is not None:
            self.certificate_body = m.get('CertificateBody')
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CertificatePrivateKey') is not None:
            self.certificate_private_key = m.get('CertificatePrivateKey')
        if m.get('DomainBindingStatus') is not None:
            self.domain_binding_status = m.get('DomainBindingStatus')
        if m.get('DomainCNAMEStatus') is not None:
            self.domain_cnamestatus = m.get('DomainCNAMEStatus')
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


class DescribeDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHistoryApisRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: str = None,
        page_size: str = None,
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


class DescribeHistoryApisResponseBodyApiHisItemsApiHisItem(TeaModel):
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


class DescribeHistoryApisResponseBodyApiHisItems(TeaModel):
    def __init__(
        self,
        api_his_item: List[DescribeHistoryApisResponseBodyApiHisItemsApiHisItem] = None,
    ):
        self.api_his_item = api_his_item

    def validate(self):
        if self.api_his_item:
            for k in self.api_his_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiHisItem'] = []
        if self.api_his_item is not None:
            for k in self.api_his_item:
                result['ApiHisItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_his_item = []
        if m.get('ApiHisItem') is not None:
            for k in m.get('ApiHisItem'):
                temp_model = DescribeHistoryApisResponseBodyApiHisItemsApiHisItem()
                self.api_his_item.append(temp_model.from_map(k))
        return self


class DescribeHistoryApisResponseBody(TeaModel):
    def __init__(
        self,
        api_his_items: DescribeHistoryApisResponseBodyApiHisItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.api_his_items = api_his_items
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.api_his_items:
            self.api_his_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_his_items is not None:
            result['ApiHisItems'] = self.api_his_items.to_map()
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
        if m.get('ApiHisItems') is not None:
            temp_model = DescribeHistoryApisResponseBodyApiHisItems()
            self.api_his_items = temp_model.from_map(m['ApiHisItems'])
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
        body: DescribeHistoryApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DescribeIpControlPolicyItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DescribeIpControlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: DescribeLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMarketRemainsQuotaRequest(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        security_token: str = None,
    ):
        self.domain_name = domain_name
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeMarketRemainsQuotaResponseBody(TeaModel):
    def __init__(
        self,
        remains_quota: int = None,
        request_id: str = None,
    ):
        self.remains_quota = remains_quota
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remains_quota is not None:
            result['RemainsQuota'] = self.remains_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainsQuota') is not None:
            self.remains_quota = m.get('RemainsQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMarketRemainsQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMarketRemainsQuotaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMarketRemainsQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModelsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
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


class DescribeModelsResponseBodyModelDetailsModelDetail(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        model_ref: str = None,
        modified_time: str = None,
        schema: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.group_id = group_id
        self.model_id = model_id
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
        if self.model_id is not None:
            result['ModelId'] = self.model_id
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
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('ModelRef') is not None:
            self.model_ref = m.get('ModelRef')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class DescribeModelsResponseBodyModelDetails(TeaModel):
    def __init__(
        self,
        model_detail: List[DescribeModelsResponseBodyModelDetailsModelDetail] = None,
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
                temp_model = DescribeModelsResponseBodyModelDetailsModelDetail()
                self.model_detail.append(temp_model.from_map(k))
        return self


class DescribeModelsResponseBody(TeaModel):
    def __init__(
        self,
        model_details: DescribeModelsResponseBodyModelDetails = None,
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
            temp_model = DescribeModelsResponseBodyModelDetails()
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


class DescribeModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeModelsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePluginSchemasRequest(TeaModel):
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


class DescribePluginSchemasResponseBodyPluginSchemasPluginSchema(TeaModel):
    def __init__(
        self,
        description: str = None,
        document_id: str = None,
        name: str = None,
        support_classic: bool = None,
        title: str = None,
    ):
        self.description = description
        self.document_id = document_id
        self.name = name
        self.support_classic = support_classic
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.document_id is not None:
            result['DocumentId'] = self.document_id
        if self.name is not None:
            result['Name'] = self.name
        if self.support_classic is not None:
            result['SupportClassic'] = self.support_classic
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SupportClassic') is not None:
            self.support_classic = m.get('SupportClassic')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribePluginSchemasResponseBodyPluginSchemas(TeaModel):
    def __init__(
        self,
        plugin_schema: List[DescribePluginSchemasResponseBodyPluginSchemasPluginSchema] = None,
    ):
        self.plugin_schema = plugin_schema

    def validate(self):
        if self.plugin_schema:
            for k in self.plugin_schema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PluginSchema'] = []
        if self.plugin_schema is not None:
            for k in self.plugin_schema:
                result['PluginSchema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugin_schema = []
        if m.get('PluginSchema') is not None:
            for k in m.get('PluginSchema'):
                temp_model = DescribePluginSchemasResponseBodyPluginSchemasPluginSchema()
                self.plugin_schema.append(temp_model.from_map(k))
        return self


class DescribePluginSchemasResponseBody(TeaModel):
    def __init__(
        self,
        plugin_schemas: DescribePluginSchemasResponseBodyPluginSchemas = None,
        request_id: str = None,
    ):
        self.plugin_schemas = plugin_schemas
        self.request_id = request_id

    def validate(self):
        if self.plugin_schemas:
            self.plugin_schemas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_schemas is not None:
            result['PluginSchemas'] = self.plugin_schemas.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginSchemas') is not None:
            temp_model = DescribePluginSchemasResponseBodyPluginSchemas()
            self.plugin_schemas = temp_model.from_map(m['PluginSchemas'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePluginSchemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePluginSchemasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePluginSchemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePluginTemplatesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        plugin_name: str = None,
        security_token: str = None,
    ):
        self.language = language
        self.plugin_name = plugin_name
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
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribePluginTemplatesResponseBodyTemplatesTemplate(TeaModel):
    def __init__(
        self,
        description: str = None,
        document_anchor: str = None,
        document_id: str = None,
        sample: str = None,
        title: str = None,
    ):
        self.description = description
        self.document_anchor = document_anchor
        self.document_id = document_id
        self.sample = sample
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.document_anchor is not None:
            result['DocumentAnchor'] = self.document_anchor
        if self.document_id is not None:
            result['DocumentId'] = self.document_id
        if self.sample is not None:
            result['Sample'] = self.sample
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentAnchor') is not None:
            self.document_anchor = m.get('DocumentAnchor')
        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribePluginTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        template: List[DescribePluginTemplatesResponseBodyTemplatesTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for k in self.template:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Template'] = []
        if self.template is not None:
            for k in self.template:
                result['Template'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k in m.get('Template'):
                temp_model = DescribePluginTemplatesResponseBodyTemplatesTemplate()
                self.template.append(temp_model.from_map(k))
        return self


class DescribePluginTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        templates: DescribePluginTemplatesResponseBodyTemplates = None,
    ):
        self.request_id = request_id
        self.templates = templates

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.templates is not None:
            result['Templates'] = self.templates.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Templates') is not None:
            temp_model = DescribePluginTemplatesResponseBodyTemplates()
            self.templates = temp_model.from_map(m['Templates'])
        return self


class DescribePluginTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePluginTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePluginTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePluginsRequestTag(TeaModel):
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


class DescribePluginsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        security_token: str = None,
        tag: List[DescribePluginsRequestTag] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
        self.plugin_type = plugin_type
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribePluginsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribePluginsResponseBodyPluginsPluginAttributeTagsTagInfo(TeaModel):
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


class DescribePluginsResponseBodyPluginsPluginAttributeTags(TeaModel):
    def __init__(
        self,
        tag_info: List[DescribePluginsResponseBodyPluginsPluginAttributeTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = DescribePluginsResponseBodyPluginsPluginAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class DescribePluginsResponseBodyPluginsPluginAttribute(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: int = None,
        modified_time: str = None,
        plugin_data: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        region_id: int = None,
        tags: DescribePluginsResponseBodyPluginsPluginAttributeTags = None,
    ):
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time
        self.plugin_data = plugin_data
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
        self.plugin_type = plugin_type
        self.region_id = region_id
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PluginData') is not None:
            self.plugin_data = m.get('PluginData')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            temp_model = DescribePluginsResponseBodyPluginsPluginAttributeTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class DescribePluginsResponseBodyPlugins(TeaModel):
    def __init__(
        self,
        plugin_attribute: List[DescribePluginsResponseBodyPluginsPluginAttribute] = None,
    ):
        self.plugin_attribute = plugin_attribute

    def validate(self):
        if self.plugin_attribute:
            for k in self.plugin_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PluginAttribute'] = []
        if self.plugin_attribute is not None:
            for k in self.plugin_attribute:
                result['PluginAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugin_attribute = []
        if m.get('PluginAttribute') is not None:
            for k in m.get('PluginAttribute'):
                temp_model = DescribePluginsResponseBodyPluginsPluginAttribute()
                self.plugin_attribute.append(temp_model.from_map(k))
        return self


class DescribePluginsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plugins: DescribePluginsResponseBodyPlugins = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.plugins = plugins
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.plugins:
            self.plugins.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plugins is not None:
            result['Plugins'] = self.plugins.to_map()
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
        if m.get('Plugins') is not None:
            temp_model = DescribePluginsResponseBodyPlugins()
            self.plugins = temp_model.from_map(m['Plugins'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePluginsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePluginsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePluginsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePluginsByApiRequest(TeaModel):
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


class DescribePluginsByApiResponseBodyPluginsPluginAttribute(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        modified_time: str = None,
        plugin_data: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
        region_id: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.modified_time = modified_time
        self.plugin_data = plugin_data
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
        self.plugin_type = plugin_type
        self.region_id = region_id

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
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PluginData') is not None:
            self.plugin_data = m.get('PluginData')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePluginsByApiResponseBodyPlugins(TeaModel):
    def __init__(
        self,
        plugin_attribute: List[DescribePluginsByApiResponseBodyPluginsPluginAttribute] = None,
    ):
        self.plugin_attribute = plugin_attribute

    def validate(self):
        if self.plugin_attribute:
            for k in self.plugin_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PluginAttribute'] = []
        if self.plugin_attribute is not None:
            for k in self.plugin_attribute:
                result['PluginAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plugin_attribute = []
        if m.get('PluginAttribute') is not None:
            for k in m.get('PluginAttribute'):
                temp_model = DescribePluginsByApiResponseBodyPluginsPluginAttribute()
                self.plugin_attribute.append(temp_model.from_map(k))
        return self


class DescribePluginsByApiResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plugins: DescribePluginsByApiResponseBodyPlugins = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.plugins = plugins
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.plugins:
            self.plugins.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plugins is not None:
            result['Plugins'] = self.plugins.to_map()
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
        if m.get('Plugins') is not None:
            temp_model = DescribePluginsByApiResponseBodyPlugins()
            self.plugins = temp_model.from_map(m['Plugins'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePluginsByApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePluginsByApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePluginsByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePurchasedApiGroupRequest(TeaModel):
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


class DescribePurchasedApiGroupResponseBodyDomainsDomainItem(TeaModel):
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


class DescribePurchasedApiGroupResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain_item: List[DescribePurchasedApiGroupResponseBodyDomainsDomainItem] = None,
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
                temp_model = DescribePurchasedApiGroupResponseBodyDomainsDomainItem()
                self.domain_item.append(temp_model.from_map(k))
        return self


class DescribePurchasedApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        domains: DescribePurchasedApiGroupResponseBodyDomains = None,
        group_id: str = None,
        group_name: str = None,
        purchased_time: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.description = description
        self.domains = domains
        self.group_id = group_id
        self.group_name = group_name
        self.purchased_time = purchased_time
        self.region_id = region_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.purchased_time is not None:
            result['PurchasedTime'] = self.purchased_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Domains') is not None:
            temp_model = DescribePurchasedApiGroupResponseBodyDomains()
            self.domains = temp_model.from_map(m['Domains'])
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('PurchasedTime') is not None:
            self.purchased_time = m.get('PurchasedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePurchasedApiGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePurchasedApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePurchasedApiGroupResponseBody()
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
        description: str = None,
        expire_time: str = None,
        group_id: str = None,
        group_name: str = None,
        invoke_times_max: int = None,
        invoke_times_now: int = None,
        purchased_time: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.billing_type = billing_type
        self.description = description
        self.expire_time = expire_time
        self.group_id = group_id
        self.group_name = group_name
        self.invoke_times_max = invoke_times_max
        self.invoke_times_now = invoke_times_now
        self.purchased_time = purchased_time
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
        if self.description is not None:
            result['Description'] = self.description
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.invoke_times_max is not None:
            result['InvokeTimesMax'] = self.invoke_times_max
        if self.invoke_times_now is not None:
            result['InvokeTimesNow'] = self.invoke_times_now
        if self.purchased_time is not None:
            result['PurchasedTime'] = self.purchased_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InvokeTimesMax') is not None:
            self.invoke_times_max = m.get('InvokeTimesMax')
        if m.get('InvokeTimesNow') is not None:
            self.invoke_times_now = m.get('InvokeTimesNow')
        if m.get('PurchasedTime') is not None:
            self.purchased_time = m.get('PurchasedTime')
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
        body: DescribePurchasedApiGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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


class DescribePurchasedApisResponseBodyPurchasedApisPurchasedApi(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        deployed_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        modified_time: str = None,
        purchased_time: str = None,
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
        self.purchased_time = purchased_time
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
        if self.purchased_time is not None:
            result['PurchasedTime'] = self.purchased_time
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
        if m.get('PurchasedTime') is not None:
            self.purchased_time = m.get('PurchasedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        return self


class DescribePurchasedApisResponseBodyPurchasedApis(TeaModel):
    def __init__(
        self,
        purchased_api: List[DescribePurchasedApisResponseBodyPurchasedApisPurchasedApi] = None,
    ):
        self.purchased_api = purchased_api

    def validate(self):
        if self.purchased_api:
            for k in self.purchased_api:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PurchasedApi'] = []
        if self.purchased_api is not None:
            for k in self.purchased_api:
                result['PurchasedApi'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.purchased_api = []
        if m.get('PurchasedApi') is not None:
            for k in m.get('PurchasedApi'):
                temp_model = DescribePurchasedApisResponseBodyPurchasedApisPurchasedApi()
                self.purchased_api.append(temp_model.from_map(k))
        return self


class DescribePurchasedApisResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        purchased_apis: DescribePurchasedApisResponseBodyPurchasedApis = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.purchased_apis = purchased_apis
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.purchased_apis:
            self.purchased_apis.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.purchased_apis is not None:
            result['PurchasedApis'] = self.purchased_apis.to_map()
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
        if m.get('PurchasedApis') is not None:
            temp_model = DescribePurchasedApisResponseBodyPurchasedApis()
            self.purchased_apis = temp_model.from_map(m['PurchasedApis'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePurchasedApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePurchasedApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePurchasedApisResponseBody()
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
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSignaturesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.signature_id = signature_id
        self.signature_name = signature_name

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
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        return self


class DescribeSignaturesResponseBodySignatureInfosSignatureInfo(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        modified_time: str = None,
        region_id: str = None,
        signature_id: str = None,
        signature_key: str = None,
        signature_name: str = None,
        signature_secret: str = None,
    ):
        self.created_time = created_time
        self.modified_time = modified_time
        self.region_id = region_id
        self.signature_id = signature_id
        self.signature_key = signature_key
        self.signature_name = signature_name
        self.signature_secret = signature_secret

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
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        if self.signature_secret is not None:
            result['SignatureSecret'] = self.signature_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        if m.get('SignatureSecret') is not None:
            self.signature_secret = m.get('SignatureSecret')
        return self


class DescribeSignaturesResponseBodySignatureInfos(TeaModel):
    def __init__(
        self,
        signature_info: List[DescribeSignaturesResponseBodySignatureInfosSignatureInfo] = None,
    ):
        self.signature_info = signature_info

    def validate(self):
        if self.signature_info:
            for k in self.signature_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SignatureInfo'] = []
        if self.signature_info is not None:
            for k in self.signature_info:
                result['SignatureInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.signature_info = []
        if m.get('SignatureInfo') is not None:
            for k in m.get('SignatureInfo'):
                temp_model = DescribeSignaturesResponseBodySignatureInfosSignatureInfo()
                self.signature_info.append(temp_model.from_map(k))
        return self


class DescribeSignaturesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        signature_infos: DescribeSignaturesResponseBodySignatureInfos = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.signature_infos = signature_infos
        self.total_count = total_count

    def validate(self):
        if self.signature_infos:
            self.signature_infos.validate()

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
        if self.signature_infos is not None:
            result['SignatureInfos'] = self.signature_infos.to_map()
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
        if m.get('SignatureInfos') is not None:
            temp_model = DescribeSignaturesResponseBodySignatureInfos()
            self.signature_infos = temp_model.from_map(m['SignatureInfos'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSignaturesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSignaturesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSignaturesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSignaturesByApiRequest(TeaModel):
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


class DescribeSignaturesByApiResponseBodySignaturesSignatureItem(TeaModel):
    def __init__(
        self,
        bound_time: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        self.bound_time = bound_time
        self.signature_id = signature_id
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        return self


class DescribeSignaturesByApiResponseBodySignatures(TeaModel):
    def __init__(
        self,
        signature_item: List[DescribeSignaturesByApiResponseBodySignaturesSignatureItem] = None,
    ):
        self.signature_item = signature_item

    def validate(self):
        if self.signature_item:
            for k in self.signature_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SignatureItem'] = []
        if self.signature_item is not None:
            for k in self.signature_item:
                result['SignatureItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.signature_item = []
        if m.get('SignatureItem') is not None:
            for k in m.get('SignatureItem'):
                temp_model = DescribeSignaturesByApiResponseBodySignaturesSignatureItem()
                self.signature_item.append(temp_model.from_map(k))
        return self


class DescribeSignaturesByApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signatures: DescribeSignaturesByApiResponseBodySignatures = None,
    ):
        self.request_id = request_id
        self.signatures = signatures

    def validate(self):
        if self.signatures:
            self.signatures.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signatures is not None:
            result['Signatures'] = self.signatures.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signatures') is not None:
            temp_model = DescribeSignaturesByApiResponseBodySignatures()
            self.signatures = temp_model.from_map(m['Signatures'])
        return self


class DescribeSignaturesByApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSignaturesByApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSignaturesByApiResponseBody()
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


class DescribeSystemParametersResponseBodySystemParamsSystemParamItem(TeaModel):
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


class DescribeSystemParametersResponseBodySystemParams(TeaModel):
    def __init__(
        self,
        system_param_item: List[DescribeSystemParametersResponseBodySystemParamsSystemParamItem] = None,
    ):
        self.system_param_item = system_param_item

    def validate(self):
        if self.system_param_item:
            for k in self.system_param_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SystemParamItem'] = []
        if self.system_param_item is not None:
            for k in self.system_param_item:
                result['SystemParamItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_param_item = []
        if m.get('SystemParamItem') is not None:
            for k in m.get('SystemParamItem'):
                temp_model = DescribeSystemParametersResponseBodySystemParamsSystemParamItem()
                self.system_param_item.append(temp_model.from_map(k))
        return self


class DescribeSystemParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        system_params: DescribeSystemParametersResponseBodySystemParams = None,
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
            temp_model = DescribeSystemParametersResponseBodySystemParams()
            self.system_params = temp_model.from_map(m['SystemParams'])
        return self


class DescribeSystemParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSystemParametersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSystemParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficControlsRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
    ):
        self.api_id = api_id
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id
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
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
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
        body: DescribeTrafficControlsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTrafficControlsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficControlsByApiRequest(TeaModel):
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


class DescribeTrafficControlsByApiResponseBodyTrafficControlItemsTrafficControlItem(TeaModel):
    def __init__(
        self,
        bound_time: str = None,
        traffic_control_item_id: str = None,
        traffic_control_item_name: str = None,
    ):
        self.bound_time = bound_time
        self.traffic_control_item_id = traffic_control_item_id
        self.traffic_control_item_name = traffic_control_item_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time
        if self.traffic_control_item_id is not None:
            result['TrafficControlItemId'] = self.traffic_control_item_id
        if self.traffic_control_item_name is not None:
            result['TrafficControlItemName'] = self.traffic_control_item_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')
        if m.get('TrafficControlItemId') is not None:
            self.traffic_control_item_id = m.get('TrafficControlItemId')
        if m.get('TrafficControlItemName') is not None:
            self.traffic_control_item_name = m.get('TrafficControlItemName')
        return self


class DescribeTrafficControlsByApiResponseBodyTrafficControlItems(TeaModel):
    def __init__(
        self,
        traffic_control_item: List[DescribeTrafficControlsByApiResponseBodyTrafficControlItemsTrafficControlItem] = None,
    ):
        self.traffic_control_item = traffic_control_item

    def validate(self):
        if self.traffic_control_item:
            for k in self.traffic_control_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TrafficControlItem'] = []
        if self.traffic_control_item is not None:
            for k in self.traffic_control_item:
                result['TrafficControlItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_control_item = []
        if m.get('TrafficControlItem') is not None:
            for k in m.get('TrafficControlItem'):
                temp_model = DescribeTrafficControlsByApiResponseBodyTrafficControlItemsTrafficControlItem()
                self.traffic_control_item.append(temp_model.from_map(k))
        return self


class DescribeTrafficControlsByApiResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_items: DescribeTrafficControlsByApiResponseBodyTrafficControlItems = None,
    ):
        self.request_id = request_id
        self.traffic_control_items = traffic_control_items

    def validate(self):
        if self.traffic_control_items:
            self.traffic_control_items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_control_items is not None:
            result['TrafficControlItems'] = self.traffic_control_items.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficControlItems') is not None:
            temp_model = DescribeTrafficControlsByApiResponseBodyTrafficControlItems()
            self.traffic_control_items = temp_model.from_map(m['TrafficControlItems'])
        return self


class DescribeTrafficControlsByApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTrafficControlsByApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTrafficControlsByApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpdateVpcInfoTaskRequest(TeaModel):
    def __init__(
        self,
        operation_uid: str = None,
        security_token: str = None,
    ):
        self.operation_uid = operation_uid
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResultsApiUpdateVpcInfoResult(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_uid: str = None,
        error_msg: str = None,
        group_id: str = None,
        group_name: str = None,
        stage_id: str = None,
        stage_name: str = None,
        update_status: str = None,
    ):
        self.api_name = api_name
        self.api_uid = api_uid
        self.error_msg = error_msg
        self.group_id = group_id
        self.group_name = group_name
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.update_status = update_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')
        return self


class DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResults(TeaModel):
    def __init__(
        self,
        api_update_vpc_info_result: List[DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResultsApiUpdateVpcInfoResult] = None,
    ):
        self.api_update_vpc_info_result = api_update_vpc_info_result

    def validate(self):
        if self.api_update_vpc_info_result:
            for k in self.api_update_vpc_info_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiUpdateVpcInfoResult'] = []
        if self.api_update_vpc_info_result is not None:
            for k in self.api_update_vpc_info_result:
                result['ApiUpdateVpcInfoResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_update_vpc_info_result = []
        if m.get('ApiUpdateVpcInfoResult') is not None:
            for k in m.get('ApiUpdateVpcInfoResult'):
                temp_model = DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResultsApiUpdateVpcInfoResult()
                self.api_update_vpc_info_result.append(temp_model.from_map(k))
        return self


class DescribeUpdateVpcInfoTaskResponseBody(TeaModel):
    def __init__(
        self,
        api_update_vpc_info_results: DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResults = None,
        request_id: str = None,
    ):
        self.api_update_vpc_info_results = api_update_vpc_info_results
        self.request_id = request_id

    def validate(self):
        if self.api_update_vpc_info_results:
            self.api_update_vpc_info_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_update_vpc_info_results is not None:
            result['ApiUpdateVpcInfoResults'] = self.api_update_vpc_info_results.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUpdateVpcInfoResults') is not None:
            temp_model = DescribeUpdateVpcInfoTaskResponseBodyApiUpdateVpcInfoResults()
            self.api_update_vpc_info_results = temp_model.from_map(m['ApiUpdateVpcInfoResults'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUpdateVpcInfoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUpdateVpcInfoTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUpdateVpcInfoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcAccessesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        vpc_access_id: str = None,
    ):
        # VPC授权名称
        self.name = name
        # 当前页码
        self.page_number = page_number
        # 每页展示条目
        self.page_size = page_size
        self.security_token = security_token
        # Vpc授权ID
        self.vpc_access_id = vpc_access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')
        return self


class DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute(TeaModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        region_id: str = None,
        vpc_access_id: str = None,
        vpc_id: str = None,
    ):
        # VPC授权的创建时间
        self.created_time = created_time
        # VPC授权的描述
        self.description = description
        # VPC中的后端服务信息
        self.instance_id = instance_id
        # VPC授权名称
        self.name = name
        # VPC中的后端服务端口
        self.port = port
        # 地域id
        self.region_id = region_id
        # vpc授权ID
        self.vpc_access_id = vpc_access_id
        # VPC的ID
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
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVpcAccessesResponseBodyVpcAccessAttributes(TeaModel):
    def __init__(
        self,
        vpc_access_attribute: List[DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute] = None,
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
                temp_model = DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute()
                self.vpc_access_attribute.append(temp_model.from_map(k))
        return self


class DescribeVpcAccessesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_access_attributes: DescribeVpcAccessesResponseBodyVpcAccessAttributes = None,
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
            temp_model = DescribeVpcAccessesResponseBodyVpcAccessAttributes()
            self.vpc_access_attributes = temp_model.from_map(m['VpcAccessAttributes'])
        return self


class DescribeVpcAccessesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVpcAccessesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcAccessesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
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


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DryRunSwaggerRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        data_format: str = None,
        global_condition: Dict[str, Any] = None,
        group_id: str = None,
        overwrite: bool = None,
        security_token: str = None,
    ):
        self.data = data
        self.data_format = data_format
        self.global_condition = global_condition
        self.group_id = group_id
        self.overwrite = overwrite
        self.security_token = security_token

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
        if self.global_condition is not None:
            result['GlobalCondition'] = self.global_condition
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('GlobalCondition') is not None:
            self.global_condition = m.get('GlobalCondition')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DryRunSwaggerShrinkRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        data_format: str = None,
        global_condition_shrink: str = None,
        group_id: str = None,
        overwrite: bool = None,
        security_token: str = None,
    ):
        self.data = data
        self.data_format = data_format
        self.global_condition_shrink = global_condition_shrink
        self.group_id = group_id
        self.overwrite = overwrite
        self.security_token = security_token

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
        if self.global_condition_shrink is not None:
            result['GlobalCondition'] = self.global_condition_shrink
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('GlobalCondition') is not None:
            self.global_condition_shrink = m.get('GlobalCondition')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DryRunSwaggerResponseBodyFailedApiImportSwaggerFailed(TeaModel):
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


class DryRunSwaggerResponseBodyFailed(TeaModel):
    def __init__(
        self,
        api_import_swagger_failed: List[DryRunSwaggerResponseBodyFailedApiImportSwaggerFailed] = None,
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
                temp_model = DryRunSwaggerResponseBodyFailedApiImportSwaggerFailed()
                self.api_import_swagger_failed.append(temp_model.from_map(k))
        return self


class DryRunSwaggerResponseBodyModelFailedApiImportModelFailed(TeaModel):
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


class DryRunSwaggerResponseBodyModelFailed(TeaModel):
    def __init__(
        self,
        api_import_model_failed: List[DryRunSwaggerResponseBodyModelFailedApiImportModelFailed] = None,
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
                temp_model = DryRunSwaggerResponseBodyModelFailedApiImportModelFailed()
                self.api_import_model_failed.append(temp_model.from_map(k))
        return self


class DryRunSwaggerResponseBodyModelSuccessApiImportModelSuccess(TeaModel):
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


class DryRunSwaggerResponseBodyModelSuccess(TeaModel):
    def __init__(
        self,
        api_import_model_success: List[DryRunSwaggerResponseBodyModelSuccessApiImportModelSuccess] = None,
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
                temp_model = DryRunSwaggerResponseBodyModelSuccessApiImportModelSuccess()
                self.api_import_model_success.append(temp_model.from_map(k))
        return self


class DryRunSwaggerResponseBodySuccessApiDryRunSwaggerSuccess(TeaModel):
    def __init__(
        self,
        api_operation: str = None,
        api_swagger: str = None,
        api_uid: str = None,
        http_method: str = None,
        path: str = None,
    ):
        self.api_operation = api_operation
        self.api_swagger = api_swagger
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
        if self.api_swagger is not None:
            result['ApiSwagger'] = self.api_swagger
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
        if m.get('ApiSwagger') is not None:
            self.api_swagger = m.get('ApiSwagger')
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')
        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DryRunSwaggerResponseBodySuccess(TeaModel):
    def __init__(
        self,
        api_dry_run_swagger_success: List[DryRunSwaggerResponseBodySuccessApiDryRunSwaggerSuccess] = None,
    ):
        self.api_dry_run_swagger_success = api_dry_run_swagger_success

    def validate(self):
        if self.api_dry_run_swagger_success:
            for k in self.api_dry_run_swagger_success:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiDryRunSwaggerSuccess'] = []
        if self.api_dry_run_swagger_success is not None:
            for k in self.api_dry_run_swagger_success:
                result['ApiDryRunSwaggerSuccess'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_dry_run_swagger_success = []
        if m.get('ApiDryRunSwaggerSuccess') is not None:
            for k in m.get('ApiDryRunSwaggerSuccess'):
                temp_model = DryRunSwaggerResponseBodySuccessApiDryRunSwaggerSuccess()
                self.api_dry_run_swagger_success.append(temp_model.from_map(k))
        return self


class DryRunSwaggerResponseBody(TeaModel):
    def __init__(
        self,
        failed: DryRunSwaggerResponseBodyFailed = None,
        global_condition: str = None,
        model_failed: DryRunSwaggerResponseBodyModelFailed = None,
        model_success: DryRunSwaggerResponseBodyModelSuccess = None,
        request_id: str = None,
        success: DryRunSwaggerResponseBodySuccess = None,
    ):
        self.failed = failed
        self.global_condition = global_condition
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
        if self.global_condition is not None:
            result['GlobalCondition'] = self.global_condition
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
            temp_model = DryRunSwaggerResponseBodyFailed()
            self.failed = temp_model.from_map(m['Failed'])
        if m.get('GlobalCondition') is not None:
            self.global_condition = m.get('GlobalCondition')
        if m.get('ModelFailed') is not None:
            temp_model = DryRunSwaggerResponseBodyModelFailed()
            self.model_failed = temp_model.from_map(m['ModelFailed'])
        if m.get('ModelSuccess') is not None:
            temp_model = DryRunSwaggerResponseBodyModelSuccess()
            self.model_success = temp_model.from_map(m['ModelSuccess'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            temp_model = DryRunSwaggerResponseBodySuccess()
            self.success = temp_model.from_map(m['Success'])
        return self


class DryRunSwaggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DryRunSwaggerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DryRunSwaggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSwaggerRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        data_format: str = None,
        dry_run: bool = None,
        global_condition: Dict[str, Any] = None,
        group_id: str = None,
        overwrite: bool = None,
        security_token: str = None,
    ):
        self.data = data
        self.data_format = data_format
        self.dry_run = dry_run
        self.global_condition = global_condition
        self.group_id = group_id
        self.overwrite = overwrite
        self.security_token = security_token

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
        if self.global_condition is not None:
            result['GlobalCondition'] = self.global_condition
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GlobalCondition') is not None:
            self.global_condition = m.get('GlobalCondition')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ImportSwaggerShrinkRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        data_format: str = None,
        dry_run: bool = None,
        global_condition_shrink: str = None,
        group_id: str = None,
        overwrite: bool = None,
        security_token: str = None,
    ):
        self.data = data
        self.data_format = data_format
        self.dry_run = dry_run
        self.global_condition_shrink = global_condition_shrink
        self.group_id = group_id
        self.overwrite = overwrite
        self.security_token = security_token

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
        if self.global_condition_shrink is not None:
            result['GlobalCondition'] = self.global_condition_shrink
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('GlobalCondition') is not None:
            self.global_condition_shrink = m.get('GlobalCondition')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        body: ImportSwaggerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportSwaggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
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
        constant_parameters: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: str = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        open_id_connect_config: str = None,
        request_config: str = None,
        request_parameters: str = None,
        result_body_model: str = None,
        result_descriptions: str = None,
        result_sample: str = None,
        result_type: str = None,
        security_token: str = None,
        service_config: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        system_parameters: str = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        self.allow_signature_method = allow_signature_method
        self.api_id = api_id
        self.api_name = api_name
        self.app_code_auth_type = app_code_auth_type
        self.auth_type = auth_type
        self.constant_parameters = constant_parameters
        self.description = description
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        self.force_nonce_check = force_nonce_check
        self.group_id = group_id
        self.open_id_connect_config = open_id_connect_config
        self.request_config = request_config
        self.request_parameters = request_parameters
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        self.result_type = result_type
        self.security_token = security_token
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.system_parameters = system_parameters
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
        if self.constant_parameters is not None:
            result['ConstantParameters'] = self.constant_parameters
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
        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters
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
        if self.system_parameters is not None:
            result['SystemParameters'] = self.system_parameters
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
            self.constant_parameters = m.get('ConstantParameters')
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
        if m.get('RequestParameters') is not None:
            self.request_parameters = m.get('RequestParameters')
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
        if m.get('SystemParameters') is not None:
            self.system_parameters = m.get('SystemParameters')
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
        body: ModifyApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiGroupRequestTag(TeaModel):
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


class ModifyApiGroupRequest(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        compatible_flags: str = None,
        custom_trace_config: str = None,
        customer_configs: str = None,
        default_domain: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        passthrough_headers: str = None,
        rpc_pattern: str = None,
        security_token: str = None,
        tag: List[ModifyApiGroupRequestTag] = None,
        user_log_config: str = None,
    ):
        self.base_path = base_path
        self.compatible_flags = compatible_flags
        self.custom_trace_config = custom_trace_config
        self.customer_configs = customer_configs
        self.default_domain = default_domain
        self.description = description
        self.group_id = group_id
        self.group_name = group_name
        self.passthrough_headers = passthrough_headers
        self.rpc_pattern = rpc_pattern
        self.security_token = security_token
        self.tag = tag
        self.user_log_config = user_log_config

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
        if self.base_path is not None:
            result['BasePath'] = self.base_path
        if self.compatible_flags is not None:
            result['CompatibleFlags'] = self.compatible_flags
        if self.custom_trace_config is not None:
            result['CustomTraceConfig'] = self.custom_trace_config
        if self.customer_configs is not None:
            result['CustomerConfigs'] = self.customer_configs
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_log_config is not None:
            result['UserLogConfig'] = self.user_log_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')
        if m.get('CompatibleFlags') is not None:
            self.compatible_flags = m.get('CompatibleFlags')
        if m.get('CustomTraceConfig') is not None:
            self.custom_trace_config = m.get('CustomTraceConfig')
        if m.get('CustomerConfigs') is not None:
            self.customer_configs = m.get('CustomerConfigs')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ModifyApiGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserLogConfig') is not None:
            self.user_log_config = m.get('UserLogConfig')
        return self


class ModifyApiGroupResponseBody(TeaModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        request_id: str = None,
        sub_domain: str = None,
    ):
        self.base_path = base_path
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
        if self.base_path is not None:
            result['BasePath'] = self.base_path
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
        if m.get('BasePath') is not None:
            self.base_path = m.get('BasePath')
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
        body: ModifyApiGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyApiGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiGroupVpcWhitelistRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        security_token: str = None,
        vpc_ids: str = None,
    ):
        self.group_id = group_id
        self.security_token = security_token
        self.vpc_ids = vpc_ids

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
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        return self


class ModifyApiGroupVpcWhitelistResponseBody(TeaModel):
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


class ModifyApiGroupVpcWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyApiGroupVpcWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyApiGroupVpcWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequestTag(TeaModel):
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


class ModifyAppRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        description: str = None,
        security_token: str = None,
        tag: List[ModifyAppRequestTag] = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.description = description
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
        if self.description is not None:
            result['Description'] = self.description
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ModifyAppRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        body: ModifyAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        instance_id: str = None,
        instance_spec: str = None,
        token: str = None,
    ):
        self.auto_pay = auto_pay
        self.instance_id = instance_id
        self.instance_spec = instance_spec
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ModifyInstanceSpecResponseBody(TeaModel):
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


class ModifyInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceSpecResponseBody()
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
        body: ModifyIpControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ModifyIpControlPolicyItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: ModifyLogConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyLogConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyModelRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        model_name: str = None,
        new_model_name: str = None,
        schema: str = None,
    ):
        self.description = description
        self.group_id = group_id
        self.model_name = model_name
        self.new_model_name = new_model_name
        self.schema = schema

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
        if self.model_name is not None:
            result['ModelName'] = self.model_name
        if self.new_model_name is not None:
            result['NewModelName'] = self.new_model_name
        if self.schema is not None:
            result['Schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')
        if m.get('NewModelName') is not None:
            self.new_model_name = m.get('NewModelName')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        return self


class ModifyModelResponseBody(TeaModel):
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


class ModifyModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyModelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPluginRequestTag(TeaModel):
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


class ModifyPluginRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        plugin_data: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        security_token: str = None,
        tag: List[ModifyPluginRequestTag] = None,
    ):
        self.description = description
        self.plugin_data = plugin_data
        self.plugin_id = plugin_id
        self.plugin_name = plugin_name
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
        if self.description is not None:
            result['Description'] = self.description
        if self.plugin_data is not None:
            result['PluginData'] = self.plugin_data
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PluginData') is not None:
            self.plugin_data = m.get('PluginData')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ModifyPluginRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ModifyPluginResponseBody(TeaModel):
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


class ModifyPluginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPluginResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPluginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySignatureRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        signature_id: str = None,
        signature_key: str = None,
        signature_name: str = None,
        signature_secret: str = None,
    ):
        self.security_token = security_token
        self.signature_id = signature_id
        self.signature_key = signature_key
        self.signature_name = signature_name
        self.signature_secret = signature_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        if self.signature_secret is not None:
            result['SignatureSecret'] = self.signature_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        if m.get('SignatureSecret') is not None:
            self.signature_secret = m.get('SignatureSecret')
        return self


class ModifySignatureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        self.request_id = request_id
        self.signature_id = signature_id
        self.signature_name = signature_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')
        return self


class ModifySignatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySignatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifySignatureResponseBody()
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
        body: ModifyTrafficControlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyTrafficControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenApiGatewayServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenApiGatewayServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenApiGatewayServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenApiGatewayServiceResponseBody()
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
        body: ReactivateDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReactivateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveApisAuthoritiesRequest(TeaModel):
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


class RemoveApisAuthoritiesResponseBody(TeaModel):
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


class RemoveApisAuthoritiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveApisAuthoritiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveApisAuthoritiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAppsAuthoritiesRequest(TeaModel):
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


class RemoveAppsAuthoritiesResponseBody(TeaModel):
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


class RemoveAppsAuthoritiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAppsAuthoritiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveAppsAuthoritiesResponseBody()
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
        body: RemoveIpControlApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: RemoveIpControlPolicyItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveIpControlPolicyItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSignatureApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        security_token: str = None,
        signature_id: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.security_token = security_token
        self.signature_id = signature_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class RemoveSignatureApisResponseBody(TeaModel):
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


class RemoveSignatureApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveSignatureApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveSignatureApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTrafficControlApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        traffic_control_id: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name
        self.traffic_control_id = traffic_control_id

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class RemoveTrafficControlApisResponseBody(TeaModel):
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


class RemoveTrafficControlApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveTrafficControlApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveTrafficControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVpcAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        need_batch_work: bool = None,
        port: int = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.need_batch_work = need_batch_work
        self.port = port
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
        if self.need_batch_work is not None:
            result['NeedBatchWork'] = self.need_batch_work
        if self.port is not None:
            result['Port'] = self.port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NeedBatchWork') is not None:
            self.need_batch_work = m.get('NeedBatchWork')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class RemoveVpcAccessResponseBodyApisApi(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        stage_id: str = None,
    ):
        self.api_id = api_id
        self.group_id = group_id
        self.stage_id = stage_id

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
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        return self


class RemoveVpcAccessResponseBodyApis(TeaModel):
    def __init__(
        self,
        api: List[RemoveVpcAccessResponseBodyApisApi] = None,
    ):
        self.api = api

    def validate(self):
        if self.api:
            for k in self.api:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Api'] = []
        if self.api is not None:
            for k in self.api:
                result['Api'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api = []
        if m.get('Api') is not None:
            for k in m.get('Api'):
                temp_model = RemoveVpcAccessResponseBodyApisApi()
                self.api.append(temp_model.from_map(k))
        return self


class RemoveVpcAccessResponseBody(TeaModel):
    def __init__(
        self,
        apis: RemoveVpcAccessResponseBodyApis = None,
        request_id: str = None,
    ):
        self.apis = apis
        self.request_id = request_id

    def validate(self):
        if self.apis:
            self.apis.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apis is not None:
            result['Apis'] = self.apis.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apis') is not None:
            temp_model = RemoveVpcAccessResponseBodyApis()
            self.apis = temp_model.from_map(m['Apis'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveVpcAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVpcAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveVpcAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVpcAccessAndAbolishApisRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        need_batch_work: bool = None,
        port: int = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        self.instance_id = instance_id
        self.need_batch_work = need_batch_work
        self.port = port
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
        if self.need_batch_work is not None:
            result['NeedBatchWork'] = self.need_batch_work
        if self.port is not None:
            result['Port'] = self.port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NeedBatchWork') is not None:
            self.need_batch_work = m.get('NeedBatchWork')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class RemoveVpcAccessAndAbolishApisResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
    ):
        self.operation_id = operation_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveVpcAccessAndAbolishApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVpcAccessAndAbolishApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveVpcAccessAndAbolishApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppCodeRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        security_token: str = None,
    ):
        self.app_code = app_code
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        body: ResetAppCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetAppCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAppSecretRequest(TeaModel):
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


class ResetAppSecretResponseBody(TeaModel):
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


class ResetAppSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetAppSecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetAppSecretResponseBody()
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
        body: SdkGenerateByAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: SdkGenerateByGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SdkGenerateByGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApisAuthoritiesRequest(TeaModel):
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


class SetApisAuthoritiesResponseBody(TeaModel):
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


class SetApisAuthoritiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetApisAuthoritiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetApisAuthoritiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppsAuthoritiesRequest(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        app_ids: str = None,
        auth_valid_time: str = None,
        description: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        self.api_id = api_id
        self.app_ids = app_ids
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
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
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
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
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


class SetAppsAuthoritiesResponseBody(TeaModel):
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


class SetAppsAuthoritiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAppsAuthoritiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppsAuthoritiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDomainRequest(TeaModel):
    def __init__(
        self,
        bind_stage_name: str = None,
        custom_domain_type: str = None,
        domain_name: str = None,
        group_id: str = None,
        is_force: bool = None,
    ):
        self.bind_stage_name = bind_stage_name
        self.custom_domain_type = custom_domain_type
        self.domain_name = domain_name
        self.group_id = group_id
        self.is_force = is_force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_stage_name is not None:
            result['BindStageName'] = self.bind_stage_name
        if self.custom_domain_type is not None:
            result['CustomDomainType'] = self.custom_domain_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.is_force is not None:
            result['IsForce'] = self.is_force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindStageName') is not None:
            self.bind_stage_name = m.get('BindStageName')
        if m.get('CustomDomainType') is not None:
            self.custom_domain_type = m.get('CustomDomainType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IsForce') is not None:
            self.is_force = m.get('IsForce')
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
        body: SetDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        certificate_private_key: str = None,
        domain_name: str = None,
        group_id: str = None,
        security_token: str = None,
    ):
        self.ca_certificate_body = ca_certificate_body
        self.certificate_body = certificate_body
        self.certificate_name = certificate_name
        self.certificate_private_key = certificate_private_key
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
        if self.ca_certificate_body is not None:
            result['CaCertificateBody'] = self.ca_certificate_body
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
        if m.get('CertificatePrivateKey') is not None:
            self.certificate_private_key = m.get('CertificatePrivateKey')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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
        body: SetDomainCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: SetDomainWebSocketStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: SetIpControlApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetIpControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSignatureApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        security_token: str = None,
        signature_id: str = None,
        stage_name: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.security_token = security_token
        self.signature_id = signature_id
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        return self


class SetSignatureApisResponseBody(TeaModel):
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


class SetSignatureApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetSignatureApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetSignatureApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTrafficControlApisRequest(TeaModel):
    def __init__(
        self,
        api_ids: str = None,
        group_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        traffic_control_id: str = None,
    ):
        self.api_ids = api_ids
        self.group_id = group_id
        self.security_token = security_token
        self.stage_name = stage_name
        self.traffic_control_id = traffic_control_id

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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')
        return self


class SetTrafficControlApisResponseBody(TeaModel):
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


class SetTrafficControlApisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetTrafficControlApisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetTrafficControlApisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetVpcAccessRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        security_token: str = None,
        vpc_id: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.name = name
        self.port = port
        self.security_token = security_token
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class SetVpcAccessResponseBody(TeaModel):
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


class SetVpcAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetVpcAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetVpcAccessResponseBody()
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
        body: SetWildcardDomainPatternsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        body: SwitchApiResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SwitchApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_id: List[str] = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.security_token = security_token
        self.tag_key = tag_key

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
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


