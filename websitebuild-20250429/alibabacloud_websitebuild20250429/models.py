# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Any, Dict


class BindAppDomainRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        extend: str = None,
        operate_type: str = None,
    ):
        self.biz_id = biz_id
        self.domain_name = domain_name
        self.extend = extend
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        return self


class BindAppDomainResponseBodyModule(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindAppDomainResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: BindAppDomainResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('Module') is not None:
            temp_model = BindAppDomainResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class BindAppDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAppDomainResponseBody = None,
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
            temp_model = BindAppDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogoTaskRequest(TeaModel):
    def __init__(
        self,
        logo_version: str = None,
        negative_prompt: str = None,
        parameters: str = None,
        prompt: str = None,
    ):
        self.logo_version = logo_version
        self.negative_prompt = negative_prompt
        self.parameters = parameters
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_version is not None:
            result['LogoVersion'] = self.logo_version
        if self.negative_prompt is not None:
            result['NegativePrompt'] = self.negative_prompt
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoVersion') is not None:
            self.logo_version = m.get('LogoVersion')
        if m.get('NegativePrompt') is not None:
            self.negative_prompt = m.get('NegativePrompt')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        return self


class CreateLogoTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateLogoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogoTaskResponseBody = None,
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
            temp_model = CreateLogoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
    ):
        self.biz_id = biz_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class DeleteAppDomainCertificateResponseBodyModule(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppDomainCertificateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: DeleteAppDomainCertificateResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('Module') is not None:
            temp_model = DeleteAppDomainCertificateResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DeleteAppDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppDomainCertificateResponseBody = None,
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
            temp_model = DeleteAppDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppDomainRedirectRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        record_id: int = None,
    ):
        self.biz_id = biz_id
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DeleteAppDomainRedirectResponseBodyModule(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppDomainRedirectResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: DeleteAppDomainRedirectResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('Module') is not None:
            temp_model = DeleteAppDomainRedirectResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DeleteAppDomainRedirectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppDomainRedirectResponseBody = None,
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
            temp_model = DeleteAppDomainRedirectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppDomainDnsRecordRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        purpose: str = None,
    ):
        self.biz_id = biz_id
        self.domain_name = domain_name
        self.purpose = purpose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.purpose is not None:
            result['Purpose'] = self.purpose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('Purpose') is not None:
            self.purpose = m.get('Purpose')
        return self


class DescribeAppDomainDnsRecordResponseBodyModule(TeaModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        self.host = host
        self.record_type = record_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAppDomainDnsRecordResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: DescribeAppDomainDnsRecordResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('Module') is not None:
            temp_model = DescribeAppDomainDnsRecordResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DescribeAppDomainDnsRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppDomainDnsRecordResponseBody = None,
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
            temp_model = DescribeAppDomainDnsRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCreateLogoTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetCreateLogoTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_status: str = None,
        urls: List[str] = None,
    ):
        self.task_id = task_id
        self.task_status = task_status
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class GetCreateLogoTaskResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        task: GetCreateLogoTaskResponseBodyTask = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Task') is not None:
            temp_model = GetCreateLogoTaskResponseBodyTask()
            self.task = temp_model.from_map(m['Task'])
        return self


class GetCreateLogoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCreateLogoTaskResponseBody = None,
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
            temp_model = GetCreateLogoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainInfoForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.domain_name = domain_name
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetDomainInfoForPartnerResponseBodyDataOwnership(TeaModel):
    def __init__(
        self,
        account: str = None,
        provider: str = None,
    ):
        self.account = account
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.provider is not None:
            result['Provider'] = self.provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        return self


class GetDomainInfoForPartnerResponseBodyData(TeaModel):
    def __init__(
        self,
        domain_name: str = None,
        name_servers: str = None,
        ownership: GetDomainInfoForPartnerResponseBodyDataOwnership = None,
        registrar: str = None,
    ):
        self.domain_name = domain_name
        self.name_servers = name_servers
        self.ownership = ownership
        self.registrar = registrar

    def validate(self):
        if self.ownership:
            self.ownership.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.name_servers is not None:
            result['NameServers'] = self.name_servers
        if self.ownership is not None:
            result['Ownership'] = self.ownership.to_map()
        if self.registrar is not None:
            result['Registrar'] = self.registrar
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NameServers') is not None:
            self.name_servers = m.get('NameServers')
        if m.get('Ownership') is not None:
            temp_model = GetDomainInfoForPartnerResponseBodyDataOwnership()
            self.ownership = temp_model.from_map(m['Ownership'])
        if m.get('Registrar') is not None:
            self.registrar = m.get('Registrar')
        return self


class GetDomainInfoForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDomainInfoForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDomainInfoForPartnerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDomainInfoForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainInfoForPartnerResponseBody = None,
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
            temp_model = GetDomainInfoForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIcpFilingInfoForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain: str = None,
    ):
        self.biz_id = biz_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetIcpFilingInfoForPartnerResponseBodyData(TeaModel):
    def __init__(
        self,
        icp_number: str = None,
        recorded: bool = None,
        site_record_number: str = None,
    ):
        self.icp_number = icp_number
        self.recorded = recorded
        self.site_record_number = site_record_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icp_number is not None:
            result['IcpNumber'] = self.icp_number
        if self.recorded is not None:
            result['Recorded'] = self.recorded
        if self.site_record_number is not None:
            result['SiteRecordNumber'] = self.site_record_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpNumber') is not None:
            self.icp_number = m.get('IcpNumber')
        if m.get('Recorded') is not None:
            self.recorded = m.get('Recorded')
        if m.get('SiteRecordNumber') is not None:
            self.site_record_number = m.get('SiteRecordNumber')
        return self


class GetIcpFilingInfoForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        data: GetIcpFilingInfoForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetIcpFilingInfoForPartnerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIcpFilingInfoForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIcpFilingInfoForPartnerResponseBody = None,
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
            temp_model = GetIcpFilingInfoForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserTmpIdentityForPartnerRequest(TeaModel):
    def __init__(
        self,
        auth_purpose: str = None,
        biz_id: str = None,
        extend: str = None,
        service_linked_role: str = None,
        user_id: str = None,
    ):
        self.auth_purpose = auth_purpose
        self.biz_id = biz_id
        self.extend = extend
        self.service_linked_role = service_linked_role
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_purpose is not None:
            result['AuthPurpose'] = self.auth_purpose
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.service_linked_role is not None:
            result['ServiceLinkedRole'] = self.service_linked_role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPurpose') is not None:
            self.auth_purpose = m.get('AuthPurpose')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('ServiceLinkedRole') is not None:
            self.service_linked_role = m.get('ServiceLinkedRole')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserTmpIdentityForPartnerResponseBodyDataCredentials(TeaModel):
    def __init__(
        self,
        encrypted_access_key_id: str = None,
        encrypted_access_key_secret: str = None,
        encrypted_security_token: str = None,
        expiration: str = None,
    ):
        self.encrypted_access_key_id = encrypted_access_key_id
        self.encrypted_access_key_secret = encrypted_access_key_secret
        self.encrypted_security_token = encrypted_security_token
        self.expiration = expiration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_access_key_id is not None:
            result['EncryptedAccessKeyId'] = self.encrypted_access_key_id
        if self.encrypted_access_key_secret is not None:
            result['EncryptedAccessKeySecret'] = self.encrypted_access_key_secret
        if self.encrypted_security_token is not None:
            result['EncryptedSecurityToken'] = self.encrypted_security_token
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedAccessKeyId') is not None:
            self.encrypted_access_key_id = m.get('EncryptedAccessKeyId')
        if m.get('EncryptedAccessKeySecret') is not None:
            self.encrypted_access_key_secret = m.get('EncryptedAccessKeySecret')
        if m.get('EncryptedSecurityToken') is not None:
            self.encrypted_security_token = m.get('EncryptedSecurityToken')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        return self


