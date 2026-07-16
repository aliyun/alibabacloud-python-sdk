# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductRequest(DaraModel):
    def __init__(
        self,
        after: str = None,
        before: str = None,
        catalog_id: str = None,
        cust_space_id: str = None,
        fields: str = None,
        limit: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        waba_id: str = None,
    ):
        # The cursor that points to the start of the next page of results.
        self.after = after
        # The cursor that points to the end of the previous page of results.
        self.before = before
        # The catalog ID. You can get it from the Meta platform.
        # 
        # This parameter is required.
        self.catalog_id = catalog_id
        # The Space ID of the ISV sub-customer.
        self.cust_space_id = cust_space_id
        # A list of fields to return. Separate multiple fields with a comma (,).
        # For more information, see [Product fields](https://help.aliyun.com/document_detail/2579419.html).
        self.fields = fields
        # The number of items to return. Valid values: 1 to 1000.
        self.limit = limit
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The WhatsApp Business Account (WABA) ID.
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
        if self.after is not None:
            result['After'] = self.after

        if self.before is not None:
            result['Before'] = self.before

        if self.catalog_id is not None:
            result['CatalogId'] = self.catalog_id

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

        if self.waba_id is not None:
            result['WabaId'] = self.waba_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('Before') is not None:
            self.before = m.get('Before')

        if m.get('CatalogId') is not None:
            self.catalog_id = m.get('CatalogId')

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

        if m.get('WabaId') is not None:
            self.waba_id = m.get('WabaId')

        return self

