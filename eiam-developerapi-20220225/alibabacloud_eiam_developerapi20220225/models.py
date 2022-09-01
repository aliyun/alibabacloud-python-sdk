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
        self.description = description
        self.organizational_unit_external_id = organizational_unit_external_id
        self.organizational_unit_name = organizational_unit_name
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
        self.description = description
        self.display_name = display_name
        self.email = email
        self.email_verified = email_verified
        self.password = password
        self.phone_number = phone_number
        self.phone_number_verified = phone_number_verified
        self.phone_region = phone_region
        self.primary_organizational_unit_id = primary_organizational_unit_id
        self.user_external_id = user_external_id
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
        scope: str = None,
    ):
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scope is not None:
            result['scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        self.device_code = device_code
        self.expires_at = expires_at
        self.expires_in = expires_in
        self.interval = interval
        self.user_code = user_code
        self.verification_uri = verification_uri
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
        self.code = code
        self.code_verifier = code_verifier
        self.device_code = device_code
        self.exclusive_tag = exclusive_tag
        self.grant_type = grant_type
        self.password = password
        self.redirect_uri = redirect_uri
        self.refresh_token = refresh_token
        self.scope = scope
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
        self.access_token = access_token
        self.expires_at = expires_at
        self.expires_in = expires_in
        self.id_token = id_token
        self.refresh_token = refresh_token
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
        self.create_time = create_time
        self.description = description
        self.instance_id = instance_id
        self.organizational_unit_external_id = organizational_unit_external_id
        self.organizational_unit_id = organizational_unit_id
        self.organizational_unit_name = organizational_unit_name
        self.organizational_unit_source_id = organizational_unit_source_id
        self.organizational_unit_source_type = organizational_unit_source_type
        self.parent_id = parent_id
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
        organizational_unit_source_id: str = None,
        organizational_unit_source_type: str = None,
    ):
        self.organizational_unit_external_id = organizational_unit_external_id
        self.organizational_unit_source_id = organizational_unit_source_id
        self.organizational_unit_source_type = organizational_unit_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organizational_unit_external_id is not None:
            result['organizationalUnitExternalId'] = self.organizational_unit_external_id
        if self.organizational_unit_source_id is not None:
            result['organizationalUnitSourceId'] = self.organizational_unit_source_id
        if self.organizational_unit_source_type is not None:
            result['organizationalUnitSourceType'] = self.organizational_unit_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('organizationalUnitExternalId') is not None:
            self.organizational_unit_external_id = m.get('organizationalUnitExternalId')
        if m.get('organizationalUnitSourceId') is not None:
            self.organizational_unit_source_id = m.get('organizationalUnitSourceId')
        if m.get('organizationalUnitSourceType') is not None:
            self.organizational_unit_source_type = m.get('organizationalUnitSourceType')
        return self


class GetOrganizationalUnitIdByExternalIdResponseBody(TeaModel):
    def __init__(
        self,
        organizational_unit_id: str = None,
    ):
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
        self.organizational_unit_id = organizational_unit_id
        self.organizational_unit_name = organizational_unit_name
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
        self.account_expire_time = account_expire_time
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.email = email
        self.email_verified = email_verified
        self.instance_id = instance_id
        self.lock_expire_time = lock_expire_time
        self.organizational_units = organizational_units
        self.phone_number = phone_number
        self.phone_number_verified = phone_number_verified
        self.phone_region = phone_region
        self.primary_organizational_unit_id = primary_organizational_unit_id
        self.register_time = register_time
        self.status = status
        self.update_time = update_time
        self.user_external_id = user_external_id
        self.user_id = user_id
        self.user_source_id = user_source_id
        self.user_source_type = user_source_type
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


class GetUserIdByEmailHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
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


class GetUserIdByEmailRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
    ):
        self.email = email

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        return self


class GetUserIdByEmailResponseBody(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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


class GetUserIdByEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserIdByEmailResponseBody = None,
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
            temp_model = GetUserIdByEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserIdByPhoneNumberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
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


class GetUserIdByPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
    ):
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        return self


class GetUserIdByPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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


class GetUserIdByPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserIdByPhoneNumberResponseBody = None,
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
            temp_model = GetUserIdByPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserIdByUserExternalIdHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
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


class GetUserIdByUserExternalIdRequest(TeaModel):
    def __init__(
        self,
        user_external_id: str = None,
        user_source_id: str = None,
        user_source_type: str = None,
    ):
        self.user_external_id = user_external_id
        self.user_source_id = user_source_id
        self.user_source_type = user_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_external_id is not None:
            result['userExternalId'] = self.user_external_id
        if self.user_source_id is not None:
            result['userSourceId'] = self.user_source_id
        if self.user_source_type is not None:
            result['userSourceType'] = self.user_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userExternalId') is not None:
            self.user_external_id = m.get('userExternalId')
        if m.get('userSourceId') is not None:
            self.user_source_id = m.get('userSourceId')
        if m.get('userSourceType') is not None:
            self.user_source_type = m.get('userSourceType')
        return self


class GetUserIdByUserExternalIdResponseBody(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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


class GetUserIdByUserExternalIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserIdByUserExternalIdResponseBody = None,
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
            temp_model = GetUserIdByUserExternalIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserIdByUsernameHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
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


class GetUserIdByUsernameRequest(TeaModel):
    def __init__(
        self,
        username: str = None,
    ):
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GetUserIdByUsernameResponseBody(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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


class GetUserIdByUsernameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserIdByUsernameResponseBody = None,
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
            temp_model = GetUserIdByUsernameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
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


class ListOrganizationalUnitParentIdsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
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
        self.page_number = page_number
        self.page_size = page_size
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
        self.create_time = create_time
        self.description = description
        self.instance_id = instance_id
        self.organizational_unit_external_id = organizational_unit_external_id
        self.organizational_unit_id = organizational_unit_id
        self.organizational_unit_name = organizational_unit_name
        self.organizational_unit_source_id = organizational_unit_source_id
        self.organizational_unit_source_type = organizational_unit_source_type
        self.parent_id = parent_id
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
        self.organizational_unit_id = organizational_unit_id
        self.page_number = page_number
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
        self.account_expire_time = account_expire_time
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.email = email
        self.email_verified = email_verified
        self.instance_id = instance_id
        self.lock_expire_time = lock_expire_time
        self.phone_number = phone_number
        self.phone_number_verified = phone_number_verified
        self.phone_region = phone_region
        self.register_time = register_time
        self.status = status
        self.update_time = update_time
        self.user_external_id = user_external_id
        self.user_id = user_id
        self.user_source_id = user_source_id
        self.user_source_type = user_source_type
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
        self.description = description
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
        self.display_name = display_name
        self.email = email
        self.email_verified = email_verified
        self.phone_number = phone_number
        self.phone_number_verified = phone_number_verified
        self.phone_region = phone_region
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
        self.token = token
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