class GetUserTmpIdentityForPartnerResponseBodyData(TeaModel):
    def __init__(
        self,
        credentials: GetUserTmpIdentityForPartnerResponseBodyDataCredentials = None,
        has_custom_role_auth: bool = None,
    ):
        self.credentials = credentials
        self.has_custom_role_auth = has_custom_role_auth

    def validate(self):
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()
        if self.has_custom_role_auth is not None:
            result['HasCustomRoleAuth'] = self.has_custom_role_auth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credentials') is not None:
            temp_model = GetUserTmpIdentityForPartnerResponseBodyDataCredentials()
            self.credentials = temp_model.from_map(m['Credentials'])
        if m.get('HasCustomRoleAuth') is not None:
            self.has_custom_role_auth = m.get('HasCustomRoleAuth')
        return self


class GetUserTmpIdentityForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        data: GetUserTmpIdentityForPartnerResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserTmpIdentityForPartnerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserTmpIdentityForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserTmpIdentityForPartnerResponseBody = None,
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
            temp_model = GetUserTmpIdentityForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppDomainRedirectRecordsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.biz_id = biz_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListAppDomainRedirectRecordsResponseBodyModuleData(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        source_domain: str = None,
        target_domain: str = None,
    ):
        self.record_id = record_id
        self.source_domain = source_domain
        self.target_domain = target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.source_domain is not None:
            result['SourceDomain'] = self.source_domain
        if self.target_domain is not None:
            result['TargetDomain'] = self.target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('SourceDomain') is not None:
            self.source_domain = m.get('SourceDomain')
        if m.get('TargetDomain') is not None:
            self.target_domain = m.get('TargetDomain')
        return self


class ListAppDomainRedirectRecordsResponseBodyModuleNext(TeaModel):
    def __init__(
        self,
        record_id: str = None,
        source_domain: str = None,
        target_domain: str = None,
    ):
        self.record_id = record_id
        self.source_domain = source_domain
        self.target_domain = target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.source_domain is not None:
            result['SourceDomain'] = self.source_domain
        if self.target_domain is not None:
            result['TargetDomain'] = self.target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('SourceDomain') is not None:
            self.source_domain = m.get('SourceDomain')
        if m.get('TargetDomain') is not None:
            self.target_domain = m.get('TargetDomain')
        return self


