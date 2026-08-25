# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserMFAAuthenticationSettingsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_mfaauthentication_settings: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether MFA is enabled for the user. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.user_mfaauthentication_settings = user_mfaauthentication_settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_mfaauthentication_settings is not None:
            result['UserMFAAuthenticationSettings'] = self.user_mfaauthentication_settings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserMFAAuthenticationSettings') is not None:
            self.user_mfaauthentication_settings = m.get('UserMFAAuthenticationSettings')

        return self

