# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CheckSmsVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        case_auth_policy: int = None,
        country_code: str = None,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
        verify_code: str = None,
    ):
        self.case_auth_policy = case_auth_policy
        self.country_code = country_code
        self.out_id = out_id
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_name = scheme_name
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_auth_policy is not None:
            result['CaseAuthPolicy'] = self.case_auth_policy
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseAuthPolicy') is not None:
            self.case_auth_policy = m.get('CaseAuthPolicy')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class CheckSmsVerifyCodeResponseBodyModel(TeaModel):
    def __init__(
        self,
        out_id: str = None,
        verify_result: str = None,
    ):
        self.out_id = out_id
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class CheckSmsVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: CheckSmsVerifyCodeResponseBodyModel = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = CheckSmsVerifyCodeResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckSmsVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckSmsVerifyCodeResponseBody = None,
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
            temp_model = CheckSmsVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchemeConfigRequest(TeaModel):
    def __init__(
        self,
        android_package_name: str = None,
        android_package_sign: str = None,
        app_name: str = None,
        h_5origin: str = None,
        h_5url: str = None,
        ios_bundle_id: str = None,
        owner_id: int = None,
        platform: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
    ):
        self.android_package_name = android_package_name
        self.android_package_sign = android_package_sign
        self.app_name = app_name
        self.h_5origin = h_5origin
        self.h_5url = h_5url
        self.ios_bundle_id = ios_bundle_id
        self.owner_id = owner_id
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_name = scheme_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_package_name is not None:
            result['AndroidPackageName'] = self.android_package_name
        if self.android_package_sign is not None:
            result['AndroidPackageSign'] = self.android_package_sign
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.h_5origin is not None:
            result['H5Origin'] = self.h_5origin
        if self.h_5url is not None:
            result['H5Url'] = self.h_5url
        if self.ios_bundle_id is not None:
            result['IosBundleId'] = self.ios_bundle_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidPackageName') is not None:
            self.android_package_name = m.get('AndroidPackageName')
        if m.get('AndroidPackageSign') is not None:
            self.android_package_sign = m.get('AndroidPackageSign')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('H5Origin') is not None:
            self.h_5origin = m.get('H5Origin')
        if m.get('H5Url') is not None:
            self.h_5url = m.get('H5Url')
        if m.get('IosBundleId') is not None:
            self.ios_bundle_id = m.get('IosBundleId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        return self


class CreateSchemeConfigResponseBodyModel(TeaModel):
    def __init__(
        self,
        scheme_code: str = None,
    ):
        self.scheme_code = scheme_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        return self


class CreateSchemeConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: CreateSchemeConfigResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = CreateSchemeConfigResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSchemeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSchemeConfigResponseBody = None,
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
            temp_model = CreateSchemeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        auth_type: str = None,
        bundle_id: str = None,
        cm_api_code: int = None,
        ct_api_code: int = None,
        cu_api_code: int = None,
        email: str = None,
        ip_white_list: str = None,
        origin: str = None,
        os_type: str = None,
        owner_id: int = None,
        pack_name: str = None,
        pack_sign: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_type: str = None,
        scheme_name: str = None,
        sms_sign_name: str = None,
        url: str = None,
    ):
        self.app_name = app_name
        self.auth_type = auth_type
        self.bundle_id = bundle_id
        self.cm_api_code = cm_api_code
        self.ct_api_code = ct_api_code
        self.cu_api_code = cu_api_code
        self.email = email
        self.ip_white_list = ip_white_list
        self.origin = origin
        self.os_type = os_type
        self.owner_id = owner_id
        self.pack_name = pack_name
        self.pack_sign = pack_sign
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_type = scene_type
        self.scheme_name = scheme_name
        self.sms_sign_name = sms_sign_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.cm_api_code is not None:
            result['CmApiCode'] = self.cm_api_code
        if self.ct_api_code is not None:
            result['CtApiCode'] = self.ct_api_code
        if self.cu_api_code is not None:
            result['CuApiCode'] = self.cu_api_code
        if self.email is not None:
            result['Email'] = self.email
        if self.ip_white_list is not None:
            result['IpWhiteList'] = self.ip_white_list
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pack_name is not None:
            result['PackName'] = self.pack_name
        if self.pack_sign is not None:
            result['PackSign'] = self.pack_sign
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CmApiCode') is not None:
            self.cm_api_code = m.get('CmApiCode')
        if m.get('CtApiCode') is not None:
            self.ct_api_code = m.get('CtApiCode')
        if m.get('CuApiCode') is not None:
            self.cu_api_code = m.get('CuApiCode')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('IpWhiteList') is not None:
            self.ip_white_list = m.get('IpWhiteList')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PackName') is not None:
            self.pack_name = m.get('PackName')
        if m.get('PackSign') is not None:
            self.pack_sign = m.get('PackSign')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateVerifySchemeResponseBodyGateVerifySchemeDTO(TeaModel):
    def __init__(
        self,
        scheme_code: str = None,
    ):
        self.scheme_code = scheme_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        return self


class CreateVerifySchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gate_verify_scheme_dto: CreateVerifySchemeResponseBodyGateVerifySchemeDTO = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.gate_verify_scheme_dto = gate_verify_scheme_dto
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.gate_verify_scheme_dto:
            self.gate_verify_scheme_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gate_verify_scheme_dto is not None:
            result['GateVerifySchemeDTO'] = self.gate_verify_scheme_dto.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GateVerifySchemeDTO') is not None:
            temp_model = CreateVerifySchemeResponseBodyGateVerifySchemeDTO()
            self.gate_verify_scheme_dto = temp_model.from_map(m['GateVerifySchemeDTO'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateVerifySchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVerifySchemeResponseBody = None,
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
            temp_model = CreateVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        customer_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_code: str = None,
    ):
        self.customer_id = customer_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_code = scheme_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        return self


class DeleteVerifySchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteVerifySchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVerifySchemeResponseBody = None,
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
            temp_model = DeleteVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        customer_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_code: str = None,
    ):
        self.customer_id = customer_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_code = scheme_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        return self


class DescribeVerifySchemeResponseBodySchemeQueryResultDTO(TeaModel):
    def __init__(
        self,
        app_encrypt_info: str = None,
    ):
        self.app_encrypt_info = app_encrypt_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_encrypt_info is not None:
            result['AppEncryptInfo'] = self.app_encrypt_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppEncryptInfo') is not None:
            self.app_encrypt_info = m.get('AppEncryptInfo')
        return self


class DescribeVerifySchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        scheme_query_result_dto: DescribeVerifySchemeResponseBodySchemeQueryResultDTO = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.scheme_query_result_dto = scheme_query_result_dto

    def validate(self):
        if self.scheme_query_result_dto:
            self.scheme_query_result_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scheme_query_result_dto is not None:
            result['SchemeQueryResultDTO'] = self.scheme_query_result_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SchemeQueryResultDTO') is not None:
            temp_model = DescribeVerifySchemeResponseBodySchemeQueryResultDTO()
            self.scheme_query_result_dto = temp_model.from_map(m['SchemeQueryResultDTO'])
        return self


class DescribeVerifySchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVerifySchemeResponseBody = None,
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
            temp_model = DescribeVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(
        self,
        origin: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        url: str = None,
    ):
        self.origin = origin
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin is not None:
            result['Origin'] = self.origin
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAuthTokenResponseBodyTokenInfo(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        jwt_token: str = None,
    ):
        self.access_token = access_token
        self.jwt_token = jwt_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.jwt_token is not None:
            result['JwtToken'] = self.jwt_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('JwtToken') is not None:
            self.jwt_token = m.get('JwtToken')
        return self


class GetAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        token_info: GetAuthTokenResponseBodyTokenInfo = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.token_info = token_info

    def validate(self):
        if self.token_info:
            self.token_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token_info is not None:
            result['TokenInfo'] = self.token_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TokenInfo') is not None:
            temp_model = GetAuthTokenResponseBodyTokenInfo()
            self.token_info = temp_model.from_map(m['TokenInfo'])
        return self


class GetAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthTokenResponseBody = None,
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
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationUrlRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        owner_id: int = None,
        phone_no: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_id: int = None,
    ):
        self.end_date = end_date
        self.owner_id = owner_id
        self.phone_no = phone_no
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_id = scheme_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        return self


class GetAuthorizationUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        authorization_url: str = None,
    ):
        self.authorization_url = authorization_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_url is not None:
            result['AuthorizationUrl'] = self.authorization_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationUrl') is not None:
            self.authorization_url = m.get('AuthorizationUrl')
        return self


class GetAuthorizationUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAuthorizationUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetAuthorizationUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthorizationUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthorizationUrlResponseBody = None,
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
            temp_model = GetAuthorizationUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFusionAuthTokenRequest(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        duration_seconds: int = None,
        owner_id: int = None,
        package_name: str = None,
        package_sign: str = None,
        platform: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_code: str = None,
    ):
        self.bundle_id = bundle_id
        self.duration_seconds = duration_seconds
        self.owner_id = owner_id
        self.package_name = package_name
        self.package_sign = package_sign
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_code = scheme_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.package_sign is not None:
            result['PackageSign'] = self.package_sign
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('PackageSign') is not None:
            self.package_sign = m.get('PackageSign')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        return self


class GetFusionAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFusionAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFusionAuthTokenResponseBody = None,
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
            temp_model = GetFusionAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMobileRequest(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.access_token = access_token
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetMobileResponseBodyGetMobileResultDTO(TeaModel):
    def __init__(
        self,
        mobile: str = None,
    ):
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class GetMobileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        get_mobile_result_dto: GetMobileResponseBodyGetMobileResultDTO = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.get_mobile_result_dto = get_mobile_result_dto
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.get_mobile_result_dto:
            self.get_mobile_result_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.get_mobile_result_dto is not None:
            result['GetMobileResultDTO'] = self.get_mobile_result_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GetMobileResultDTO') is not None:
            temp_model = GetMobileResponseBodyGetMobileResultDTO()
            self.get_mobile_result_dto = temp_model.from_map(m['GetMobileResultDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMobileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMobileResponseBody = None,
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
            temp_model = GetMobileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneWithTokenRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sp_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sp_token = sp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sp_token is not None:
            result['SpToken'] = self.sp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpToken') is not None:
            self.sp_token = m.get('SpToken')
        return self


class GetPhoneWithTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        mobile: str = None,
    ):
        self.mobile = mobile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        return self


class GetPhoneWithTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPhoneWithTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetPhoneWithTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPhoneWithTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneWithTokenResponseBody = None,
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
            temp_model = GetPhoneWithTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmsAuthTokensRequest(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        expire: int = None,
        os_type: str = None,
        owner_id: int = None,
        package_name: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_code: str = None,
        sign_name: str = None,
        sms_code_expire: int = None,
        sms_template_code: str = None,
    ):
        self.bundle_id = bundle_id
        self.expire = expire
        self.os_type = os_type
        self.owner_id = owner_id
        self.package_name = package_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_code = scene_code
        self.sign_name = sign_name
        self.sms_code_expire = sms_code_expire
        self.sms_template_code = sms_template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_code_expire is not None:
            result['SmsCodeExpire'] = self.sms_code_expire
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsCodeExpire') is not None:
            self.sms_code_expire = m.get('SmsCodeExpire')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        return self


class GetSmsAuthTokensResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_token: str = None,
        expire_time: int = None,
        sts_access_key_id: str = None,
        sts_access_key_secret: str = None,
        sts_token: str = None,
    ):
        self.biz_token = biz_token
        self.expire_time = expire_time
        self.sts_access_key_id = sts_access_key_id
        self.sts_access_key_secret = sts_access_key_secret
        self.sts_token = sts_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_token is not None:
            result['BizToken'] = self.biz_token
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.sts_access_key_id is not None:
            result['StsAccessKeyId'] = self.sts_access_key_id
        if self.sts_access_key_secret is not None:
            result['StsAccessKeySecret'] = self.sts_access_key_secret
        if self.sts_token is not None:
            result['StsToken'] = self.sts_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizToken') is not None:
            self.biz_token = m.get('BizToken')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('StsAccessKeyId') is not None:
            self.sts_access_key_id = m.get('StsAccessKeyId')
        if m.get('StsAccessKeySecret') is not None:
            self.sts_access_key_secret = m.get('StsAccessKeySecret')
        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')
        return self


class GetSmsAuthTokensResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSmsAuthTokensResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSmsAuthTokensResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSmsAuthTokensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSmsAuthTokensResponseBody = None,
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
            temp_model = GetSmsAuthTokensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGateVerifyBillingPublicRequest(TeaModel):
    def __init__(
        self,
        authentication_type: int = None,
        month: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
    ):
        self.authentication_type = authentication_type
        self.month = month
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type
        if self.month is not None:
            result['Month'] = self.month
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class QueryGateVerifyBillingPublicResponseBodyDataSceneBillingList(TeaModel):
    def __init__(
        self,
        add: str = None,
        amount: str = None,
        app_name: str = None,
        item_name: str = None,
        scene_code: str = None,
        scene_name: str = None,
        single_price: str = None,
    ):
        self.add = add
        self.amount = amount
        self.app_name = app_name
        self.item_name = item_name
        self.scene_code = scene_code
        self.scene_name = scene_name
        self.single_price = single_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.single_price is not None:
            result['SinglePrice'] = self.single_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SinglePrice') is not None:
            self.single_price = m.get('SinglePrice')
        return self


class QueryGateVerifyBillingPublicResponseBodyData(TeaModel):
    def __init__(
        self,
        amount_sum: str = None,
        scene_billing_list: List[QueryGateVerifyBillingPublicResponseBodyDataSceneBillingList] = None,
    ):
        self.amount_sum = amount_sum
        self.scene_billing_list = scene_billing_list

    def validate(self):
        if self.scene_billing_list:
            for k in self.scene_billing_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount_sum is not None:
            result['AmountSum'] = self.amount_sum
        result['SceneBillingList'] = []
        if self.scene_billing_list is not None:
            for k in self.scene_billing_list:
                result['SceneBillingList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmountSum') is not None:
            self.amount_sum = m.get('AmountSum')
        self.scene_billing_list = []
        if m.get('SceneBillingList') is not None:
            for k in m.get('SceneBillingList'):
                temp_model = QueryGateVerifyBillingPublicResponseBodyDataSceneBillingList()
                self.scene_billing_list.append(temp_model.from_map(k))
        return self


class QueryGateVerifyBillingPublicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryGateVerifyBillingPublicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryGateVerifyBillingPublicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryGateVerifyBillingPublicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGateVerifyBillingPublicResponseBody = None,
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
            temp_model = QueryGateVerifyBillingPublicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGateVerifyStatisticPublicRequest(TeaModel):
    def __init__(
        self,
        authentication_type: int = None,
        end_date: str = None,
        os_type: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        scene_code: str = None,
        start_date: str = None,
    ):
        self.authentication_type = authentication_type
        self.end_date = end_date
        self.os_type = os_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.scene_code = scene_code
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryGateVerifyStatisticPublicResponseBodyDataDayStatistic(TeaModel):
    def __init__(
        self,
        statistic_date_str: str = None,
        total_fail: int = None,
        total_success: int = None,
        total_unknown: int = None,
    ):
        self.statistic_date_str = statistic_date_str
        self.total_fail = total_fail
        self.total_success = total_success
        self.total_unknown = total_unknown

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.statistic_date_str is not None:
            result['StatisticDateStr'] = self.statistic_date_str
        if self.total_fail is not None:
            result['TotalFail'] = self.total_fail
        if self.total_success is not None:
            result['TotalSuccess'] = self.total_success
        if self.total_unknown is not None:
            result['TotalUnknown'] = self.total_unknown
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatisticDateStr') is not None:
            self.statistic_date_str = m.get('StatisticDateStr')
        if m.get('TotalFail') is not None:
            self.total_fail = m.get('TotalFail')
        if m.get('TotalSuccess') is not None:
            self.total_success = m.get('TotalSuccess')
        if m.get('TotalUnknown') is not None:
            self.total_unknown = m.get('TotalUnknown')
        return self


class QueryGateVerifyStatisticPublicResponseBodyData(TeaModel):
    def __init__(
        self,
        day_statistic: List[QueryGateVerifyStatisticPublicResponseBodyDataDayStatistic] = None,
        total: int = None,
        total_fail: int = None,
        total_success: int = None,
        total_unknown: int = None,
    ):
        self.day_statistic = day_statistic
        self.total = total
        self.total_fail = total_fail
        self.total_success = total_success
        self.total_unknown = total_unknown

    def validate(self):
        if self.day_statistic:
            for k in self.day_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DayStatistic'] = []
        if self.day_statistic is not None:
            for k in self.day_statistic:
                result['DayStatistic'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.total_fail is not None:
            result['TotalFail'] = self.total_fail
        if self.total_success is not None:
            result['TotalSuccess'] = self.total_success
        if self.total_unknown is not None:
            result['TotalUnknown'] = self.total_unknown
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.day_statistic = []
        if m.get('DayStatistic') is not None:
            for k in m.get('DayStatistic'):
                temp_model = QueryGateVerifyStatisticPublicResponseBodyDataDayStatistic()
                self.day_statistic.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TotalFail') is not None:
            self.total_fail = m.get('TotalFail')
        if m.get('TotalSuccess') is not None:
            self.total_success = m.get('TotalSuccess')
        if m.get('TotalUnknown') is not None:
            self.total_unknown = m.get('TotalUnknown')
        return self


class QueryGateVerifyStatisticPublicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryGateVerifyStatisticPublicResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryGateVerifyStatisticPublicResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryGateVerifyStatisticPublicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryGateVerifyStatisticPublicResponseBody = None,
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
            temp_model = QueryGateVerifyStatisticPublicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySendDetailsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        current_page: int = None,
        owner_id: int = None,
        page_size: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        send_date: str = None,
    ):
        self.biz_id = biz_id
        self.current_page = current_page
        self.owner_id = owner_id
        self.page_size = page_size
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.send_date = send_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        return self


class QuerySendDetailsResponseBodyModel(TeaModel):
    def __init__(
        self,
        content: str = None,
        err_code: str = None,
        out_id: str = None,
        phone_num: str = None,
        receive_date: str = None,
        send_date: str = None,
        send_status: int = None,
        template_code: str = None,
    ):
        self.content = content
        self.err_code = err_code
        self.out_id = out_id
        self.phone_num = phone_num
        self.receive_date = receive_date
        self.send_date = send_date
        self.send_status = send_status
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class QuerySendDetailsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: List[QuerySendDetailsResponseBodyModel] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = QuerySendDetailsResponseBodyModel()
                self.model.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySendDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySendDetailsResponseBody = None,
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
            temp_model = QuerySendDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendSmsVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        code_length: int = None,
        code_type: int = None,
        country_code: str = None,
        duplicate_policy: int = None,
        interval: int = None,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        return_verify_code: bool = None,
        scheme_name: str = None,
        sign_name: str = None,
        sms_up_extend_code: str = None,
        template_code: str = None,
        template_param: str = None,
        valid_time: int = None,
    ):
        self.code_length = code_length
        self.code_type = code_type
        self.country_code = country_code
        self.duplicate_policy = duplicate_policy
        self.interval = interval
        self.out_id = out_id
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.return_verify_code = return_verify_code
        self.scheme_name = scheme_name
        self.sign_name = sign_name
        self.sms_up_extend_code = sms_up_extend_code
        self.template_code = template_code
        self.template_param = template_param
        self.valid_time = valid_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_length is not None:
            result['CodeLength'] = self.code_length
        if self.code_type is not None:
            result['CodeType'] = self.code_type
        if self.country_code is not None:
            result['CountryCode'] = self.country_code
        if self.duplicate_policy is not None:
            result['DuplicatePolicy'] = self.duplicate_policy
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.return_verify_code is not None:
            result['ReturnVerifyCode'] = self.return_verify_code
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeLength') is not None:
            self.code_length = m.get('CodeLength')
        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')
        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')
        if m.get('DuplicatePolicy') is not None:
            self.duplicate_policy = m.get('DuplicatePolicy')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ReturnVerifyCode') is not None:
            self.return_verify_code = m.get('ReturnVerifyCode')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        return self


