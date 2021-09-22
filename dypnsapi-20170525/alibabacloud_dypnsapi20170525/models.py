# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetAuthorizationUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_no: str = None,
        scheme_id: int = None,
        end_date: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_no = phone_no
        self.scheme_id = scheme_id
        self.end_date = end_date

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
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
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
        message: str = None,
        request_id: str = None,
        data: GetAuthorizationUrlResponseBodyData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.data = data

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAuthorizationUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAuthorizationUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthorizationUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuthorizationUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmsAuthTokensRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        package_name: str = None,
        sign_name: str = None,
        scene_code: str = None,
        os_type: str = None,
        bundle_id: str = None,
        expire: int = None,
        sms_template_code: str = None,
        sms_code_expire: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.package_name = package_name
        self.sign_name = sign_name
        self.scene_code = scene_code
        self.os_type = os_type
        self.bundle_id = bundle_id
        self.expire = expire
        self.sms_template_code = sms_template_code
        self.sms_code_expire = sms_code_expire

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
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code
        if self.sms_code_expire is not None:
            result['SmsCodeExpire'] = self.sms_code_expire
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')
        if m.get('SmsCodeExpire') is not None:
            self.sms_code_expire = m.get('SmsCodeExpire')
        return self


class GetSmsAuthTokensResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_token: str = None,
        sts_access_key_secret: str = None,
        sts_access_key_id: str = None,
        expire_time: int = None,
        sts_token: str = None,
    ):
        self.biz_token = biz_token
        self.sts_access_key_secret = sts_access_key_secret
        self.sts_access_key_id = sts_access_key_id
        self.expire_time = expire_time
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
        if self.sts_access_key_secret is not None:
            result['StsAccessKeySecret'] = self.sts_access_key_secret
        if self.sts_access_key_id is not None:
            result['StsAccessKeyId'] = self.sts_access_key_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.sts_token is not None:
            result['StsToken'] = self.sts_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizToken') is not None:
            self.biz_token = m.get('BizToken')
        if m.get('StsAccessKeySecret') is not None:
            self.sts_access_key_secret = m.get('StsAccessKeySecret')
        if m.get('StsAccessKeyId') is not None:
            self.sts_access_key_id = m.get('StsAccessKeyId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')
        return self


class GetSmsAuthTokensResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        data: GetSmsAuthTokensResponseBodyData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.data = data

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetSmsAuthTokensResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSmsAuthTokensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSmsAuthTokensResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSmsAuthTokensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_name: str = None,
        app_name: str = None,
        os_type: str = None,
        pack_name: str = None,
        pack_sign: str = None,
        bundle_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_name = scheme_name
        self.app_name = app_name
        self.os_type = os_type
        self.pack_name = pack_name
        self.pack_sign = pack_sign
        self.bundle_id = bundle_id

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
        if self.scheme_name is not None:
            result['SchemeName'] = self.scheme_name
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.pack_name is not None:
            result['PackName'] = self.pack_name
        if self.pack_sign is not None:
            result['PackSign'] = self.pack_sign
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeName') is not None:
            self.scheme_name = m.get('SchemeName')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PackName') is not None:
            self.pack_name = m.get('PackName')
        if m.get('PackSign') is not None:
            self.pack_sign = m.get('PackSign')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
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
        message: str = None,
        request_id: str = None,
        gate_verify_scheme_dto: CreateVerifySchemeResponseBodyGateVerifySchemeDTO = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.gate_verify_scheme_dto = gate_verify_scheme_dto

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gate_verify_scheme_dto is not None:
            result['GateVerifySchemeDTO'] = self.gate_verify_scheme_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GateVerifySchemeDTO') is not None:
            temp_model = CreateVerifySchemeResponseBodyGateVerifySchemeDTO()
            self.gate_verify_scheme_dto = temp_model.from_map(m['GateVerifySchemeDTO'])
        return self


class CreateVerifySchemeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVerifySchemeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSmsCodeRequest(TeaModel):
    def __init__(
        self,
        biz_token: str = None,
        phone_number: str = None,
        scene_code: str = None,
        os_type: str = None,
    ):
        self.biz_token = biz_token
        self.phone_number = phone_number
        self.scene_code = scene_code
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_token is not None:
            result['BizToken'] = self.biz_token
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizToken') is not None:
            self.biz_token = m.get('BizToken')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class GetSmsCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        sms_token: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.sms_token = sms_token
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
        if self.message is not None:
            result['Message'] = self.message
        if self.sms_token is not None:
            result['SmsToken'] = self.sms_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SmsToken') is not None:
            self.sms_token = m.get('SmsToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSmsCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSmsCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSmsCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifySmsCodeRequest(TeaModel):
    def __init__(
        self,
        sms_code: str = None,
        phone_number: str = None,
        sms_token: str = None,
    ):
        self.sms_code = sms_code
        self.phone_number = phone_number
        self.sms_token = sms_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sms_code is not None:
            result['SmsCode'] = self.sms_code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.sms_token is not None:
            result['SmsToken'] = self.sms_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SmsCode') is not None:
            self.sms_code = m.get('SmsCode')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SmsToken') is not None:
            self.sms_token = m.get('SmsToken')
        return self


class VerifySmsCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.data = data
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
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifySmsCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifySmsCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifySmsCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_code: str = None,
        customer_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_code = scheme_code
        self.customer_id = customer_id

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
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
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
        body: DeleteVerifySchemeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPhoneWithTokenRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_number: str = None,
        sp_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_number = phone_number
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
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
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
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SpToken') is not None:
            self.sp_token = m.get('SpToken')
        return self


class VerifyPhoneWithTokenResponseBodyGateVerify(TeaModel):
    def __init__(
        self,
        verify_result: str = None,
        verify_id: str = None,
    ):
        self.verify_result = verify_result
        self.verify_id = verify_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        return self


class VerifyPhoneWithTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        gate_verify: VerifyPhoneWithTokenResponseBodyGateVerify = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.gate_verify = gate_verify

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gate_verify is not None:
            result['GateVerify'] = self.gate_verify.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GateVerify') is not None:
            temp_model = VerifyPhoneWithTokenResponseBodyGateVerify()
            self.gate_verify = temp_model.from_map(m['GateVerify'])
        return self


class VerifyPhoneWithTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyPhoneWithTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyPhoneWithTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMobileRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        access_token: str = None,
        out_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.access_token = access_token
        self.out_id = out_id

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
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.out_id is not None:
            result['OutId'] = self.out_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
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
        message: str = None,
        request_id: str = None,
        get_mobile_result_dto: GetMobileResponseBodyGetMobileResultDTO = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.get_mobile_result_dto = get_mobile_result_dto

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.get_mobile_result_dto is not None:
            result['GetMobileResultDTO'] = self.get_mobile_result_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GetMobileResultDTO') is not None:
            temp_model = GetMobileResponseBodyGetMobileResultDTO()
            self.get_mobile_result_dto = temp_model.from_map(m['GetMobileResultDTO'])
        return self


class GetMobileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMobileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMobileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TwiceTelVerifyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        since: str = None,
        phone_number: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.since = since
        self.phone_number = phone_number

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
        if self.since is not None:
            result['Since'] = self.since
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Since') is not None:
            self.since = m.get('Since')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class TwiceTelVerifyResponseBodyTwiceTelVerifyResult(TeaModel):
    def __init__(
        self,
        carrier: str = None,
        verify_result: int = None,
    ):
        self.carrier = carrier
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class TwiceTelVerifyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        twice_tel_verify_result: TwiceTelVerifyResponseBodyTwiceTelVerifyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.twice_tel_verify_result = twice_tel_verify_result

    def validate(self):
        if self.twice_tel_verify_result:
            self.twice_tel_verify_result.validate()

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
        if self.twice_tel_verify_result is not None:
            result['TwiceTelVerifyResult'] = self.twice_tel_verify_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TwiceTelVerifyResult') is not None:
            temp_model = TwiceTelVerifyResponseBodyTwiceTelVerifyResult()
            self.twice_tel_verify_result = temp_model.from_map(m['TwiceTelVerifyResult'])
        return self


class TwiceTelVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TwiceTelVerifyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TwiceTelVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCertifyResultRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.token = token

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
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetCertifyResultResponseBodyData(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        identity_info: str = None,
        verify_desc: str = None,
        verify_result: str = None,
        device_token: str = None,
    ):
        self.material_info = material_info
        self.identity_info = identity_info
        self.verify_desc = verify_desc
        self.verify_result = verify_result
        self.device_token = device_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.identity_info is not None:
            result['IdentityInfo'] = self.identity_info
        if self.verify_desc is not None:
            result['VerifyDesc'] = self.verify_desc
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('IdentityInfo') is not None:
            self.identity_info = m.get('IdentityInfo')
        if m.get('VerifyDesc') is not None:
            self.verify_desc = m.get('VerifyDesc')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        return self


class GetCertifyResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        data: List[GetCertifyResultResponseBodyData] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCertifyResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetCertifyResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCertifyResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCertifyResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVerifySchemeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheme_code: str = None,
        customer_id: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scheme_code = scheme_code
        self.customer_id = customer_id

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
        if self.scheme_code is not None:
            result['SchemeCode'] = self.scheme_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SchemeCode') is not None:
            self.scheme_code = m.get('SchemeCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
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
        body: DescribeVerifySchemeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVerifySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        url: str = None,
        origin: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.url = url
        self.origin = origin

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
        if self.url is not None:
            result['Url'] = self.url
        if self.origin is not None:
            result['Origin'] = self.origin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Origin') is not None:
            self.origin = m.get('Origin')
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
        body: GetAuthTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyMobileRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        access_code: str = None,
        phone_number: str = None,
        out_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.access_code = access_code
        self.phone_number = phone_number
        self.out_id = out_id

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
        if self.access_code is not None:
            result['AccessCode'] = self.access_code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.out_id is not None:
            result['OutId'] = self.out_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AccessCode') is not None:
            self.access_code = m.get('AccessCode')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        return self


class VerifyMobileResponseBodyGateVerifyResultDTO(TeaModel):
    def __init__(
        self,
        verify_result: str = None,
        verify_id: str = None,
    ):
        self.verify_result = verify_result
        self.verify_id = verify_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        if self.verify_id is not None:
            result['VerifyId'] = self.verify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        if m.get('VerifyId') is not None:
            self.verify_id = m.get('VerifyId')
        return self


class VerifyMobileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        gate_verify_result_dto: VerifyMobileResponseBodyGateVerifyResultDTO = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.gate_verify_result_dto = gate_verify_result_dto

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gate_verify_result_dto is not None:
            result['GateVerifyResultDTO'] = self.gate_verify_result_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GateVerifyResultDTO') is not None:
            temp_model = VerifyMobileResponseBodyGateVerifyResultDTO()
            self.gate_verify_result_dto = temp_model.from_map(m['GateVerifyResultDTO'])
        return self


class VerifyMobileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyMobileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyMobileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        service_name: str = None,
        spiregion_id: str = None,
        deletion_task_id: str = None,
        account_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.role_arn = role_arn
        self.service_name = service_name
        self.spiregion_id = spiregion_id
        self.deletion_task_id = deletion_task_id
        self.account_id = account_id

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
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: List[str] = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeletingResponseBody(TeaModel):
    def __init__(
        self,
        deletable: str = None,
        request_id: str = None,
        role_usages: List[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages] = None,
    ):
        self.deletable = deletable
        self.request_id = request_id
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckServiceLinkedRoleForDeletingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


