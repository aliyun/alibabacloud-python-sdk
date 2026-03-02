# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccessKeyLastUsedRequest(DaraModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_principal_name: str = None,
    ):
        # This parameter is required.
        self.user_access_key_id = user_access_key_id
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

