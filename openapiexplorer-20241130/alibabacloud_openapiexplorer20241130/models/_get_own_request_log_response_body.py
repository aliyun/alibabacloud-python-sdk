# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_openapiexplorer20241130 import models as main_models
from darabonba.model import DaraModel

class GetOwnRequestLogResponseBody(DaraModel):
    def __init__(
        self,
        log_info: main_models.GetOwnRequestLogResponseBodyLogInfo = None,
        request_id: str = None,
    ):
        # The detailed information about the log of the API call.
        self.log_info = log_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_info is not None:
            result['logInfo'] = self.log_info.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logInfo') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m.get('logInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetOwnRequestLogResponseBodyLogInfo(DaraModel):
    def __init__(
        self,
        authentication_info: main_models.GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo = None,
        basic_info: main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfo = None,
        caller_info: main_models.GetOwnRequestLogResponseBodyLogInfoCallerInfo = None,
        parameters: List[main_models.GetOwnRequestLogResponseBodyLogInfoParameters] = None,
        responses: main_models.GetOwnRequestLogResponseBodyLogInfoResponses = None,
    ):
        # The authentication information.
        self.authentication_info = authentication_info
        # The basic information about the log of the API call.
        self.basic_info = basic_info
        # The information about the caller.
        self.caller_info = caller_info
        # The information about the request parameters.
        self.parameters = parameters
        # The information that is returned for the request.
        self.responses = responses

    def validate(self):
        if self.authentication_info:
            self.authentication_info.validate()
        if self.basic_info:
            self.basic_info.validate()
        if self.caller_info:
            self.caller_info.validate()
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.responses:
            self.responses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_info is not None:
            result['authenticationInfo'] = self.authentication_info.to_map()

        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()

        if self.caller_info is not None:
            result['callerInfo'] = self.caller_info.to_map()

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        if self.responses is not None:
            result['responses'] = self.responses.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationInfo') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo()
            self.authentication_info = temp_model.from_map(m.get('authenticationInfo'))

        if m.get('basicInfo') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfo()
            self.basic_info = temp_model.from_map(m.get('basicInfo'))

        if m.get('callerInfo') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoCallerInfo()
            self.caller_info = temp_model.from_map(m.get('callerInfo'))

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('responses') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoResponses()
            self.responses = temp_model.from_map(m.get('responses'))

        return self

class GetOwnRequestLogResponseBodyLogInfoResponses(DaraModel):
    def __init__(
        self,
        response_body: str = None,
        response_body_format: str = None,
    ):
        # The response body.
        self.response_body = response_body
        # The type of the response body. Valid values: JSON, XML, and HTML.
        self.response_body_format = response_body_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.response_body is not None:
            result['responseBody'] = self.response_body

        if self.response_body_format is not None:
            result['responseBodyFormat'] = self.response_body_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('responseBody') is not None:
            self.response_body = m.get('responseBody')

        if m.get('responseBodyFormat') is not None:
            self.response_body_format = m.get('responseBodyFormat')

        return self

class GetOwnRequestLogResponseBodyLogInfoParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        type: str = None,
        value: Any = None,
    ):
        # The name of the request parameter.
        self.name = name
        # Indicates whether the request parameter is required.
        self.required = required
        # The type of the request parameter.
        self.type = type
        # The value of the request parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetOwnRequestLogResponseBodyLogInfoCallerInfo(DaraModel):
    def __init__(
        self,
        caller_account_id: str = None,
        caller_ip: str = None,
        caller_type: str = None,
        master_account_id: str = None,
        user_agent: str = None,
    ):
        # The account ID of the caller.
        self.caller_account_id = caller_account_id
        # The IP address of the caller.
        self.caller_ip = caller_ip
        # The type of the caller. Valid values:
        # 
        # 1.  customer: an Alibaba Cloud account
        # 2.  sub: a RAM user
        # 3.  AssumedRoleUser: a user that uses a temporary Security Token Service (STS) token
        self.caller_type = caller_type
        # The ID of the Alibaba Cloud account.
        self.master_account_id = master_account_id
        # The information about the user agent.
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_account_id is not None:
            result['callerAccountId'] = self.caller_account_id

        if self.caller_ip is not None:
            result['callerIp'] = self.caller_ip

        if self.caller_type is not None:
            result['callerType'] = self.caller_type

        if self.master_account_id is not None:
            result['masterAccountId'] = self.master_account_id

        if self.user_agent is not None:
            result['userAgent'] = self.user_agent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerAccountId') is not None:
            self.caller_account_id = m.get('callerAccountId')

        if m.get('callerIp') is not None:
            self.caller_ip = m.get('callerIp')

        if m.get('callerType') is not None:
            self.caller_type = m.get('callerType')

        if m.get('masterAccountId') is not None:
            self.master_account_id = m.get('masterAccountId')

        if m.get('userAgent') is not None:
            self.user_agent = m.get('userAgent')

        return self

