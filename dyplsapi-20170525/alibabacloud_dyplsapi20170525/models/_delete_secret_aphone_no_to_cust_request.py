# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecretAPhoneNoToCustRequest(DaraModel):
    def __init__(
        self,
        ano_white_group_id: int = None,
        owner_id: int = None,
        phone_no_a: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # A-number group ID.
        # 
        # This parameter is required.
        self.ano_white_group_id = ano_white_group_id
        self.owner_id = owner_id
        # A-number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ano_white_group_id is not None:
            result['ANoWhiteGroupId'] = self.ano_white_group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ANoWhiteGroupId') is not None:
            self.ano_white_group_id = m.get('ANoWhiteGroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

