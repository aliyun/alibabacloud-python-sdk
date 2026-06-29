# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddOrganizationMemberRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        org_role_code: str = None,
        spec_type: str = None,
    ):
        # The display name. If this parameter is not empty, the name field of the account is updated synchronously.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The organization role code. Only ORG_ADMIN or ORG_MEMBER is allowed. Default value: ORG_MEMBER.
        # 
        # This parameter is required.
        self.org_role_code = org_role_code
        # The seat specification. Valid values:
        # 
        # - standard: standard seat.
        # - pro: premium seat.
        # - max: exclusive seat.
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.org_role_code is not None:
            result['OrgRoleCode'] = self.org_role_code

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('OrgRoleCode') is not None:
            self.org_role_code = m.get('OrgRoleCode')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        return self

