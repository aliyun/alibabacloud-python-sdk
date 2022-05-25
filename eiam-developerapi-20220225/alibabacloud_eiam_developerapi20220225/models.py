# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateOrganizationalUnitHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateOrganizationalUnitRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        organizational_unit_external_id: str = None,
        organizational_unit_name: str = None,
        parent_id: str = None,
    ):
        # 描述
        self.description = description
        # 机构外部ID
        self.organizational_unit_external_id = organizational_unit_external_id
        # 机构名称
        self.organizational_unit_name = organizational_unit_name
        # 父机构ID
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')
        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        return self


class CreateOrganizationalUnitResponseBody(TeaModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
    ):
        # 机构ID
        self.organizational_unit_id = organizational_unit_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')
        return self


class CreateOrganizationalUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrganizationalUnitResponseBody = None,
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
            temp_model = CreateOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        password: str = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        primary_organizational_unit_id: str = None,
        user_external_id: str = None,
        username: str = None,
    ):
        # 描述
        self.description = description
        # 账户展示名
        self.display_name = display_name
        # 邮箱
        self.email = email
        # 邮箱是否验证，邮箱若设置此字段必须设置，无特殊业务可直接设置为true
        self.email_verified = email_verified
        # 密码, 参考密码策略
        self.password = password
        # 手机号
        self.phone_number = phone_number
        # 手机号是否验证，手机号若设置此字段必须设置，无特殊业务可直接设置为true
        self.phone_number_verified = phone_number_verified
        # 手机地区编号,示例：中国大陆手区号为86，不带 00 或 +, 手机号若设置，此参数必填
        self.phone_region = phone_region
        # 账户主机构ID
        self.primary_organizational_unit_id = primary_organizational_unit_id
        # 账户外部ID
        self.user_external_id = user_external_id
        # 账户名
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified
        if self.password is not None:
            result['password'] = self.password
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region
        if self.primary_organizational_unit_id is not None:
            result['primaryOrganizationalUnitId'] = self.primary_organizational_unit_id
        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')
        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')
        if m.get('primaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('primaryOrganizationalUnitId')
        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 账户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserResponseBody = None,
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOrganizationalUnitHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteOrganizationalUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteUserHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GenerateDeviceCodeRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        scope: str = None,
    ):
        # 客户端ID
        self.client_id = client_id
        # scope范围
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.scope is not None:
            result['scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        return self


class GenerateDeviceCodeResponseBody(TeaModel):
    def __init__(
        self,
        device_code: str = None,
        expires_at: int = None,
        expires_in: int = None,
        interval: int = None,
        user_code: str = None,
        verification_uri: str = None,
        verification_uri_complete: str = None,
    ):
        # 设备验证码
        self.device_code = device_code
        # 过期时间
        self.expires_at = expires_at
        # device_code和user_code的有效时长，单位秒
        self.expires_in = expires_in
        # 请求token节点的超时时间，单位秒
        self.interval = interval
        # 终端用户验证码
        self.user_code = user_code
        # 验证URI
        self.verification_uri = verification_uri
        # 包含user_code的完整验证URI
        self.verification_uri_complete = verification_uri_complete

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_code is not None:
            result['device_code'] = self.device_code
        if self.expires_at is not None:
            result['expires_at'] = self.expires_at
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.interval is not None:
            result['interval'] = self.interval
        if self.user_code is not None:
            result['user_code'] = self.user_code
        if self.verification_uri is not None:
            result['verification_uri'] = self.verification_uri
        if self.verification_uri_complete is not None:
            result['verification_uri_complete'] = self.verification_uri_complete
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('device_code') is not None:
            self.device_code = m.get('device_code')
        if m.get('expires_at') is not None:
            self.expires_at = m.get('expires_at')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('user_code') is not None:
            self.user_code = m.get('user_code')
        if m.get('verification_uri') is not None:
            self.verification_uri = m.get('verification_uri')
        if m.get('verification_uri_complete') is not None:
            self.verification_uri_complete = m.get('verification_uri_complete')
        return self


class GenerateDeviceCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateDeviceCodeResponseBody = None,
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
            temp_model = GenerateDeviceCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        code_verifier: str = None,
        device_code: str = None,
        exclusive_tag: str = None,
        grant_type: str = None,
        password: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
        scope: str = None,
        username: str = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        # code码
        self.code = code
        # 验证code
        self.code_verifier = code_verifier
        # 设备码
        self.device_code = device_code
        # 排除的tag
        self.exclusive_tag = exclusive_tag
        # 授权类型
        self.grant_type = grant_type
        # 密码
        self.password = password
        # 重定向URI
        self.redirect_uri = redirect_uri
        # 更新token
        self.refresh_token = refresh_token
        # scope范围
        self.scope = scope
        # 用户名
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.client_secret is not None:
            result['client_secret'] = self.client_secret
        if self.code is not None:
            result['code'] = self.code
        if self.code_verifier is not None:
            result['code_verifier'] = self.code_verifier
        if self.device_code is not None:
            result['device_code'] = self.device_code
        if self.exclusive_tag is not None:
            result['exclusive_tag'] = self.exclusive_tag
        if self.grant_type is not None:
            result['grant_type'] = self.grant_type
        if self.password is not None:
            result['password'] = self.password
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.scope is not None:
            result['scope'] = self.scope
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('code_verifier') is not None:
            self.code_verifier = m.get('code_verifier')
        if m.get('device_code') is not None:
            self.device_code = m.get('device_code')
        if m.get('exclusive_tag') is not None:
            self.exclusive_tag = m.get('exclusive_tag')
        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GenerateTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expires_at: int = None,
        expires_in: int = None,
        id_token: str = None,
        refresh_token: str = None,
        token_type: str = None,
    ):
        # access_token
        self.access_token = access_token
        # 过期时间
        self.expires_at = expires_at
        # 有效时长，单位秒
        self.expires_in = expires_in
        # id_token
        self.id_token = id_token
        # refresh_token
        self.refresh_token = refresh_token
        # token类型，包含Basic,Bearer
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.expires_at is not None:
            result['expires_at'] = self.expires_at
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.id_token is not None:
            result['id_token'] = self.id_token
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.token_type is not None:
            result['token_type'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('expires_at') is not None:
            self.expires_at = m.get('expires_at')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('id_token') is not None:
            self.id_token = m.get('id_token')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        return self


class GenerateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateTokenResponseBody = None,
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
            temp_model = GenerateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationProvisioningScopeHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetApplicationProvisioningScopeResponseBody(TeaModel):
    def __init__(
        self,
        organizational_unit_ids: List[str] = None,
    ):
        # 机构ID列表
        self.organizational_unit_ids = organizational_unit_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_ids is not None:
            result['organizationalUnitIds'] = self.organizational_unit_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitIds') is not None:
            self.organizational_unit_ids = m.get('organizationalUnitIds')
        return self


class GetApplicationProvisioningScopeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationProvisioningScopeResponseBody = None,
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
            temp_model = GetApplicationProvisioningScopeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationalUnitHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetOrganizationalUnitResponseBody(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        organizational_unit_external_id: str = None,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        organizational_unit_source_id: str = None,
        organizational_unit_source_type: str = None,
        parent_id: str = None,
        update_time: int = None,
    ):
        # 创建时间，毫秒
        self.create_time = create_time
        # 描述
        self.description = description
        # 实例ID
        self.instance_id = instance_id
        # 外部ID
        self.organizational_unit_external_id = organizational_unit_external_id
        # 机构ID
        self.organizational_unit_id = organizational_unit_id
        # 机构名称
        self.organizational_unit_name = organizational_unit_name
        # 来源ID
        self.organizational_unit_source_id = organizational_unit_source_id
        # 来源类型
        self.organizational_unit_source_type = organizational_unit_source_type
        # 父机构ID
        self.parent_id = parent_id
        # 最近一次更新时间，毫秒
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name
        if self.organizational_unit_source_id is not None:
            result['organizationalUnitSourceId'] = self.organizational_unit_source_id
        if self.organizational_unit_source_type is not None:
            result['organizationalUnitSourceType'] = self.organizational_unit_source_type
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')
        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')
        if m.get('organizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('organizationalUnitSourceId')
        if m.get('organizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('organizationalUnitSourceType')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class GetOrganizationalUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrganizationalUnitResponseBody = None,
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
            temp_model = GetOrganizationalUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrganizationalUnitIdByExternalIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetOrganizationalUnitIdByExternalIdRequest(TeaModel):
    def __init__(
        self,
        organizational_unit_external_id: str = None,
    ):
        # 机构外部ID
        self.organizational_unit_external_id = organizational_unit_external_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')
        return self


class GetOrganizationalUnitIdByExternalIdResponseBody(TeaModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
    ):
        # 机构ID
        self.organizational_unit_id = organizational_unit_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')
        return self


class GetOrganizationalUnitIdByExternalIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOrganizationalUnitIdByExternalIdResponseBody = None,
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
            temp_model = GetOrganizationalUnitIdByExternalIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUserResponseBodyOrganizationalUnits(TeaModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        primary: bool = None,
    ):
        # 机构ID
        self.organizational_unit_id = organizational_unit_id
        # 机构名称
        self.organizational_unit_name = organizational_unit_name
        # 是否主机构
        self.primary = primary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name
        if self.primary is not None:
            result['primary'] = self.primary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')
        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')
        if m.get('primary') is not None:
            self.primary = m.get('primary')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        account_expire_time: int = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        instance_id: str = None,
        lock_expire_time: int = None,
        organizational_units: List[GetUserResponseBodyOrganizationalUnits] = None,
        password_set: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        primary_organizational_unit_id: str = None,
        register_time: int = None,
        status: str = None,
        update_time: int = None,
        user_external_id: str = None,
        user_id: str = None,
        user_source_id: str = None,
        user_source_type: str = None,
        username: str = None,
    ):
        # 账户过期时间, 毫秒时间
        self.account_expire_time = account_expire_time
        # 创建时间, 毫秒时间
        self.create_time = create_time
        # 账号描述
        self.description = description
        # 显示名
        self.display_name = display_name
        # 邮箱
        self.email = email
        # 邮箱是否验证
        self.email_verified = email_verified
        # 实例ID
        self.instance_id = instance_id
        # 锁定过期时间, 毫秒时间
        self.lock_expire_time = lock_expire_time
        # 账户所属组织列表
        self.organizational_units = organizational_units
        # 密码是否已设置
        self.password_set = password_set
        # 手机号
        self.phone_number = phone_number
        # 手机号是否验证
        self.phone_number_verified = phone_number_verified
        # 手机地区编号,示例：中国大陆手区号为86，不带 00 或 +\
        self.phone_region = phone_region
        # 账户主机构ID
        self.primary_organizational_unit_id = primary_organizational_unit_id
        self.register_time = register_time
        # 账户状态, enabled:启用,disabled:禁用
        self.status = status
        # 最近一次更新时间, 毫秒时间
        self.update_time = update_time
        # 外部ID
        self.user_external_id = user_external_id
        # 账户ID
        self.user_id = user_id
        # 来源ID
        self.user_source_id = user_source_id
        # 来源类型，build_in[自建],ding_talk[钉钉导入],ad[AD导入],ldap[LDAP导入]
        self.user_source_type = user_source_type
        # 账户名
        self.username = username

    def validate(self):
        if self.organizational_units:
            for k in self.organizational_units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_expire_time is not None:
            result['accountExpireTime'] = self.account_expire_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_expire_time is not None:
            result['lockExpireTime'] = self.lock_expire_time
        result['organizationalUnits'] = []
        if self.organizational_units is not None:
            for k in self.organizational_units:
                result['organizationalUnits'].append(k.to_map() if k else None)
        if self.password_set is not None:
            result['passwordSet'] = self.password_set
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region
        if self.primary_organizational_unit_id is not None:
            result['primaryOrganizationalUnitId'] = self.primary_organizational_unit_id
        if self.register_time is not None:
            result['registerTime'] = self.register_time
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_source_id is not None:
            result['userSourceId'] = self.user_source_id
        if self.user_source_type is not None:
            result['userSourceType'] = self.user_source_type
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountExpireTime') is not None:
            self.account_expire_time = m.get('accountExpireTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockExpireTime') is not None:
            self.lock_expire_time = m.get('lockExpireTime')
        self.organizational_units = []
        if m.get('organizationalUnits') is not None:
            for k in m.get('organizationalUnits'):
                temp_model = GetUserResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k))
        if m.get('passwordSet') is not None:
            self.password_set = m.get('passwordSet')
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')
        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')
        if m.get('primaryOrganizationalUnitId') is not None:
            self.primary_organizational_unit_id = m.get('primaryOrganizationalUnitId')
        if m.get('registerTime') is not None:
            self.register_time = m.get('registerTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userSourceId') is not None:
            self.user_source_id = m.get('userSourceId')
        if m.get('userSourceType') is not None:
            self.user_source_type = m.get('userSourceType')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserIdByExternalIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUserIdByExternalIdRequest(TeaModel):
    def __init__(
        self,
        user_external_id: str = None,
    ):
        # 账户外部ID
        self.user_external_id = user_external_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')
        return self


