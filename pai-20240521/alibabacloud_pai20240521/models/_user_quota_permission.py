# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UserQuotaPermission(DaraModel):
    def __init__(
        self,
        permissions: List[str] = None,
        quota_id: str = None,
    ):
        self.permissions = permissions
        self.quota_id = quota_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permissions is not None:
            result['Permissions'] = self.permissions

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        return self

