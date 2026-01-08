# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomAudienceShrinkRequest(DaraModel):
    def __init__(
        self,
        ad_account_id: str = None,
        cust_space_id: str = None,
        custom_audience_id: str = None,
        custom_audience_name: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        page_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token_type: str = None,
    ):
        self.ad_account_id = ad_account_id
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.custom_audience_id = custom_audience_id
        self.custom_audience_name = custom_audience_name
        self.owner_id = owner_id
        # This parameter is required.
        self.page_shrink = page_shrink
        # This parameter is required.
        self.page_id = page_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_id is not None:
            result['AdAccountId'] = self.ad_account_id

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.custom_audience_id is not None:
            result['CustomAudienceId'] = self.custom_audience_id

        if self.custom_audience_name is not None:
            result['CustomAudienceName'] = self.custom_audience_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.token_type is not None:
            result['TokenType'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountId') is not None:
            self.ad_account_id = m.get('AdAccountId')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustomAudienceId') is not None:
            self.custom_audience_id = m.get('CustomAudienceId')

        if m.get('CustomAudienceName') is not None:
            self.custom_audience_name = m.get('CustomAudienceName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')

        return self

