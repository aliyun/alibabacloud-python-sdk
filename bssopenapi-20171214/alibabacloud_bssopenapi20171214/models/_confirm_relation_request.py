# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfirmRelationRequest(DaraModel):
    def __init__(
        self,
        child_user_id: int = None,
        confirm_code: str = None,
        parent_user_id: int = None,
        permission_codes: List[str] = None,
        relation_id: int = None,
        relation_type: str = None,
        request_id: str = None,
    ):
        # The Alibaba Cloud UID of the linked account.
        self.child_user_id = child_user_id
        # The confirmation action. Valid values:
        # - child_agree: The linked account agrees.
        # - child_disagree: The linked account rejects.
        # - 主账号取消确认: The main account cancels the confirmation.
        # 
        # This parameter is required.
        self.confirm_code = confirm_code
        # The Alibaba Cloud UID of the main account.
        self.parent_user_id = parent_user_id
        # The permissions granted to the linked account. Valid values:
        # - SYNCHRONIZE_FINANCE_IDENTITY: Allows synchronizing the credit-based payment identity to the linked account.
        # - SYNCHRONIZE_FINANCE_DISCOUNT_POLICY_TO_TARGET: Allows synchronizing discounts to the linked account.
        # - FORBID_WITHDRAW_CASH: Prohibits the linked account from withdrawing cash from the balance.
        # - FORBID_MANAGE_INVOICE: Prohibits the linked account from managing invoices.
        # - CHECK_FINANCE_INFO: Allows requesting to view the account linking information.
        # - MANAGE_TARGET_INVOICE: Allows managing invoices of the target account.
        # - CHECK_TARGET_CONSUMPTION: Allows viewing the consumption information of the linked account.
        # 
        # This parameter is required.
        self.permission_codes = permission_codes
        # The relationship ID. You can obtain the value from the relationId field in the response of the QueryRelationList operation.
        self.relation_id = relation_id
        # The relationship type. Valid values: enterprise_group.
        self.relation_type = relation_type
        # The unique identifier of the request.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_user_id is not None:
            result['ChildUserId'] = self.child_user_id

        if self.confirm_code is not None:
            result['ConfirmCode'] = self.confirm_code

        if self.parent_user_id is not None:
            result['ParentUserId'] = self.parent_user_id

        if self.permission_codes is not None:
            result['PermissionCodes'] = self.permission_codes

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildUserId') is not None:
            self.child_user_id = m.get('ChildUserId')

        if m.get('ConfirmCode') is not None:
            self.confirm_code = m.get('ConfirmCode')

        if m.get('ParentUserId') is not None:
            self.parent_user_id = m.get('ParentUserId')

        if m.get('PermissionCodes') is not None:
            self.permission_codes = m.get('PermissionCodes')

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

