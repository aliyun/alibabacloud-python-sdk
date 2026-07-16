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
        # The recipient\\"s email address and template parameters, in an array format.
        self.custom_detail = custom_detail
        # The recipient details. You can upload up to 500 recipients in a single request. The value is a string in a JSON array format. Each object in the array represents a recipient. For example: \\`[{ },{ },{ }...]\\`. The format for each recipient object is \\`[{"b":"birthday","e":"xxx\\@example.net","g":"gender","m":"mobile","n":"nickname","u":"name"}]\\`. If you add a duplicate recipient address, the system returns \\`"ErrorCount": 1\\`.
        # 
        # The format is \\`[{ },{ },{ }...]\\`. The format of the content within each \\`{}\\` is as follows:
        # 
        # [{"b":"birthday","e":"xxx\\@example.net","g":"gender","m":"mobile","n":"nickname","u":"name"}]. Pass the value as a string, not a list.
        # 
        # Inserting a duplicate recipient address returns "ErrorCount": 1.
        self.detail = detail
        self.owner_id = owner_id
        # The ID of the recipient list.
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

