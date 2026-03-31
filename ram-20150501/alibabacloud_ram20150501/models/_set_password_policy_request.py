# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetPasswordPolicyRequest(DaraModel):
    def __init__(
        self,
        hard_expiry: bool = None,
        max_login_attemps: int = None,
        max_password_age: int = None,
        minimum_password_length: int = None,
        password_reuse_prevention: int = None,
        require_lowercase_characters: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_uppercase_characters: bool = None,
    ):
        # Specifies whether a password will expire. Valid values: `true` and `false`. Default value: `false`. If you leave this parameter unspecified, the default value false is used.
        # 
        # *   If you set this parameter to `true`, the Alibaba Cloud account to which the RAM users belong must reset the passwords before the RAM users can log on to the Alibaba Cloud Management Console.
        # *   If you set this parameter to `false`, the RAM users can change the passwords after the passwords expire and then log on to the Alibaba Cloud Management Console.
        self.hard_expiry = hard_expiry
        # The maximum number of permitted logon attempts within one hour. The number of logon attempts is reset to zero if a RAM user changes the password.
        self.max_login_attemps = max_login_attemps
        # The number of days for which a password is valid. If you reset a password, the password validity period restarts. Default value: 0. The default value indicates that the password never expires.
        self.max_password_age = max_password_age
        # The minimum number of characters in a password.
        # 
        # Valid values: 8 to 32. Default value: 8.
        self.minimum_password_length = minimum_password_length
        # The number of previous passwords that a RAM user is prevented from reusing. Default value: 0. The default value indicates that the RAM user can reuse previous passwords.
        self.password_reuse_prevention = password_reuse_prevention
        # Specifies whether a password must contain one or more lowercase letters.
        self.require_lowercase_characters = require_lowercase_characters
        # Specifies whether a password must contain one or more digits.
        self.require_numbers = require_numbers
        # Specifies whether a password must contain one or more special characters.
        self.require_symbols = require_symbols
        # Specifies whether a password must contain one or more uppercase letters.
        self.require_uppercase_characters = require_uppercase_characters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hard_expiry is not None:
            result['HardExpiry'] = self.hard_expiry

        if self.max_login_attemps is not None:
            result['MaxLoginAttemps'] = self.max_login_attemps

        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age

        if self.minimum_password_length is not None:
            result['MinimumPasswordLength'] = self.minimum_password_length

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
        if m.get('HardExpiry') is not None:
            self.hard_expiry = m.get('HardExpiry')

        if m.get('MaxLoginAttemps') is not None:
            self.max_login_attemps = m.get('MaxLoginAttemps')

        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')

        if m.get('MinimumPasswordLength') is not None:
            self.minimum_password_length = m.get('MinimumPasswordLength')

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

