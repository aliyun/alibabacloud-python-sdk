# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetPasswordPolicyResponseBody(DaraModel):
    def __init__(
        self,
        password_policy: main_models.GetPasswordPolicyResponseBodyPasswordPolicy = None,
        request_id: str = None,
    ):
        # The password strength policy information.
        self.password_policy = password_policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.password_policy:
            self.password_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_policy is not None:
            result['PasswordPolicy'] = self.password_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordPolicy') is not None:
            temp_model = main_models.GetPasswordPolicyResponseBodyPasswordPolicy()
            self.password_policy = temp_model.from_map(m.get('PasswordPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPasswordPolicyResponseBodyPasswordPolicy(DaraModel):
    def __init__(
        self,
        hard_expire: bool = None,
        initial_password_age: int = None,
        intercept_risk_password_on_api: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        minimum_password_different_character: int = None,
        minimum_password_length: int = None,
        password_not_contain_user_name: bool = None,
        password_reuse_prevention: int = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_uppercase_characters: bool = None,
    ):
        # Indicates whether logon is restricted after the password expires.
        self.hard_expire = hard_expire
        # The validity period of the initial password.
        self.initial_password_age = initial_password_age
        # Indicates whether to block threat passwords when a password is set using OpenAPI.
        # 
        # Valid values:
        # 
        # - true: Threat passwords are blocked when you set a password using OpenAPI.
        # 
        # - false: Threat passwords are not blocked when you set a password using OpenAPI.
        # 
        # Default value: false
        self.intercept_risk_password_on_api = intercept_risk_password_on_api
        # The maximum number of logon attempts.
        self.max_login_attemps = max_login_attemps
        # The password validity period.
        self.max_password_age = max_password_age
        # The minimum number of different characters in the password.
        self.minimum_password_different_character = minimum_password_different_character
        # The minimum password length.
        self.minimum_password_length = minimum_password_length
        # Indicates whether the password must not contain the username.
        self.password_not_contain_user_name = password_not_contain_user_name
        # The password reuse prevention policy.
        self.password_reuse_prevention = password_reuse_prevention
        # Indicates whether the password must contain lowercase letters.
        self.require_lowercase_characters = require_lowercase_characters
        # Indicates whether the password must contain numbers.
        self.require_numbers = require_numbers
        # Indicates whether the password must contain symbols.
        self.require_symbols = require_symbols
        # Indicates whether the password must contain uppercase letters.
        self.require_uppercase_characters = require_uppercase_characters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hard_expire is not None:
            result['HardExpire'] = self.hard_expire

        if self.initial_password_age is not None:
            result['InitialPasswordAge'] = self.initial_password_age

        if self.intercept_risk_password_on_api is not None:
            result['InterceptRiskPasswordOnApi'] = self.intercept_risk_password_on_api

        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps

        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age

        if self.minimum_password_different_character is not None:
            result['MinimumPasswordDifferentCharacter'] = self.minimum_password_different_character

        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length

        if self.password_not_contain_user_name is not None:
            result['PasswordNotContainUserName'] = self.password_not_contain_user_name

        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention

        if self.require_lowercase_characters is not None:
            result['RequireLowercaseCharacters'] = self.require_lowercase_characters

        if self.require_numbers is not None:
            result['RequireNumbers'] = self.require_numbers

        if self.require_symbols is not None:
            result['RequireSymbols'] = self.require_symbols

        if self.require_uppercase_characters is not None:
            result['RequireUppercaseCharacters'] = self.require_uppercase_characters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HardExpire') is not None:
            self.hard_expire = m.get('HardExpire')

        if m.get('InitialPasswordAge') is not None:
            self.initial_password_age = m.get('InitialPasswordAge')

        if m.get('InterceptRiskPasswordOnApi') is not None:
            self.intercept_risk_password_on_api = m.get('InterceptRiskPasswordOnApi')

        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')

        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')

        if m.get('MinimumPasswordDifferentCharacter') is not None:
            self.minimum_password_different_character = m.get('MinimumPasswordDifferentCharacter')

        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')

        if m.get('PasswordNotContainUserName') is not None:
            self.password_not_contain_user_name = m.get('PasswordNotContainUserName')

        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')

        if m.get('RequireLowercaseCharacters') is not None:
            self.require_lowercase_characters = m.get('RequireLowercaseCharacters')

        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')

        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')

        if m.get('RequireUppercaseCharacters') is not None:
            self.require_uppercase_characters = m.get('RequireUppercaseCharacters')

        return self

