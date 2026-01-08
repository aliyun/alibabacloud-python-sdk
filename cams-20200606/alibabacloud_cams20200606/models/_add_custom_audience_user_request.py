# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class AddCustomAudienceUserRequest(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        batch_last_flag: bool = None,
        cust_space_id: str = None,
        custom_audience_id: str = None,
        estimated_num_total: int = None,
        owner_id: int = None,
        page_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        users: List[main_models.AddCustomAudienceUserRequestUsers] = None,
    ):
        # This parameter is required.
        self.ad_account_id = ad_account_id
        self.batch_last_flag = batch_last_flag
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # This parameter is required.
        self.custom_audience_id = custom_audience_id
        self.estimated_num_total = estimated_num_total
        self.owner_id = owner_id
        # This parameter is required.
        self.page_id = page_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.batch_last_flag is not None:
            result['BatchLastFlag'] = self.batch_last_flag

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.custom_audience_id is not None:
            result['CustomAudienceId'] = self.custom_audience_id

        if self.estimated_num_total is not None:
            result['EstimatedNumTotal'] = self.estimated_num_total

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('BatchLastFlag') is not None:
            self.batch_last_flag = m.get('BatchLastFlag')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustomAudienceId') is not None:
            self.custom_audience_id = m.get('CustomAudienceId')

        if m.get('EstimatedNumTotal') is not None:
            self.estimated_num_total = m.get('EstimatedNumTotal')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.AddCustomAudienceUserRequestUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class AddCustomAudienceUserRequestUsers(DaraModel):
    def __init__(
        self,
        email: str = None,
        phone: str = None,
    ):
        self.email = email
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.phone is not None:
            result['Phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        return self

