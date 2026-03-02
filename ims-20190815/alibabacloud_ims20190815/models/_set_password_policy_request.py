# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetPasswordPolicyRequest(DaraModel):
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
        # Specifies whether to prevent a RAM user from logging on after the password expires. Valid values:
        # 
        # - true: After the password expires, the RAM user cannot log on to the console. The password must be reset by the Alibaba Cloud account or a RAM user with administrative permissions before the RAM user can log on.
        # 
        # - false (default): After the password expires, the RAM user can change the password and then log on.
        self.hard_expire = hard_expire
        # The validity period of an initial password. An initial password is the password that is set when you create a RAM user or re-enable console logon.
        # 
        # Valid values: 0 to 90. Unit: days.
        # 
        # Default value: 14.
        # 
        # A value of 0 disables this feature.
        self.initial_password_age = initial_password_age
        self.intercept_risk_password_on_api = intercept_risk_password_on_api
        # The maximum number of consecutive logon failures that are allowed. If the number of failures is reached, the account is locked for one hour.
        # 
        # Valid values: 0 to 32.
        # 
        # Default value: 0. A value of 0 disables this feature.
        self.max_login_attemps = max_login_attemps
        # The validity period of a password.
        # 
        # Valid values: 0 to 1095. Unit: days.
        # 
        # Default value: 0. A value of 0 indicates that the password never expires.
        self.max_password_age = max_password_age
        # The minimum number of unique characters in a password.
        # 
        # Valid values: 0 to 8.
        # 
        # Default value: 0. A value of 0 indicates that no limit is imposed on the number of unique characters.
        self.minimum_password_different_character = minimum_password_different_character
        # The minimum length of the password.
        # 
        # Valid values: 8 to 32. Default value: 8.
        self.minimum_password_length = minimum_password_length
        # Specifies whether the password can contain the username. Valid values:
        # 
        # - true: The password cannot contain the username.
        # 
        # - false (default): The password can contain the username.
        self.password_not_contain_user_name = password_not_contain_user_name
        # The number of previous passwords that cannot be reused.
        # 
        # Valid values: 0 to 24.
        # 
        # Default value: 0. A value of 0 disables this feature.
        self.password_reuse_prevention = password_reuse_prevention
        # Specifies whether the password must contain lowercase letters. Valid values:
        # 
        # - true
        # 
        # - false (default)
        self.require_lowercase_characters = require_lowercase_characters
        # Specifies whether the password must contain digits. Valid values:
        # 
        # - true
        # 
        # - false (default)
        self.require_numbers = require_numbers
        # Specifies whether the password must contain symbols. Valid values:
        # 
        # - true
        # 
        # - false (default)
        self.require_symbols = require_symbols
        # Specifies whether the password must contain uppercase letters. Valid values:
        # 
        # - true
        # 
        # - false (default)
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

