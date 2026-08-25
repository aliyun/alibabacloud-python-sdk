# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserMFAAuthenticationSettingsRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
        user_mfaauthentication_settings: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The ID of the user.
        self.user_id = user_id
        # Specifies whether to enable MFA for the user. Valid values:
        # 
        # - Enabled: enables MFA for the user.
        # 
        # - Disabled: disables MFA for the user.
        self.user_mfaauthentication_settings = user_mfaauthentication_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_mfaauthentication_settings is not None:
            result['UserMFAAuthenticationSettings'] = self.user_mfaauthentication_settings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserMFAAuthenticationSettings') is not None:
            self.user_mfaauthentication_settings = m.get('UserMFAAuthenticationSettings')

        return self

