# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetLoginPreferenceResponseBody(DaraModel):
    def __init__(
        self,
        login_preference: main_models.GetLoginPreferenceResponseBodyLoginPreference = None,
        password_policy: main_models.GetLoginPreferenceResponseBodyPasswordPolicy = None,
        request_id: str = None,
    ):
        self.login_preference = login_preference
        self.password_policy = password_policy
        self.request_id = request_id

    def validate(self):
        if self.login_preference:
            self.login_preference.validate()
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_preference is not None:
            result['LoginPreference'] = self.login_preference.to_map()

        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginPreference') is not None:
            temp_model = main_models.GetLoginPreferenceResponseBodyLoginPreference()
            self.login_preference = temp_model.from_map(m.get('LoginPreference'))

        if m.get('PasswordPolicy') is not None:
            temp_model = main_models.GetLoginPreferenceResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m.get('PasswordPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLoginPreferenceResponseBodyPasswordPolicy(DaraModel):
    def __init__(
        self,
        hard_expire: bool = None,
        max_login_attempts: int = None,
        max_password_age: int = None,
        max_password_length: int = None,
        min_password_length: int = None,
        password_not_contain_user_name: bool = None,
        require_lower_case_chars: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_upper_case_chars: bool = None,
    ):
        self.hard_expire = hard_expire
        self.max_login_attempts = max_login_attempts
        self.max_password_age = max_password_age
        self.max_password_length = max_password_length
        self.min_password_length = min_password_length
        self.password_not_contain_user_name = password_not_contain_user_name
        self.require_lower_case_chars = require_lower_case_chars
        self.require_numbers = require_numbers
        self.require_symbols = require_symbols
        self.require_upper_case_chars = require_upper_case_chars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire

        if self.max_login_attempts is not None:
            result['MaxLoginAttempts'] = self.max_login_attempts

        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age

        if self.max_password_length is not None:
            result['MaxPasswordLength'] = self.max_password_length

        if self.min_password_length is not None:
            result['MinPasswordLength'] = self.min_password_length

        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name

        if self.require_lower_case_chars is not None:
            result['RequireLowerCaseChars'] = self.require_lower_case_chars

        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers

        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols

        if self.require_upper_case_chars is not None:
            result['RequireUpperCaseChars'] = self.require_upper_case_chars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')

        if m.get('MaxLoginAttempts') is not None:
            self.max_login_attempts = m.get('MaxLoginAttempts')

        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')

        if m.get('MaxPasswordLength') is not None:
            self.max_password_length = m.get('MaxPasswordLength')

        if m.get('MinPasswordLength') is not None:
            self.min_password_length = m.get('MinPasswordLength')

        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')

        if m.get('RequireLowerCaseChars') is not None:
            self.require_lower_case_chars = m.get('RequireLowerCaseChars')

        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')

        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')

        if m.get('RequireUpperCaseChars') is not None:
            self.require_upper_case_chars = m.get('RequireUpperCaseChars')

        return self

class GetLoginPreferenceResponseBodyLoginPreference(DaraModel):
    def __init__(
        self,
        enable_password_login: bool = None,
    ):
        self.enable_password_login = enable_password_login

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_password_login is not None:
            result['EnablePasswordLogin'] = self.enable_password_login

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePasswordLogin') is not None:
            self.enable_password_login = m.get('EnablePasswordLogin')

        return self

