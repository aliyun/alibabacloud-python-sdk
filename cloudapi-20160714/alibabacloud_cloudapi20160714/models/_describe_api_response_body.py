# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiResponseBody(DaraModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        backend_config: main_models.DescribeApiResponseBodyBackendConfig = None,
        backend_enable: bool = None,
        constant_parameters: main_models.DescribeApiResponseBodyConstantParameters = None,
        created_time: str = None,
        custom_system_parameters: main_models.DescribeApiResponseBodyCustomSystemParameters = None,
        deployed_infos: main_models.DescribeApiResponseBodyDeployedInfos = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: main_models.DescribeApiResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        mock: str = None,
        mock_result: str = None,
        modified_time: str = None,
        open_id_connect_config: main_models.DescribeApiResponseBodyOpenIdConnectConfig = None,
        region_id: str = None,
        request_config: main_models.DescribeApiResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: main_models.DescribeApiResponseBodyRequestParameters = None,
        result_body_model: str = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: main_models.DescribeApiResponseBodyServiceConfig = None,
        service_parameters: main_models.DescribeApiResponseBodyServiceParameters = None,
        service_parameters_map: main_models.DescribeApiResponseBodyServiceParametersMap = None,
        system_parameters: main_models.DescribeApiResponseBodySystemParameters = None,
        tag_list: main_models.DescribeApiResponseBodyTagList = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        # If **AuthType** is set to **APP**, this value must be passed to specify the signature algorithm. If you do not specify a value, HmacSHA256 is used by default. Valid values:
        # 
        # *   HmacSHA256
        # *   HmacSHA1,HmacSHA256
        self.allow_signature_method = allow_signature_method
        # The ID of the API.
        self.api_id = api_id
        # The name of the API, which is unique in the group.
        self.api_name = api_name
        # If **AuthType** is set to **APP**, the valid values are:
        # 
        # *   **DEFAULT**: The default value that is used if no other values are passed. This value means that the setting of the group is used.
        # *   **DISABLE**: The authentication is disabled.
        # *   **HEADER**: AppCode can be placed in the Header parameter for authentication.
        # *   **HEADER_QUERY**: AppCode can be placed in the Header or Query parameter for authentication.
        self.app_code_auth_type = app_code_auth_type
        # The security authentication method of the API. Valid values:
        # 
        # *   **APP**: Only authorized applications can call the API.
        # 
        # *   **ANONYMOUS**: The API can be anonymously called. In this mode, you must take note of the following rules:
        # 
        #     *   All users who have obtained the API service information can call this API. API Gateway does not authenticate callers and cannot set user-specific throttling policies. If you make this API public, set API-specific throttling policies.
        #     *   We recommend that you do not make the API whose security authentication method is ANONYMOUS available in Alibaba Cloud Marketplace because API Gateway cannot meter calls on the caller or limit the number of calls on the API. If you want to make the API group to which the API belongs available in Alibaba Cloud Marketplace, we recommend that you move the API to another group, set its type to PRIVATE, or set its security authentication method to APP.
        # 
        # *   **APPOPENID**: The OpenID Connect account authentication method is used. Only applications authorized by OpenID Connect can call the API. If this method is selected, the OpenIdConnectConfig parameter is required.
        self.auth_type = auth_type
        # Backend configurations
        self.backend_config = backend_config
        # Specifies whether to enable backend services.
        self.backend_enable = backend_enable
        # System parameters sent by API Gateway to the backend service
        self.constant_parameters = constant_parameters
        # The creation time of the API.
        self.created_time = created_time
        # Custom system parameters
        self.custom_system_parameters = custom_system_parameters
        # The API publishing status.
        self.deployed_infos = deployed_infos
        # The description of the API.
        self.description = description
        # Specifies whether to limit API calls to within the VPC. Valid values:
        # 
        # *   **true**: Only API calls from the VPC are supported.
        # *   **false**: API calls from the VPC and Internet are both supported.
        self.disable_internet = disable_internet
        # The sample error codes returned by the backend service.
        self.error_code_samples = error_code_samples
        # The sample error response from the backend service.
        self.fail_result_sample = fail_result_sample
        # Specifies whether to carry the header : X-Ca-Nonce when calling an API. This is the unique identifier of the request and is generally identified by UUID. After receiving this parameter, API Gateway verifies the validity of this parameter. The same value can be used only once within 15 minutes. This helps prevent reply attacks. Valid values:
        # 
        # *   **true**: This field is forcibly checked when an API is requested to prevent replay attacks.
        # *   **false**: This field is not checked.
        self.force_nonce_check = force_nonce_check
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # Specifies whether to enable the Mock mode. Valid values:
        # 
        # *   OPEN: The Mock mode is enabled.
        # *   CLOSED: The Mock mode is not enabled.
        self.mock = mock
        # The result returned for service mocking.
        self.mock_result = mock_result
        # The last modification time of the API.
        self.modified_time = modified_time
        # Configuration items of the third-party OpenID Connect authentication method
        self.open_id_connect_config = open_id_connect_config
        # The region ID of the API.
        self.region_id = region_id
        # The configuration items of API requests sent by the consumer to API Gateway.
        self.request_config = request_config
        # The ID of the request.
        self.request_id = request_id
        # The parameters of API requests sent by the consumer to API Gateway.
        self.request_parameters = request_parameters
        # The returned description of the API.
        self.result_body_model = result_body_model
        # The sample response from the backend service.
        self.result_sample = result_sample
        # The format of the response from the backend service. Valid values: JSON, TEXT, BINARY, XML, and HTML.
        self.result_type = result_type
        # The configuration items of API requests that API Gateway sends to the backend service.
        self.service_config = service_config
        # The parameters of API requests sent by API Gateway to the backend service.
        self.service_parameters = service_parameters
        # The mappings between parameters of requests sent by the consumer to API Gateway and parameters of requests sent by API Gateway to the backend service.
        self.service_parameters_map = service_parameters_map
        # System parameters sent by API Gateway to the backend service
        self.system_parameters = system_parameters
        # Tag List.
        self.tag_list = tag_list
        # Specifies whether to make the API public. Valid values:
        # 
        # *   **PUBLIC**: Make the API public. If you set this parameter to PUBLIC, this API is displayed on the APIs page for all users after the API is published to the production environment.
        # *   **PRIVATE**: Make the API private. Private APIs are not displayed in the Alibaba Cloud Marketplace after the API group to which they belong is made available.
        self.visibility = visibility
        # The type of the two-way communication API.
        # 
        # *   **COMMON**: common API
        # *   **REGISTER**: registered API
        # *   **UNREGISTER**: unregistered API
        # *   **NOTIFY**: downstream notification API
        self.web_socket_api_type = web_socket_api_type

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
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
        if self.service_config:
            self.service_config.validate()
        if self.service_parameters:
            self.service_parameters.validate()
        if self.service_parameters_map:
            self.service_parameters_map.validate()
        if self.system_parameters:
            self.system_parameters.validate()
        if self.tag_list:
            self.tag_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.backend_config is not None:
            result['BackendConfig'] = self.backend_config.to_map()

        if self.backend_enable is not None:
            result['BackendEnable'] = self.backend_enable

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

        if self.tag_list is not None:
            result['TagList'] = self.tag_list.to_map()

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

        if m.get('BackendConfig') is not None:
            temp_model = main_models.DescribeApiResponseBodyBackendConfig()
            self.backend_config = temp_model.from_map(m.get('BackendConfig'))

        if m.get('BackendEnable') is not None:
            self.backend_enable = m.get('BackendEnable')

        if m.get('ConstantParameters') is not None:
            temp_model = main_models.DescribeApiResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m.get('ConstantParameters'))

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CustomSystemParameters') is not None:
            temp_model = main_models.DescribeApiResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m.get('CustomSystemParameters'))

        if m.get('DeployedInfos') is not None:
            temp_model = main_models.DescribeApiResponseBodyDeployedInfos()
            self.deployed_infos = temp_model.from_map(m.get('DeployedInfos'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')

        if m.get('ErrorCodeSamples') is not None:
            temp_model = main_models.DescribeApiResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m.get('ErrorCodeSamples'))

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
            temp_model = main_models.DescribeApiResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m.get('OpenIdConnectConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestConfig') is not None:
            temp_model = main_models.DescribeApiResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m.get('RequestConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestParameters') is not None:
            temp_model = main_models.DescribeApiResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m.get('RequestParameters'))

        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')

        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('ServiceConfig') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m.get('ServiceConfig'))

        if m.get('ServiceParameters') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceParameters()
            self.service_parameters = temp_model.from_map(m.get('ServiceParameters'))

        if m.get('ServiceParametersMap') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceParametersMap()
            self.service_parameters_map = temp_model.from_map(m.get('ServiceParametersMap'))

        if m.get('SystemParameters') is not None:
            temp_model = main_models.DescribeApiResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m.get('SystemParameters'))

        if m.get('TagList') is not None:
            temp_model = main_models.DescribeApiResponseBodyTagList()
            self.tag_list = temp_model.from_map(m.get('TagList'))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')

        return self

