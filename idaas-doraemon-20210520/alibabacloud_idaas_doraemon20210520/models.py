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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器类型
        self.authenticator_type = authenticator_type
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign
        # 注册上下文
        self.registration_context = registration_context
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json
        # 用户展示名
        self.user_display_name = user_display_name
        # 用户id
        self.user_id = user_id
        # 用户姓名
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
        # 防重放挑战码
        self.challenge_base_64 = challenge_base_64
        # 创建认证器的Options
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
        body: CreateAuthenticatorRegistrationResponseBody = None,
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器类型
        self.authenticator_type = authenticator_type
        # 操作hash，用来和认证绑定
        self.bind_hash_base_64 = bind_hash_base_64
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json
        # 用户id
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
        # 防重放挑战码
        self.challenge_base_64 = challenge_base_64
        # 创建认证的Options，内容是JSON
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
        body: CreateUserAuthenticateOptionsResponseBody = None,
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid
        # 用户id
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
        body: DeregisterAuthenticatorResponseBody = None,
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
        xclient_ip: str = None,
    ):
        self.application_external_id = application_external_id
        self.mobile_extend_params_json = mobile_extend_params_json
        self.mobile_extend_params_json_sign = mobile_extend_params_json_sign
        self.server_extend_params_json = server_extend_params_json
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
        body: FetchAccessTokenResponseBody = None,
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid
        # 用户ID
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
        # 认证器名字
        self.authenticator_name = authenticator_name
        self.authenticator_uuid = authenticator_uuid
        # 创建认证器的Options
        self.credential_id = credential_id
        self.custom_authenticator = custom_authenticator
        # 用户最后签名IP
        self.last_verify_source_ip = last_verify_source_ip
        # 最后验证时间
        self.last_verify_time = last_verify_time
        # 用户最后签名userAgent
        self.last_verify_user_agent = last_verify_user_agent
        # 用户注册IP
        self.register_source_ip = register_source_ip
        # 注册时间
        self.register_time = register_time
        # 认证器类型
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
        body: GetAuthenticatorResponseBody = None,
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
        # 返回列表长度
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
        body: ListAuthenticationLogsResponseBody = None,
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
        # 返回列表长度
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
        body: ListAuthenticatorOpsLogsResponseBody = None,
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器类型
        self.authenticator_type = authenticator_type
        # 当前开始读取的位置，不设置时默认为1
        self.page_number = page_number
        # 本次读取的最大数据记录数量，不指定时使用默认值
        self.page_size = page_size
        # 用户id
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
        # 应用ID
        self.application_external_id = application_external_id
        # 身份认证对应的认证器名称
        self.authenticator_name = authenticator_name
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid
        # 身份认证ID
        self.credential_id = credential_id
        # 最后验证时间，如果新注册则为注册时间
        self.last_verify_time = last_verify_time
        # 创建时间
        self.register_time = register_time
        # 认证器类型
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
        # 读取到的位置
        self.page_number = page_number
        # 每页记录数量
        self.page_size = page_size
        self.request_id = request_id
        # 查询结果数据总数
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
        body: ListAuthenticatorsResponseBody = None,
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
            temp_model = ListAuthenticatorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPwnedPasswordsRequest(TeaModel):
    def __init__(
        self,
        prefix_hex_password_sha_1hash: str = None,
    ):
        # 泄露密码SHA1值前6位
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
        # 泄露密码SHA1值
        self.hex_password_sha_1hash = hex_password_sha_1hash
        # 泄露次数
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
        pwned_password_infos: List[ListPwnedPasswordsResponseBodyPwnedPasswordInfos] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.pwned_password_infos = pwned_password_infos
        self.request_id = request_id
        # 返回列表长度
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
        body: ListPwnedPasswordsResponseBody = None,
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
            temp_model = ListPwnedPasswordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        application_external_id: str = None,
        user_id: str = None,
    ):
        # 应用外部Id
        self.application_external_id = application_external_id
        # 用户id
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
        # 查询结果数据总数
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
        body: ListUsersResponseBody = None,
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
            temp_model = ListUsersResponseBody()
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器名字
        self.authenticator_name = authenticator_name
        # 认证器类型
        self.authenticator_type = authenticator_type
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign
        # 用户自定义记录审计日志信息
        self.log_params = log_params
        # 注册上下文
        self.registration_context = registration_context
        # 会话绑定的challenge base64标识
        self.require_challenge_base_64 = require_challenge_base_64
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json
        # 用户id
        self.user_id = user_id
        # 用户端来源IP地址，用于审计
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
        request_id: str = None,
    ):
        # 认证器UUID
        self.authenticator_uuid = authenticator_uuid
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticatorUuid') is not None:
            self.authenticator_uuid = m.get('AuthenticatorUuid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterAuthenticatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterAuthenticatorResponseBody = None,
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
        self.application_external_id = application_external_id
        self.doraemon_action = doraemon_action
        self.mobile_extend_params_json = mobile_extend_params_json
        self.mobile_extend_params_json_sign = mobile_extend_params_json_sign
        self.server_extend_params_json = server_extend_params_json
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
        if self.success is not None:
            result['Success'] = self.success
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
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ServiceInvokeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ServiceInvokeResponseBody = None,
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证器名字
        self.authenticator_name = authenticator_name
        # 认证器uuid
        self.authenticator_uuid = authenticator_uuid
        # 用户id
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
        body: UpdateAuthenticatorAttributeResponseBody = None,
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
            temp_model = UpdateAuthenticatorAttributeResponseBody()
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
        # 应用外部Id
        self.application_external_id = application_external_id
        # 认证上下文，由AuthenticatorType决定格式
        self.authentication_context = authentication_context
        # 认证器类型
        self.authenticator_type = authenticator_type
        # 客户端SDK生成认证上下文
        self.client_extend_params_json = client_extend_params_json
        # 客户端SDK生成认证上下文签名信息
        self.client_extend_params_json_sign = client_extend_params_json_sign
        # 用户自定义记录审计日志信息
        self.log_params = log_params
        # 用户自定义记录审计日志标签
        self.log_tag = log_tag
        # 认证绑定的操作hash base64标识
        self.require_bind_hash_base_64 = require_bind_hash_base_64
        # 会话绑定的challenge base64标识
        self.require_challenge_base_64 = require_challenge_base_64
        # 服务端配置项，决定认证要求属性
        self.server_extend_params_json = server_extend_params_json
        # 用户id
        self.user_id = user_id
        # 用户端来源IP地址，用于审计
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
        # 这次认证绑定的操作hash
        self.bind_hash_base_64 = bind_hash_base_64
        # 认证使用的凭据Id
        self.credential_id = credential_id
        # 认证通过的用户Id
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
        request_id: str = None,
        verify_result: bool = None,
    ):
        # 认证结果
        self.authenticate_result_info = authenticate_result_info
        self.request_id = request_id
        # 认证结果，true or false
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class VerifyUserAuthenticationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyUserAuthenticationResponseBody = None,
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
            temp_model = VerifyUserAuthenticationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


