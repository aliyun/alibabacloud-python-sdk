# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApiConfigurationRequest(DaraModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_id: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        backend_name: str = None,
        body_format: str = None,
        body_model: str = None,
        content_type_category: str = None,
        content_type_value: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: str = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        function_compute_config: str = None,
        http_config: str = None,
        mock_config: str = None,
        model_name: str = None,
        oss_config: str = None,
        post_body_description: str = None,
        request_http_method: str = None,
        request_mode: str = None,
        request_parameters: str = None,
        request_path: str = None,
        request_protocol: str = None,
        result_sample: str = None,
        result_type: str = None,
        security_token: str = None,
        service_parameters: str = None,
        service_parameters_map: str = None,
        service_protocol: str = None,
        service_timeout: int = None,
        use_backend_service: bool = None,
        visibility: str = None,
        vpc_config: str = None,
    ):
        # If the **AuthType** parameter is set to **APP**, you must include this parameter to specify the signature algorithm. If you do not specify a value, HmacSHA256 is used by default. Valid values:
        # 
        # *   HmacSHA256
        # *   HmacSHA1,HmacSHA256
        self.allow_signature_method = allow_signature_method
        # The ID of the API.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # If the **AuthType** parameter is set to **APP**, the valid values are:
        # 
        # *   **DEFAULT**: The default value that is used if no other values are passed. This value indicates that the settings of the group are used.
        # *   **DISABLE**: The authentication is disabled.
        # *   **HEADER**: AppCode can be placed in the Header parameter for authentication.
        # *   **HEADER_QUERY**: AppCode can be placed in the Header or Query parameter for authentication.
        self.app_code_auth_type = app_code_auth_type
        # API安全认证类型，目前可以取值：
        # 
        # - **APP**：只允许已授权的APP调用
        # - **ANONYMOUS**：允许匿名调用，设置为允许匿名调用需要注意：
        #      - 任何能够获取该API服务信息的人，都将能够调用该API。网关不会对调用者做身份认证，也无法设置按用户的流量控制，若开放该API请设置好按API的流量控制；
        #      - AppCodeAuthType的值不会生效。
        self.auth_type = auth_type
        # The name of the backend service. This parameter takes effect only when the UseBackendService parameter is set to TRUE.
        self.backend_name = backend_name
        # This parameter takes effect only when the **RequestMode** parameter is set to **MAPPING**.
        # 
        # The format in which data is transmitted to the server for POST and PUT requests. Valid values: **FORM** and **STREAM**. FORM indicates that data is transmitted in the key-value pair format. STREAM indicates that data is transmitted as byte streams.
        self.body_format = body_format
        # The body model.
        self.body_model = body_model
        # The ContentType configuration of the backend request.
        # 
        # *   DEFAULT: the default configuration in API Gateway
        # *   CUSTOM: a custom configuration
        self.content_type_category = content_type_category
        # The value of the ContentType header when the ServiceProtocol parameter is set to HTTP and the ContentTypeCatagory parameter is set to DEFAULT or CUSTOM.
        self.content_type_value = content_type_value
        # The description of the API.
        self.description = description
        # *   Specifies whether to call the API only in an internal network. If the **DisableInternet** parameter is set to **true**, the API can be called only in an internal network.
        # *   If the **DisableInternet** parameter is set to **false**, the API can be called over the Internet and in an internal network.
        self.disable_internet = disable_internet
        # The sample error codes returned by the backend service.
        # 
        # For more information, see [ErrorCodeSample](https://help.aliyun.com/document_detail/44392.html).
        self.error_code_samples = error_code_samples
        # The sample error response from the backend service. This value is used only to generate documents. It does not affect the returned result.
        self.fail_result_sample = fail_result_sample
        # *   Specifies whether to forcibly check X-Ca-Nonce. If the **ForceNonceCheck** parameter is set to **true**, X-Ca-Nonce is forcibly checked. X-Ca-Nonce is the unique identifier of the request and is generally identified by UUID. After receiving this parameter, API Gateway verifies the validity of this parameter. The same value can be used only once within 15 minutes. This helps prevent replay attacks.
        # *   If the **ForceNonceCheck** parameter is set to **false**, X-Ca-Nonce is not checked. If you do not modify this parameter when you modify an API, the original value is used.
        self.force_nonce_check = force_nonce_check
        # The Function Compute configuration.
        self.function_compute_config = function_compute_config
        # The HTTP configuration.
        self.http_config = http_config
        # The Mock configuration.
        self.mock_config = mock_config
        # The name of the model.
        self.model_name = model_name
        # The OSS configuration.
        self.oss_config = oss_config
        # The description of the request body.
        self.post_body_description = post_body_description
        # The HTTP method used to make the request. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS.
        self.request_http_method = request_http_method
        # The request mode. Valid values:
        # 
        # *   MAPPING: Parameters are mapped. Unknown parameters are filtered out.
        # *   PASSTHROUGH: Parameters are passed through.
        # *   MAPPING_PASSTHROUGH: Parameters are mapped. Unknown parameters are passed through.
        self.request_mode = request_mode
        # The parameters of API requests sent by the consumer to API Gateway.
        # 
        # For more information, see [RequestParameter](https://help.aliyun.com/document_detail/43986.html).
        self.request_parameters = request_parameters
        # The path of the API request. If the complete API URL is `http://api.a.com:8080/object/add?key1=value1&key2=value2`, the path of the API request is `/object/add`.
        self.request_path = request_path
        # The protocol type supported by the API. Valid values: HTTP and HTTPS. Separate multiple values with commas (,), such as "HTTP,HTTPS".
        self.request_protocol = request_protocol
        # The sample response from the backend service. This value is used only to generate documents. It does not affect the returned result.
        self.result_sample = result_sample
        # The format of the response from the backend service. Valid values: JSON, TEXT, BINARY, XML, and HTML. This value is used only to generate documents. It does not affect the returned result.
        self.result_type = result_type
        self.security_token = security_token
        # The parameters of API requests sent by API Gateway to the backend service.
        # 
        # For more information, see [ServiceParameter](https://help.aliyun.com/document_detail/43988.html).
        self.service_parameters = service_parameters
        # The mappings between parameters of requests sent by the consumer to API Gateway and parameters of requests sent by API Gateway to the backend service.
        # 
        # For more information, see [ServiceParameterMap](https://help.aliyun.com/document_detail/43989.html).
        self.service_parameters_map = service_parameters_map
        # The protocol that is used to access backend services. Valid values:
        # 
        # *   Http: for backend services that use HTTP or HTTPS
        # *   Vpc: for backend services that use VPC
        # *   FC: for Function Compute
        # *   OSS: for Object Storage Service
        # *   Mock: for backend services that use the Mock mode
        # *   EventBridge: for EventBridge
        # 
        # You must specify the config value for the corresponding backend service.
        self.service_protocol = service_protocol
        # The timeout period of the backend service. Unit: milliseconds.
        self.service_timeout = service_timeout
        # Specifies whether to use the information about the created backend service. Valid values:
        # 
        # *   TRUE: uses the information about the created backend service.
        # *   FALSE: uses the information about the custom backend service.
        self.use_backend_service = use_backend_service
        # Specifies whether to make the API public. Valid values:
        # 
        # *   **PUBLIC:** The API is public. If this parameter is set to PUBLIC, the API is displayed on the APIs page for all users after the API is published to the production environment.
        # *   **PRIVATE:** The API is private. Private APIs are not displayed in the Alibaba Cloud Marketplace after the API group to which they belong is made available.
        self.visibility = visibility
        # The VPC configuration.
        self.vpc_config = vpc_config

    def validate(self):
        pass

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

        if self.backend_name is not None:
            result['BackendName'] = self.backend_name

        if self.body_format is not None:
            result['BodyFormat'] = self.body_format

        if self.body_model is not None:
            result['BodyModel'] = self.body_model

        if self.content_type_category is not None:
            result['ContentTypeCategory'] = self.content_type_category

        if self.content_type_value is not None:
            result['ContentTypeValue'] = self.content_type_value

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

        if self.function_compute_config is not None:
            result['FunctionComputeConfig'] = self.function_compute_config

        if self.http_config is not None:
            result['HttpConfig'] = self.http_config

        if self.mock_config is not None:
            result['MockConfig'] = self.mock_config

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.oss_config is not None:
            result['OssConfig'] = self.oss_config

        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description

        if self.request_http_method is not None:
            result['RequestHttpMethod'] = self.request_http_method

        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode

        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters

        if self.request_path is not None:
            result['RequestPath'] = self.request_path

        if self.request_protocol is not None:
            result['RequestProtocol'] = self.request_protocol

        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        if self.service_parameters_map is not None:
            result['ServiceParametersMap'] = self.service_parameters_map

        if self.service_protocol is not None:
            result['ServiceProtocol'] = self.service_protocol

        if self.service_timeout is not None:
            result['ServiceTimeout'] = self.service_timeout

        if self.use_backend_service is not None:
            result['UseBackendService'] = self.use_backend_service

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.vpc_config is not None:
            result['VpcConfig'] = self.vpc_config

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

        if m.get('BackendName') is not None:
            self.backend_name = m.get('BackendName')

        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')

        if m.get('BodyModel') is not None:
            self.body_model = m.get('BodyModel')

        if m.get('ContentTypeCategory') is not None:
            self.content_type_category = m.get('ContentTypeCategory')

        if m.get('ContentTypeValue') is not None:
            self.content_type_value = m.get('ContentTypeValue')

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

        if m.get('FunctionComputeConfig') is not None:
            self.function_compute_config = m.get('FunctionComputeConfig')

        if m.get('HttpConfig') is not None:
            self.http_config = m.get('HttpConfig')

        if m.get('MockConfig') is not None:
            self.mock_config = m.get('MockConfig')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('OssConfig') is not None:
            self.oss_config = m.get('OssConfig')

        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')

        if m.get('RequestHttpMethod') is not None:
            self.request_http_method = m.get('RequestHttpMethod')

        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')

        if m.get('RequestParameters') is not None:
            self.request_parameters = m.get('RequestParameters')

        if m.get('RequestPath') is not None:
            self.request_path = m.get('RequestPath')

        if m.get('RequestProtocol') is not None:
            self.request_protocol = m.get('RequestProtocol')

        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        if m.get('ServiceParametersMap') is not None:
            self.service_parameters_map = m.get('ServiceParametersMap')

        if m.get('ServiceProtocol') is not None:
            self.service_protocol = m.get('ServiceProtocol')

        if m.get('ServiceTimeout') is not None:
            self.service_timeout = m.get('ServiceTimeout')

        if m.get('UseBackendService') is not None:
            self.use_backend_service = m.get('UseBackendService')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VpcConfig') is not None:
            self.vpc_config = m.get('VpcConfig')

        return self

