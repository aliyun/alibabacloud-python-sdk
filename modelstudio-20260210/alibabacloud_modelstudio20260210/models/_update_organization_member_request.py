# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateOrganizationMemberRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        new_role_code: str = None,
    ):
        self.account_ids = account_ids
        # This parameter is required.
        self.new_role_code = new_role_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.new_role_code is not None:
            result['NewRoleCode'] = self.new_role_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('NewRoleCode') is not None:
            self.new_role_code = m.get('NewRoleCode')

        return self

