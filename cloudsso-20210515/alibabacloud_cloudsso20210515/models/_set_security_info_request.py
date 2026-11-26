# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSecurityInfoRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        security_email: str = None,
        user_id: str = None,
        verify_type: str = None,
    ):
        # The directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The security email address of the user.
        # 
        # The value can be up to 64 characters in length, must conform to the standard email format, and cannot contain whitespace characters. The security email address of each user in the same directory must be unique. The uniqueness check is case-insensitive, but the original case is preserved when the address is saved.
        # 
        # This parameter is required.
        self.security_email = security_email
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The verification type for the security information. Valid values:
        # 
        # - SecurityEmail: security email address.
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.security_email is not None:
            result['SecurityEmail'] = self.security_email

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('SecurityEmail') is not None:
            self.security_email = m.get('SecurityEmail')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

