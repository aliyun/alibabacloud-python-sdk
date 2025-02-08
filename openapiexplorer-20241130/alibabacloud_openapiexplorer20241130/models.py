# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GetErrorCodeSolutionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        error_code: str = None,
        error_message: str = None,
        product: str = None,
    ):
        self.accept_language = accept_language
        # This parameter is required.
        self.error_code = error_code
        self.error_message = error_message
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.product is not None:
            result['product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('product') is not None:
            self.product = m.get('product')
        return self


class GetErrorCodeSolutionsResponseBodySolutions(TeaModel):
    def __init__(
        self,
        content: str = None,
        error_code: str = None,
        error_message: str = None,
        product: str = None,
        product_name: str = None,
        solution_id: str = None,
    ):
        self.content = content
        self.error_code = error_code
        self.error_message = error_message
        self.product = product
        self.product_name = product_name
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.solution_id is not None:
            result['solutionId'] = self.solution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('solutionId') is not None:
            self.solution_id = m.get('solutionId')
        return self


class GetErrorCodeSolutionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        solutions: List[GetErrorCodeSolutionsResponseBodySolutions] = None,
    ):
        self.request_id = request_id
        self.solutions = solutions

    def validate(self):
        if self.solutions:
            for k in self.solutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['solutions'] = []
        if self.solutions is not None:
            for k in self.solutions:
                result['solutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.solutions = []
        if m.get('solutions') is not None:
            for k in m.get('solutions'):
                temp_model = GetErrorCodeSolutionsResponseBodySolutions()
                self.solutions.append(temp_model.from_map(k))
        return self


class GetErrorCodeSolutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErrorCodeSolutionsResponseBody = None,
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
            temp_model = GetErrorCodeSolutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOwnRequestLogRequest(TeaModel):
    def __init__(
        self,
        log_request_id: str = None,
    ):
        # This parameter is required.
        self.log_request_id = log_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')
        return self


class GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        signature_method: str = None,
        signature_version: str = None,
    ):
        self.authentication_type = authentication_type
        self.signature_method = signature_method
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail(TeaModel):
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
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc(TeaModel):
    def __init__(
        self,
        alibabacloud_site: str = None,
        aliyun_site: str = None,
    ):
        self.alibabacloud_site = alibabacloud_site
        self.aliyun_site = aliyun_site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        en_name: str = None,
    ):
        self.cn_name = cn_name
        self.en_name = en_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfoBasicInfo(TeaModel):
    def __init__(
        self,
        access_denied_detail: GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail = None,
        api: str = None,
        api_doc: GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc = None,
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
        product_name: GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName = None,
        region_id: str = None,
        request_duration: str = None,
        sdk_request_time: str = None,
        throttling_result: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.api = api
        self.api_doc = api_doc
        self.api_style = api_style
        self.api_version = api_version
        self.endpoint = endpoint
        self.error_code = error_code
        self.error_message = error_message
        self.gateway_process_time = gateway_process_time
        self.http_method = http_method
        self.http_status_code = http_status_code
        self.log_request_id = log_request_id
        self.product = product
        self.product_name = product_name
        self.region_id = region_id
        self.request_duration = request_duration
        self.sdk_request_time = sdk_request_time
        self.throttling_result = throttling_result

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.api_doc:
            self.api_doc.validate()
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['accessDeniedDetail'])
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiDoc') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfoApiDoc()
            self.api_doc = temp_model.from_map(m['apiDoc'])
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
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfoProductName()
            self.product_name = temp_model.from_map(m['productName'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestDuration') is not None:
            self.request_duration = m.get('requestDuration')
        if m.get('sdkRequestTime') is not None:
            self.sdk_request_time = m.get('sdkRequestTime')
        if m.get('throttlingResult') is not None:
            self.throttling_result = m.get('throttlingResult')
        return self


class GetOwnRequestLogResponseBodyLogInfoCallerInfo(TeaModel):
    def __init__(
        self,
        caller_account_id: str = None,
        caller_ip: str = None,
        caller_type: str = None,
        master_account_id: str = None,
        user_agent: str = None,
    ):
        self.caller_account_id = caller_account_id
        self.caller_ip = caller_ip
        self.caller_type = caller_type
        self.master_account_id = master_account_id
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfoParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        type: str = None,
        value: Any = None,
    ):
        self.name = name
        self.required = required
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfoResponses(TeaModel):
    def __init__(
        self,
        response_body: str = None,
        response_body_format: str = None,
    ):
        self.response_body = response_body
        self.response_body_format = response_body_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetOwnRequestLogResponseBodyLogInfo(TeaModel):
    def __init__(
        self,
        authentication_info: GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo = None,
        basic_info: GetOwnRequestLogResponseBodyLogInfoBasicInfo = None,
        caller_info: GetOwnRequestLogResponseBodyLogInfoCallerInfo = None,
        parameters: List[GetOwnRequestLogResponseBodyLogInfoParameters] = None,
        responses: GetOwnRequestLogResponseBodyLogInfoResponses = None,
    ):
        self.authentication_info = authentication_info
        self.basic_info = basic_info
        self.caller_info = caller_info
        self.parameters = parameters
        self.responses = responses

    def validate(self):
        if self.authentication_info:
            self.authentication_info.validate()
        if self.basic_info:
            self.basic_info.validate()
        if self.caller_info:
            self.caller_info.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.responses:
            self.responses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_info is not None:
            result['authenticationInfo'] = self.authentication_info.to_map()
        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()
        if self.caller_info is not None:
            result['callerInfo'] = self.caller_info.to_map()
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        if self.responses is not None:
            result['responses'] = self.responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoAuthenticationInfo()
            self.authentication_info = temp_model.from_map(m['authenticationInfo'])
        if m.get('basicInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoBasicInfo()
            self.basic_info = temp_model.from_map(m['basicInfo'])
        if m.get('callerInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoCallerInfo()
            self.caller_info = temp_model.from_map(m['callerInfo'])
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetOwnRequestLogResponseBodyLogInfoParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('responses') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfoResponses()
            self.responses = temp_model.from_map(m['responses'])
        return self


class GetOwnRequestLogResponseBody(TeaModel):
    def __init__(
        self,
        log_info: GetOwnRequestLogResponseBodyLogInfo = None,
        request_id: str = None,
    ):
        self.log_info = log_info
        self.request_id = request_id

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_info is not None:
            result['logInfo'] = self.log_info.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logInfo') is not None:
            temp_model = GetOwnRequestLogResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m['logInfo'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetOwnRequestLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOwnRequestLogResponseBody = None,
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
            temp_model = GetOwnRequestLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestLogRequest(TeaModel):
    def __init__(
        self,
        log_request_id: str = None,
    ):
        # This parameter is required.
        self.log_request_id = log_request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_request_id is not None:
            result['logRequestId'] = self.log_request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logRequestId') is not None:
            self.log_request_id = m.get('logRequestId')
        return self


class GetRequestLogResponseBodyLogInfoAuthenticationInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        signature_method: str = None,
        signature_version: str = None,
    ):
        self.authentication_type = authentication_type
        self.signature_method = signature_method
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail(TeaModel):
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
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfoBasicInfoApiDoc(TeaModel):
    def __init__(
        self,
        alibabacloud_site: str = None,
        aliyun_site: str = None,
    ):
        self.alibabacloud_site = alibabacloud_site
        self.aliyun_site = aliyun_site

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfoBasicInfoProductName(TeaModel):
    def __init__(
        self,
        cn_name: str = None,
        en_name: str = None,
    ):
        self.cn_name = cn_name
        self.en_name = en_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfoBasicInfo(TeaModel):
    def __init__(
        self,
        access_denied_detail: GetRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail = None,
        api: str = None,
        api_doc: GetRequestLogResponseBodyLogInfoBasicInfoApiDoc = None,
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
        product_name: GetRequestLogResponseBodyLogInfoBasicInfoProductName = None,
        region_id: str = None,
        request_duration: str = None,
        sdk_request_time: str = None,
        throttling_result: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.api = api
        self.api_doc = api_doc
        self.api_style = api_style
        self.api_version = api_version
        self.endpoint = endpoint
        self.error_code = error_code
        self.error_message = error_message
        self.gateway_process_time = gateway_process_time
        self.http_method = http_method
        self.http_status_code = http_status_code
        self.log_request_id = log_request_id
        self.product = product
        self.product_name = product_name
        self.region_id = region_id
        self.request_duration = request_duration
        self.sdk_request_time = sdk_request_time
        self.throttling_result = throttling_result

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.api_doc:
            self.api_doc.validate()
        if self.product_name:
            self.product_name.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfoAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['accessDeniedDetail'])
        if m.get('api') is not None:
            self.api = m.get('api')
        if m.get('apiDoc') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfoApiDoc()
            self.api_doc = temp_model.from_map(m['apiDoc'])
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
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfoProductName()
            self.product_name = temp_model.from_map(m['productName'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestDuration') is not None:
            self.request_duration = m.get('requestDuration')
        if m.get('sdkRequestTime') is not None:
            self.sdk_request_time = m.get('sdkRequestTime')
        if m.get('throttlingResult') is not None:
            self.throttling_result = m.get('throttlingResult')
        return self


class GetRequestLogResponseBodyLogInfoCallerInfo(TeaModel):
    def __init__(
        self,
        caller_account_id: str = None,
        caller_ip: str = None,
        caller_type: str = None,
        master_account_id: str = None,
        user_agent: str = None,
    ):
        self.caller_account_id = caller_account_id
        self.caller_ip = caller_ip
        self.caller_type = caller_type
        self.master_account_id = master_account_id
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfoParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        type: str = None,
        value: Any = None,
    ):
        self.name = name
        self.required = required
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfoResponses(TeaModel):
    def __init__(
        self,
        response_body: str = None,
        response_body_format: str = None,
    ):
        self.response_body = response_body
        self.response_body_format = response_body_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetRequestLogResponseBodyLogInfo(TeaModel):
    def __init__(
        self,
        authentication_info: GetRequestLogResponseBodyLogInfoAuthenticationInfo = None,
        basic_info: GetRequestLogResponseBodyLogInfoBasicInfo = None,
        caller_info: GetRequestLogResponseBodyLogInfoCallerInfo = None,
        parameters: List[GetRequestLogResponseBodyLogInfoParameters] = None,
        responses: GetRequestLogResponseBodyLogInfoResponses = None,
    ):
        self.authentication_info = authentication_info
        self.basic_info = basic_info
        self.caller_info = caller_info
        self.parameters = parameters
        self.responses = responses

    def validate(self):
        if self.authentication_info:
            self.authentication_info.validate()
        if self.basic_info:
            self.basic_info.validate()
        if self.caller_info:
            self.caller_info.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.responses:
            self.responses.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_info is not None:
            result['authenticationInfo'] = self.authentication_info.to_map()
        if self.basic_info is not None:
            result['basicInfo'] = self.basic_info.to_map()
        if self.caller_info is not None:
            result['callerInfo'] = self.caller_info.to_map()
        result['parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['parameters'].append(k.to_map() if k else None)
        if self.responses is not None:
            result['responses'] = self.responses.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoAuthenticationInfo()
            self.authentication_info = temp_model.from_map(m['authenticationInfo'])
        if m.get('basicInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoBasicInfo()
            self.basic_info = temp_model.from_map(m['basicInfo'])
        if m.get('callerInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoCallerInfo()
            self.caller_info = temp_model.from_map(m['callerInfo'])
        self.parameters = []
        if m.get('parameters') is not None:
            for k in m.get('parameters'):
                temp_model = GetRequestLogResponseBodyLogInfoParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('responses') is not None:
            temp_model = GetRequestLogResponseBodyLogInfoResponses()
            self.responses = temp_model.from_map(m['responses'])
        return self


class GetRequestLogResponseBody(TeaModel):
    def __init__(
        self,
        log_info: GetRequestLogResponseBodyLogInfo = None,
        request_id: str = None,
    ):
        self.log_info = log_info
        self.request_id = request_id

    def validate(self):
        if self.log_info:
            self.log_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_info is not None:
            result['logInfo'] = self.log_info.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logInfo') is not None:
            temp_model = GetRequestLogResponseBodyLogInfo()
            self.log_info = temp_model.from_map(m['logInfo'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRequestLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRequestLogResponseBody = None,
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
            temp_model = GetRequestLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


