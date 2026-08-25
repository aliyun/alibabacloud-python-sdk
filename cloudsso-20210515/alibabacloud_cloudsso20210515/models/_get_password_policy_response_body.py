# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetPasswordPolicyResponseBody(DaraModel):
    def __init__(
        self,
        password_policy: main_models.GetPasswordPolicyResponseBodyPasswordPolicy = None,
        request_id: str = None,
    ):
        # The password policy.
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
        max_login_attempts: int = None,
        max_password_age: int = None,
        max_password_length: int = None,
        min_password_different_chars: int = None,
        min_password_length: int = None,
        password_not_contain_username: bool = None,
        password_reuse_prevention: int = None,
        require_lower_case_chars: bool = None,
        require_numbers: bool = None,
        require_symbols: bool = None,
        require_upper_case_chars: bool = None,
    ):
        # Indicates whether to disable logon after a password expires. Valid values:
        # 
        # *   true: disables logon after a password expires.
        # *   false: does not disable logon after a password expires.
        self.hard_expire = hard_expire
        # The number of password retries.
        # 
        # If wrong passwords are entered for the specified consecutive times, the account is locked for 1 hour.
        # 
        # Valid values: 0 to 32. The value 0 indicates that the number of password retries is not limited.
        self.max_login_attempts = max_login_attempts
        # The validity period of a password.
        # 
        # Valid values: 1 to 120. Unit: days.
        self.max_password_age = max_password_age
        # The maximum password length.
        self.max_password_length = max_password_length
        # The minimum number of different characters in a password.
        # 
        # The minimum value is 0, which indicates that the minimum number of different characters in a password is not limited. The maximum value is the value of the `MinPasswordLength` parameter.
        self.min_password_different_chars = min_password_different_chars
        # The minimum password length.
        # 
        # Valid values: 8 to 32 characters.
        self.min_password_length = min_password_length
        # Indicates whether to exclude the username from the password. Valid values:
        # 
        # *   true: A password cannot contain the username.
        # *   false: A password can contain the username.
        self.password_not_contain_username = password_not_contain_username
        # The policy for password history check.
        # 
        # The previous N passwords cannot be reused. Valid values of N: 0 to 24. The value 0 indicates that all historical passwords can be reused.
        # 
        # >  Passwords that are generated before January 5, 2024 are not counted as historical passwords.
        self.password_reuse_prevention = password_reuse_prevention
        # Indicates whether lowercase letters are required in a password. Valid values:
        # 
        # *   true: Lowercase letters are required in a password.
        # *   false: Lowercase letters are not required in a password.
        self.require_lower_case_chars = require_lower_case_chars
        # Indicates whether digits are required in a password. Valid values:
        # 
        # *   true: Digits are required in a password.
        # *   false: Digits are not required in a password.
        self.require_numbers = require_numbers
        # Indicates whether special characters are required in a password. Valid values:
        # 
        # *   true: Special characters are required in a password.
        # *   false: Special characters are not required in a password.
        self.require_symbols = require_symbols
        # Indicates whether uppercase letters are required in a password. Valid values:
        # 
        # *   true: Uppercase letters are required in a password.
        # *   false: Uppercase letters are not required in a password.
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

        if self.min_password_different_chars is not None:
            result['MinPasswordDifferentChars'] = self.min_password_different_chars

        if self.min_password_length is not None:
            result['MinPasswordLength'] = self.min_password_length

        if self.password_not_contain_username is not None:
            result['PasswordNotContainUsername'] = self.password_not_contain_username

        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention

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

        if m.get('MinPasswordDifferentChars') is not None:
            self.min_password_different_chars = m.get('MinPasswordDifferentChars')

        if m.get('MinPasswordLength') is not None:
            self.min_password_length = m.get('MinPasswordLength')

        if m.get('PasswordNotContainUsername') is not None:
            self.password_not_contain_username = m.get('PasswordNotContainUsername')

        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')

        if m.get('RequireLowerCaseChars') is not None:
            self.require_lower_case_chars = m.get('RequireLowerCaseChars')

        if m.get('RequireNumbers') is not None:
            self.require_numbers = m.get('RequireNumbers')

        if m.get('RequireSymbols') is not None:
            self.require_symbols = m.get('RequireSymbols')

        if m.get('RequireUpperCaseChars') is not None:
            self.require_upper_case_chars = m.get('RequireUpperCaseChars')

        return self

