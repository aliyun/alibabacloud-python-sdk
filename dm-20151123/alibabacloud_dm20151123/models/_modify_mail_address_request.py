# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMailAddressRequest(DaraModel):
    def __init__(
        self,
        mail_address_id: int = None,
        owner_id: int = None,
        password: str = None,
        reply_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Sending address ID
        # 
        # This parameter is required.
        self.mail_address_id = mail_address_id
        self.owner_id = owner_id
        # - Length should be 10 to 20 characters, and must include numbers, uppercase letters, and lowercase letters.
        # 
        # - Must contain at least 2 digits, 2 uppercase letters, and 2 lowercase letters, and neither the digits nor the letters can consist of a single character repeated.
        # 
        # - Cannot be the same as the last set password.
        self.password = password
        # Reply address
        self.reply_address = reply_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

