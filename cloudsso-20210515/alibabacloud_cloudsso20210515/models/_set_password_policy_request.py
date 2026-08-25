# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetPasswordPolicyRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        max_login_attempts: int = None,
        max_password_age: int = None,
        min_password_different_chars: int = None,
        min_password_length: int = None,
        password_not_contain_username: bool = None,
        password_reuse_prevention: int = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The number of password retries.
        # 
        # If you enter wrong passwords for the specified consecutive times, the account is locked for 1 hour.
        # 
        # Valid values: 0 to 32. The value 0 specifies that the number of password retries is not limited.
        self.max_login_attempts = max_login_attempts
        # The validity period of a password.
        # 
        # Valid values: 1 to 120. Unit: days.
        self.max_password_age = max_password_age
        # The minimum number of unique characters in a password.
        # 
        # The minimum value is 0, which specifies that the minimum number of unique characters in a password is not limited. The maximum value is the value of the `MinPasswordLength` parameter.
        self.min_password_different_chars = min_password_different_chars
        # The minimum password length.
        # 
        # Valid values: 8 to 32 characters.
        self.min_password_length = min_password_length
        # Specifies whether a password can contain the username. Valid value:
        # 
        # *   true: A password cannot contain the username.
        # *   false: A password can contain the username.
        self.password_not_contain_username = password_not_contain_username
        # The policy for password history check.
        # 
        # The previous N passwords cannot be reused. Valid values of N: 0 to 24. The value 0 specifies that all historical passwords can be reused.
        # 
        # >  Passwords that are generated before January 5, 2024 are not counted as historical passwords.
        self.password_reuse_prevention = password_reuse_prevention

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.max_login_attempts is not None:
            result['MaxLoginAttempts'] = self.max_login_attempts

        if self.max_password_age is not None:
            result['MaxPasswordAge'] = self.max_password_age

        if self.min_password_different_chars is not None:
            result['MinPasswordDifferentChars'] = self.min_password_different_chars

        if self.min_password_length is not None:
            result['MinPasswordLength'] = self.min_password_length

        if self.password_not_contain_username is not None:
            result['PasswordNotContainUsername'] = self.password_not_contain_username

        if self.password_reuse_prevention is not None:
            result['PasswordReusePrevention'] = self.password_reuse_prevention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MaxLoginAttempts') is not None:
            self.max_login_attempts = m.get('MaxLoginAttempts')

        if m.get('MaxPasswordAge') is not None:
            self.max_password_age = m.get('MaxPasswordAge')

        if m.get('MinPasswordDifferentChars') is not None:
            self.min_password_different_chars = m.get('MinPasswordDifferentChars')

        if m.get('MinPasswordLength') is not None:
            self.min_password_length = m.get('MinPasswordLength')

        if m.get('PasswordNotContainUsername') is not None:
            self.password_not_contain_username = m.get('PasswordNotContainUsername')

        if m.get('PasswordReusePrevention') is not None:
            self.password_reuse_prevention = m.get('PasswordReusePrevention')

        return self

