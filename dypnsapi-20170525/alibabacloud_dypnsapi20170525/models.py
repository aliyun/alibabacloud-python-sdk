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
        # The verification policy for uppercase and lowercase letters of the verification code. Valid values:
        # 
        # *   1: The verification policy does not distinguish uppercase and lowercase letters.
        # *   2: The verification policy distinguishes uppercase and lowercase letters.
        self.case_auth_policy = case_auth_policy
        # The country code of the phone number. Default value: 86.
        self.country_code = country_code
        # The external ID.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The verification service name. If this parameter is not specified, the default service is used. The name can be up to 20 characters in length.
        self.scheme_name = scheme_name
        # The verification code.
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
        # The external ID.
        self.out_id = out_id
        # The verification results. Valid values:
        # 
        # *   PASS: The verification is successful.
        # *   UNKNOWN: The verification failed.
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [Response codes](https://help.aliyun.com/zh/pnvs/developer-reference/api-return-code?spm=a2c4g.11174283.0.0.70c5616bkj38Wa).
        self.code = code
        # The returned message.
        self.message = message
        # The returned data.
        self.model = model
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
        # The package name. This parameter is required when Platform is set to Android. The name must be 1 to 128 characters in length and can contain digits, letters, hyphens (-), underscores (\_), and periods (.).
        self.android_package_name = android_package_name
        # The package signature. This parameter is required when Platform is set to Android. The signature must be 32 characters in length and can contain digits and letters.
        self.android_package_sign = android_package_sign
        # The app name, which can be up to 20 characters in length and can contain letters.
        self.app_name = app_name
        # The reserved field. HTML5 apps are not supported.
        self.h_5origin = h_5origin
        # The reserved field. HTML5 apps are not supported.
        self.h_5url = h_5url
        # The bundle ID. This parameter is required when OsType is set to iOS. The bundle ID must be 1 to 128 characters in length and can contain digits, letters, hyphens (-), underscores (\_), and periods (.).
        self.ios_bundle_id = ios_bundle_id
        self.owner_id = owner_id
        # The app platform.
        # 
        # Valid values:
        # 
        # *   Android
        # *   iOS
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service name, which can be up to 10 characters in length and can contain letters.
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
        # The service code.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](https://help.aliyun.com/zh/pnvs/developer-reference/api-return-code?spm=a2c4g.11186623.0.0.5c3a662fbgeAuk).
        self.code = code
        # The returned message.
        self.message = message
        # The returned results.
        self.model = model
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        # The app name.
        self.app_name = app_name
        # The verification type. You can select multiple types only when the phone number verification is supported. Separate multiple types with commas (,).
        # 
        # *   **1**: phone number verification
        # *   **2**: SMS verification
        self.auth_type = auth_type
        # The bundle ID. This parameter is required when OsType is set to iOS. The bundle ID must be 1 to 128 characters in length and can contain digits, letters, hyphens (-), underscores (\_), and periods (.).
        self.bundle_id = bundle_id
        # The channel code of China Mobile.
        self.cm_api_code = cm_api_code
        # The channel code of China Telecom.
        self.ct_api_code = ct_api_code
        # The channel code of China Unicom.
        self.cu_api_code = cu_api_code
        # The email address that receives the key.
        self.email = email
        # The IP address whitelist.
        self.ip_white_list = ip_white_list
        # The source URL of the HTML5 app page. We recommend that you specify this parameter as a domain name.
        self.origin = origin
        # The type of the operating system for the terminal. Valid values: iOS and Android.
        self.os_type = os_type
        self.owner_id = owner_id
        # The package name. This parameter is required when OsType is set to Android. The name must be 1 to 128 characters in length and can contain digits, letters, hyphens (-), underscores (\_), and periods (.).
        self.pack_name = pack_name
        # The package signature. This parameter is required when OsType is set to Android. The signature must be 32 characters in length and can contain digits and letters.
        self.pack_sign = pack_sign
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service type.
        self.scene_type = scene_type
        # The service name.
        self.scheme_name = scheme_name
        # The bound SMS signature. This parameter is valid only when AuthType is set to 2. The signature must be approved.
        self.sms_sign_name = sms_sign_name
        # The URL of the HTML5 app page.
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
        # The service code.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.gate_verify_scheme_dto = gate_verify_scheme_dto
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        # The user ID.
        self.customer_id = customer_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service code.
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
        # The request is successful. For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The result of the operation. Valid values:
        # 
        # *   **true**: The verification service is deleted.
        # *   **false**: The verification service failed to be deleted.
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
        # The user ID.
        self.customer_id = customer_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service code.
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
        # The key generated when you create a service in the console.
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
        # The response code. OK indicates that the request is successful. For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response parameters.
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
        scene_code: str = None,
        url: str = None,
    ):
        # The requested domain name.
        self.origin = origin
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_code = scene_code
        # The URL of the requested web page.
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
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
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
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAuthTokenResponseBodyTokenInfo(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        jwt_token: str = None,
    ):
        # The business authentication token.
        # 
        # >  AccessToken is valid for 10 minutes and can be used repeatedly within its validity period.
        self.access_token = access_token
        # The API authentication token.
        # 
        # >  JwtToken is valid for 1 hour and can be used repeatedly within its validity period.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The response parameters.
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
        # The authorization end date, which is in the yyyy-MM-dd format. This parameter is required for services of contract type.
        self.end_date = end_date
        self.owner_id = owner_id
        # The phone number.
        self.phone_no = phone_no
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the authorization scenario. You can view the ID of the authorization scenario on the **Authorization Scenario Management** page in the **Phone Number Verification Service console**.
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
        # The authorization URL.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The bundle ID of the app. This parameter is required when Platform is set to iOS.
        self.bundle_id = bundle_id
        # The validity period of the token. Unit: seconds. Valid values: 900 to 43200.
        self.duration_seconds = duration_seconds
        self.owner_id = owner_id
        # The package name of the app. This parameter is required when Platform is set to Android.
        self.package_name = package_name
        # The package signature of the app. This parameter is required when Platform is set to Android.
        self.package_sign = package_sign
        # The platform type. Valid values: Android and iOS.
        self.platform = platform
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service code.
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
        # The response code. If OK is returned, the request is successful. Other values indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The authentication code. The value of this parameter is a string.
        self.model = model
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true false
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
        # The logon token obtained by the SDK for your app.
        self.access_token = access_token
        # The external ID.
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
        # The phone number,
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.get_mobile_result_dto = get_mobile_result_dto
        # The returned message.
        self.message = message
        # The request ID.
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
        # The token for phone number verification that is obtained by the JavaScript SDK. The validity period of the token is 10 minutes for China Telecom, 30 minutes for China Unicom, and 2 minutes for China Mobile. The token can be used only once.
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
        # The phone number.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The ID of the iOS application. This parameter is required if OsType is set to **iOS**.
        self.bundle_id = bundle_id
        # The validity period of the token. Unit: seconds. Valid values: 900 to 43200.
        self.expire = expire
        # The type of the operating system. Valid values: **Android** and **iOS**.
        self.os_type = os_type
        self.owner_id = owner_id
        # The package name. This parameter is required if OsType is set to **Android**.
        self.package_name = package_name
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The service code.
        self.scene_code = scene_code
        # The signature. This parameter is required if OsType is set to **Android**.
        self.sign_name = sign_name
        # The validity period of the SMS verification code. Unit: seconds. Default value: 180.
        self.sms_code_expire = sms_code_expire
        # The code of the text message template.
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
        # The business token.
        self.biz_token = biz_token
        # The time when the token expired. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.expire_time = expire_time
        # The AccessKey ID.
        self.sts_access_key_id = sts_access_key_id
        # The AccessKey secret.
        self.sts_access_key_secret = sts_access_key_secret
        # The security token.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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


class JyCreateVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        bundle_id: str = None,
        cm_api_code: int = None,
        ct_api_code: int = None,
        cu_api_code: int = None,
        os_type: str = None,
        owner_id: int = None,
        pack_name: str = None,
        pack_sign: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
    ):
        self.app_name = app_name
        self.bundle_id = bundle_id
        self.cm_api_code = cm_api_code
        self.ct_api_code = ct_api_code
        self.cu_api_code = cu_api_code
        self.os_type = os_type
        self.owner_id = owner_id
        self.pack_name = pack_name
        self.pack_sign = pack_sign
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
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.cm_api_code is not None:
            result['CmApiCode'] = self.cm_api_code
        if self.ct_api_code is not None:
            result['CtApiCode'] = self.ct_api_code
        if self.cu_api_code is not None:
            result['CuApiCode'] = self.cu_api_code
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
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('CmApiCode') is not None:
            self.cm_api_code = m.get('CmApiCode')
        if m.get('CtApiCode') is not None:
            self.ct_api_code = m.get('CtApiCode')
        if m.get('CuApiCode') is not None:
            self.cu_api_code = m.get('CuApiCode')
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
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        return self


class JyCreateVerifySchemeResponseBodyGateVerifySchemeData(TeaModel):
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


class JyCreateVerifySchemeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gate_verify_scheme_data: JyCreateVerifySchemeResponseBodyGateVerifySchemeData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.gate_verify_scheme_data = gate_verify_scheme_data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.gate_verify_scheme_data:
            self.gate_verify_scheme_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gate_verify_scheme_data is not None:
            result['GateVerifySchemeData'] = self.gate_verify_scheme_data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GateVerifySchemeData') is not None:
            temp_model = JyCreateVerifySchemeResponseBodyGateVerifySchemeData()
            self.gate_verify_scheme_data = temp_model.from_map(m['GateVerifySchemeData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JyCreateVerifySchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JyCreateVerifySchemeResponseBody = None,
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
            temp_model = JyCreateVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JyQueryAppInfoBySceneCodeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_code = scene_code

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
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        return self


class JyQueryAppInfoBySceneCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        cm_app_id: str = None,
        cm_app_key: str = None,
        ct_app_id: str = None,
        ct_app_key: str = None,
    ):
        self.cm_app_id = cm_app_id
        self.cm_app_key = cm_app_key
        self.ct_app_id = ct_app_id
        self.ct_app_key = ct_app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cm_app_id is not None:
            result['CmAppId'] = self.cm_app_id
        if self.cm_app_key is not None:
            result['CmAppKey'] = self.cm_app_key
        if self.ct_app_id is not None:
            result['CtAppId'] = self.ct_app_id
        if self.ct_app_key is not None:
            result['CtAppKey'] = self.ct_app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmAppId') is not None:
            self.cm_app_id = m.get('CmAppId')
        if m.get('CmAppKey') is not None:
            self.cm_app_key = m.get('CmAppKey')
        if m.get('CtAppId') is not None:
            self.ct_app_id = m.get('CtAppId')
        if m.get('CtAppKey') is not None:
            self.ct_app_key = m.get('CtAppKey')
        return self


class JyQueryAppInfoBySceneCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: JyQueryAppInfoBySceneCodeResponseBodyData = None,
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
            temp_model = JyQueryAppInfoBySceneCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JyQueryAppInfoBySceneCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JyQueryAppInfoBySceneCodeResponseBody = None,
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
            temp_model = JyQueryAppInfoBySceneCodeResponseBody()
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
        # The verification method. Valid values:
        # 
        # *   **0**: phone number verification
        # *   **1**: one-click logon
        # *   **2**: all
        # *   **3**: facial recognition
        # *   **4**: SMS verification
        self.authentication_type = authentication_type
        # The month in which the bill is generated. Specify this parameter in the YYYYMM format. Example: 202111.
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
        # The billable items.
        self.add = add
        # The fees generated for the verification service. Unitrogen: CNY.
        self.amount = amount
        # The application name.
        self.app_name = app_name
        # The verification method.
        self.item_name = item_name
        # The service code.
        self.scene_code = scene_code
        # The service name.
        self.scene_name = scene_name
        # The unit price. Unit: CNY.
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
        # The fees generated for all verification services. Unitrogen: CNY.
        self.amount_sum = amount_sum
        # The details of fees.
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
        # The response code. Valid values:
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The billing information about each verification service.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The verification method. Valid values:
        # 
        # *   **1**: one-click logon
        # *   **2**: phone number verification, including the verification of the phone number used in HTML5 pages
        # *   **3**: SMS verification
        # *   **4**: facial recognition
        self.authentication_type = authentication_type
        # The end date. Specify this parameter in the YYYYMMDD format. Example: 20220106.
        self.end_date = end_date
        # The type of the operating system. Valid values:
        # 
        # *   **Android**\
        # *   **iOS**\
        self.os_type = os_type
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        # The service code.
        self.scene_code = scene_code
        # The start date. Specify this parameter in the YYYYMMDD format. Example: 20220101.
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
        # The date. This field is accurate to the day. The value of this field is in the YYYYMMDD format. Example: 20220103.
        self.statistic_date_str = statistic_date_str
        # The failed calls on the day.
        self.total_fail = total_fail
        # The successful calls on the day.
        self.total_success = total_success
        # The unknown calls on the day.
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
        # The information about the daily calls.
        self.day_statistic = day_statistic
        # The total calls.
        self.total = total
        # The failed calls.
        self.total_fail = total_fail
        # The successful calls.
        self.total_success = total_success
        # The unknown calls.
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
        # The response code. Valid values:
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The information about the calls of Phone Number Verification Service, including the total calls, the successful calls, failed calls, unknown calls, and daily calls within the statistical date range.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The unique ID of the business, which is provided by Alibaba Cloud.
        self.biz_id = biz_id
        # The number of the page on which you are reading the text message. Pages start from page 1. The value of this parameter cannot exceed the maximum page number.
        self.current_page = current_page
        self.owner_id = owner_id
        # The number of entries per page.
        self.page_size = page_size
        # The phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The date when the text message was sent. You can query text messages that were sent within the last 30 days.
        # 
        # Specify the date in the yyyyMMdd format. Example: 20181225.
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
        # The content of the text message.
        self.content = content
        # The status code returned by the carrier.
        # 
        # *   If the text message was delivered, "DELIVERED" is returned.
        # *   If the text message failed to be sent, see [Error codes](https://help.aliyun.com/document_detail/101347.html?spm=a2c4g.419277.0.i8) for more information.
        self.err_code = err_code
        # The extension field.
        self.out_id = out_id
        # The phone number.
        self.phone_num = phone_num
        # The date and time when the text message was received.
        self.receive_date = receive_date
        # The date when the text message was sent. You can query text messages that were sent within the last 30 days.
        # 
        # The date is in the yyyyMMdd format. Example: 20181225.
        self.send_date = send_date
        # The delivery status of the text message.
        # 
        # *   1: A delivery receipt is to be sent.
        # *   2: The text message failed to be sent.
        # *   3: The text message was sent.
        self.send_status = send_status
        # The code of the text message template.
        # 
        # Log on to the SMS console. In the left-side navigation pane, click **Go China** or **Go Globe**. You can view the text message template code in the **Template Code** column on the **Message Templates** tab.
        # 
        # >  The text message templates must be created on the Go Globe page and approved.
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # If OK is returned, the request is successful. Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html?spm=a2c4g.419277.0.i11).
        self.code = code
        # The returned message.
        self.message = message
        # The returned data.
        self.model = model
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries in the list.
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
        # The length of the verification code. Default value: 4. Valid values: 4 to 8.
        self.code_length = code_length
        # The type of the generated verification code. Default value: 1. Valid values:
        # 
        # *   1: digits only
        # *   2: uppercase letters only
        # *   3: lowercase letters only
        # *   4: uppercase and lowercase letters
        # *   5: digits and uppercase letters
        # *   6: digits and lowercase letters
        # *   7: digits and uppercase and lowercase letters
        self.code_type = code_type
        # The country code of the phone number. SMS verification codes can be sent only by using phone numbers in the Chinese mainland. Default value: 86.
        self.country_code = country_code
        # Specifies how to handle the verification codes received earlier in a case where verification codes are sent to the same phone number for the same scenario within the validity period.
        # 
        # *   1 (default): The latest verification code overwrites the verification codes received earlier. In this case, verification codes received earlier expire.
        # *   2: Verification codes within their validity period are valid and can be used for verification.
        self.duplicate_policy = duplicate_policy
        # The time interval. Unit: seconds. Default value: 60. This parameter specifies how often you can send a verification code.
        self.interval = interval
        # The external ID.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to return a verification code.
        # 
        # *   **true**\
        # *   **false**\
        self.return_verify_code = return_verify_code
        # The verification service name. If this parameter is not specified, the default service is used. The name can be up to 20 characters in length.
        self.scheme_name = scheme_name
        # The signature.
        self.sign_name = sign_name
        # The extension code of the upstream text message. Upstream text messages are text messages sent to the communication service provider. Upstream text messages are used to customize a service, complete an inquiry, or send a request. You are charged for sending upstream text messages based on the billing standards of the service provider.
        # 
        # >  The extension code is automatically generated by the system when the signature is generated. You do not need to specify the extension code. You can skip this parameter based on your business requirements. If you want to use custom extension codes, contact your account manager.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the text message template.
        # 
        # Log on to the [SMS console](https://dysms.console.aliyun.com/dysms.htm?spm=5176.12818093.categories-n-products.ddysms.3b2816d0xml2NA#/overview). In the left-side navigation pane, click **Go China** or **Go Globe**. You can view the text message template code in the **Template Code** column on the **Message Templates** tab.
        # 
        # >  The text message templates must be created on the Go Globe page and approved.
        self.template_code = template_code
        # The value of the variable in the text message template. The verification code is replaced with "##code##".
        # 
        # Example 1: For a system-defined template that contains variables, if the template content is "Your verification code is ${code} and valid for 5 minutes. Do not disclose the verification code to others.", specify the value of this parameter as {"code":"##code##"}
        # 
        # Example 2: For a custom template, if the template content is ${content}, specify the value of this parameter as {"content":"Your verification code is ##code## and must be used within 5 minutes."}.
        # 
        # > 
        # 
        # *   If line breaks are required in JSON-formatted data, they must meet the relevant requirements that are specified in the standard JSON protocol.
        # 
        # *   For more information about template variables, see [SMS template specifications](~~108253~~).
        self.template_param = template_param
        # The validity period of the verification code. Unit: seconds. Default value: 300.
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
        # The business ID.
        self.biz_id = biz_id
        # The external ID.
        self.out_id = out_id
        # The request ID.
        self.request_id = request_id
        # The verification code.
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. If OK is returned, the request is successful. For more information, see [Response codes](https://help.aliyun.com/zh/pnvs/developer-reference/api-return-code?spm=a2c4g.11174283.0.0.70c5616bkj38Wa).
        self.code = code
        # The returned message.
        self.message = message
        # The returned data.
        self.model = model
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
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
        # The token obtained by the SDK for your app.
        self.access_code = access_code
        # The external ID.
        self.out_id = out_id
        self.owner_id = owner_id
        # The phone number.
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
        # The verification ID.
        self.verify_id = verify_id
        # The verification results. Valid values:
        # 
        # *   **PASS: The input phone number is consistent with the phone number that you use.**\
        # *   **REJECT: The input phone number is different from the phone number that you use.**\
        # *   **UNKNOWN: The system cannot judge whether the input phone number is consistent with the phone number that you use.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.gate_verify_result_dto = gate_verify_result_dto
        # The returned message.
        self.message = message
        # The request ID.
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
        # The phone number.
        self.phone_number = phone_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The token for phone number verification that is obtained by the JavaScript SDK.
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
        # The external ID.
        self.verify_id = verify_id
        # The verification results. Valid values:
        # 
        # *   PASS: The input phone number is consistent with the phone number used in HTML5 pages.
        # *   REJECT: The input phone number is different from the phone number used in HTML5 pages.
        # *   UNKNOWN: The system cannot judge whether the input phone number is consistent with the phone number used in HTML5 pages.
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # The response parameters.
        self.gate_verify = gate_verify
        # The returned message.
        self.message = message
        # The request ID.
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
        # The phone number, which is used to receive SMS verification codes.
        self.phone_number = phone_number
        # The SMS verification code.
        self.sms_code = sms_code
        # The text message verification code. After you successfully call the corresponding API operation to send the SMS verification code, the end users receive the SMS verification code. SmsToken is returned by the SDK for SMS verification for you to verify the text message verification code. For an Android client, sendVerifyCode is called to send the verification code. For an iOS client, sendVerifyCodeWithTimeout is called to send the verification code. For more information, see [Overview](~~400434~~).
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
        # The response code.
        # 
        # *   If OK is returned, the request is successful.
        # *   For more information about other error codes, see [API response codes](~~85198~~).
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
        # The unified verification token that is returned by the client SDKs.
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
        # The phone number, which is returned when the verification is successful.
        self.phone_number = phone_number
        # The phone number score, which is generated only after the phone number scoring node is enabled and the verification is successful. The higher the score, the more risky the phone number. Valid values: 0 to 100.
        self.phone_score = phone_score
        # The verification result. Valid values: PASS and UNKNOWN.
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
        # The response code. If OK is returned, the request is successful. Other values indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The returned data.
        self.model = model
        # The request ID, which is used to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true false
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


