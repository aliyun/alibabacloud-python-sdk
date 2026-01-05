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
        # The time when the OTP message was delivered. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # *   If you leave the parameter empty, the current timestamp is specified by default.
        # *   If you specify the parameter, the timestamp must be greater than the message sending time and less than the current timestamp.
        self.conversion_time = conversion_time
        # Specifies whether customers replied to the OTP message. Valid values: true and false.
        # 
        # This parameter is required.
        self.delivered = delivered
        # The ID of the message.
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

