# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckReplyToMailAddressRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        mail_address_id: int = None,
        owner_id: int = None,
        region: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Language.
        # 
        # en is English, and any other value or an empty value defaults to Chinese.
        self.lang = lang
        # Sender Address ID
        # 
        # This parameter is required.
        self.mail_address_id = mail_address_id
        self.owner_id = owner_id
        # Region
        self.region = region
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.mail_address_id is not None:
            result['MailAddressId'] = self.mail_address_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MailAddressId') is not None:
            self.mail_address_id = m.get('MailAddressId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

