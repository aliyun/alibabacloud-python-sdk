# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProductDataRedundancyTypeStatShrinkRequest(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        resource_category_id: str = None,
        resource_owner_ids_shrink: str = None,
    ):
        # The type of the cloud service.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The resource category ID.
        self.resource_category_id = resource_category_id
        self.resource_owner_ids_shrink = resource_owner_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        if self.resource_owner_ids_shrink is not None:
            result['ResourceOwnerIds'] = self.resource_owner_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceOwnerIds') is not None:
            self.resource_owner_ids_shrink = m.get('ResourceOwnerIds')

        return self

