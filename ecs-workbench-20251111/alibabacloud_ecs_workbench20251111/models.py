# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class DescribeTerminalSettingsResponseBodyPasswordlessLoginConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeTerminalSettingsResponseBody(TeaModel):
    def __init__(
        self,
        passwordless_login_config: DescribeTerminalSettingsResponseBodyPasswordlessLoginConfig = None,
        request_id: str = None,
    ):
        self.passwordless_login_config = passwordless_login_config
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.passwordless_login_config:
            self.passwordless_login_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passwordless_login_config is not None:
            result['PasswordlessLoginConfig'] = self.passwordless_login_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordlessLoginConfig') is not None:
            temp_model = DescribeTerminalSettingsResponseBodyPasswordlessLoginConfig()
            self.passwordless_login_config = temp_model.from_map(m['PasswordlessLoginConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTerminalSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTerminalSettingsResponseBody = None,
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
            temp_model = DescribeTerminalSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTerminalSettingsRequestPasswordlessLoginConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # 免密功能开关
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ModifyTerminalSettingsRequest(TeaModel):
    def __init__(
        self,
        passwordless_login_config: ModifyTerminalSettingsRequestPasswordlessLoginConfig = None,
    ):
        # 免密登录配置
        # 
        # This parameter is required.
        self.passwordless_login_config = passwordless_login_config

    def validate(self):
        if self.passwordless_login_config:
            self.passwordless_login_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passwordless_login_config is not None:
            result['PasswordlessLoginConfig'] = self.passwordless_login_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordlessLoginConfig') is not None:
            temp_model = ModifyTerminalSettingsRequestPasswordlessLoginConfig()
            self.passwordless_login_config = temp_model.from_map(m['PasswordlessLoginConfig'])
        return self


class ModifyTerminalSettingsShrinkRequest(TeaModel):
    def __init__(
        self,
        passwordless_login_config_shrink: str = None,
    ):
        # 免密登录配置
        # 
        # This parameter is required.
        self.passwordless_login_config_shrink = passwordless_login_config_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.passwordless_login_config_shrink is not None:
            result['PasswordlessLoginConfig'] = self.passwordless_login_config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordlessLoginConfig') is not None:
            self.passwordless_login_config_shrink = m.get('PasswordlessLoginConfig')
        return self


class ModifyTerminalSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
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


class ModifyTerminalSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTerminalSettingsResponseBody = None,
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
            temp_model = ModifyTerminalSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


