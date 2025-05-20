# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ActivateLicenseRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        license_code: str = None,
        license_no: str = None,
        license_publisher: str = None,
    ):
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.license_code = license_code
        self.license_no = license_no
        # This parameter is required.
        self.license_publisher = license_publisher

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.license_no is not None:
            result['LicenseNo'] = self.license_no
        if self.license_publisher is not None:
            result['LicensePublisher'] = self.license_publisher
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('LicenseNo') is not None:
            self.license_no = m.get('LicenseNo')
        if m.get('LicensePublisher') is not None:
            self.license_publisher = m.get('LicensePublisher')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class ActivateLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateLicenseResponseBody = None,
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
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CallbackTaskRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        biz_code: str = None,
        lang: str = None,
        order_id: str = None,
        original_request: str = None,
        out_task_id: str = None,
        principal_key: str = None,
        task_data: str = None,
        task_id: str = None,
        task_type: str = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        self.biz_code = biz_code
        # lang
        self.lang = lang
        # orderId
        self.order_id = order_id
        # originalRequest
        self.original_request = original_request
        # outTaskId
        self.out_task_id = out_task_id
        self.principal_key = principal_key
        # taskData
        self.task_data = task_data
        # taskId
        self.task_id = task_id
        # taskType
        self.task_type = task_type
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.out_task_id is not None:
            result['OutTaskId'] = self.out_task_id
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.task_data is not None:
            result['TaskData'] = self.task_data
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('OutTaskId') is not None:
            self.out_task_id = m.get('OutTaskId')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('TaskData') is not None:
            self.task_data = m.get('TaskData')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class CallbackTaskResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CallbackTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CallbackTaskResponseBody = None,
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
            temp_model = CallbackTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAgreementStatusRequest(TeaModel):
    def __init__(
        self,
        agreement_code: str = None,
    ):
        self.agreement_code = agreement_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class DescribeAgreementStatusResponseBody(TeaModel):
    def __init__(
        self,
        agreement_code: str = None,
        request_id: str = None,
        status: int = None,
        user_id: str = None,
    ):
        self.agreement_code = agreement_code
        self.request_id = request_id
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeAgreementStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAgreementStatusResponseBody = None,
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
            temp_model = DescribeAgreementStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadFilePolicyForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        file_name: str = None,
        file_type: str = None,
    ):
        self.biz_type = biz_type
        self.file_name = file_name
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class GenerateUploadFilePolicyForPartnerResponseBodyModule(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        encoded_policy: str = None,
        expire_time: int = None,
        file_dir: str = None,
        host: str = None,
        oss_url: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.encoded_policy = encoded_policy
        self.expire_time = expire_time
        self.file_dir = file_dir
        self.host = host
        self.oss_url = oss_url
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.encoded_policy is not None:
            result['EncodedPolicy'] = self.encoded_policy
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_dir is not None:
            result['FileDir'] = self.file_dir
        if self.host is not None:
            result['Host'] = self.host
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('EncodedPolicy') is not None:
            self.encoded_policy = m.get('EncodedPolicy')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileDir') is not None:
            self.file_dir = m.get('FileDir')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GenerateUploadFilePolicyForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: GenerateUploadFilePolicyForPartnerResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.module = module
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = GenerateUploadFilePolicyForPartnerResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateUploadFilePolicyForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUploadFilePolicyForPartnerResponseBody = None,
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
            temp_model = GenerateUploadFilePolicyForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeByFlowIdRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        flow_id: int = None,
        lang: str = None,
        original_request: str = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        self.flow_id = flow_id
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class GetNodeByFlowIdResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNodeByFlowIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeByFlowIdResponseBody = None,
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
            temp_model = GetNodeByFlowIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeByTemplateIdRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        lang: str = None,
        original_request: str = None,
        template_id: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        self.template_id = template_id
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class GetNodeByTemplateIdResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNodeByTemplateIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeByTemplateIdResponseBody = None,
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
            temp_model = GetNodeByTemplateIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProxyByTypeRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        lang: str = None,
        original_request: str = None,
        type: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        # type
        self.type = type
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.type is not None:
            result['Type'] = self.type
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class GetProxyByTypeResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProxyByTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProxyByTypeResponseBody = None,
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
            temp_model = GetProxyByTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRedisValueRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        key: str = None,
        lang: str = None,
        original_request: str = None,
        timeout: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
        value: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # key
        self.key = key
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        # timeout
        self.timeout = timeout
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.key is not None:
            result['Key'] = self.key
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetRedisValueResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRedisValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRedisValueResponseBody = None,
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
            temp_model = GetRedisValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVariableRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        lang: str = None,
        original_request: str = None,
        template_id: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        self.template_id = template_id
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class GetVariableResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVariableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVariableResponseBody = None,
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
            temp_model = GetVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IdentifyCodeRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        data: str = None,
        label: str = None,
        lang: str = None,
        original_request: str = None,
        type: str = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        self.data = data
        self.label = label
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        self.type = type
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.data is not None:
            result['Data'] = self.data
        if self.label is not None:
            result['Label'] = self.label
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.type is not None:
            result['Type'] = self.type
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class IdentifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IdentifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IdentifyCodeResponseBody = None,
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
            temp_model = IdentifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullRpaModelRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        lang: str = None,
        original_request: str = None,
        template_id: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        # templateId
        self.template_id = template_id
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class PullRpaModelResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PullRpaModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PullRpaModelResponseBody = None,
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
            temp_model = PullRpaModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullTaskRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        biz_code: str = None,
        lang: str = None,
        order_id: str = None,
        original_request: str = None,
        principal_key: str = None,
        task_type: str = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_security_transport: bool = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        self.biz_code = biz_code
        # lang
        self.lang = lang
        self.order_id = order_id
        # originalRequest
        self.original_request = original_request
        self.principal_key = principal_key
        # taskType
        self.task_type = task_type
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerSecurityTransport
        self.user_caller_security_transport = user_caller_security_transport
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_security_transport is not None:
            result['UserCallerSecurityTransport'] = self.user_caller_security_transport
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerSecurityTransport') is not None:
            self.user_caller_security_transport = m.get('UserCallerSecurityTransport')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class PullTaskResponseBodyModule(TeaModel):
    def __init__(
        self,
        biz_code: str = None,
        order_id: str = None,
        out_task_id: str = None,
        principal_key: str = None,
        task_data: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        self.biz_code = biz_code
        self.order_id = order_id
        self.out_task_id = out_task_id
        self.principal_key = principal_key
        self.task_data = task_data
        self.task_id = task_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.out_task_id is not None:
            result['OutTaskId'] = self.out_task_id
        if self.principal_key is not None:
            result['PrincipalKey'] = self.principal_key
        if self.task_data is not None:
            result['TaskData'] = self.task_data
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OutTaskId') is not None:
            self.out_task_id = m.get('OutTaskId')
        if m.get('PrincipalKey') is not None:
            self.principal_key = m.get('PrincipalKey')
        if m.get('TaskData') is not None:
            self.task_data = m.get('TaskData')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class PullTaskResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: PullTaskResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            temp_model = PullTaskResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PullTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PullTaskResponseBody = None,
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
            temp_model = PullTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushRpaTaskRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        lang: str = None,
        model_id: int = None,
        name: str = None,
        original_request: str = None,
        request: str = None,
        status: int = None,
        task_id: int = None,
        template_id: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # lang
        self.lang = lang
        # modelId
        self.model_id = model_id
        # name
        self.name = name
        # originalRequest
        self.original_request = original_request
        # request
        self.request = request
        # status
        self.status = status
        # taskId
        self.task_id = task_id
        # templateId
        self.template_id = template_id
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.name is not None:
            result['Name'] = self.name
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.request is not None:
            result['Request'] = self.request
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('Request') is not None:
            self.request = m.get('Request')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class PushRpaTaskResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushRpaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushRpaTaskResponseBody = None,
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
            temp_model = PushRpaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushRpaTaskDetailRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        input_data: str = None,
        input_html: str = None,
        input_screenshot: str = None,
        lang: str = None,
        model_detail_id: int = None,
        original_request: str = None,
        output_data: str = None,
        output_html: str = None,
        output_screenshot: str = None,
        status: int = None,
        task_detail_id: int = None,
        task_id: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_security_token: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        # inputData
        self.input_data = input_data
        # inputHtml
        self.input_html = input_html
        # inputScreenshot
        self.input_screenshot = input_screenshot
        # lang
        self.lang = lang
        # modelDetailId
        self.model_detail_id = model_detail_id
        # originalRequest
        self.original_request = original_request
        # outputData
        self.output_data = output_data
        # outputHtml
        self.output_html = output_html
        # outputScreenshot
        self.output_screenshot = output_screenshot
        # status
        self.status = status
        # taskDetailId
        self.task_detail_id = task_detail_id
        # taskId
        self.task_id = task_id
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userSecurityToken
        self.user_security_token = user_security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.input_data is not None:
            result['InputData'] = self.input_data
        if self.input_html is not None:
            result['InputHtml'] = self.input_html
        if self.input_screenshot is not None:
            result['InputScreenshot'] = self.input_screenshot
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.model_detail_id is not None:
            result['ModelDetailId'] = self.model_detail_id
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.output_data is not None:
            result['OutputData'] = self.output_data
        if self.output_html is not None:
            result['OutputHtml'] = self.output_html
        if self.output_screenshot is not None:
            result['OutputScreenshot'] = self.output_screenshot
        if self.status is not None:
            result['Status'] = self.status
        if self.task_detail_id is not None:
            result['TaskDetailId'] = self.task_detail_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('InputData') is not None:
            self.input_data = m.get('InputData')
        if m.get('InputHtml') is not None:
            self.input_html = m.get('InputHtml')
        if m.get('InputScreenshot') is not None:
            self.input_screenshot = m.get('InputScreenshot')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ModelDetailId') is not None:
            self.model_detail_id = m.get('ModelDetailId')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('OutputData') is not None:
            self.output_data = m.get('OutputData')
        if m.get('OutputHtml') is not None:
            self.output_html = m.get('OutputHtml')
        if m.get('OutputScreenshot') is not None:
            self.output_screenshot = m.get('OutputScreenshot')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskDetailId') is not None:
            self.task_detail_id = m.get('TaskDetailId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        return self


class PushRpaTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushRpaTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushRpaTaskDetailResponseBody = None,
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
            temp_model = PushRpaTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendNotificationForPartnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        channel_type: str = None,
        notify_type: str = None,
        notifycation_event_type: str = None,
        param_map: Dict[str, str] = None,
        send_target: str = None,
        smart_sub_channels: List[str] = None,
        track_id: str = None,
    ):
        self.biz_id = biz_id
        self.channel_type = channel_type
        self.notify_type = notify_type
        self.notifycation_event_type = notifycation_event_type
        self.param_map = param_map
        self.send_target = send_target
        self.smart_sub_channels = smart_sub_channels
        self.track_id = track_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.notifycation_event_type is not None:
            result['NotifycationEventType'] = self.notifycation_event_type
        if self.param_map is not None:
            result['ParamMap'] = self.param_map
        if self.send_target is not None:
            result['SendTarget'] = self.send_target
        if self.smart_sub_channels is not None:
            result['SmartSubChannels'] = self.smart_sub_channels
        if self.track_id is not None:
            result['TrackId'] = self.track_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('NotifycationEventType') is not None:
            self.notifycation_event_type = m.get('NotifycationEventType')
        if m.get('ParamMap') is not None:
            self.param_map = m.get('ParamMap')
        if m.get('SendTarget') is not None:
            self.send_target = m.get('SendTarget')
        if m.get('SmartSubChannels') is not None:
            self.smart_sub_channels = m.get('SmartSubChannels')
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')
        return self


class SendNotificationForPartnerShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        channel_type: str = None,
        notify_type: str = None,
        notifycation_event_type: str = None,
        param_map_shrink: str = None,
        send_target: str = None,
        smart_sub_channels_shrink: str = None,
        track_id: str = None,
    ):
        self.biz_id = biz_id
        self.channel_type = channel_type
        self.notify_type = notify_type
        self.notifycation_event_type = notifycation_event_type
        self.param_map_shrink = param_map_shrink
        self.send_target = send_target
        self.smart_sub_channels_shrink = smart_sub_channels_shrink
        self.track_id = track_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.notifycation_event_type is not None:
            result['NotifycationEventType'] = self.notifycation_event_type
        if self.param_map_shrink is not None:
            result['ParamMap'] = self.param_map_shrink
        if self.send_target is not None:
            result['SendTarget'] = self.send_target
        if self.smart_sub_channels_shrink is not None:
            result['SmartSubChannels'] = self.smart_sub_channels_shrink
        if self.track_id is not None:
            result['TrackId'] = self.track_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('NotifycationEventType') is not None:
            self.notifycation_event_type = m.get('NotifycationEventType')
        if m.get('ParamMap') is not None:
            self.param_map_shrink = m.get('ParamMap')
        if m.get('SendTarget') is not None:
            self.send_target = m.get('SendTarget')
        if m.get('SmartSubChannels') is not None:
            self.smart_sub_channels_shrink = m.get('SmartSubChannels')
        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')
        return self


class SendNotificationForPartnerResponseBody(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        msg_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_msg = error_msg
        self.msg_id = msg_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendNotificationForPartnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendNotificationForPartnerResponseBody = None,
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
            temp_model = SendNotificationForPartnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRedisValueRequest(TeaModel):
    def __init__(
        self,
        aliyun_kp: str = None,
        api_type: str = None,
        bid: str = None,
        key: str = None,
        lang: str = None,
        original_request: str = None,
        request_id: str = None,
        timeout: int = None,
        user_access_key_id: str = None,
        user_bid: str = None,
        user_caller_parent_id: int = None,
        user_caller_type: str = None,
        user_client_ip: str = None,
        user_kp: str = None,
        user_mfa_present: bool = None,
        user_security_token: str = None,
        value: str = None,
    ):
        # aliyunKp
        self.aliyun_kp = aliyun_kp
        # apiType
        self.api_type = api_type
        # bid
        self.bid = bid
        self.key = key
        # lang
        self.lang = lang
        # originalRequest
        self.original_request = original_request
        # requestId
        self.request_id = request_id
        # timeout
        self.timeout = timeout
        # userAccessKeyId
        self.user_access_key_id = user_access_key_id
        # userBid
        self.user_bid = user_bid
        # userCallerParentId
        self.user_caller_parent_id = user_caller_parent_id
        # userCallerType
        self.user_caller_type = user_caller_type
        # userClientIp
        self.user_client_ip = user_client_ip
        # userKp
        self.user_kp = user_kp
        # userMfaPresent
        self.user_mfa_present = user_mfa_present
        # userSecurityToken
        self.user_security_token = user_security_token
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_kp is not None:
            result['AliyunKp'] = self.aliyun_kp
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.key is not None:
            result['Key'] = self.key
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.original_request is not None:
            result['OriginalRequest'] = self.original_request
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id
        if self.user_bid is not None:
            result['UserBid'] = self.user_bid
        if self.user_caller_parent_id is not None:
            result['UserCallerParentId'] = self.user_caller_parent_id
        if self.user_caller_type is not None:
            result['UserCallerType'] = self.user_caller_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.user_kp is not None:
            result['UserKp'] = self.user_kp
        if self.user_mfa_present is not None:
            result['UserMfaPresent'] = self.user_mfa_present
        if self.user_security_token is not None:
            result['UserSecurityToken'] = self.user_security_token
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunKp') is not None:
            self.aliyun_kp = m.get('AliyunKp')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OriginalRequest') is not None:
            self.original_request = m.get('OriginalRequest')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')
        if m.get('UserBid') is not None:
            self.user_bid = m.get('UserBid')
        if m.get('UserCallerParentId') is not None:
            self.user_caller_parent_id = m.get('UserCallerParentId')
        if m.get('UserCallerType') is not None:
            self.user_caller_type = m.get('UserCallerType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')
        if m.get('UserMfaPresent') is not None:
            self.user_mfa_present = m.get('UserMfaPresent')
        if m.get('UserSecurityToken') is not None:
            self.user_security_token = m.get('UserSecurityToken')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetRedisValueResponseBody(TeaModel):
    def __init__(
        self,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_status_code: int = None,
        module: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # allowRetry
        self.allow_retry = allow_retry
        # appName
        self.app_name = app_name
        # dynamicCode
        self.dynamic_code = dynamic_code
        # dynamicMessage
        self.dynamic_message = dynamic_message
        # errorCode
        self.error_code = error_code
        # errorMsg
        self.error_msg = error_msg
        # httpStatusCode
        self.http_status_code = http_status_code
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetRedisValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetRedisValueResponseBody = None,
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
            temp_model = SetRedisValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgreementStatusRequest(TeaModel):
    def __init__(
        self,
        agreement_code: str = None,
    ):
        self.agreement_code = agreement_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agreement_code is not None:
            result['AgreementCode'] = self.agreement_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreementCode') is not None:
            self.agreement_code = m.get('AgreementCode')
        return self


class UpdateAgreementStatusResponseBody(TeaModel):
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


class UpdateAgreementStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAgreementStatusResponseBody = None,
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
            temp_model = UpdateAgreementStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