class DescribeApiResponseBodyTagList(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeApiResponseBodyTagListTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeApiResponseBodyTagListTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyTagListTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # Label key.
        self.tag_key = tag_key
        # Label value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeApiResponseBodySystemParameters(DaraModel):
    def __init__(
        self,
        system_parameter: List[main_models.DescribeApiResponseBodySystemParametersSystemParameter] = None,
    ):
        self.system_parameter = system_parameter

    def validate(self):
        if self.system_parameter:
            for v1 in self.system_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SystemParameter'] = []
        if self.system_parameter is not None:
            for k1 in self.system_parameter:
                result['SystemParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_parameter = []
        if m.get('SystemParameter') is not None:
            for k1 in m.get('SystemParameter'):
                temp_model = main_models.DescribeApiResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodySystemParametersSystemParameter(DaraModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        # The example value.
        self.demo_value = demo_value
        # The parameter description.
        self.description = description
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The system parameter. Valid values: CaClientIp, CaDomain, CaRequestHandleTime, CaAppId, CaRequestId, CaHttpSchema, and CaProxy.
        self.parameter_name = parameter_name
        # The mapped parameter name in the backend service.
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyServiceParametersMap(DaraModel):
    def __init__(
        self,
        service_parameter_map: List[main_models.DescribeApiResponseBodyServiceParametersMapServiceParameterMap] = None,
    ):
        self.service_parameter_map = service_parameter_map

    def validate(self):
        if self.service_parameter_map:
            for v1 in self.service_parameter_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceParameterMap'] = []
        if self.service_parameter_map is not None:
            for k1 in self.service_parameter_map:
                result['ServiceParameterMap'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_parameter_map = []
        if m.get('ServiceParameterMap') is not None:
            for k1 in m.get('ServiceParameterMap'):
                temp_model = main_models.DescribeApiResponseBodyServiceParametersMapServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyServiceParametersMapServiceParameterMap(DaraModel):
    def __init__(
        self,
        request_parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        # The corresponding frontend parameter name. The value must be contained in RequestParametersObject and match RequestParam.ApiParameterName.
        self.request_parameter_name = request_parameter_name
        # The mapped parameter name in the backend service.
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyServiceParameters(DaraModel):
    def __init__(
        self,
        service_parameter: List[main_models.DescribeApiResponseBodyServiceParametersServiceParameter] = None,
    ):
        self.service_parameter = service_parameter

    def validate(self):
        if self.service_parameter:
            for v1 in self.service_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServiceParameter'] = []
        if self.service_parameter is not None:
            for k1 in self.service_parameter:
                result['ServiceParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_parameter = []
        if m.get('ServiceParameter') is not None:
            for k1 in m.get('ServiceParameter'):
                temp_model = main_models.DescribeApiResponseBodyServiceParametersServiceParameter()
                self.service_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyServiceParametersServiceParameter(DaraModel):
    def __init__(
        self,
        location: str = None,
        parameter_type: str = None,
        service_parameter_name: str = None,
    ):
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The data type of the parameter. Valid values: STRING, NUMBER, and BOOLEAN.
        self.parameter_type = parameter_type
        # The mapped parameter name in the backend service.
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyServiceConfig(DaraModel):
    def __init__(
        self,
        aone_app_name: str = None,
        content_type_catagory: str = None,
        content_type_value: str = None,
        event_bridge_config: main_models.DescribeApiResponseBodyServiceConfigEventBridgeConfig = None,
        function_compute_config: main_models.DescribeApiResponseBodyServiceConfigFunctionComputeConfig = None,
        mock: str = None,
        mock_headers: main_models.DescribeApiResponseBodyServiceConfigMockHeaders = None,
        mock_result: str = None,
        mock_status_code: int = None,
        oss_config: main_models.DescribeApiResponseBodyServiceConfigOssConfig = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        vpc_config: main_models.DescribeApiResponseBodyServiceConfigVpcConfig = None,
    ):
        # The application name in AONE.
        self.aone_app_name = aone_app_name
        # The ContentType header type used when you call the backend service over HTTP.
        # 
        # *   **DEFAULT**: the default header type in API Gateway
        # *   **CUSTOM**: a custom header type
        # *   **CLIENT**: the ContentType header type of the client
        self.content_type_catagory = content_type_catagory
        # The value of the ContentType header when the ServiceProtocol parameter is set to HTTP and the ContentTypeCatagory parameter is set to DEFAULT or CUSTOM.
        self.content_type_value = content_type_value
        # Configuration items of EventBridge
        self.event_bridge_config = event_bridge_config
        # Backend configuration items when the backend service is Function Compute
        self.function_compute_config = function_compute_config
        # Specifies whether to enable the Mock mode. Valid values:
        # 
        # *   **TRUE**: The Mock mode is enabled.
        # *   **FALSE**: The Mock mode is not enabled.
        self.mock = mock
        # The simulated headers.
        self.mock_headers = mock_headers
        # The result returned when the Mock mode is enabled.
        self.mock_result = mock_result
        # The status code returned for service mocking.
        self.mock_status_code = mock_status_code
        # The information returned when the backend service is Object Storage Service (OSS).
        self.oss_config = oss_config
        # The URL used to call the back-end service. If the complete back-end service URL is `http://api.a.com:8080/object/add?key1=value1&key2=value2`, the value of ServiceAddress is **http://api.a.com:8080**.``
        self.service_address = service_address
        # The HTTP method used to call a backend service. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS.
        self.service_http_method = service_http_method
        self.service_path = service_path
        # The protocol used by the backend service. Valid values: HTTP and HTTPS.
        self.service_protocol = service_protocol
        # The timeout period of the backend service. Unit: milliseconds.
        self.service_timeout = service_timeout
        # Specifies whether to enable the VPC channel. Valid values:
        # 
        # *   **TRUE**: The VPC channel is enabled. You must create the corresponding VPC access authorization before you can enable a VPC channel.
        # *   **FALSE**: The VPC channel is not enabled.
        self.service_vpc_enable = service_vpc_enable
        # Configuration items related to VPC channels
        self.vpc_config = vpc_config

    def validate(self):
        if self.event_bridge_config:
            self.event_bridge_config.validate()
        if self.function_compute_config:
            self.function_compute_config.validate()
        if self.mock_headers:
            self.mock_headers.validate()
        if self.oss_config:
            self.oss_config.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aone_app_name is not None:
            result['AoneAppName'] = self.aone_app_name

        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory

        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value

        if self.event_bridge_config is not None:
            result['EventBridgeConfig'] = self.event_bridge_config.to_map()

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

        if m.get('EventBridgeConfig') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceConfigEventBridgeConfig()
            self.event_bridge_config = temp_model.from_map(m.get('EventBridgeConfig'))

        if m.get('FunctionComputeConfig') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m.get('FunctionComputeConfig'))

        if m.get('Mock') is not None:
            self.mock = m.get('Mock')

        if m.get('MockHeaders') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceConfigMockHeaders()
            self.mock_headers = temp_model.from_map(m.get('MockHeaders'))

        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')

        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')

        if m.get('OssConfig') is not None:
            temp_model = main_models.DescribeApiResponseBodyServiceConfigOssConfig()
            self.oss_config = temp_model.from_map(m.get('OssConfig'))

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
            temp_model = main_models.DescribeApiResponseBodyServiceConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m.get('VpcConfig'))

        return self

class DescribeApiResponseBodyServiceConfigVpcConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
        vpc_scheme: str = None,
    ):
        # The ID of the ECS or SLB instance in the VPC.
        self.instance_id = instance_id
        # The name of the VPC access authorization.
        self.name = name
        # The port number that corresponds to the instance.
        self.port = port
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The VPC protocol.
        self.vpc_scheme = vpc_scheme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyServiceConfigOssConfig(DaraModel):
    def __init__(
        self,
        action: str = None,
        bucket_name: str = None,
        key: str = None,
        oss_region_id: str = None,
    ):
        # The operation options on OSS. Valid values:
        # 
        # *   GetObject
        # *   PostObject
        # *   DeleteObject
        # *   PutObject
        # *   HeadObject
        # *   GetObjectMeta
        # *   AppendObject
        self.action = action
        # The OSS bucket.
        self.bucket_name = bucket_name
        # The stored object or folder path.
        self.key = key
        # The ID of the region where the OSS instance is located.
        self.oss_region_id = oss_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyServiceConfigMockHeaders(DaraModel):
    def __init__(
        self,
        mock_header: List[main_models.DescribeApiResponseBodyServiceConfigMockHeadersMockHeader] = None,
    ):
        self.mock_header = mock_header

    def validate(self):
        if self.mock_header:
            for v1 in self.mock_header:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MockHeader'] = []
        if self.mock_header is not None:
            for k1 in self.mock_header:
                result['MockHeader'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mock_header = []
        if m.get('MockHeader') is not None:
            for k1 in m.get('MockHeader'):
                temp_model = main_models.DescribeApiResponseBodyServiceConfigMockHeadersMockHeader()
                self.mock_header.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyServiceConfigMockHeadersMockHeader(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        # The HTTP header.
        self.header_name = header_name
        # The value of the HTTP header.
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyServiceConfigFunctionComputeConfig(DaraModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        fc_base_url: str = None,
        fc_type: str = None,
        fc_version: str = None,
        function_name: str = None,
        method: str = None,
        only_business_path: bool = None,
        path: str = None,
        qualifier: str = None,
        region_id: str = None,
        role_arn: str = None,
        service_name: str = None,
        trigger_name: str = None,
    ):
        # The ContentType header type used when you call the backend service over HTTP.
        # 
        # *   **DEFAULT**: the default header type in API Gateway
        # *   **CUSTOM**: a custom header type
        # *   **CLIENT**: the ContentType header type of the client
        self.content_type_catagory = content_type_catagory
        # The value of the ContentType header when the ContentTypeCatagory parameter is set to DEFAULT or CUSTOM.
        self.content_type_value = content_type_value
        # The root path of Function Compute.
        self.fc_base_url = fc_base_url
        # The type of the Function Compute instance.
        self.fc_type = fc_type
        self.fc_version = fc_version
        # The function name defined in Function Compute.
        self.function_name = function_name
        # The request method.
        self.method = method
        # The backend only receives the service path.
        self.only_business_path = only_business_path
        # The API request path.
        self.path = path
        # The alias of the function.
        self.qualifier = qualifier
        # The region where the Function Compute instance is located.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role to be assumed by API Gateway to access Function Compute.
        self.role_arn = role_arn
        # The service name defined in Function Compute.
        self.service_name = service_name
        # The name of the trigger.
        # 
        # You can specify the TriggerName or TriggerUrl parameter. The TriggerName parameter is optional.
        self.trigger_name = trigger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type_catagory is not None:
            result['ContentTypeCatagory'] = self.content_type_catagory

        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value

        if self.fc_base_url is not None:
            result['FcBaseUrl'] = self.fc_base_url

        if self.fc_type is not None:
            result['FcType'] = self.fc_type

        if self.fc_version is not None:
            result['FcVersion'] = self.fc_version

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

        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name

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

        if m.get('FcVersion') is not None:
            self.fc_version = m.get('FcVersion')

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

        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')

        return self

class DescribeApiResponseBodyServiceConfigEventBridgeConfig(DaraModel):
    def __init__(
        self,
        event_bridge_region_id: str = None,
        event_bus: str = None,
        event_source: str = None,
        role_arn: str = None,
    ):
        # The ID of the region where the EventBridge instance is located.
        self.event_bridge_region_id = event_bridge_region_id
        # The event bus.
        self.event_bus = event_bus
        # The event source.
        self.event_source = event_source
        # The Arn that is authorized by a RAM user to EventBridge.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bridge_region_id is not None:
            result['EventBridgeRegionId'] = self.event_bridge_region_id

        if self.event_bus is not None:
            result['EventBus'] = self.event_bus

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBridgeRegionId') is not None:
            self.event_bridge_region_id = m.get('EventBridgeRegionId')

        if m.get('EventBus') is not None:
            self.event_bus = m.get('EventBus')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class DescribeApiResponseBodyRequestParameters(DaraModel):
    def __init__(
        self,
        request_parameter: List[main_models.DescribeApiResponseBodyRequestParametersRequestParameter] = None,
    ):
        self.request_parameter = request_parameter

    def validate(self):
        if self.request_parameter:
            for v1 in self.request_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RequestParameter'] = []
        if self.request_parameter is not None:
            for k1 in self.request_parameter:
                result['RequestParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_parameter = []
        if m.get('RequestParameter') is not None:
            for k1 in m.get('RequestParameter'):
                temp_model = main_models.DescribeApiResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyRequestParametersRequestParameter(DaraModel):
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
        # The parameter name.
        self.api_parameter_name = api_parameter_name
        # The type of the array element.
        self.array_items_type = array_items_type
        # The default value.
        self.default_value = default_value
        # The example value.
        self.demo_value = demo_value
        # The parameter description.
        self.description = description
        # The order in which the parameter is sorted in the document.
        self.doc_order = doc_order
        # Indicates whether the document is public. Valid values: **PUBLIC** and **PRIVATE**.
        self.doc_show = doc_show
        # The hash values that are supported when **ParameterType** is set to Int, Long, Float, Double, or String. Separate values with commas (,). Examples: 1,2,3,4,9 and A,B,C,E,F.
        self.enum_value = enum_value
        # The JSON Schema used for JSON validation when **ParameterType** is set to String.
        self.json_scheme = json_scheme
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The maximum parameter length when **ParameterType** is set to String.
        self.max_length = max_length
        # The maximum parameter value when **ParameterType** is set to Int, Long, Float, or Double.
        self.max_value = max_value
        # The minimum parameter length when **ParameterType** is set to String.
        self.min_length = min_length
        # The minimum parameter value when **ParameterType** is set to Int, Long, Float, or Double.
        self.min_value = min_value
        # The data type of the parameter. Valid values: String, Int, Long, Float, Double, and Boolean.
        self.parameter_type = parameter_type
        # The regular expression that is used for parameter validation when **ParameterType** is set to String.
        self.regular_expression = regular_expression
        # Indicates whether the parameter is required. Valid values: **REQUIRED** and **OPTIONAL**.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyRequestConfig(DaraModel):
    def __init__(
        self,
        body_format: str = None,
        body_model: str = None,
        escape_path_param: bool = None,
        post_body_description: str = None,
        request_http_method: str = None,
        request_mode: str = None,
        request_path: str = None,
        request_protocol: str = None,
    ):
        # This parameter takes effect only when the RequestMode parameter is set to MAPPING.********
        # 
        # The server data transmission method used for POST and PUT requests. Valid values: FORM and STREAM. FORM indicates that data in key-value pairs is transmitted as forms. STREAM indicates that data is transmitted as byte streams.
        self.body_format = body_format
        # The body model.
        self.body_model = body_model
        # Whether to escape the Path parameter, if true, the [param] on the Path will be treated as a regular character.
        self.escape_path_param = escape_path_param
        # The description of the request body.
        self.post_body_description = post_body_description
        # The HTTP method used to make the request. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS.
        self.request_http_method = request_http_method
        # The request mode. Valid values: MAPPING and PASSTHROUGH.
        self.request_mode = request_mode
        # The API request path. If the complete API URL is `http://api.a.com:8080/object/add?key1=value1&key2=value2`, the API request path is ` /object/add  `.
        self.request_path = request_path
        # The protocol type supported by the API. Valid values: HTTP and HTTPS. Separate multiple values with commas (,), such as "HTTP,HTTPS".
        self.request_protocol = request_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format

        if self.body_model is not None:
            result['BodyModel'] = self.body_model

        if self.escape_path_param is not None:
            result['EscapePathParam'] = self.escape_path_param

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

        if m.get('EscapePathParam') is not None:
            self.escape_path_param = m.get('EscapePathParam')

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

class DescribeApiResponseBodyOpenIdConnectConfig(DaraModel):
    def __init__(
        self,
        id_token_param_name: str = None,
        open_id_api_type: str = None,
        public_key: str = None,
        public_key_id: str = None,
    ):
        # The name of the parameter that corresponds to the token.
        self.id_token_param_name = id_token_param_name
        # The OpenID Connect mode. Valid values:
        # 
        # *   **IDTOKEN**: indicates the APIs that are called by clients to obtain tokens. If you specify this value, the PublicKeyId parameter and the PublicKey parameter are required.
        # *   **BUSINESS**: indicates business APIs. Tokens are used to call the business APIs. If you specify this value, the IdTokenParamName parameter is required.
        self.open_id_api_type = open_id_api_type
        # The public key.
        self.public_key = public_key
        # The ID of the public key.
        self.public_key_id = public_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyErrorCodeSamples(DaraModel):
    def __init__(
        self,
        error_code_sample: List[main_models.DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample] = None,
    ):
        self.error_code_sample = error_code_sample

    def validate(self):
        if self.error_code_sample:
            for v1 in self.error_code_sample:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k1 in self.error_code_sample:
                result['ErrorCodeSample'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k1 in m.get('ErrorCodeSample'):
                temp_model = main_models.DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyErrorCodeSamplesErrorCodeSample(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
        model: str = None,
    ):
        # The returned error code.
        self.code = code
        # The error description.
        self.description = description
        # The returned error message.
        self.message = message
        # The model.
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyDeployedInfos(DaraModel):
    def __init__(
        self,
        deployed_info: List[main_models.DescribeApiResponseBodyDeployedInfosDeployedInfo] = None,
    ):
        self.deployed_info = deployed_info

    def validate(self):
        if self.deployed_info:
            for v1 in self.deployed_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployedInfo'] = []
        if self.deployed_info is not None:
            for k1 in self.deployed_info:
                result['DeployedInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_info = []
        if m.get('DeployedInfo') is not None:
            for k1 in m.get('DeployedInfo'):
                temp_model = main_models.DescribeApiResponseBodyDeployedInfosDeployedInfo()
                self.deployed_info.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyDeployedInfosDeployedInfo(DaraModel):
    def __init__(
        self,
        deployed_status: str = None,
        effective_version: str = None,
        stage_name: str = None,
    ):
        # The deployment status. Valid values: DEPLOYED and NONDEPLOYED.
        self.deployed_status = deployed_status
        # The effective version.
        self.effective_version = effective_version
        # The environment to which the API is published. Valid values: RELEASE and TEST.
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyCustomSystemParameters(DaraModel):
    def __init__(
        self,
        custom_system_parameter: List[main_models.DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter] = None,
    ):
        self.custom_system_parameter = custom_system_parameter

    def validate(self):
        if self.custom_system_parameter:
            for v1 in self.custom_system_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomSystemParameter'] = []
        if self.custom_system_parameter is not None:
            for k1 in self.custom_system_parameter:
                result['CustomSystemParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_system_parameter = []
        if m.get('CustomSystemParameter') is not None:
            for k1 in m.get('CustomSystemParameter'):
                temp_model = main_models.DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyCustomSystemParametersCustomSystemParameter(DaraModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        # The example value.
        self.demo_value = demo_value
        # The parameter description.
        self.description = description
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The name of the system parameter. Valid values: CaClientIp, CaDomain, CaRequestHandleTime, CaAppId, CaRequestId, CaHttpSchema, and CaProxy.
        self.parameter_name = parameter_name
        # The mapped parameter name in the backend service.
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyConstantParameters(DaraModel):
    def __init__(
        self,
        constant_parameter: List[main_models.DescribeApiResponseBodyConstantParametersConstantParameter] = None,
    ):
        self.constant_parameter = constant_parameter

    def validate(self):
        if self.constant_parameter:
            for v1 in self.constant_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConstantParameter'] = []
        if self.constant_parameter is not None:
            for k1 in self.constant_parameter:
                result['ConstantParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constant_parameter = []
        if m.get('ConstantParameter') is not None:
            for k1 in m.get('ConstantParameter'):
                temp_model = main_models.DescribeApiResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiResponseBodyConstantParametersConstantParameter(DaraModel):
    def __init__(
        self,
        constant_value: str = None,
        description: str = None,
        location: str = None,
        service_parameter_name: str = None,
    ):
        # The constant parameter value.
        self.constant_value = constant_value
        # The parameter description.
        self.description = description
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The mapped parameter name in the backend service.
        self.service_parameter_name = service_parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiResponseBodyBackendConfig(DaraModel):
    def __init__(
        self,
        backend_id: str = None,
        backend_name: str = None,
        backend_type: str = None,
    ):
        # The ID of the backend service.
        self.backend_id = backend_id
        # The name of the backend service.
        self.backend_name = backend_name
        # Backend service type
        self.backend_type = backend_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.backend_type is not None:
            result['BackendType'] = self.backend_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('BackendType') is not None:
            self.backend_type = m.get('BackendType')

        return self

