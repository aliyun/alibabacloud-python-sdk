# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmsConversionIntlRequest(DaraModel):
    def __init__(
        self,
        conversion_time: int = None,
        delivered: bool = None,
        message_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The timestamp at which the message reached the recipient. Must be a Unix timestamp, expressed as a long integer in milliseconds.
        # 
        # - If this field is not specified: defaults to the current timestamp.
        # 
        # - If this field is specified: the timestamp must be greater than the send time and less than the current timestamp.
        self.conversion_time = conversion_time
        # Set to true if your user replied to the message you sent. Otherwise, set to false.
        # 
        # This parameter is required.
        self.delivered = delivered
        # Message ID.
        # 
        # This parameter is required.
        self.message_id = message_id
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
        if self.conversion_time is not None:
            result['ConversionTime'] = self.conversion_time

        if self.delivered is not None:
            result['Delivered'] = self.delivered

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversionTime') is not None:
            self.conversion_time = m.get('ConversionTime')

        if m.get('Delivered') is not None:
            self.delivered = m.get('Delivered')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

