# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchGrantRolesCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        role_ids: List[int] = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        self.role_ids = role_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.role_ids is not None:
            result['roleIds'] = self.role_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('roleIds') is not None:
            self.role_ids = m.get('roleIds')

        return self