class GetUserIdByExternalIdResponseBody(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 账户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetUserIdByExternalIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserIdByExternalIdResponseBody = None,
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
            temp_model = GetUserIdByExternalIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GetUserPasswordPolicyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetUserPasswordPolicyResponseBodyPasswordComplexityItem(TeaModel):
    def __init__(
        self,
        contain_lower_case: bool = None,
        contain_number: bool = None,
        contain_special_char: bool = None,
        contain_upper_case: bool = None,
        display_name_check: bool = None,
        email_check: bool = None,
        phone_check: bool = None,
        username_check: bool = None,
    ):
        # 是否包含小写字母
        self.contain_lower_case = contain_lower_case
        # 是否包含数字
        self.contain_number = contain_number
        # 是否包含特殊字符
        self.contain_special_char = contain_special_char
        # 是否包含大写字母
        self.contain_upper_case = contain_upper_case
        # 是否进行包含显示名检测
        self.display_name_check = display_name_check
        # 是否进行email检测
        self.email_check = email_check
        # 是否进行包含手机号检测
        self.phone_check = phone_check
        # 是否进行包含用户名检测
        self.username_check = username_check

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_lower_case is not None:
            result['containLowerCase'] = self.contain_lower_case
        if self.contain_number is not None:
            result['containNumber'] = self.contain_number
        if self.contain_special_char is not None:
            result['containSpecialChar'] = self.contain_special_char
        if self.contain_upper_case is not None:
            result['containUpperCase'] = self.contain_upper_case
        if self.display_name_check is not None:
            result['displayNameCheck'] = self.display_name_check
        if self.email_check is not None:
            result['emailCheck'] = self.email_check
        if self.phone_check is not None:
            result['phoneCheck'] = self.phone_check
        if self.username_check is not None:
            result['usernameCheck'] = self.username_check
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containLowerCase') is not None:
            self.contain_lower_case = m.get('containLowerCase')
        if m.get('containNumber') is not None:
            self.contain_number = m.get('containNumber')
        if m.get('containSpecialChar') is not None:
            self.contain_special_char = m.get('containSpecialChar')
        if m.get('containUpperCase') is not None:
            self.contain_upper_case = m.get('containUpperCase')
        if m.get('displayNameCheck') is not None:
            self.display_name_check = m.get('displayNameCheck')
        if m.get('emailCheck') is not None:
            self.email_check = m.get('emailCheck')
        if m.get('phoneCheck') is not None:
            self.phone_check = m.get('phoneCheck')
        if m.get('usernameCheck') is not None:
            self.username_check = m.get('usernameCheck')
        return self


class GetUserPasswordPolicyResponseBody(TeaModel):
    def __init__(
        self,
        active_cycle: int = None,
        instance_id: str = None,
        min_length: int = None,
        password_complexity_item: GetUserPasswordPolicyResponseBodyPasswordComplexityItem = None,
        reservation_count: int = None,
    ):
        # 密码修改周期, 单位毫秒，-1表示永不过期
        self.active_cycle = active_cycle
        # 实例ID
        self.instance_id = instance_id
        # 密码最短长度，-1表示不限制
        self.min_length = min_length
        # 密码复杂项
        self.password_complexity_item = password_complexity_item
        # 保留最近密码记录数
        self.reservation_count = reservation_count

    def validate(self):
        if self.password_complexity_item:
            self.password_complexity_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_cycle is not None:
            result['activeCycle'] = self.active_cycle
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.min_length is not None:
            result['minLength'] = self.min_length
        if self.password_complexity_item is not None:
            result['passwordComplexityItem'] = self.password_complexity_item.to_map()
        if self.reservation_count is not None:
            result['reservationCount'] = self.reservation_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeCycle') is not None:
            self.active_cycle = m.get('activeCycle')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('minLength') is not None:
            self.min_length = m.get('minLength')
        if m.get('passwordComplexityItem') is not None:
            temp_model = GetUserPasswordPolicyResponseBodyPasswordComplexityItem()
            self.password_complexity_item = temp_model.from_map(m['passwordComplexityItem'])
        if m.get('reservationCount') is not None:
            self.reservation_count = m.get('reservationCount')
        return self


class GetUserPasswordPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserPasswordPolicyResponseBody = None,
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
            temp_model = GetUserPasswordPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationalUnitParentIdsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListOrganizationalUnitParentIdsResponseBody(TeaModel):
    def __init__(
        self,
        parent_ids: List[str] = None,
    ):
        # 父机构ID列表，顺序层级从上到下
        self.parent_ids = parent_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_ids is not None:
            result['parentIds'] = self.parent_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentIds') is not None:
            self.parent_ids = m.get('parentIds')
        return self


class ListOrganizationalUnitParentIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOrganizationalUnitParentIdsResponseBody = None,
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
            temp_model = ListOrganizationalUnitParentIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrganizationalUnitsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListOrganizationalUnitsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        parent_id: str = None,
    ):
        # 页码，默认1
        self.page_number = page_number
        # 单页大小，默认20
        self.page_size = page_size
        # 父机构ID
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        return self


class ListOrganizationalUnitsResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        organizational_unit_external_id: str = None,
        organizational_unit_id: str = None,
        organizational_unit_name: str = None,
        organizational_unit_source_id: str = None,
        organizational_unit_source_type: str = None,
        parent_id: str = None,
        update_time: int = None,
    ):
        # 创建时间，毫秒
        self.create_time = create_time
        # 描述
        self.description = description
        # 实例ID
        self.instance_id = instance_id
        # 外部ID
        self.organizational_unit_external_id = organizational_unit_external_id
        # 机构ID
        self.organizational_unit_id = organizational_unit_id
        # 机构名称
        self.organizational_unit_name = organizational_unit_name
        # 来源ID
        self.organizational_unit_source_id = organizational_unit_source_id
        # 来源类型
        self.organizational_unit_source_type = organizational_unit_source_type
        # 父机构ID
        self.parent_id = parent_id
        # 最近一次更新时间，毫秒
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id
        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name
        if self.organizational_unit_source_id is not None:
            result['organizationalUnitSourceId'] = self.organizational_unit_source_id
        if self.organizational_unit_source_type is not None:
            result['organizationalUnitSourceType'] = self.organizational_unit_source_type
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')
        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')
        if m.get('organizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('organizationalUnitSourceId')
        if m.get('organizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('organizationalUnitSourceType')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListOrganizationalUnitsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListOrganizationalUnitsResponseBodyData] = None,
        total_count: int = None,
    ):
        self.data = data
        # 记录总数
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListOrganizationalUnitsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListOrganizationalUnitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOrganizationalUnitsResponseBody = None,
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
            temp_model = ListOrganizationalUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 机构ID
        self.organizational_unit_id = organizational_unit_id
        # 页码，默认1
        self.page_number = page_number
        # 单页大小，默认20
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_id is not None:
            result['organizationalUnitId'] = self.organizational_unit_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitId') is not None:
            self.organizational_unit_id = m.get('organizationalUnitId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        account_expire_time: int = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        instance_id: str = None,
        lock_expire_time: int = None,
        password_set: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        register_time: int = None,
        status: str = None,
        update_time: int = None,
        user_external_id: str = None,
        user_id: str = None,
        user_source_id: str = None,
        user_source_type: str = None,
        username: str = None,
    ):
        # 账户过期时间, 毫秒时间
        self.account_expire_time = account_expire_time
        # 创建时间, 毫秒时间
        self.create_time = create_time
        # 账号描述
        self.description = description
        # 显示名
        self.display_name = display_name
        # 邮箱
        self.email = email
        # 邮箱是否验证
        self.email_verified = email_verified
        # 实例ID
        self.instance_id = instance_id
        # 锁定过期时间, 毫秒时间
        self.lock_expire_time = lock_expire_time
        # 密码是否已设置
        self.password_set = password_set
        # 手机号
        self.phone_number = phone_number
        # 手机号是否验证
        self.phone_number_verified = phone_number_verified
        # 手机地区编号,示例：中国大陆手区号为86，不带 00 或 +\
        self.phone_region = phone_region
        self.register_time = register_time
        # 账户状态, enabled:启用,disabled:禁用
        self.status = status
        # 最近一次更新时间, 毫秒时间
        self.update_time = update_time
        # 外部ID
        self.user_external_id = user_external_id
        # 账户ID
        self.user_id = user_id
        # 来源ID
        self.user_source_id = user_source_id
        # 来源类型，build_in[自建],ding_talk[钉钉导入],ad[AD导入],ldap[LDAP导入]
        self.user_source_type = user_source_type
        # 账户名
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_expire_time is not None:
            result['accountExpireTime'] = self.account_expire_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lock_expire_time is not None:
            result['lockExpireTime'] = self.lock_expire_time
        if self.password_set is not None:
            result['passwordSet'] = self.password_set
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region
        if self.register_time is not None:
            result['registerTime'] = self.register_time
        if self.status is not None:
            result['status'] = self.status
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_source_id is not None:
            result['userSourceId'] = self.user_source_id
        if self.user_source_type is not None:
            result['userSourceType'] = self.user_source_type
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountExpireTime') is not None:
            self.account_expire_time = m.get('accountExpireTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lockExpireTime') is not None:
            self.lock_expire_time = m.get('lockExpireTime')
        if m.get('passwordSet') is not None:
            self.password_set = m.get('passwordSet')
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')
        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')
        if m.get('registerTime') is not None:
            self.register_time = m.get('registerTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userSourceId') is not None:
            self.user_source_id = m.get('userSourceId')
        if m.get('userSourceType') is not None:
            self.user_source_type = m.get('userSourceType')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListUsersResponseBodyData] = None,
        total_count: int = None,
    ):
        self.data = data
        # 记录总数
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListUsersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PatchOrganizationalUnitHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PatchOrganizationalUnitRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        organizational_unit_name: str = None,
    ):
        # 机构描述
        self.description = description
        # 机构名称
        self.organizational_unit_name = organizational_unit_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.organizational_unit_name is not None:
            result['organizationalUnitName'] = self.organizational_unit_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('organizationalUnitName') is not None:
            self.organizational_unit_name = m.get('organizationalUnitName')
        return self


class PatchOrganizationalUnitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PatchUserHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        # 认证信息，格式:Bearer access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PatchUserRequest(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        email_verified: bool = None,
        phone_number: str = None,
        phone_number_verified: bool = None,
        phone_region: str = None,
        username: str = None,
    ):
        # 账户展示名
        self.display_name = display_name
        # 邮箱
        self.email = email
        # 邮箱是否验证，邮箱若设置此字段必须设置，无特殊业务可直接设置为true
        self.email_verified = email_verified
        # 手机号
        self.phone_number = phone_number
        # 手机号是否验证，手机号若设置此字段必须设置，无特殊业务可直接设置为true
        self.phone_number_verified = phone_number_verified
        # 手机地区编号,示例：中国大陆手区号为86，不带 00 或 +, 手机号若设置，此参数必填
        self.phone_region = phone_region
        # 账户名
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.email is not None:
            result['email'] = self.email
        if self.email_verified is not None:
            result['emailVerified'] = self.email_verified
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        if self.phone_number_verified is not None:
            result['phoneNumberVerified'] = self.phone_number_verified
        if self.phone_region is not None:
            result['phoneRegion'] = self.phone_region
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('emailVerified') is not None:
            self.email_verified = m.get('emailVerified')
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        if m.get('phoneNumberVerified') is not None:
            self.phone_number_verified = m.get('phoneNumberVerified')
        if m.get('phoneRegion') is not None:
            self.phone_region = m.get('phoneRegion')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class PatchUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RevokeTokenRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        client_secret: str = None,
        token: str = None,
        token_type_hint: str = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        # 撤销的token
        self.token = token
        # token类型
        self.token_type_hint = token_type_hint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.client_secret is not None:
            result['client_secret'] = self.client_secret
        if self.token is not None:
            result['token'] = self.token
        if self.token_type_hint is not None:
            result['token_type_hint'] = self.token_type_hint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('token_type_hint') is not None:
            self.token_type_hint = m.get('token_type_hint')
        return self


class RevokeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

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
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


