# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSecurityInfoPreferenceRequest(DaraModel):
    def __init__(
        self,
        allow_user_manage_security_email: bool = None,
        directory_id: str = None,
    ):
        # Specifies whether to allow CloudSSO users in the directory to manage their security email addresses in the CloudSSO user portal, including setting, modifying, and deleting security email addresses, and sending verification emails. Valid values:
        # 
        # - true: allowed.
        # - false: not allowed.
        # 
        # This parameter is required.
        self.allow_user_manage_security_email = allow_user_manage_security_email
        # The directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_user_manage_security_email is not None:
            result['AllowUserManageSecurityEmail'] = self.allow_user_manage_security_email

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUserManageSecurityEmail') is not None:
            self.allow_user_manage_security_email = m.get('AllowUserManageSecurityEmail')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        return self

