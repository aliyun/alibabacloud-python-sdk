# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiHistoryResponseBody(DaraModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        backend_config: main_models.DescribeApiHistoryResponseBodyBackendConfig = None,
        backend_enable: bool = None,
        constant_parameters: main_models.DescribeApiHistoryResponseBodyConstantParameters = None,
        custom_system_parameters: main_models.DescribeApiHistoryResponseBodyCustomSystemParameters = None,
        deployed_time: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: main_models.DescribeApiHistoryResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        history_version: str = None,
        open_id_connect_config: main_models.DescribeApiHistoryResponseBodyOpenIdConnectConfig = None,
        region_id: str = None,
        request_config: main_models.DescribeApiHistoryResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: main_models.DescribeApiHistoryResponseBodyRequestParameters = None,
        result_body_model: str = None,
        result_descriptions: main_models.DescribeApiHistoryResponseBodyResultDescriptions = None,
        result_sample: str = None,
        result_type: str = None,
        service_config: main_models.DescribeApiHistoryResponseBodyServiceConfig = None,
        service_parameters: main_models.DescribeApiHistoryResponseBodyServiceParameters = None,
        service_parameters_map: main_models.DescribeApiHistoryResponseBodyServiceParametersMap = None,
        stage_name: str = None,
        status: str = None,
        system_parameters: main_models.DescribeApiHistoryResponseBodySystemParameters = None,
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
        # The name of the API.
        self.api_name = api_name
        # The AppCode authentication type supported. Valid values:
        # 
        # *   DEFAULT: supported after being made available in Alibaba Cloud Marketplace
        # *   DISABLE: not supported.
        # *   HEADER : supported only in the Header parameter
        # *   HEADER_QUERY : supported in the Header or Query parameter.
        self.app_code_auth_type = app_code_auth_type
        # The security authentication method of the API. Valid values:
        # 
        # *   **APP: Only authorized applications can call the API.**
        # 
        # *   **ANONYMOUS: The API can be anonymously called. In this mode, you must take note of the following rules:**
        # 
        #     *   All users who have obtained the API service information can call this API. API Gateway does not authenticate callers and cannot set user-specific throttling policies. If you make this API public, set API-specific throttling policies.
        self.auth_type = auth_type
        # Backend configurations
        self.backend_config = backend_config
        # Specifies whether to enable backend services.
        self.backend_enable = backend_enable
        # The constant parameters.
        self.constant_parameters = constant_parameters
        # The custom system parameters.
        self.custom_system_parameters = custom_system_parameters
        # The publishing time (UTC) of the API.
        self.deployed_time = deployed_time
        # The description of the API.
        self.description = description
        # *   Specifies whether to set **DisableInternet** to **true** to limit API calls to within the VPC.
        # *   If you set **DisableInternet** to **false**, the limit is lifted. The default value is false when you create an API.
        self.disable_internet = disable_internet
        # The sample error codes returned by the backend service.
        # 
        # For more information, see [ErrorCodeSample](https://help.aliyun.com/document_detail/44392.html).
        self.error_code_samples = error_code_samples
        # The sample error response from the backend service.
        self.fail_result_sample = fail_result_sample
        # *   Specifies whether to set **ForceNonceCheck** to **true** to force the check of X-Ca-Nonce during the request. This is the unique identifier of the request and is generally identified by UUID. After receiving this parameter, API Gateway verifies the validity of this parameter. The same value can be used only once within 15 minutes. This helps prevent replay attacks.
        # *   If you set **ForceNonceCheck** to **false**, the check is not performed. The default value is false when you create an API.
        self.force_nonce_check = force_nonce_check
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The historical version number.
        self.history_version = history_version
        # The configuration items of the third-party OpenID Connect authentication method.
        self.open_id_connect_config = open_id_connect_config
        # The region where the API is located.
        self.region_id = region_id
        # The configuration items of API requests sent by the consumer to API Gateway.
        # 
        # For more information, see [RequestConfig](https://help.aliyun.com/document_detail/43985.html).
        self.request_config = request_config
        # The ID of the request.
        self.request_id = request_id
        # The parameters of API requests sent by the consumer to API Gateway.
        # 
        # For more information, see [RequestParameter](https://help.aliyun.com/document_detail/43986.html).
        self.request_parameters = request_parameters
        # The return description of the API.
        self.result_body_model = result_body_model
        # The return description of the API.
        self.result_descriptions = result_descriptions
        # The sample response.
        self.result_sample = result_sample
        # The type of the data to return.
        self.result_type = result_type
        # The information about a backend service call.
        self.service_config = service_config
        # The parameters of API requests sent by API Gateway to the backend service.
        # 
        # For more information, see [ServiceParameter](https://help.aliyun.com/document_detail/43988.html).
        self.service_parameters = service_parameters
        # The mappings between parameters of requests sent by the consumer to API Gateway and parameters of requests sent by API Gateway to the backend service.
        # 
        # For more information, see [ServiceParameterMap](https://help.aliyun.com/document_detail/43989.html).
        self.service_parameters_map = service_parameters_map
        # The environment in which the API is requested. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the pre-release environment
        # *   **TEST**: the test environment
        self.stage_name = stage_name
        # The invocation status of the API.
        self.status = status
        # The common parameters of the APIs, in JSON format.
        self.system_parameters = system_parameters
        # Specifies whether to make the API public. Valid values:
        # 
        # *   **PUBLIC**: Make the API public. If you set this parameter to PUBLIC, this API is displayed on the APIs page for all users after the API is published to the production environment.
        # *   **PRIVATE**: Make the API private. Private APIs are not displayed in the Alibaba Cloud Marketplace after the API group to which they belong is made available.
        self.visibility = visibility
        # The type of the two-way communication API. Valid values:
        # 
        # *   **COMMON**: general APIs
        # *   **REGISTER**: registered APIs
        # *   **UNREGISTER**: unregistered APIs
        # *   **NOTIFY**: downstream notification
        self.web_socket_api_type = web_socket_api_type

    def validate(self):
        if self.backend_config:
            self.backend_config.validate()
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

        if m.get('BackendConfig') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyBackendConfig()
            self.backend_config = temp_model.from_map(m.get('BackendConfig'))

        if m.get('BackendEnable') is not None:
            self.backend_enable = m.get('BackendEnable')

        if m.get('ConstantParameters') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyConstantParameters()
            self.constant_parameters = temp_model.from_map(m.get('ConstantParameters'))

        if m.get('CustomSystemParameters') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyCustomSystemParameters()
            self.custom_system_parameters = temp_model.from_map(m.get('CustomSystemParameters'))

        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')

        if m.get('ErrorCodeSamples') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m.get('ErrorCodeSamples'))

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
            temp_model = main_models.DescribeApiHistoryResponseBodyOpenIdConnectConfig()
            self.open_id_connect_config = temp_model.from_map(m.get('OpenIdConnectConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestConfig') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m.get('RequestConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestParameters') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m.get('RequestParameters'))

        if m.get('ResultBodyModel') is not None:
            self.result_body_model = m.get('ResultBodyModel')

        if m.get('ResultDescriptions') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyResultDescriptions()
            self.result_descriptions = temp_model.from_map(m.get('ResultDescriptions'))

        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('ServiceConfig') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfig()
            self.service_config = temp_model.from_map(m.get('ServiceConfig'))

        if m.get('ServiceParameters') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceParameters()
            self.service_parameters = temp_model.from_map(m.get('ServiceParameters'))

        if m.get('ServiceParametersMap') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceParametersMap()
            self.service_parameters_map = temp_model.from_map(m.get('ServiceParametersMap'))

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemParameters') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodySystemParameters()
            self.system_parameters = temp_model.from_map(m.get('SystemParameters'))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')

        return self

