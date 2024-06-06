# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAuthenticatorRegistrationRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_type: str = None,
        client_extend_params_json: str = None,
        client_extend_params_json_sign: str = None,
        registration_context: str = None,
        server_extend_params_json: str = None,
        user_display_name: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.authenticator_type = authenticator_type
        self.client_extend_params_json = client_extend_params_json
        self.client_extend_params_json_sign = client_extend_params_json_sign
        self.registration_context = registration_context
        self.server_extend_params_json = server_extend_params_json
        self.user_display_name = user_display_name
        # This parameter is required.
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.registration_context is not None:
            result['RegistrationContext'] = self.registration_context
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_display_name is not None:
            result['UserDisplayName'] = self.user_display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('RegistrationContext') is not None:
            self.registration_context = m.get('RegistrationContext')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserDisplayName') is not None:
            self.user_display_name = m.get('UserDisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAuthenticatorRegistrationResponseBody(TeaModel):
    def __init__(
        self,
        challenge_base_64: str = None,
        options: str = None,
        request_id: str = None,
    ):
        self.challenge_base_64 = challenge_base_64
        self.options = options
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.options is not None:
            result['Options'] = self.options
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAuthenticatorRegistrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAuthenticatorRegistrationResponseBody = None,
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
            temp_model = CreateAuthenticatorRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserAuthenticateOptionsRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_type: str = None,
        bind_hash_base_64: str = None,
        client_extend_params_json: str = None,
        client_extend_params_json_sign: str = None,
        server_extend_params_json: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.authenticator_type = authenticator_type
        self.bind_hash_base_64 = bind_hash_base_64
        self.client_extend_params_json = client_extend_params_json
        self.client_extend_params_json_sign = client_extend_params_json_sign
        self.server_extend_params_json = server_extend_params_json
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.bind_hash_base_64 is not None:
            result['BindHashBase64'] = self.bind_hash_base_64
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('BindHashBase64') is not None:
            self.bind_hash_base_64 = m.get('BindHashBase64')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserAuthenticateOptionsResponseBody(TeaModel):
    def __init__(
        self,
        challenge_base_64: str = None,
        options: str = None,
        request_id: str = None,
    ):
        self.challenge_base_64 = challenge_base_64
        self.options = options
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.options is not None:
            result['Options'] = self.options
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserAuthenticateOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserAuthenticateOptionsResponseBody = None,
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
            temp_model = CreateUserAuthenticateOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterAuthenticatorRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_uuid: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.authenticator_uuid = authenticator_uuid
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeregisterAuthenticatorResponseBody(TeaModel):
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


class DeregisterAuthenticatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeregisterAuthenticatorResponseBody = None,
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
            temp_model = DeregisterAuthenticatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchAccessTokenRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        mobile_extend_params_json: str = None,
        mobile_extend_params_json_sign: str = None,
        server_extend_params_json: str = None,
        user_id: str = None,
        xclient_ip: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.mobile_extend_params_json = mobile_extend_params_json
        # This parameter is required.
        self.mobile_extend_params_json_sign = mobile_extend_params_json_sign
        self.server_extend_params_json = server_extend_params_json
        self.user_id = user_id
        self.xclient_ip = xclient_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.mobile_extend_params_json is not None:
            result['MobileExtendParamsJson'] = self.mobile_extend_params_json
        if self.mobile_extend_params_json_sign is not None:
            result['MobileExtendParamsJsonSign'] = self.mobile_extend_params_json_sign
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.xclient_ip is not None:
            result['XClientIp'] = self.xclient_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('MobileExtendParamsJson') is not None:
            self.mobile_extend_params_json = m.get('MobileExtendParamsJson')
        if m.get('MobileExtendParamsJsonSign') is not None:
            self.mobile_extend_params_json_sign = m.get('MobileExtendParamsJsonSign')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('XClientIp') is not None:
            self.xclient_ip = m.get('XClientIp')
        return self


class FetchAccessTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expires_in: str = None,
        id_token: str = None,
        refresh_token: str = None,
        scope: str = None,
        token_type: str = None,
    ):
        self.access_token = access_token
        self.expires_in = expires_in
        self.id_token = id_token
        self.refresh_token = refresh_token
        self.scope = scope
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['Access_token'] = self.access_token
        if self.expires_in is not None:
            result['Expires_in'] = self.expires_in
        if self.id_token is not None:
            result['Id_token'] = self.id_token
        if self.refresh_token is not None:
            result['Refresh_token'] = self.refresh_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.token_type is not None:
            result['Token_type'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Access_token') is not None:
            self.access_token = m.get('Access_token')
        if m.get('Expires_in') is not None:
            self.expires_in = m.get('Expires_in')
        if m.get('Id_token') is not None:
            self.id_token = m.get('Id_token')
        if m.get('Refresh_token') is not None:
            self.refresh_token = m.get('Refresh_token')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Token_type') is not None:
            self.token_type = m.get('Token_type')
        return self


class FetchAccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: FetchAccessTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = FetchAccessTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchAccessTokenResponseBody = None,
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
            temp_model = FetchAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthenticatorRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_uuid: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.authenticator_uuid = authenticator_uuid
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAuthenticatorResponseBodyAuthenticator(TeaModel):
    def __init__(
        self,
        authenticator_name: str = None,
        authenticator_uuid: str = None,
        credential_id: str = None,
        custom_authenticator: str = None,
        last_verify_source_ip: str = None,
        last_verify_time: int = None,
        last_verify_user_agent: str = None,
        register_source_ip: str = None,
        register_time: int = None,
        type: str = None,
    ):
        self.authenticator_name = authenticator_name
        self.authenticator_uuid = authenticator_uuid
        self.credential_id = credential_id
        self.custom_authenticator = custom_authenticator
        self.last_verify_source_ip = last_verify_source_ip
        self.last_verify_time = last_verify_time
        self.last_verify_user_agent = last_verify_user_agent
        self.register_source_ip = register_source_ip
        self.register_time = register_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.custom_authenticator is not None:
            result['CustomAuthenticator'] = self.custom_authenticator
        if self.last_verify_source_ip is not None:
            result['LastVerifySourceIp'] = self.last_verify_source_ip
        if self.last_verify_time is not None:
            result['LastVerifyTime'] = self.last_verify_time
        if self.last_verify_user_agent is not None:
            result['LastVerifyUserAgent'] = self.last_verify_user_agent
        if self.register_source_ip is not None:
            result['RegisterSourceIp'] = self.register_source_ip
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('CustomAuthenticator') is not None:
            self.custom_authenticator = m.get('CustomAuthenticator')
        if m.get('LastVerifySourceIp') is not None:
            self.last_verify_source_ip = m.get('LastVerifySourceIp')
        if m.get('LastVerifyTime') is not None:
            self.last_verify_time = m.get('LastVerifyTime')
        if m.get('LastVerifyUserAgent') is not None:
            self.last_verify_user_agent = m.get('LastVerifyUserAgent')
        if m.get('RegisterSourceIp') is not None:
            self.register_source_ip = m.get('RegisterSourceIp')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAuthenticatorResponseBody(TeaModel):
    def __init__(
        self,
        authenticator: GetAuthenticatorResponseBodyAuthenticator = None,
        request_id: str = None,
    ):
        self.authenticator = authenticator
        self.request_id = request_id

    def validate(self):
        if self.authenticator:
            self.authenticator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticator is not None:
            result['Authenticator'] = self.authenticator.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authenticator') is not None:
            temp_model = GetAuthenticatorResponseBodyAuthenticator()
            self.authenticator = temp_model.from_map(m['Authenticator'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthenticatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthenticatorResponseBody = None,
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
            temp_model = GetAuthenticatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticationLogsRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_type: str = None,
        authenticator_uuid: str = None,
        credential_id: str = None,
        from_time: int = None,
        log_tag: str = None,
        page_number: int = None,
        page_size: int = None,
        to_time: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        self.authenticator_type = authenticator_type
        self.authenticator_uuid = authenticator_uuid
        self.credential_id = credential_id
        self.from_time = from_time
        self.log_tag = log_tag
        self.page_number = page_number
        self.page_size = page_size
        self.to_time = to_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.from_time is not None:
            result['FromTime'] = self.from_time
        if self.log_tag is not None:
            result['LogTag'] = self.log_tag
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.to_time is not None:
            result['ToTime'] = self.to_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('FromTime') is not None:
            self.from_time = m.get('FromTime')
        if m.get('LogTag') is not None:
            self.log_tag = m.get('LogTag')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToTime') is not None:
            self.to_time = m.get('ToTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAuthenticationLogsResponseBodyAuthenticationLogContent(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        application_external_id: str = None,
        application_uuid: str = None,
        authentication_action: str = None,
        authentication_time: int = None,
        authenticator_name: str = None,
        authenticator_type: str = None,
        authenticator_uuid: str = None,
        challenge_base_64: str = None,
        credential_id: str = None,
        error_code: str = None,
        error_message: str = None,
        log_params: str = None,
        log_tag: str = None,
        raw_authentication_context: str = None,
        tenant_id: str = None,
        user_agent: str = None,
        user_id: str = None,
        user_source_ip: str = None,
        verify_result: bool = None,
    ):
        self.ali_uid = ali_uid
        self.application_external_id = application_external_id
        self.application_uuid = application_uuid
        self.authentication_action = authentication_action
        self.authentication_time = authentication_time
        self.authenticator_name = authenticator_name
        self.authenticator_type = authenticator_type
        self.authenticator_uuid = authenticator_uuid
        self.challenge_base_64 = challenge_base_64
        self.credential_id = credential_id
        self.error_code = error_code
        self.error_message = error_message
        self.log_params = log_params
        self.log_tag = log_tag
        self.raw_authentication_context = raw_authentication_context
        self.tenant_id = tenant_id
        self.user_agent = user_agent
        self.user_id = user_id
        self.user_source_ip = user_source_ip
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.application_uuid is not None:
            result['ApplicationUuid'] = self.application_uuid
        if self.authentication_action is not None:
            result['AuthenticationAction'] = self.authentication_action
        if self.authentication_time is not None:
            result['AuthenticationTime'] = self.authentication_time
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.log_tag is not None:
            result['LogTag'] = self.log_tag
        if self.raw_authentication_context is not None:
            result['RawAuthenticationContext'] = self.raw_authentication_context
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_agent is not None:
            result['UserAgent'] = self.user_agent
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('ApplicationUuid') is not None:
            self.application_uuid = m.get('ApplicationUuid')
        if m.get('AuthenticationAction') is not None:
            self.authentication_action = m.get('AuthenticationAction')
        if m.get('AuthenticationTime') is not None:
            self.authentication_time = m.get('AuthenticationTime')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('LogTag') is not None:
            self.log_tag = m.get('LogTag')
        if m.get('RawAuthenticationContext') is not None:
            self.raw_authentication_context = m.get('RawAuthenticationContext')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserAgent') is not None:
            self.user_agent = m.get('UserAgent')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class ListAuthenticationLogsResponseBody(TeaModel):
    def __init__(
        self,
        authentication_log_content: List[ListAuthenticationLogsResponseBodyAuthenticationLogContent] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authentication_log_content = authentication_log_content
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authentication_log_content:
            for k in self.authentication_log_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthenticationLogContent'] = []
        if self.authentication_log_content is not None:
            for k in self.authentication_log_content:
                result['AuthenticationLogContent'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authentication_log_content = []
        if m.get('AuthenticationLogContent') is not None:
            for k in m.get('AuthenticationLogContent'):
                temp_model = ListAuthenticationLogsResponseBodyAuthenticationLogContent()
                self.authentication_log_content.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthenticationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAuthenticationLogsResponseBody = None,
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
            temp_model = ListAuthenticationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticatorOpsLogsRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_type: str = None,
        authenticator_uuid: str = None,
        from_time: int = None,
        page_number: int = None,
        page_size: int = None,
        to_time: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        self.authenticator_type = authenticator_type
        self.authenticator_uuid = authenticator_uuid
        self.from_time = from_time
        self.page_number = page_number
        self.page_size = page_size
        self.to_time = to_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.from_time is not None:
            result['FromTime'] = self.from_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.to_time is not None:
            result['ToTime'] = self.to_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('FromTime') is not None:
            self.from_time = m.get('FromTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToTime') is not None:
            self.to_time = m.get('ToTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        application_external_id: str = None,
        application_uuid: str = None,
        authenticator_name: str = None,
        authenticator_type: str = None,
        authenticator_uuid: str = None,
        challenge_base_64: str = None,
        credential_id: str = None,
        error_code: str = None,
        error_message: str = None,
        log_params: str = None,
        operation_action: str = None,
        operation_result: bool = None,
        operation_time: int = None,
        raw_context: str = None,
        tenant_id: str = None,
        user_agent: str = None,
        user_id: str = None,
        user_source_ip: str = None,
    ):
        self.ali_uid = ali_uid
        self.application_external_id = application_external_id
        self.application_uuid = application_uuid
        self.authenticator_name = authenticator_name
        self.authenticator_type = authenticator_type
        self.authenticator_uuid = authenticator_uuid
        self.challenge_base_64 = challenge_base_64
        self.credential_id = credential_id
        self.error_code = error_code
        self.error_message = error_message
        self.log_params = log_params
        self.operation_action = operation_action
        self.operation_result = operation_result
        self.operation_time = operation_time
        self.raw_context = raw_context
        self.tenant_id = tenant_id
        self.user_agent = user_agent
        self.user_id = user_id
        self.user_source_ip = user_source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.application_uuid is not None:
            result['ApplicationUuid'] = self.application_uuid
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.challenge_base_64 is not None:
            result['ChallengeBase64'] = self.challenge_base_64
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.operation_action is not None:
            result['OperationAction'] = self.operation_action
        if self.operation_result is not None:
            result['OperationResult'] = self.operation_result
        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time
        if self.raw_context is not None:
            result['RawContext'] = self.raw_context
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_agent is not None:
            result['UserAgent'] = self.user_agent
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('ApplicationUuid') is not None:
            self.application_uuid = m.get('ApplicationUuid')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('ChallengeBase64') is not None:
            self.challenge_base_64 = m.get('ChallengeBase64')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('OperationAction') is not None:
            self.operation_action = m.get('OperationAction')
        if m.get('OperationResult') is not None:
            self.operation_result = m.get('OperationResult')
        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')
        if m.get('RawContext') is not None:
            self.raw_context = m.get('RawContext')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserAgent') is not None:
            self.user_agent = m.get('UserAgent')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        return self


class ListAuthenticatorOpsLogsResponseBody(TeaModel):
    def __init__(
        self,
        authentication_log_content: List[ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authentication_log_content = authentication_log_content
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authentication_log_content:
            for k in self.authentication_log_content:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthenticationLogContent'] = []
        if self.authentication_log_content is not None:
            for k in self.authentication_log_content:
                result['AuthenticationLogContent'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authentication_log_content = []
        if m.get('AuthenticationLogContent') is not None:
            for k in m.get('AuthenticationLogContent'):
                temp_model = ListAuthenticatorOpsLogsResponseBodyAuthenticationLogContent()
                self.authentication_log_content.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthenticatorOpsLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAuthenticatorOpsLogsResponseBody = None,
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
            temp_model = ListAuthenticatorOpsLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticatorsRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_type: str = None,
        page_number: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        self.authenticator_type = authenticator_type
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListAuthenticatorsResponseBodyAuthenticator(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_name: str = None,
        authenticator_uuid: str = None,
        credential_id: str = None,
        last_verify_time: int = None,
        register_time: int = None,
        type: str = None,
    ):
        self.application_external_id = application_external_id
        self.authenticator_name = authenticator_name
        self.authenticator_uuid = authenticator_uuid
        self.credential_id = credential_id
        self.last_verify_time = last_verify_time
        self.register_time = register_time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.last_verify_time is not None:
            result['LastVerifyTime'] = self.last_verify_time
        if self.register_time is not None:
            result['RegisterTime'] = self.register_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('LastVerifyTime') is not None:
            self.last_verify_time = m.get('LastVerifyTime')
        if m.get('RegisterTime') is not None:
            self.register_time = m.get('RegisterTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAuthenticatorsResponseBody(TeaModel):
    def __init__(
        self,
        authenticator: List[ListAuthenticatorsResponseBodyAuthenticator] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.authenticator = authenticator
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.authenticator:
            for k in self.authenticator:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Authenticator'] = []
        if self.authenticator is not None:
            for k in self.authenticator:
                result['Authenticator'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authenticator = []
        if m.get('Authenticator') is not None:
            for k in m.get('Authenticator'):
                temp_model = ListAuthenticatorsResponseBodyAuthenticator()
                self.authenticator.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAuthenticatorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAuthenticatorsResponseBody = None,
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
            temp_model = ListAuthenticatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCostUnitOrdersRequest(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        final_date: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.begin_date = begin_date
        self.final_date = final_date
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.final_date is not None:
            result['FinalDate'] = self.final_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('FinalDate') is not None:
            self.final_date = m.get('FinalDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCostUnitOrdersResponseBodyItems(TeaModel):
    def __init__(
        self,
        ali_order_code: str = None,
        ali_order_instance_id: str = None,
        create_time: int = None,
        exhausted: bool = None,
        expired_time: int = None,
        order_status: str = None,
        refund_time: int = None,
        total_cost_unit: int = None,
        used_cost_unit: int = None,
    ):
        self.ali_order_code = ali_order_code
        self.ali_order_instance_id = ali_order_instance_id
        self.create_time = create_time
        self.exhausted = exhausted
        self.expired_time = expired_time
        self.order_status = order_status
        self.refund_time = refund_time
        self.total_cost_unit = total_cost_unit
        self.used_cost_unit = used_cost_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_order_code is not None:
            result['AliOrderCode'] = self.ali_order_code
        if self.ali_order_instance_id is not None:
            result['AliOrderInstanceId'] = self.ali_order_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exhausted is not None:
            result['Exhausted'] = self.exhausted
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.refund_time is not None:
            result['RefundTime'] = self.refund_time
        if self.total_cost_unit is not None:
            result['TotalCostUnit'] = self.total_cost_unit
        if self.used_cost_unit is not None:
            result['UsedCostUnit'] = self.used_cost_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliOrderCode') is not None:
            self.ali_order_code = m.get('AliOrderCode')
        if m.get('AliOrderInstanceId') is not None:
            self.ali_order_instance_id = m.get('AliOrderInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Exhausted') is not None:
            self.exhausted = m.get('Exhausted')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('RefundTime') is not None:
            self.refund_time = m.get('RefundTime')
        if m.get('TotalCostUnit') is not None:
            self.total_cost_unit = m.get('TotalCostUnit')
        if m.get('UsedCostUnit') is not None:
            self.used_cost_unit = m.get('UsedCostUnit')
        return self


class ListCostUnitOrdersResponseBody(TeaModel):
    def __init__(
        self,
        items: List[ListCostUnitOrdersResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListCostUnitOrdersResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListCostUnitOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCostUnitOrdersResponseBody = None,
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
            temp_model = ListCostUnitOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrderConsumeStatisticRecordsRequest(TeaModel):
    def __init__(
        self,
        ali_order_code: str = None,
        application_external_id: str = None,
        page_number: int = None,
        page_size: int = None,
        service_code: str = None,
        statistic_time_max: str = None,
        statistic_time_min: str = None,
    ):
        self.ali_order_code = ali_order_code
        self.application_external_id = application_external_id
        self.page_number = page_number
        self.page_size = page_size
        self.service_code = service_code
        self.statistic_time_max = statistic_time_max
        self.statistic_time_min = statistic_time_min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_order_code is not None:
            result['AliOrderCode'] = self.ali_order_code
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.statistic_time_max is not None:
            result['StatisticTimeMax'] = self.statistic_time_max
        if self.statistic_time_min is not None:
            result['StatisticTimeMin'] = self.statistic_time_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliOrderCode') is not None:
            self.ali_order_code = m.get('AliOrderCode')
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StatisticTimeMax') is not None:
            self.statistic_time_max = m.get('StatisticTimeMax')
        if m.get('StatisticTimeMin') is not None:
            self.statistic_time_min = m.get('StatisticTimeMin')
        return self


class ListOrderConsumeStatisticRecordsResponseBodyItems(TeaModel):
    def __init__(
        self,
        ali_order_code: str = None,
        application_external_id: str = None,
        charged_count: int = None,
        service_code: str = None,
        statistic_time: int = None,
        total_price: int = None,
        unit_price: int = None,
    ):
        self.ali_order_code = ali_order_code
        self.application_external_id = application_external_id
        self.charged_count = charged_count
        self.service_code = service_code
        self.statistic_time = statistic_time
        self.total_price = total_price
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_order_code is not None:
            result['AliOrderCode'] = self.ali_order_code
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.charged_count is not None:
            result['ChargedCount'] = self.charged_count
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.statistic_time is not None:
            result['StatisticTime'] = self.statistic_time
        if self.total_price is not None:
            result['TotalPrice'] = self.total_price
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliOrderCode') is not None:
            self.ali_order_code = m.get('AliOrderCode')
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('ChargedCount') is not None:
            self.charged_count = m.get('ChargedCount')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('StatisticTime') is not None:
            self.statistic_time = m.get('StatisticTime')
        if m.get('TotalPrice') is not None:
            self.total_price = m.get('TotalPrice')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class ListOrderConsumeStatisticRecordsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[ListOrderConsumeStatisticRecordsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_elements = total_elements
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = ListOrderConsumeStatisticRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListOrderConsumeStatisticRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOrderConsumeStatisticRecordsResponseBody = None,
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
            temp_model = ListOrderConsumeStatisticRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPwnedPasswordsRequest(TeaModel):
    def __init__(
        self,
        prefix_hex_password_sha_1hash: str = None,
    ):
        # This parameter is required.
        self.prefix_hex_password_sha_1hash = prefix_hex_password_sha_1hash

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prefix_hex_password_sha_1hash is not None:
            result['PrefixHexPasswordSha1Hash'] = self.prefix_hex_password_sha_1hash
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrefixHexPasswordSha1Hash') is not None:
            self.prefix_hex_password_sha_1hash = m.get('PrefixHexPasswordSha1Hash')
        return self


class ListPwnedPasswordsResponseBodyPwnedPasswordInfos(TeaModel):
    def __init__(
        self,
        hex_password_sha_1hash: str = None,
        pwned_count: int = None,
    ):
        self.hex_password_sha_1hash = hex_password_sha_1hash
        self.pwned_count = pwned_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hex_password_sha_1hash is not None:
            result['HexPasswordSha1Hash'] = self.hex_password_sha_1hash
        if self.pwned_count is not None:
            result['PwnedCount'] = self.pwned_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HexPasswordSha1Hash') is not None:
            self.hex_password_sha_1hash = m.get('HexPasswordSha1Hash')
        if m.get('PwnedCount') is not None:
            self.pwned_count = m.get('PwnedCount')
        return self


class ListPwnedPasswordsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pwned_password_infos: List[ListPwnedPasswordsResponseBodyPwnedPasswordInfos] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.pwned_password_infos = pwned_password_infos
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.pwned_password_infos:
            for k in self.pwned_password_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PwnedPasswordInfos'] = []
        if self.pwned_password_infos is not None:
            for k in self.pwned_password_infos:
                result['PwnedPasswordInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pwned_password_infos = []
        if m.get('PwnedPasswordInfos') is not None:
            for k in m.get('PwnedPasswordInfos'):
                temp_model = ListPwnedPasswordsResponseBodyPwnedPasswordInfos()
                self.pwned_password_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPwnedPasswordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPwnedPasswordsResponseBody = None,
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
            temp_model = ListPwnedPasswordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_display_name: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_display_name = user_display_name
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_display_name is not None:
            result['UserDisplayName'] = self.user_display_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserDisplayName') is not None:
            self.user_display_name = m.get('UserDisplayName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[ListUsersResponseBodyUsers] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
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


class QuerySmsReportsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        event_id: str = None,
    ):
        self.app_id = app_id
        self.event_id = event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        return self


class QuerySmsReportsResponseBodySmsReports(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        charged_count: int = None,
        code: str = None,
        event_id: str = None,
        mobile: str = None,
        sn: str = None,
        stat: str = None,
        tenant_id: str = None,
        tid: str = None,
        time: str = None,
    ):
        self.app_id = app_id
        self.charged_count = charged_count
        self.code = code
        self.event_id = event_id
        self.mobile = mobile
        self.sn = sn
        self.stat = stat
        self.tenant_id = tenant_id
        self.tid = tid
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.charged_count is not None:
            result['ChargedCount'] = self.charged_count
        if self.code is not None:
            result['Code'] = self.code
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.stat is not None:
            result['Stat'] = self.stat
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChargedCount') is not None:
            self.charged_count = m.get('ChargedCount')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Stat') is not None:
            self.stat = m.get('Stat')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QuerySmsReportsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sms_reports: List[QuerySmsReportsResponseBodySmsReports] = None,
        total_elements: int = None,
    ):
        self.request_id = request_id
        self.sms_reports = sms_reports
        self.total_elements = total_elements

    def validate(self):
        if self.sms_reports:
            for k in self.sms_reports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmsReports'] = []
        if self.sms_reports is not None:
            for k in self.sms_reports:
                result['SmsReports'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sms_reports = []
        if m.get('SmsReports') is not None:
            for k in m.get('SmsReports'):
                temp_model = QuerySmsReportsResponseBodySmsReports()
                self.sms_reports.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class QuerySmsReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsReportsResponseBody = None,
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
            temp_model = QuerySmsReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySmsUpsResponseBodySmsUps(TeaModel):
    def __init__(
        self,
        content: str = None,
        dest_code: str = None,
        phone_number: str = None,
        send_time: str = None,
        sequence_id: str = None,
        tenant_id: str = None,
    ):
        self.content = content
        self.dest_code = dest_code
        self.phone_number = phone_number
        self.send_time = send_time
        self.sequence_id = sequence_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.dest_code is not None:
            result['DestCode'] = self.dest_code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.send_time is not None:
            result['SendTime'] = self.send_time
        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DestCode') is not None:
            self.dest_code = m.get('DestCode')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('SendTime') is not None:
            self.send_time = m.get('SendTime')
        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QuerySmsUpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sms_ups: List[QuerySmsUpsResponseBodySmsUps] = None,
        total_elements: int = None,
    ):
        self.request_id = request_id
        self.sms_ups = sms_ups
        self.total_elements = total_elements

    def validate(self):
        if self.sms_ups:
            for k in self.sms_ups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SmsUps'] = []
        if self.sms_ups is not None:
            for k in self.sms_ups:
                result['SmsUps'].append(k.to_map() if k else None)
        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sms_ups = []
        if m.get('SmsUps') is not None:
            for k in m.get('SmsUps'):
                temp_model = QuerySmsUpsResponseBodySmsUps()
                self.sms_ups.append(temp_model.from_map(k))
        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')
        return self


class QuerySmsUpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySmsUpsResponseBody = None,
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
            temp_model = QuerySmsUpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterAuthenticatorRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_name: str = None,
        authenticator_type: str = None,
        client_extend_params_json: str = None,
        client_extend_params_json_sign: str = None,
        log_params: str = None,
        registration_context: str = None,
        require_challenge_base_64: str = None,
        server_extend_params_json: str = None,
        user_id: str = None,
        user_source_ip: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        self.authenticator_name = authenticator_name
        # This parameter is required.
        self.authenticator_type = authenticator_type
        self.client_extend_params_json = client_extend_params_json
        self.client_extend_params_json_sign = client_extend_params_json_sign
        self.log_params = log_params
        # This parameter is required.
        self.registration_context = registration_context
        self.require_challenge_base_64 = require_challenge_base_64
        self.server_extend_params_json = server_extend_params_json
        # This parameter is required.
        self.user_id = user_id
        self.user_source_ip = user_source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.registration_context is not None:
            result['RegistrationContext'] = self.registration_context
        if self.require_challenge_base_64 is not None:
            result['RequireChallengeBase64'] = self.require_challenge_base_64
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('RegistrationContext') is not None:
            self.registration_context = m.get('RegistrationContext')
        if m.get('RequireChallengeBase64') is not None:
            self.require_challenge_base_64 = m.get('RequireChallengeBase64')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        return self


class RegisterAuthenticatorResponseBody(TeaModel):
    def __init__(
        self,
        authenticator_uuid: str = None,
        etas_response_sting: str = None,
        request_id: str = None,
    ):
        self.authenticator_uuid = authenticator_uuid
        self.etas_response_sting = etas_response_sting
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.etas_response_sting is not None:
            result['EtasResponseSting'] = self.etas_response_sting
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('EtasResponseSting') is not None:
            self.etas_response_sting = m.get('EtasResponseSting')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterAuthenticatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterAuthenticatorResponseBody = None,
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
            temp_model = RegisterAuthenticatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ServiceInvokeRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        doraemon_action: str = None,
        mobile_extend_params_json: str = None,
        mobile_extend_params_json_sign: str = None,
        server_extend_params_json: str = None,
        service_code: str = None,
        test_model: bool = None,
        xclient_ip: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.doraemon_action = doraemon_action
        self.mobile_extend_params_json = mobile_extend_params_json
        self.mobile_extend_params_json_sign = mobile_extend_params_json_sign
        self.server_extend_params_json = server_extend_params_json
        # This parameter is required.
        self.service_code = service_code
        self.test_model = test_model
        self.xclient_ip = xclient_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.doraemon_action is not None:
            result['DoraemonAction'] = self.doraemon_action
        if self.mobile_extend_params_json is not None:
            result['MobileExtendParamsJson'] = self.mobile_extend_params_json
        if self.mobile_extend_params_json_sign is not None:
            result['MobileExtendParamsJsonSign'] = self.mobile_extend_params_json_sign
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.test_model is not None:
            result['TestModel'] = self.test_model
        if self.xclient_ip is not None:
            result['XClientIp'] = self.xclient_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('DoraemonAction') is not None:
            self.doraemon_action = m.get('DoraemonAction')
        if m.get('MobileExtendParamsJson') is not None:
            self.mobile_extend_params_json = m.get('MobileExtendParamsJson')
        if m.get('MobileExtendParamsJsonSign') is not None:
            self.mobile_extend_params_json_sign = m.get('MobileExtendParamsJsonSign')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('TestModel') is not None:
            self.test_model = m.get('TestModel')
        if m.get('XClientIp') is not None:
            self.xclient_ip = m.get('XClientIp')
        return self


class ServiceInvokeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        event_id: str = None,
        id_token: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.event_id = event_id
        self.id_token = id_token
        self.message = message
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
        if self.data is not None:
            result['Data'] = self.data
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.id_token is not None:
            result['IdToken'] = self.id_token
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IdToken') is not None:
            self.id_token = m.get('IdToken')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ServiceInvokeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ServiceInvokeResponseBody = None,
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
            temp_model = ServiceInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthenticatorAttributeRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authenticator_name: str = None,
        authenticator_uuid: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.authenticator_name = authenticator_name
        # This parameter is required.
        self.authenticator_uuid = authenticator_uuid
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authenticator_name is not None:
            result['AuthenticatorName'] = self.authenticator_name
        if self.authenticator_uuid is not None:
            result['AuthenticatorUuid'] = self.authenticator_uuid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticatorName') is not None:
            self.authenticator_name = m.get('AuthenticatorName')
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateAuthenticatorAttributeResponseBody(TeaModel):
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


class UpdateAuthenticatorAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAuthenticatorAttributeResponseBody = None,
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
            temp_model = UpdateAuthenticatorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyIdTokenRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        jwt_id_token: str = None,
    ):
        self.application_external_id = application_external_id
        # jwtIdToken
        self.jwt_id_token = jwt_id_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.jwt_id_token is not None:
            result['JwtIdToken'] = self.jwt_id_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('JwtIdToken') is not None:
            self.jwt_id_token = m.get('JwtIdToken')
        return self


class VerifyIdTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_id: str = None,
    ):
        self.request_id = request_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyIdTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyIdTokenResponseBody = None,
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
            temp_model = VerifyIdTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyUserAuthenticationRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        authentication_context: str = None,
        authenticator_type: str = None,
        client_extend_params_json: str = None,
        client_extend_params_json_sign: str = None,
        log_params: str = None,
        log_tag: str = None,
        require_bind_hash_base_64: str = None,
        require_challenge_base_64: str = None,
        server_extend_params_json: str = None,
        user_id: str = None,
        user_source_ip: str = None,
    ):
        # This parameter is required.
        self.application_external_id = application_external_id
        # This parameter is required.
        self.authentication_context = authentication_context
        # This parameter is required.
        self.authenticator_type = authenticator_type
        self.client_extend_params_json = client_extend_params_json
        self.client_extend_params_json_sign = client_extend_params_json_sign
        self.log_params = log_params
        self.log_tag = log_tag
        self.require_bind_hash_base_64 = require_bind_hash_base_64
        self.require_challenge_base_64 = require_challenge_base_64
        self.server_extend_params_json = server_extend_params_json
        # This parameter is required.
        self.user_id = user_id
        self.user_source_ip = user_source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_external_id is not None:
            result['ApplicationExternalId'] = self.application_external_id
        if self.authentication_context is not None:
            result['AuthenticationContext'] = self.authentication_context
        if self.authenticator_type is not None:
            result['AuthenticatorType'] = self.authenticator_type
        if self.client_extend_params_json is not None:
            result['ClientExtendParamsJson'] = self.client_extend_params_json
        if self.client_extend_params_json_sign is not None:
            result['ClientExtendParamsJsonSign'] = self.client_extend_params_json_sign
        if self.log_params is not None:
            result['LogParams'] = self.log_params
        if self.log_tag is not None:
            result['LogTag'] = self.log_tag
        if self.require_bind_hash_base_64 is not None:
            result['RequireBindHashBase64'] = self.require_bind_hash_base_64
        if self.require_challenge_base_64 is not None:
            result['RequireChallengeBase64'] = self.require_challenge_base_64
        if self.server_extend_params_json is not None:
            result['ServerExtendParamsJson'] = self.server_extend_params_json
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source_ip is not None:
            result['UserSourceIp'] = self.user_source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationExternalId') is not None:
            self.application_external_id = m.get('ApplicationExternalId')
        if m.get('AuthenticationContext') is not None:
            self.authentication_context = m.get('AuthenticationContext')
        if m.get('AuthenticatorType') is not None:
            self.authenticator_type = m.get('AuthenticatorType')
        if m.get('ClientExtendParamsJson') is not None:
            self.client_extend_params_json = m.get('ClientExtendParamsJson')
        if m.get('ClientExtendParamsJsonSign') is not None:
            self.client_extend_params_json_sign = m.get('ClientExtendParamsJsonSign')
        if m.get('LogParams') is not None:
            self.log_params = m.get('LogParams')
        if m.get('LogTag') is not None:
            self.log_tag = m.get('LogTag')
        if m.get('RequireBindHashBase64') is not None:
            self.require_bind_hash_base_64 = m.get('RequireBindHashBase64')
        if m.get('RequireChallengeBase64') is not None:
            self.require_challenge_base_64 = m.get('RequireChallengeBase64')
        if m.get('ServerExtendParamsJson') is not None:
            self.server_extend_params_json = m.get('ServerExtendParamsJson')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSourceIp') is not None:
            self.user_source_ip = m.get('UserSourceIp')
        return self


class VerifyUserAuthenticationResponseBodyAuthenticateResultInfo(TeaModel):
    def __init__(
        self,
        bind_hash_base_64: str = None,
        credential_id: str = None,
        user_id: str = None,
    ):
        self.bind_hash_base_64 = bind_hash_base_64
        self.credential_id = credential_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_hash_base_64 is not None:
            result['BindHashBase64'] = self.bind_hash_base_64
        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindHashBase64') is not None:
            self.bind_hash_base_64 = m.get('BindHashBase64')
        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class VerifyUserAuthenticationResponseBody(TeaModel):
    def __init__(
        self,
        authenticate_result_info: VerifyUserAuthenticationResponseBodyAuthenticateResultInfo = None,
        etas_sdkstring: str = None,
        id_token: str = None,
        request_id: str = None,
        verify_result: bool = None,
    ):
        self.authenticate_result_info = authenticate_result_info
        self.etas_sdkstring = etas_sdkstring
        self.id_token = id_token
        self.request_id = request_id
        self.verify_result = verify_result

    def validate(self):
        if self.authenticate_result_info:
            self.authenticate_result_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authenticate_result_info is not None:
            result['AuthenticateResultInfo'] = self.authenticate_result_info.to_map()
        if self.etas_sdkstring is not None:
            result['EtasSDKString'] = self.etas_sdkstring
        if self.id_token is not None:
            result['IdToken'] = self.id_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticateResultInfo') is not None:
            temp_model = VerifyUserAuthenticationResponseBodyAuthenticateResultInfo()
            self.authenticate_result_info = temp_model.from_map(m['AuthenticateResultInfo'])
        if m.get('EtasSDKString') is not None:
            self.etas_sdkstring = m.get('EtasSDKString')
        if m.get('IdToken') is not None:
            self.id_token = m.get('IdToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyUserAuthenticationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyUserAuthenticationResponseBody = None,
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
            temp_model = VerifyUserAuthenticationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


