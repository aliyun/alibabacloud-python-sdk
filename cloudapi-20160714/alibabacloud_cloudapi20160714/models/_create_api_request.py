# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreateApiRequest(DaraModel):
    def __init__(
        self,
        allow_signature_method: str = None,
        api_name: str = None,
        app_code_auth_type: str = None,
        auth_type: str = None,
        backend_enable: bool = None,
        backend_id: str = None,
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
        tag: List[main_models.CreateApiRequestTag] = None,
        visibility: str = None,
        web_socket_api_type: str = None,
    ):
        # The type of the two-way communication API.
        # 
        # *   **COMMON**: normal APIs
        # *   **REGISTER**: registered APIs
        # *   **UNREGISTER**: unregistered APIs
        # *   **NOTIFY**: downstream notification APIs
        self.allow_signature_method = allow_signature_method
        # The name of the API that you want to create. The name must be unique within the API group. The name must be 4 to 50 characters in length. It must start with a letter and can contain letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.api_name = api_name
        # The IDof the backend service
        self.app_code_auth_type = app_code_auth_type
        # The configuration items of API requests sent by the consumer to API Gateway.
        # 
        # For more information, see [RequestConfig](https://help.aliyun.com/document_detail/43985.html).
        self.auth_type = auth_type
        # Specifies whether to enable backend services.
        self.backend_enable = backend_enable
        # Specifies whether to enable backend services.
        self.backend_id = backend_id
        self.constant_parameters = constant_parameters
        # The description of the API. The description can be up to 180 characters in length.
        self.description = description
        # If **AuthType** is set to **APP**, the valid values are:
        # 
        # *   **DEFAULT**: The default value that is used if no other values are passed. This value means that the setting of the group is used.
        # *   **DISABLE**: The authentication is disabled.
        # *   **HEADER**: AppCode can be placed in the Header parameter for authentication.
        # *   **HEADER_QUERY**: AppCode can be placed in the Header or Query parameter for authentication.
        self.disable_internet = disable_internet
        self.error_code_samples = error_code_samples
        self.fail_result_sample = fail_result_sample
        # *   Specifies whether to set **DisableInternet** to **true** to limit API calls to within the VPC.
        # *   If you set **DisableInternet** to **false**, the limit is lifted. The default value is false when you create an API.
        self.force_nonce_check = force_nonce_check
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # If the **AuthType** is **APP** authentication, you need to pass this value to specify the signature algorithm. If you do not specify this parameter, the default value HmacSHA256 is used. Valid values:
        # 
        # *   HmacSHA256
        # *   HmacSHA1,HmacSHA256
        self.open_id_connect_config = open_id_connect_config
        # The configuration items of API requests sent by API Gateway to the backend service.
        # 
        # For more information, see [ServiceConfig](https://help.aliyun.com/document_detail/43987.html).
        # 
        # This parameter is required.
        self.request_config = request_config
        self.request_parameters = request_parameters
        # *   Specifies whether to set **ForceNonceCheck** to **true** to force the check of X-Ca-Nonce during the request. This is the unique identifier of the request and is generally identified by UUID. After receiving this parameter, API Gateway verifies the validity of this parameter. The same value can be used only once within 15 minutes. This helps prevent replay attacks.
        # *   If you set **ForceNonceCheck** to **false**, the check is not performed. The default value is false when you create an API.
        self.result_body_model = result_body_model
        self.result_descriptions = result_descriptions
        self.result_sample = result_sample
        # The sample response from the backend service.
        self.result_type = result_type
        self.security_token = security_token
        # The parameters of API requests sent by the consumer to API Gateway.
        # 
        # For more information, see [RequestParameter](https://help.aliyun.com/document_detail/43986.html).
        # 
        # This parameter is required.
        self.service_config = service_config
        self.service_parameters = service_parameters
        self.service_parameters_map = service_parameters_map
        self.system_parameters = system_parameters
        # The list of tags.
        self.tag = tag
        # Specifies whether to make the API public. Valid values:
        # 
        # *   **PUBLIC**: Make the API public. If you set this parameter to PUBLIC, this API is displayed on the APIs page for all users after the API is published to the production environment.
        # *   **PRIVATE**: Make the API private. Private APIs are not displayed in the Alibaba Cloud Marketplace after the API group to which they belong is made available.
        # 
        # This parameter is required.
        self.visibility = visibility
        # The return description of the API.
        self.web_socket_api_type = web_socket_api_type

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
        if self.allow_signature_method is not None:
            result['AllowSignatureMethod'] = self.allow_signature_method

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.app_code_auth_type is not None:
            result['AppCodeAuthType'] = self.app_code_auth_type

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.backend_enable is not None:
            result['BackendEnable'] = self.backend_enable

        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        if m.get('BackendEnable') is not None:
            self.backend_enable = m.get('BackendEnable')

        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateApiRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('WebSocketApiType') is not None:
            self.web_socket_api_type = m.get('WebSocketApiType')

        return self

class CreateApiRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

