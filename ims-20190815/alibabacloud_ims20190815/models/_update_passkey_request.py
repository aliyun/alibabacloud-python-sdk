# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePasskeyRequest(DaraModel):
    def __init__(
        self,
        passkey_id: str = None,
        passkey_name: str = None,
        user_principal_name: str = None,
    ):
        # The ID of the passkey.
        self.passkey_id = passkey_id
        # The name of the passkey.
        self.passkey_name = passkey_name
        # The logon name of the Resource Access Management (RAM) user.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passkey_id is not None:
            result['PasskeyId'] = self.passkey_id

        if self.passkey_name is not None:
            result['PasskeyName'] = self.passkey_name

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasskeyId') is not None:
            self.passkey_id = m.get('PasskeyId')

        if m.get('PasskeyName') is not None:
            self.passkey_name = m.get('PasskeyName')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

