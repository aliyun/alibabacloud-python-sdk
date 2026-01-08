# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateChatGroupRequest(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        description: str = None,
        group_id: str = None,
        owner_id: int = None,
        profile_picture_file: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.description = description
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        self.profile_picture_file = profile_picture_file
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject

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

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.profile_picture_file is not None:
            result['ProfilePictureFile'] = self.profile_picture_file

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.subject is not None:
            result['Subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessNumber') is not None:
            self.business_number = m.get('BusinessNumber')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProfilePictureFile') is not None:
            self.profile_picture_file = m.get('ProfilePictureFile')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

