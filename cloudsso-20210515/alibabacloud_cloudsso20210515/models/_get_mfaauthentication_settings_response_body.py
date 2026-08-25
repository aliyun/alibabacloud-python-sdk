# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMFAAuthenticationSettingsResponseBody(DaraModel):
    def __init__(
        self,
        mfaauthentication_advance_settings: str = None,
        request_id: str = None,
    ):
        # Indicates whether MFA is enabled for all users. Valid values:
        # 
        # *   Enabled: MFA is enabled for all users.
        # *   Byuser: User-specific settings are applied.
        # *   Disabled: MFA is disabled for all users.
        self.mfaauthentication_advance_settings = mfaauthentication_advance_settings
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mfaauthentication_advance_settings is not None:
            result['MFAAuthenticationAdvanceSettings'] = self.mfaauthentication_advance_settings

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MFAAuthenticationAdvanceSettings') is not None:
            self.mfaauthentication_advance_settings = m.get('MFAAuthenticationAdvanceSettings')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

