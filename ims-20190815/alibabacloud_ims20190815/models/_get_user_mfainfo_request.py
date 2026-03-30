# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserMFAInfoRequest(DaraModel):
    def __init__(
        self,
        user_principal_name: str = None,
    ):
        # The logon name of the RAM user. This parameter is differently set in the following scenarios:
        # 
        # *   If you use a RAM user to call this operation, this parameter can be left empty. If you do not specify this parameter, information about the MFA device that is bound to the RAM user is queried.
        # *   If you use an Alibaba Cloud account to call this operation, you must set this parameter to the logon name of the RAM user that you want to query.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