class GetOwnRequestLogResponseBodyLogInfoBasicInfo(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail = None,
        api: str = None,
        api_doc: main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc = None,
        api_style: str = None,
        api_version: str = None,
        endpoint: str = None,
        error_code: str = None,
        error_message: str = None,
        gateway_process_time: str = None,
        http_method: str = None,
        http_status_code: str = None,
        log_request_id: str = None,
        product: str = None,
        product_name: main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName = None,
        region_id: str = None,
        request_duration: str = None,
        sdk_request_time: str = None,
        throttling_result: str = None,
    ):
        # The error message returned if the operator does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The name of the API.
        self.api = api
        # The information about the API documentation.
        self.api_doc = api_doc
        # The API style. Valid values: roa and rpc.
        self.api_style = api_style
        # The version of the API.
        self.api_version = api_version
        # The endpoint of the service region.
        self.endpoint = endpoint
        # The error code in the log. This parameter is left empty if no error is reported in the API call.
        self.error_code = error_code
        # The error message in the log. This parameter is left empty if no error is reported in the API call.
        self.error_message = error_message
        # The time when the gateway receives the request. Indicate the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.gateway_process_time = gateway_process_time
        # The HTTP request method.
        self.http_method = http_method
        # The HTTP status code in the log.
        self.http_status_code = http_status_code
        # The request ID.
        self.log_request_id = log_request_id
        # The product code.
        self.product = product
        # The product name, which includes the Chinese name and English name.
        self.product_name = product_name
        # The service region ID.
        self.region_id = region_id
        # The duration from when the gateway receives the request to when the client receives a response. Unit: milliseconds.
        self.request_duration = request_duration
        # The time when the request is initiated. Indicate the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.sdk_request_time = sdk_request_time
        # The throttling result. Valid values: FC.PASS: The task is not blocked by throttling. FC.DENY: The task is blocked by throttling.
        self.throttling_result = throttling_result

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.api_doc:
            self.api_doc.validate()
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.api is not None:
            result['api'] = self.api

        if self.api_doc is not None:
            result['apiDoc'] = self.api_doc.to_map()

        if self.api_style is not None:
            result['apiStyle'] = self.api_style

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.gateway_process_time is not None:
            result['gatewayProcessTime'] = self.gateway_process_time

        if self.http_method is not None:
            result['httpMethod'] = self.http_method

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id

        if self.product is not None:
            result['product'] = self.product

        if self.product_name is not None:
            result['productName'] = self.product_name.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_duration is not None:
            result['requestDuration'] = self.request_duration

        if self.sdk_request_time is not None:
            result['sdkRequestTime'] = self.sdk_request_time

        if self.throttling_result is not None:
            result['throttlingResult'] = self.throttling_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('accessDeniedDetail'))

        if m.get('api') is not None:
            self.api = m.get('api')

        if m.get('apiDoc') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc()
            self.api_doc = temp_model.from_map(m.get('apiDoc'))

        if m.get('apiStyle') is not None:
            self.api_style = m.get('apiStyle')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('gatewayProcessTime') is not None:
            self.gateway_process_time = m.get('gatewayProcessTime')

        if m.get('httpMethod') is not None:
            self.http_method = m.get('httpMethod')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('productName') is not None:
            temp_model = main_models.GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName()
            self.product_name = temp_model.from_map(m.get('productName'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestDuration') is not None:
            self.request_duration = m.get('requestDuration')

        if m.get('sdkRequestTime') is not None:
            self.sdk_request_time = m.get('sdkRequestTime')

        if m.get('throttlingResult') is not None:
            self.throttling_result = m.get('throttlingResult')

        return self

class GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        en_name: str = None,
    ):
        # The product name in Chinese.
        self.cn_name = cn_name
        # The product name in English.
        self.en_name = en_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_name is not None:
            result['cnName'] = self.cn_name

        if self.en_name is not None:
            result['enName'] = self.en_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cnName') is not None:
            self.cn_name = m.get('cnName')

        if m.get('enName') is not None:
            self.en_name = m.get('enName')

        return self

class GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc(DaraModel):
    def __init__(
        self,
        alibabacloud_site: str = None,
        aliyun_site: str = None,
    ):
        # The documentation URL on the international site (alibabacloud.com).
        self.alibabacloud_site = alibabacloud_site
        # The documentation URL on the China site (aliyun.com).
        self.aliyun_site = aliyun_site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alibabacloud_site is not None:
            result['alibabacloudSite'] = self.alibabacloud_site

        if self.aliyun_site is not None:
            result['aliyunSite'] = self.aliyun_site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alibabacloudSite') is not None:
            self.alibabacloud_site = m.get('alibabacloudSite')

        if m.get('aliyunSite') is not None:
            self.aliyun_site = m.get('aliyunSite')

        return self

class GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The operation that the operator does not have permissions to perform.
        self.auth_action = auth_action
        # The identity.
        self.auth_principal_display_name = auth_principal_display_name
        # The ID of the Alibaba Cloud account to which the current identity belongs.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type of the operator.
        self.auth_principal_type = auth_principal_type
        # The information after encoding, which can be used for troubleshooting. You can call the DecodeDiagnosticMessage operation of Resource Access Management (RAM) for further diagnostics.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The cause of the permission-related error.
        self.no_permission_type = no_permission_type
        # The type of the policy that causes the permission-related error.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['authAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['authPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['authPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['authPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['encodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['noPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authAction') is not None:
            self.auth_action = m.get('authAction')

        if m.get('authPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('authPrincipalDisplayName')

        if m.get('authPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('authPrincipalOwnerId')

        if m.get('authPrincipalType') is not None:
            self.auth_principal_type = m.get('authPrincipalType')

        if m.get('encodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('encodedDiagnosticMessage')

        if m.get('noPermissionType') is not None:
            self.no_permission_type = m.get('noPermissionType')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        return self

class GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo(DaraModel):
    def __init__(
        self,
        authentication_type: str = None,
        signature_method: str = None,
        signature_version: str = None,
    ):
        # The authentication type. Valid values:
        # 
        # *   AK: includes a permanent AccessKey pair, a temporary AccessKey pair, and a STS token.
        # *   PRIVATEKEY: an AccessKey pair for an asymmetric cryptography algorithm.
        # *   BEARETOKEN: an authentication mechanism that is widely used in the OAuth 2.0 framework and cloud services.
        # *   CUSTOM_SPI: an efficient and secure authentication method that is suitable for the delivery and management of Software as a Service (SaaS) services in Alibaba Cloud Marketplace.
        # *   Anonymous: anonymous access.
        # *   DPS: an authentication method that is similar to AK. Its signature algorithm is different from that of Alibaba Cloud services and is exclusive to specific products.
        self.authentication_type = authentication_type
        # The signature algorithm. Valid values:
        # 
        # *   HMAC-SHA1
        # *   HMAC-SHA256
        self.signature_method = signature_method
        # The signature version.
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['authenticationType'] = self.authentication_type

        if self.signature_method is not None:
            result['signatureMethod'] = self.signature_method

        if self.signature_version is not None:
            result['signatureVersion'] = self.signature_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationType') is not None:
            self.authentication_type = m.get('authenticationType')

        if m.get('signatureMethod') is not None:
            self.signature_method = m.get('signatureMethod')

        if m.get('signatureVersion') is not None:
            self.signature_version = m.get('signatureVersion')

        return self