class ListAppDomainRedirectRecordsResponseBodyModule(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListAppDomainRedirectRecordsResponseBodyModuleData] = None,
        next: ListAppDomainRedirectRecordsResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next = next
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next is not None:
            result['Next'] = self.next.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppDomainRedirectRecordsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k))
        if m.get('Next') is not None:
            temp_model = ListAppDomainRedirectRecordsResponseBodyModuleNext()
            self.next = temp_model.from_map(m['Next'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListAppDomainRedirectRecordsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: ListAppDomainRedirectRecordsResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.max_results = max_results
        self.module = module
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Module') is not None:
            temp_model = ListAppDomainRedirectRecordsResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class ListAppDomainRedirectRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppDomainRedirectRecordsResponseBody = None,
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
            temp_model = ListAppDomainRedirectRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstanceDomainsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
        self.max_results = max_results
        self.next_token = next_token
        self.order_column = order_column
        self.order_type = order_type
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_column is not None:
            result['OrderColumn'] = self.order_column
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppInstanceDomainsResponseBodyModuleDataCertificate(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        certificate_status: str = None,
        certificate_type: str = None,
        end_time: str = None,
    ):
        self.certificate_name = certificate_name
        self.certificate_status = certificate_status
        self.certificate_type = certificate_type
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListAppInstanceDomainsResponseBodyModuleDataOwnership(TeaModel):
    def __init__(
        self,
        account: str = None,
        provider: str = None,
        root_domain: str = None,
    ):
        self.account = account
        self.provider = provider
        self.root_domain = root_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')
        return self


class ListAppInstanceDomainsResponseBodyModuleDataResolutionDnsRecord(TeaModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        self.host = host
        self.record_type = record_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAppInstanceDomainsResponseBodyModuleDataResolution(TeaModel):
    def __init__(
        self,
        dns_record: ListAppInstanceDomainsResponseBodyModuleDataResolutionDnsRecord = None,
        error_msg: str = None,
        resolution_status: str = None,
    ):
        self.dns_record = dns_record
        self.error_msg = error_msg
        self.resolution_status = resolution_status

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.resolution_status is not None:
            result['ResolutionStatus'] = self.resolution_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleDataResolutionDnsRecord()
            self.dns_record = temp_model.from_map(m['DnsRecord'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ResolutionStatus') is not None:
            self.resolution_status = m.get('ResolutionStatus')
        return self


class ListAppInstanceDomainsResponseBodyModuleDataVerificationDnsRecord(TeaModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        self.host = host
        self.record_type = record_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAppInstanceDomainsResponseBodyModuleDataVerification(TeaModel):
    def __init__(
        self,
        dns_record: ListAppInstanceDomainsResponseBodyModuleDataVerificationDnsRecord = None,
        error_msg: str = None,
        verification_status: str = None,
        verification_status_code: str = None,
    ):
        self.dns_record = dns_record
        self.error_msg = error_msg
        self.verification_status = verification_status
        self.verification_status_code = verification_status_code

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        if self.verification_status_code is not None:
            result['VerificationStatusCode'] = self.verification_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleDataVerificationDnsRecord()
            self.dns_record = temp_model.from_map(m['DnsRecord'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        if m.get('VerificationStatusCode') is not None:
            self.verification_status_code = m.get('VerificationStatusCode')
        return self


class ListAppInstanceDomainsResponseBodyModuleData(TeaModel):
    def __init__(
        self,
        certificate: ListAppInstanceDomainsResponseBodyModuleDataCertificate = None,
        create_time: str = None,
        domain_name: str = None,
        overall_status: str = None,
        ownership: ListAppInstanceDomainsResponseBodyModuleDataOwnership = None,
        resolution: ListAppInstanceDomainsResponseBodyModuleDataResolution = None,
        verification: ListAppInstanceDomainsResponseBodyModuleDataVerification = None,
    ):
        self.certificate = certificate
        self.create_time = create_time
        self.domain_name = domain_name
        self.overall_status = overall_status
        self.ownership = ownership
        self.resolution = resolution
        self.verification = verification

    def validate(self):
        if self.certificate:
            self.certificate.validate()
        if self.ownership:
            self.ownership.validate()
        if self.resolution:
            self.resolution.validate()
        if self.verification:
            self.verification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.overall_status is not None:
            result['OverallStatus'] = self.overall_status
        if self.ownership is not None:
            result['Ownership'] = self.ownership.to_map()
        if self.resolution is not None:
            result['Resolution'] = self.resolution.to_map()
        if self.verification is not None:
            result['Verification'] = self.verification.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleDataCertificate()
            self.certificate = temp_model.from_map(m['Certificate'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OverallStatus') is not None:
            self.overall_status = m.get('OverallStatus')
        if m.get('Ownership') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleDataOwnership()
            self.ownership = temp_model.from_map(m['Ownership'])
        if m.get('Resolution') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleDataResolution()
            self.resolution = temp_model.from_map(m['Resolution'])
        if m.get('Verification') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleDataVerification()
            self.verification = temp_model.from_map(m['Verification'])
        return self


class ListAppInstanceDomainsResponseBodyModuleNextCertificate(TeaModel):
    def __init__(
        self,
        certificate_name: str = None,
        certificate_status: str = None,
        certificate_type: str = None,
        end_time: str = None,
    ):
        self.certificate_name = certificate_name
        self.certificate_status = certificate_status
        self.certificate_type = certificate_type
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListAppInstanceDomainsResponseBodyModuleNextOwnership(TeaModel):
    def __init__(
        self,
        account: str = None,
        provider: str = None,
    ):
        self.account = account
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.provider is not None:
            result['Provider'] = self.provider
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        return self


class ListAppInstanceDomainsResponseBodyModuleNextResolutionDnsRecord(TeaModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        self.host = host
        self.record_type = record_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAppInstanceDomainsResponseBodyModuleNextResolution(TeaModel):
    def __init__(
        self,
        dns_record: ListAppInstanceDomainsResponseBodyModuleNextResolutionDnsRecord = None,
        error_msg: str = None,
        resolution_status: str = None,
    ):
        self.dns_record = dns_record
        self.error_msg = error_msg
        self.resolution_status = resolution_status

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.resolution_status is not None:
            result['ResolutionStatus'] = self.resolution_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNextResolutionDnsRecord()
            self.dns_record = temp_model.from_map(m['DnsRecord'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ResolutionStatus') is not None:
            self.resolution_status = m.get('ResolutionStatus')
        return self


class ListAppInstanceDomainsResponseBodyModuleNextVerificationDnsRecord(TeaModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        self.host = host
        self.record_type = record_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAppInstanceDomainsResponseBodyModuleNextVerification(TeaModel):
    def __init__(
        self,
        dns_record: ListAppInstanceDomainsResponseBodyModuleNextVerificationDnsRecord = None,
        error_msg: str = None,
        verification_status: str = None,
    ):
        self.dns_record = dns_record
        self.error_msg = error_msg
        self.verification_status = verification_status

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNextVerificationDnsRecord()
            self.dns_record = temp_model.from_map(m['DnsRecord'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')
        return self


class ListAppInstanceDomainsResponseBodyModuleNext(TeaModel):
    def __init__(
        self,
        certificate: ListAppInstanceDomainsResponseBodyModuleNextCertificate = None,
        create_time: str = None,
        domain_name: str = None,
        overall_status: str = None,
        ownership: ListAppInstanceDomainsResponseBodyModuleNextOwnership = None,
        resolution: ListAppInstanceDomainsResponseBodyModuleNextResolution = None,
        verification: ListAppInstanceDomainsResponseBodyModuleNextVerification = None,
    ):
        self.certificate = certificate
        self.create_time = create_time
        self.domain_name = domain_name
        self.overall_status = overall_status
        self.ownership = ownership
        self.resolution = resolution
        self.verification = verification

    def validate(self):
        if self.certificate:
            self.certificate.validate()
        if self.ownership:
            self.ownership.validate()
        if self.resolution:
            self.resolution.validate()
        if self.verification:
            self.verification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.overall_status is not None:
            result['OverallStatus'] = self.overall_status
        if self.ownership is not None:
            result['Ownership'] = self.ownership.to_map()
        if self.resolution is not None:
            result['Resolution'] = self.resolution.to_map()
        if self.verification is not None:
            result['Verification'] = self.verification.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNextCertificate()
            self.certificate = temp_model.from_map(m['Certificate'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('OverallStatus') is not None:
            self.overall_status = m.get('OverallStatus')
        if m.get('Ownership') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNextOwnership()
            self.ownership = temp_model.from_map(m['Ownership'])
        if m.get('Resolution') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNextResolution()
            self.resolution = temp_model.from_map(m['Resolution'])
        if m.get('Verification') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNextVerification()
            self.verification = temp_model.from_map(m['Verification'])
        return self


class ListAppInstanceDomainsResponseBodyModule(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[ListAppInstanceDomainsResponseBodyModuleData] = None,
        next: ListAppInstanceDomainsResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next = next
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next is not None:
            result['Next'] = self.next.to_map()
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pre_page is not None:
            result['PrePage'] = self.pre_page
        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit
        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppInstanceDomainsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k))
        if m.get('Next') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModuleNext()
            self.next = temp_model.from_map(m['Next'])
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')
        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')
        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class ListAppInstanceDomainsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: ListAppInstanceDomainsResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.max_results = max_results
        self.module = module
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Module') is not None:
            temp_model = ListAppInstanceDomainsResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class ListAppInstanceDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppInstanceDomainsResponseBody = None,
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
            temp_model = ListAppInstanceDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAppInstanceForPartnerRequest(TeaModel):
    def __init__(
        self,
        extend: str = None,
        operate_event: str = None,
    ):
        self.extend = extend
        self.operate_event = operate_event

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.operate_event is not None:
            result['OperateEvent'] = self.operate_event
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('OperateEvent') is not None:
            self.operate_event = m.get('OperateEvent')
        return self


class OperateAppInstanceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateAppInstanceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAppInstanceForPartnerResponseBody = None,
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
            temp_model = OperateAppInstanceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAppServiceForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        extend: str = None,
        operate_event: str = None,
        service_type: str = None,
    ):
        self.biz_id = biz_id
        self.extend = extend
        self.operate_event = operate_event
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.operate_event is not None:
            result['OperateEvent'] = self.operate_event
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('OperateEvent') is not None:
            self.operate_event = m.get('OperateEvent')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class OperateAppServiceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OperateAppServiceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAppServiceForPartnerResponseBody = None,
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
            temp_model = OperateAppServiceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageRequest(TeaModel):
    def __init__(
        self,
        color_hex: str = None,
        has_person: bool = None,
        image_category: str = None,
        image_ratio: str = None,
        max_height: int = None,
        max_results: int = None,
        max_width: int = None,
        min_height: int = None,
        min_width: int = None,
        next_token: str = None,
        oss_key: str = None,
        size: int = None,
        start: int = None,
        tags: List[str] = None,
        text: str = None,
    ):
        self.color_hex = color_hex
        self.has_person = has_person
        self.image_category = image_category
        self.image_ratio = image_ratio
        self.max_height = max_height
        self.max_results = max_results
        self.max_width = max_width
        self.min_height = min_height
        self.min_width = min_width
        self.next_token = next_token
        # Osskey。
        self.oss_key = oss_key
        self.size = size
        self.start = start
        self.tags = tags
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_hex is not None:
            result['ColorHex'] = self.color_hex
        if self.has_person is not None:
            result['HasPerson'] = self.has_person
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_ratio is not None:
            result['ImageRatio'] = self.image_ratio
        if self.max_height is not None:
            result['MaxHeight'] = self.max_height
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.max_width is not None:
            result['MaxWidth'] = self.max_width
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.min_width is not None:
            result['MinWidth'] = self.min_width
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.size is not None:
            result['Size'] = self.size
        if self.start is not None:
            result['Start'] = self.start
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorHex') is not None:
            self.color_hex = m.get('ColorHex')
        if m.get('HasPerson') is not None:
            self.has_person = m.get('HasPerson')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageRatio') is not None:
            self.image_ratio = m.get('ImageRatio')
        if m.get('MaxHeight') is not None:
            self.max_height = m.get('MaxHeight')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MaxWidth') is not None:
            self.max_width = m.get('MaxWidth')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('MinWidth') is not None:
            self.min_width = m.get('MinWidth')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageShrinkRequest(TeaModel):
    def __init__(
        self,
        color_hex: str = None,
        has_person: bool = None,
        image_category: str = None,
        image_ratio: str = None,
        max_height: int = None,
        max_results: int = None,
        max_width: int = None,
        min_height: int = None,
        min_width: int = None,
        next_token: str = None,
        oss_key: str = None,
        size: int = None,
        start: int = None,
        tags_shrink: str = None,
        text: str = None,
    ):
        self.color_hex = color_hex
        self.has_person = has_person
        self.image_category = image_category
        self.image_ratio = image_ratio
        self.max_height = max_height
        self.max_results = max_results
        self.max_width = max_width
        self.min_height = min_height
        self.min_width = min_width
        self.next_token = next_token
        # Osskey。
        self.oss_key = oss_key
        self.size = size
        self.start = start
        self.tags_shrink = tags_shrink
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.color_hex is not None:
            result['ColorHex'] = self.color_hex
        if self.has_person is not None:
            result['HasPerson'] = self.has_person
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_ratio is not None:
            result['ImageRatio'] = self.image_ratio
        if self.max_height is not None:
            result['MaxHeight'] = self.max_height
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.max_width is not None:
            result['MaxWidth'] = self.max_width
        if self.min_height is not None:
            result['MinHeight'] = self.min_height
        if self.min_width is not None:
            result['MinWidth'] = self.min_width
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.size is not None:
            result['Size'] = self.size
        if self.start is not None:
            result['Start'] = self.start
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColorHex') is not None:
            self.color_hex = m.get('ColorHex')
        if m.get('HasPerson') is not None:
            self.has_person = m.get('HasPerson')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageRatio') is not None:
            self.image_ratio = m.get('ImageRatio')
        if m.get('MaxHeight') is not None:
            self.max_height = m.get('MaxHeight')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MaxWidth') is not None:
            self.max_width = m.get('MaxWidth')
        if m.get('MinHeight') is not None:
            self.min_height = m.get('MinHeight')
        if m.get('MinWidth') is not None:
            self.min_width = m.get('MinWidth')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageResponseBodyImageResponseImageList(TeaModel):
    def __init__(
        self,
        descriptive_tones: str = None,
        height: int = None,
        image_category: str = None,
        image_ratio: str = None,
        image_uuid: str = None,
        oss_key: str = None,
        quantitative_palette: str = None,
        tags_from_image: str = None,
        url: str = None,
        width: int = None,
    ):
        self.descriptive_tones = descriptive_tones
        self.height = height
        self.image_category = image_category
        self.image_ratio = image_ratio
        self.image_uuid = image_uuid
        # oss key
        self.oss_key = oss_key
        self.quantitative_palette = quantitative_palette
        self.tags_from_image = tags_from_image
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.descriptive_tones is not None:
            result['DescriptiveTones'] = self.descriptive_tones
        if self.height is not None:
            result['Height'] = self.height
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.image_ratio is not None:
            result['ImageRatio'] = self.image_ratio
        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.quantitative_palette is not None:
            result['QuantitativePalette'] = self.quantitative_palette
        if self.tags_from_image is not None:
            result['TagsFromImage'] = self.tags_from_image
        if self.url is not None:
            result['Url'] = self.url
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescriptiveTones') is not None:
            self.descriptive_tones = m.get('DescriptiveTones')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('ImageRatio') is not None:
            self.image_ratio = m.get('ImageRatio')
        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('QuantitativePalette') is not None:
            self.quantitative_palette = m.get('QuantitativePalette')
        if m.get('TagsFromImage') is not None:
            self.tags_from_image = m.get('TagsFromImage')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class SearchImageResponseBodyImageResponse(TeaModel):
    def __init__(
        self,
        image_list: List[SearchImageResponseBodyImageResponseImageList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.image_list = image_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = SearchImageResponseBodyImageResponseImageList()
                self.image_list.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class SearchImageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        image_response: SearchImageResponseBodyImageResponse = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.image_response = image_response
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.image_response:
            self.image_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.image_response is not None:
            result['ImageResponse'] = self.image_response.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ImageResponse') is not None:
            temp_model = SearchImageResponseBodyImageResponse()
            self.image_response = temp_model.from_map(m['ImageResponse'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageResponseBody = None,
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
            temp_model = SearchImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppDomainCertificateRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        certificate_name: str = None,
        certificate_type: str = None,
        domain_name: str = None,
        private_key: str = None,
        public_key: str = None,
    ):
        self.biz_id = biz_id
        self.certificate_name = certificate_name
        self.certificate_type = certificate_type
        self.domain_name = domain_name
        self.private_key = private_key
        self.public_key = public_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        return self


class SetAppDomainCertificateResponseBodyModule(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetAppDomainCertificateResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: SetAppDomainCertificateResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('Module') is not None:
            temp_model = SetAppDomainCertificateResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class SetAppDomainCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetAppDomainCertificateResponseBody = None,
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
            temp_model = SetAppDomainCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncAppInstanceForPartnerRequestAppInstanceProfile(TeaModel):
    def __init__(
        self,
        deploy_area: str = None,
        lx_instance_id: str = None,
        order_id: str = None,
        site_version: str = None,
        template_etag: str = None,
        template_id: str = None,
    ):
        self.deploy_area = deploy_area
        self.lx_instance_id = lx_instance_id
        self.order_id = order_id
        self.site_version = site_version
        self.template_etag = template_etag
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_area is not None:
            result['DeployArea'] = self.deploy_area
        if self.lx_instance_id is not None:
            result['LxInstanceId'] = self.lx_instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.site_version is not None:
            result['SiteVersion'] = self.site_version
        if self.template_etag is not None:
            result['TemplateEtag'] = self.template_etag
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployArea') is not None:
            self.deploy_area = m.get('DeployArea')
        if m.get('LxInstanceId') is not None:
            self.lx_instance_id = m.get('LxInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')
        if m.get('TemplateEtag') is not None:
            self.template_etag = m.get('TemplateEtag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SyncAppInstanceForPartnerRequestAppInstance(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        biz_id: str = None,
        deleted: str = None,
        domain: str = None,
        end_time: str = None,
        gmt_delete: str = None,
        gmt_publish: str = None,
        icon_url: str = None,
        name: str = None,
        profile: SyncAppInstanceForPartnerRequestAppInstanceProfile = None,
        site_host: str = None,
        slug: str = None,
        start_time: str = None,
        status: str = None,
        thumbnail_url: str = None,
        user_id: str = None,
    ):
        self.app_type = app_type
        self.biz_id = biz_id
        self.deleted = deleted
        self.domain = domain
        self.end_time = end_time
        self.gmt_delete = gmt_delete
        self.gmt_publish = gmt_publish
        self.icon_url = icon_url
        self.name = name
        self.profile = profile
        # siteId
        self.site_host = site_host
        self.slug = slug
        self.start_time = start_time
        self.status = status
        self.thumbnail_url = thumbnail_url
        # 123123123131232
        self.user_id = user_id

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_delete is not None:
            result['GmtDelete'] = self.gmt_delete
        if self.gmt_publish is not None:
            result['GmtPublish'] = self.gmt_publish
        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile.to_map()
        if self.site_host is not None:
            result['SiteHost'] = self.site_host
        if self.slug is not None:
            result['Slug'] = self.slug
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.thumbnail_url is not None:
            result['ThumbnailUrl'] = self.thumbnail_url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtDelete') is not None:
            self.gmt_delete = m.get('GmtDelete')
        if m.get('GmtPublish') is not None:
            self.gmt_publish = m.get('GmtPublish')
        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            temp_model = SyncAppInstanceForPartnerRequestAppInstanceProfile()
            self.profile = temp_model.from_map(m['Profile'])
        if m.get('SiteHost') is not None:
            self.site_host = m.get('SiteHost')
        if m.get('Slug') is not None:
            self.slug = m.get('Slug')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ThumbnailUrl') is not None:
            self.thumbnail_url = m.get('ThumbnailUrl')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SyncAppInstanceForPartnerRequest(TeaModel):
    def __init__(
        self,
        app_instance: SyncAppInstanceForPartnerRequestAppInstance = None,
        event_type: str = None,
        operator: str = None,
        source_biz_id: str = None,
        source_type: str = None,
    ):
        self.app_instance = app_instance
        self.event_type = event_type
        self.operator = operator
        self.source_biz_id = source_biz_id
        self.source_type = source_type

    def validate(self):
        if self.app_instance:
            self.app_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance is not None:
            result['AppInstance'] = self.app_instance.to_map()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            temp_model = SyncAppInstanceForPartnerRequestAppInstance()
            self.app_instance = temp_model.from_map(m['AppInstance'])
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SyncAppInstanceForPartnerShrinkRequest(TeaModel):
    def __init__(
        self,
        app_instance_shrink: str = None,
        event_type: str = None,
        operator: str = None,
        source_biz_id: str = None,
        source_type: str = None,
    ):
        self.app_instance_shrink = app_instance_shrink
        self.event_type = event_type
        self.operator = operator
        self.source_biz_id = source_biz_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_shrink is not None:
            result['AppInstance'] = self.app_instance_shrink
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            self.app_instance_shrink = m.get('AppInstance')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class SyncAppInstanceForPartnerResponseBodyDataAppInstance(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SyncAppInstanceForPartnerResponseBodyData(TeaModel):
    def __init__(
        self,
        app_instance: SyncAppInstanceForPartnerResponseBodyDataAppInstance = None,
    ):
        self.app_instance = app_instance

    def validate(self):
        if self.app_instance:
            self.app_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance is not None:
            result['AppInstance'] = self.app_instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstance') is not None:
            temp_model = SyncAppInstanceForPartnerResponseBodyDataAppInstance()
            self.app_instance = temp_model.from_map(m['AppInstance'])
        return self


class SyncAppInstanceForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        data: SyncAppInstanceForPartnerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SyncAppInstanceForPartnerResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SyncAppInstanceForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncAppInstanceForPartnerResponseBody = None,
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
            temp_model = SyncAppInstanceForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAppDomainRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
    ):
        self.biz_id = biz_id
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class UnbindAppDomainResponseBodyModule(TeaModel):
    def __init__(
        self,
        success: bool = None,
    ):
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindAppDomainResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: UnbindAppDomainResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code
        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')
        if m.get('Module') is not None:
            temp_model = UnbindAppDomainResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')
        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class UnbindAppDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindAppDomainResponseBody = None,
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
            temp_model = UnbindAppDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


