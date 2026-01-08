# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindDmAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        account_code: str = None,
        cust_space_id: str = None,
        extend_attr_shrink: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.account_code = account_code
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.extend_attr_shrink = extend_attr_shrink
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_code is not None:
            result['AccountCode'] = self.account_code

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.extend_attr_shrink is not None:
            result['ExtendAttr'] = self.extend_attr_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCode') is not None:
            self.account_code = m.get('AccountCode')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('ExtendAttr') is not None:
            self.extend_attr_shrink = m.get('ExtendAttr')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