class SendSmsVerifyCodeResponseBodyModel(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        out_id: str = None,
        request_id: str = None,
        verify_code: str = None,
    ):
        self.biz_id = biz_id
        self.out_id = out_id
        self.request_id = request_id
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class SendSmsVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: SendSmsVerifyCodeResponseBodyModel = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = SendSmsVerifyCodeResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendSmsVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendSmsVerifyCodeResponseBody = None,
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
            temp_model = SendSmsVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMobileRequest(TeaModel):
    def __init__(
        self,
        access_code: str = None,
        out_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.access_code = access_code
        self.out_id = out_id
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_code is not None:
            result['AccessCode'] = self.access_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCode') is not None:
            self.access_code = m.get('AccessCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class VerifyMobileResponseBodyGateVerifyResultDTO(TeaModel):
    def __init__(
        self,
        verify_id: str = None,
        verify_result: str = None,
    ):
        self.verify_id = verify_id
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyMobileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gate_verify_result_dto: VerifyMobileResponseBodyGateVerifyResultDTO = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.gate_verify_result_dto = gate_verify_result_dto
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.gate_verify_result_dto:
            self.gate_verify_result_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gate_verify_result_dto is not None:
            result['GateVerifyResultDTO'] = self.gate_verify_result_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GateVerifyResultDTO') is not None:
            temp_model = VerifyMobileResponseBodyGateVerifyResultDTO()
            self.gate_verify_result_dto = temp_model.from_map(m['GateVerifyResultDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyMobileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyMobileResponseBody = None,
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
            temp_model = VerifyMobileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPhoneWithTokenRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sp_token: str = None,
    ):
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sp_token = sp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sp_token is not None:
            result['SpToken'] = self.sp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpToken') is not None:
            self.sp_token = m.get('SpToken')
        return self


class VerifyPhoneWithTokenResponseBodyGateVerify(TeaModel):
    def __init__(
        self,
        verify_id: str = None,
        verify_result: str = None,
    ):
        self.verify_id = verify_id
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyPhoneWithTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gate_verify: VerifyPhoneWithTokenResponseBodyGateVerify = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.gate_verify = gate_verify
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.gate_verify:
            self.gate_verify.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gate_verify is not None:
            result['GateVerify'] = self.gate_verify.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GateVerify') is not None:
            temp_model = VerifyPhoneWithTokenResponseBodyGateVerify()
            self.gate_verify = temp_model.from_map(m['GateVerify'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyPhoneWithTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyPhoneWithTokenResponseBody = None,
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
            temp_model = VerifyPhoneWithTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifySmsCodeRequest(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        sms_code: str = None,
        sms_token: str = None,
    ):
        self.phone_number = phone_number
        self.sms_code = sms_code
        self.sms_token = sms_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.sms_code is not None:
            result['SmsCode'] = self.sms_code
        if self.sms_token is not None:
            result['SmsToken'] = self.sms_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SmsCode') is not None:
            self.sms_code = m.get('SmsCode')
        if m.get('SmsToken') is not None:
            self.sms_token = m.get('SmsToken')
        return self


class VerifySmsCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifySmsCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifySmsCodeResponseBody = None,
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
            temp_model = VerifySmsCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyWithFusionAuthTokenRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verify_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.verify_token = verify_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class VerifyWithFusionAuthTokenResponseBodyModel(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        phone_score: int = None,
        verify_result: str = None,
    ):
        self.phone_number = phone_number
        self.phone_score = phone_score
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_score is not None:
            result['PhoneScore'] = self.phone_score
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneScore') is not None:
            self.phone_score = m.get('PhoneScore')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyWithFusionAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        model: VerifyWithFusionAuthTokenResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = VerifyWithFusionAuthTokenResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class VerifyWithFusionAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyWithFusionAuthTokenResponseBody = None,
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
            temp_model = VerifyWithFusionAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


