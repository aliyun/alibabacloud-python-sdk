# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FlowRebindPhoneRequest(DaraModel):
    def __init__(
        self,
        channel_code: str = None,
        channel_type: str = None,
        flow_code: str = None,
        flow_version: str = None,
        owner_id: int = None,
        phone_numbers: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # Message channel code
        # 
        # This parameter is required.
        self.channel_code = channel_code
        # Message channel type
        # 
        # This parameter is required.
        self.channel_type = channel_type
        # Flow code.
        # 
        # This parameter is required.
        self.flow_code = flow_code
        # Flow version
        self.flow_version = flow_version
        self.owner_id = owner_id
        # Phone numbers or PageIds under the channel instance, etc.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # WABA account ID, or PageId for other channel types, etc.
        # 
        # This parameter is required.
        self.waba_id = waba_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.flow_code is not None:
            result['FlowCode'] = self.flow_code

        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.waba_id is not None:
            result['WabaId'] = self.waba_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('FlowCode') is not None:
            self.flow_code = m.get('FlowCode')

        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')

        return self

