# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccountWebhookRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        http_flag: str = None,
        owner_id: int = None,
        queue_flag: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status_callback_url: str = None,
    ):
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # Specifies whether to use HTTP callbacks to receive message receipts. Valid values:
        # 
        # *   Y: indicates that HTTP callbacks are used to receive receipts.
        # *   N: indicates that HTTP callbacks are not used to receive receipts.
        self.http_flag = http_flag
        self.owner_id = owner_id
        # Specifies whether to use Message Service (MNS) queues to receive receipts. Valid values:
        # 
        # *   Y: indicates that MNS queues are used to receive receipts.
        # *   N: indicates that MNS queues are not used to receive receipts.
        self.queue_flag = queue_flag
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The callback URL to which status reports are sent by using HTTP callbacks.
        self.status_callback_url = status_callback_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.http_flag is not None:
            result['HttpFlag'] = self.http_flag

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.queue_flag is not None:
            result['QueueFlag'] = self.queue_flag

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status_callback_url is not None:
            result['StatusCallbackUrl'] = self.status_callback_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('HttpFlag') is not None:
            self.http_flag = m.get('HttpFlag')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueueFlag') is not None:
            self.queue_flag = m.get('QueueFlag')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StatusCallbackUrl') is not None:
            self.status_callback_url = m.get('StatusCallbackUrl')

        return self

