# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddOrganizationMemberRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        caller_uac_account_id: str = None,
        namespace_id: str = None,
        org_id: str = None,
        org_role_code: str = None,
        spec_type: str = None,
    ):
        # The display name. If this parameter is not empty, the name field of the account is also updated.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The account information of the TokenPlan management platform.
        self.caller_uac_account_id = caller_uac_account_id
        # The product namespace ID. For the TokenPlan product, this field is fixed to namespace-1.
        self.namespace_id = namespace_id
        # The organization ID.
        # 
        # This parameter is required.
        self.org_id = org_id
        # The organization role code. Valid values: ORG_ADMIN and ORG_MEMBER. Default value: ORG_MEMBER.
        # 
        # This parameter is required.
        self.org_role_code = org_role_code
        # The seat specification.
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

        if self.caller_uac_account_id is not None:
            result['CallerUacAccountId'] = self.caller_uac_account_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.org_role_code is not None:
            result['OrgRoleCode'] = self.org_role_code

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('CallerUacAccountId') is not None:
            self.caller_uac_account_id = m.get('CallerUacAccountId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OrgRoleCode') is not None:
            self.org_role_code = m.get('OrgRoleCode')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        return self

