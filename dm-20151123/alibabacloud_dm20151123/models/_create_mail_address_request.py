# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMailAddressRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        address_type: str = None,
        owner_id: int = None,
        reply_address: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sendtype: str = None,
    ):
        # The sender address.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The type of the address to create. Valid values:
        # EXTERNAL: The domain name of the address to create has not been created in this system.
        # INTERNAL: The domain name of the address to create has already been created in this system.
        self.address_type = address_type
        self.owner_id = owner_id
        # The reply-to address.
        self.reply_address = reply_address
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of email. Valid values:
        # 
        # - batch: batch email
        # 
        # - trigger: triggered email
        # 
        # This parameter is required.
        self.sendtype = sendtype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reply_address is not None:
            result['ReplyAddress'] = self.reply_address

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sendtype is not None:
            result['Sendtype'] = self.sendtype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReplyAddress') is not None:
            self.reply_address = m.get('ReplyAddress')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Sendtype') is not None:
            self.sendtype = m.get('Sendtype')

        return self

