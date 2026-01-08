# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListChatGroupRequest(DaraModel):
    def __init__(
        self,
        business_number: str = None,
        channel_type: str = None,
        cust_space_id: str = None,
        group_status: str = None,
        owner_id: int = None,
        page: main_models.ListChatGroupRequestPage = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subject: str = None,
    ):
        # This parameter is required.
        self.business_number = business_number
        self.channel_type = channel_type
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.group_status = group_status
        self.owner_id = owner_id
        # This parameter is required.
        self.page = page
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subject = subject

    def validate(self):
        if self.page:
            self.page.validate()

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

        if self.group_status is not None:
            result['GroupStatus'] = self.group_status

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page is not None:
            result['Page'] = self.page.to_map()

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

        if m.get('GroupStatus') is not None:
            self.group_status = m.get('GroupStatus')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            temp_model = main_models.ListChatGroupRequestPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

class ListChatGroupRequestPage(DaraModel):
    def __init__(
        self,
        index: int = None,
        size: int = None,
    ):
        # This parameter is required.
        self.index = index
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

