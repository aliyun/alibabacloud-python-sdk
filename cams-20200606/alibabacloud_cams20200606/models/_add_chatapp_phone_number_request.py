# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddChatappPhoneNumberRequest(DaraModel):
    def __init__(
        self,
        cc: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        phone_number: str = None,
        pre_validate_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        verified_name: str = None,
    ):
        # You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        # 
        # This parameter is required.
        self.cc = cc
        # Adds a phone number for a WhatsApp Business account (WABA).
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # AddChatappPhoneNumber
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # cams:ChatappPhoneNumberRegister
        self.pre_validate_id = pre_validate_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Private
        # 
        # This parameter is required.
        self.verified_name = verified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc is not None:
            result['Cc'] = self.cc

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.pre_validate_id is not None:
            result['PreValidateId'] = self.pre_validate_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.verified_name is not None:
            result['VerifiedName'] = self.verified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            self.cc = m.get('Cc')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PreValidateId') is not None:
            self.pre_validate_id = m.get('PreValidateId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VerifiedName') is not None:
            self.verified_name = m.get('VerifiedName')

        return self

