# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetUserPasswordRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        generate_random_password: bool = None,
        password: str = None,
        require_password_reset_for_next_login: bool = None,
        user_id: str = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # Specifies whether to automatically generate a password. Valid values:
        # 
        # - True: The password is automatically generated.
        # - False (default): The password is manually specified.
        self.generate_random_password = generate_random_password
        # The new password.
        # 
        # Format: The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
        # 
        # Length: 8 to 32 characters.
        # 
        # > If GenerateRandomPassword is set to False, you must specify Password.
        self.password = password
        # Specifies whether the user must reset the password upon the next logon. Valid values:
        # 
        # - True: The user must reset the password.
        # - False (default): The user does not need to reset the password.
        self.require_password_reset_for_next_login = require_password_reset_for_next_login
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.generate_random_password is not None:
            result['GenerateRandomPassword'] = self.generate_random_password

        if self.password is not None:
            result['Password'] = self.password

        if self.require_password_reset_for_next_login is not None:
            result['RequirePasswordResetForNextLogin'] = self.require_password_reset_for_next_login

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('GenerateRandomPassword') is not None:
            self.generate_random_password = m.get('GenerateRandomPassword')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RequirePasswordResetForNextLogin') is not None:
            self.require_password_reset_for_next_login = m.get('RequirePasswordResetForNextLogin')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

