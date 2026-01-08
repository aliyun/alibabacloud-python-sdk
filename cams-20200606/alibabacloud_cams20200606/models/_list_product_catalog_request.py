# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductCatalogRequest(DaraModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
        business_id: int = None,
        cust_space_id: str = None,
        fields: str = None,
        limit: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cursor that points to the end of the page of the returned data.
        self.after = after
        # The cursor that points to the beginning of the page of the returned data.
        self.before = before
        # The Business Manager ID.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The space ID of the user within the independent software vendor (ISV) account.
        self.cust_space_id = cust_space_id
        # The fields. Separate multiple fields with commas (,).
        # see  [catalog fields](https://help.aliyun.com/document_detail/2579419.html)
        self.fields = fields
        # The number of catalogs to be queried. Valid values: 1 to 1000.
        self.limit = limit
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
        if self.after is not None:
            result['After'] = self.after

        if self.before is not None:
            result['Before'] = self.before

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.fields is not None:
            result['Fields'] = self.fields

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('Before') is not None:
            self.before = m.get('Before')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

