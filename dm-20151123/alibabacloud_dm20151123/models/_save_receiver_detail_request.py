# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveReceiverDetailRequest(DaraModel):
    def __init__(
        self,
        custom_detail: str = None,
        detail: str = None,
        owner_id: int = None,
        receiver_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.custom_detail = custom_detail
        # Content, supports uploading multiple recipients at once, with a limit of 500 records per upload. Each record is separated by {} and commas, example:
        # 
        # [{ },{ },{ }...], the format within {} is as follows:
        # 
        # [{"b":"birthday","e":"xxx@example.net","g":"gender","m":"mobile","n":"nickname","u":"name"}], when passing values, pass it as a string, not a list.
        # 
        # If a duplicate recipient address is inserted, it will return "ErrorCount": 1
        self.detail = detail
        self.owner_id = owner_id
        # Recipient list ID
        # 
        # This parameter is required.
        self.receiver_id = receiver_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_detail is not None:
            result['CustomDetail'] = self.custom_detail

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDetail') is not None:
            self.custom_detail = m.get('CustomDetail')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

