# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChatGroupParticipantsShrinkRequest(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_id: str = None,
        list_shrink: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.group_id = group_id
        self.list_shrink = list_shrink
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
        if self.business_number is not None:
            result['BusinessNumber'] = self.business_number

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.list_shrink is not None:
            result['List'] = self.list_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('List') is not None:
            self.list_shrink = m.get('List')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

