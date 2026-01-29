# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddAccountRelationRequest(DaraModel):
    def __init__(
        self,
        child_nick: str = None,
        child_user_id: int = None,
        parent_user_id: int = None,
        permission_codes: List[str] = None,
        relation_type: str = None,
        request_id: str = None,
        role_codes: List[str] = None,
    ):
        # The display name of the member. This helps clarify the scenario in which the account is used.
        self.child_nick = child_nick
        # The ID of the Alibaba Cloud account that is used as the member.
        # 
        # This parameter is required.
        self.child_user_id = child_user_id
        # The ID of the Alibaba Cloud account that is used as the management account.
        # 
        # This parameter is required.
        self.parent_user_id = parent_user_id
        # The permissions that can be granted to the member. Valid values:
        # 
        # *   SYNCHRONIZE_FINANCE_IDENTITY: allows the credit control identity to be shared with the member.
        # *   SYNCHRONIZE_FINANCE_DISCOUNT_POLICY_TO_TARGET: allows the discount policy to be shared with the member.
        # *   FORBID_WITHDRAW_CASH: does not allow the member to withdraw the balance.
        # *   FORBID_MANAGE_INVOICE: does not allow the member to manage invoices.
        # *   CHECK_FINANCE_INFO: requests to view information about the financial relationship.
        # *   MANAGE_TARGET_INVOICE: allows the member to manage invoices.
        # *   CHECK_TARGET_CONSUMPTION: allows the member to view the bills.
        # 
        # The params[PermissionCodes, RoleCodes] can not be null at the same time.
        self.permission_codes = permission_codes
        # The type of the financial relationship. Set the value to enterprise_group.
        # 
        # This parameter is required.
        self.relation_type = relation_type
        # The unique ID of the request. The ID is used to mark a request and troubleshoot a problem.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The roles that can be assigned to the member. Set the value to trusteeship.
        self.role_codes = role_codes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_nick is not None:
            result['ChildNick'] = self.child_nick

        if self.child_user_id is not None:
            result['ChildUserId'] = self.child_user_id

        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id

        if self.permission_codes is not None:
            result['PermissionCodes'] = self.permission_codes

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_codes is not None:
            result['RoleCodes'] = self.role_codes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildNick') is not None:
            self.child_nick = m.get('ChildNick')

        if m.get('ChildUserId') is not None:
            self.child_user_id = m.get('ChildUserId')

        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')

        if m.get('PermissionCodes') is not None:
            self.permission_codes = m.get('PermissionCodes')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleCodes') is not None:
            self.role_codes = m.get('RoleCodes')

        return self