class DescribeApiHistoryResponseBodySystemParameters(DaraModel):
    def __init__(
        self,
        system_parameter: List[main_models.DescribeApiHistoryResponseBodySystemParametersSystemParameter] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodySystemParametersSystemParameter()
                self.system_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodySystemParametersSystemParameter(DaraModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        # The sample value.
        self.demo_value = demo_value
        # The description.
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

class DescribeApiHistoryResponseBodyServiceParametersMap(DaraModel):
    def __init__(
        self,
        service_parameter_map: List[main_models.DescribeApiHistoryResponseBodyServiceParametersMapServiceParameterMap] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyServiceParametersMapServiceParameterMap()
                self.service_parameter_map.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyServiceParametersMapServiceParameterMap(DaraModel):
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

class DescribeApiHistoryResponseBodyServiceParameters(DaraModel):
    def __init__(
        self,
        service_parameter: List[main_models.DescribeApiHistoryResponseBodyServiceParametersServiceParameter] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyServiceParametersServiceParameter()
                self.service_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyServiceParametersServiceParameter(DaraModel):
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

class DescribeApiHistoryResponseBodyServiceConfig(DaraModel):
    def __init__(
        self,
        content_type_catagory: str = None,
        content_type_value: str = None,
        event_bridge_config: main_models.DescribeApiHistoryResponseBodyServiceConfigEventBridgeConfig = None,
        function_compute_config: main_models.DescribeApiHistoryResponseBodyServiceConfigFunctionComputeConfig = None,
        mock: str = None,
        mock_headers: main_models.DescribeApiHistoryResponseBodyServiceConfigMockHeaders = None,
        mock_result: str = None,
        mock_status_code: int = None,
        oss_config: main_models.DescribeApiHistoryResponseBodyServiceConfigOssConfig = None,
        service_address: str = None,
        service_http_method: str = None,
        service_path: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        service_vpc_enable: str = None,
        vpc_config: main_models.DescribeApiHistoryResponseBodyServiceConfigVpcConfig = None,
        vpc_id: str = None,
    ):
        # The ContentType header type used when you call the backend service over HTTP.
        # 
        # *   DEFAULT: the default header type in API Gateway
        # *   CUSTOM: a custom header type
        # *   CLIENT: the ContentType header type of the client
        self.content_type_catagory = content_type_catagory
        # The value of the ContentType header when the ServiceProtocol parameter is set to HTTP and the ContentTypeCatagory parameter is set to DEFAULT or CUSTOM.
        self.content_type_value = content_type_value
        # Configuration items of EventBridge
        self.event_bridge_config = event_bridge_config
        # Backend configuration items when the backend service is Function Compute
        self.function_compute_config = function_compute_config
        # Specifies whether to enable the MOCK mode. Valid values:
        # 
        # *   TRUE: The Mock mode is enabled.
        # *   FALSE: The Mock mode is not enabled.
        self.mock = mock
        # The simulated Headers.
        self.mock_headers = mock_headers
        # The result returned when the Mock mode is enabled.
        self.mock_result = mock_result
        # The status code returned for service mocking.
        self.mock_status_code = mock_status_code
        # Information when the backend service is OSS
        self.oss_config = oss_config
        # The URL used to call the backend service.
        self.service_address = service_address
        # The HTTP request method used when calling the backend service. Valid values: PUT, GET, POST, DELETE, PATCH, HEAD, OPTIONS, and ANY.
        self.service_http_method = service_http_method
        # The path used when you call the backend service.
        self.service_path = service_path
        # The backend service protocol. Currently, only HTTP, HTTPS, and FunctionCompute are supported.
        self.service_protocol = service_protocol
        # The timeout period of the backend service, in millisecond.
        self.service_timeout = service_timeout
        # Specifies whether to enable the VPC channel. Valid values:
        # 
        # *   TRUE: The VPC channel is enabled.
        # *   FALSE: The VPC channel is not enabled.
        # 
        # You must create the corresponding VPC access authorization before you can enable a VPC channel.
        self.service_vpc_enable = service_vpc_enable
        # Configuration items related to VPC channels
        self.vpc_config = vpc_config
        # The ID of the VPC.
        self.vpc_id = vpc_id

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

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentTypeCatagory') is not None:
            self.content_type_catagory = m.get('ContentTypeCatagory')

        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')

        if m.get('EventBridgeConfig') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfigEventBridgeConfig()
            self.event_bridge_config = temp_model.from_map(m.get('EventBridgeConfig'))

        if m.get('FunctionComputeConfig') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfigFunctionComputeConfig()
            self.function_compute_config = temp_model.from_map(m.get('FunctionComputeConfig'))

        if m.get('Mock') is not None:
            self.mock = m.get('Mock')

        if m.get('MockHeaders') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfigMockHeaders()
            self.mock_headers = temp_model.from_map(m.get('MockHeaders'))

        if m.get('MockResult') is not None:
            self.mock_result = m.get('MockResult')

        if m.get('MockStatusCode') is not None:
            self.mock_status_code = m.get('MockStatusCode')

        if m.get('OssConfig') is not None:
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfigOssConfig()
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
            temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfigVpcConfig()
            self.vpc_config = temp_model.from_map(m.get('VpcConfig'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeApiHistoryResponseBodyServiceConfigVpcConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        vpc_id: str = None,
        vpc_scheme: str = None,
    ):
        # The IDs of the ELB and SLB instances in the VPC.
        self.instance_id = instance_id
        # The name of the VPC.
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

class DescribeApiHistoryResponseBodyServiceConfigOssConfig(DaraModel):
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

class DescribeApiHistoryResponseBodyServiceConfigMockHeaders(DaraModel):
    def __init__(
        self,
        mock_header: List[main_models.DescribeApiHistoryResponseBodyServiceConfigMockHeadersMockHeader] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyServiceConfigMockHeadersMockHeader()
                self.mock_header.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyServiceConfigMockHeadersMockHeader(DaraModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        # The HTTP headers.
        self.header_name = header_name
        # The values of the HTTP headers.
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

class DescribeApiHistoryResponseBodyServiceConfigFunctionComputeConfig(DaraModel):
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
        # The ContentType header type used when you call the backend service over HTTP.
        # 
        # *   **DEFAULT: the default header type in API Gateway.**
        # *   **CUSTOM: a custom header type.**
        # *   **CLIENT: the ContentType header type of the client.
        self.content_type_catagory = content_type_catagory
        # The value of the ContentType header when the ServiceProtocol parameter is set to HTTP and the ContentTypeCatagory parameter is set to DEFAULT or CUSTOM.
        self.content_type_value = content_type_value
        # The root path of Function Compute.
        self.fc_base_url = fc_base_url
        # The type of the Function Compute instance.
        self.fc_type = fc_type
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
        # The ID of the region.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role to be assumed by API Gateway to access Function Compute.
        self.role_arn = role_arn
        # The service name defined in Function Compute.
        self.service_name = service_name

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

class DescribeApiHistoryResponseBodyServiceConfigEventBridgeConfig(DaraModel):
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
        # The event source of the managed rule.
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

class DescribeApiHistoryResponseBodyResultDescriptions(DaraModel):
    def __init__(
        self,
        result_description: List[main_models.DescribeApiHistoryResponseBodyResultDescriptionsResultDescription] = None,
    ):
        self.result_description = result_description

    def validate(self):
        if self.result_description:
            for v1 in self.result_description:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResultDescription'] = []
        if self.result_description is not None:
            for k1 in self.result_description:
                result['ResultDescription'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result_description = []
        if m.get('ResultDescription') is not None:
            for k1 in m.get('ResultDescription'):
                temp_model = main_models.DescribeApiHistoryResponseBodyResultDescriptionsResultDescription()
                self.result_description.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyResultDescriptionsResultDescription(DaraModel):
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
        # The subnode description.
        self.description = description
        # Indicates whether a subnode exists.
        self.has_child = has_child
        # The result ID.
        self.id = id
        # The primary key of the result.
        self.key = key
        # Indicates whether the parameter is required.
        self.mandatory = mandatory
        # The result name.
        self.name = name
        # The ID of the parent node.
        self.pid = pid
        # The result type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeApiHistoryResponseBodyRequestParameters(DaraModel):
    def __init__(
        self,
        request_parameter: List[main_models.DescribeApiHistoryResponseBodyRequestParametersRequestParameter] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyRequestParametersRequestParameter(DaraModel):
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
        # The name of the parameter in the API request.
        self.api_parameter_name = api_parameter_name
        # The type of the array element.
        self.array_items_type = array_items_type
        # The default value.
        self.default_value = default_value
        # The sample value.
        self.demo_value = demo_value
        # The parameter description.
        self.description = description
        # The order in which the parameter is sorted in the document.
        self.doc_order = doc_order
        # Indicates whether the document is public. Valid values: **PUBLIC** and **PRIVATE**.
        self.doc_show = doc_show
        # The hash values that are supported when **ParameterType** is set to Int, Long, Float, Double, or String. Separate values with commas (,). Examples: 1,2,3,4,9 and A,B,C,E,F.
        self.enum_value = enum_value
        # JSON scheme
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

class DescribeApiHistoryResponseBodyRequestConfig(DaraModel):
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
        # The server data transmission method used for POST and PUT requests. Valid values: FORM and STREAM. FORM indicates that data in key-value pairs is transmitted as forms. STREAM indicates that data is transmitted as byte streams. This parameter takes effect only when the RequestMode parameter is set to MAPPING.
        self.body_format = body_format
        # The body model.
        self.body_model = body_model
        # Whether to escape the Path parameter, if true, the [param] on the Path will be treated as a regular character.
        self.escape_path_param = escape_path_param
        # The description of the request body.
        self.post_body_description = post_body_description
        # The HTTP method. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS.
        self.request_http_method = request_http_method
        # The request mode. Valid values:
        # 
        # *   MAPPING: Parameters are mapped. Unknown parameters are filtered out.
        # *   PASSTHROUGH: Parameters are passed through.
        # *   MAPPING_PASSTHROUGH: Parameters are mapped. Unknown parameters are passed through.
        self.request_mode = request_mode
        # API path
        self.request_path = request_path
        # The protocol type supported by the API. Valid values: HTTP, HTTPS, and WebSocket. Separate multiple values with commas (,), such as "HTTP,HTTPS".
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

class DescribeApiHistoryResponseBodyOpenIdConnectConfig(DaraModel):
    def __init__(
        self,
        id_token_param_name: str = None,
        open_id_api_type: str = None,
        public_key: str = None,
        public_key_id: str = None,
    ):
        # The name of the parameter that corresponds to the token.
        self.id_token_param_name = id_token_param_name
        # The configuration of OpenID Connect authentication. Valid values:
        # 
        # *   **IDTOKEN: indicates the APIs that are called by clients to obtain tokens. If you specify this value, the PublicKeyId parameter and the PublicKey parameter are required.**
        # *   **BUSINESS: indicates business APIs. Tokens are used to call the business APIs. If you specify this value, the IdTokenParamName parameter is required.
        self.open_id_api_type = open_id_api_type
        # The public key of the API.
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

class DescribeApiHistoryResponseBodyErrorCodeSamples(DaraModel):
    def __init__(
        self,
        error_code_sample: List[main_models.DescribeApiHistoryResponseBodyErrorCodeSamplesErrorCodeSample] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyErrorCodeSamplesErrorCodeSample(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
    ):
        # The returned error code.
        self.code = code
        # The error description.
        self.description = description
        # The returned error message.
        self.message = message

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

class DescribeApiHistoryResponseBodyCustomSystemParameters(DaraModel):
    def __init__(
        self,
        custom_system_parameter: List[main_models.DescribeApiHistoryResponseBodyCustomSystemParametersCustomSystemParameter] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyCustomSystemParametersCustomSystemParameter()
                self.custom_system_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyCustomSystemParametersCustomSystemParameter(DaraModel):
    def __init__(
        self,
        demo_value: str = None,
        description: str = None,
        location: str = None,
        parameter_name: str = None,
        service_parameter_name: str = None,
    ):
        # The sample value.
        self.demo_value = demo_value
        # The parameter description.
        self.description = description
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The parameter name.
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

class DescribeApiHistoryResponseBodyConstantParameters(DaraModel):
    def __init__(
        self,
        constant_parameter: List[main_models.DescribeApiHistoryResponseBodyConstantParametersConstantParameter] = None,
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
                temp_model = main_models.DescribeApiHistoryResponseBodyConstantParametersConstantParameter()
                self.constant_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiHistoryResponseBodyConstantParametersConstantParameter(DaraModel):
    def __init__(
        self,
        constant_value: str = None,
        description: str = None,
        location: str = None,
        service_parameter_name: str = None,
    ):
        # The value of the constant parameter.
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

class DescribeApiHistoryResponseBodyBackendConfig(DaraModel):
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
        # The type of the backend service.
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

