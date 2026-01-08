# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMessengerPageShrinkRequest(DaraModel):
    def __init__(
        self,
        ad_account_ids_shrink: str = None,
        authentication_code: str = None,
        business_id: str = None,
        cust_space_id: str = None,
        owner_id: int = None,
        page_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.ad_account_ids_shrink = ad_account_ids_shrink
        # This parameter is required.
        self.authentication_code = authentication_code
        # This parameter is required.
        self.business_id = business_id
        # This parameter is required.
        self.cust_space_id = cust_space_id
        self.owner_id = owner_id
        # This parameter is required.
        self.page_id = page_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_account_ids_shrink is not None:
            result['AdAccountIds'] = self.ad_account_ids_shrink

        if self.authentication_code is not None:
            result['AuthenticationCode'] = self.authentication_code

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAccountIds') is not None:
            self.ad_account_ids_shrink = m.get('AdAccountIds')

        if m.get('AuthenticationCode') is not None:
            self.authentication_code = m.get('AuthenticationCode')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

