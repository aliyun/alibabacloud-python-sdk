# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDeveloperRoleRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        company_id: int = None,
        platform: str = None,
        role_name: str = None,
    ):
        self.account_id = account_id
        self.company_id = company_id
        self.platform = platform
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.platform is not None:
            result['platform'] = self.platform

        if self.role_name is not None:
            result['roleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        return self

