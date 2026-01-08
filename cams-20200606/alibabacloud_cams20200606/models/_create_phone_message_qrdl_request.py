# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePhoneMessageQrdlRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        generate_qr_image: str = None,
        owner_id: int = None,
        phone_number: str = None,
        prefilled_message: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.generate_qr_image = generate_qr_image
        self.owner_id = owner_id
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.prefilled_message = prefilled_message
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.generate_qr_image is not None:
            result['GenerateQrImage'] = self.generate_qr_image

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.prefilled_message is not None:
            result['PrefilledMessage'] = self.prefilled_message

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('GenerateQrImage') is not None:
            self.generate_qr_image = m.get('GenerateQrImage')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PrefilledMessage') is not None:
            self.prefilled_message = m.get('PrefilledMessage')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

