# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserRequest(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
        wn_account_id: str = None,
        wn_user_id: str = None,
    ):
        # The ID of the tenant to which the task belongs.
        self.tenant_id = tenant_id
        # The WINNEXO logon account. This is a unique identifier and cannot be empty.
        self.wn_account_id = wn_account_id
        # The WINNEXO platform user ID. Specify either this parameter or accountId.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.wn_account_id is not None:
            result['wnAccountId'] = self.wn_account_id

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('wnAccountId') is not None:
            self.wn_account_id = m.get('wnAccountId')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

