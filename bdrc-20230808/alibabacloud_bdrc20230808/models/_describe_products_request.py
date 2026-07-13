# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeProductsRequest(DaraModel):
    def __init__(
        self,
        product_type: str = None,
        resource_category_id: str = None,
        resource_owner_ids: List[int] = None,
        resource_region_id: str = None,
    ):
        # The product type of the resource. If you omit this parameter, the API returns resources of all product types. For example, specify `oss` to query resources from Object Storage Service.
        self.product_type = product_type
        # The resource category ID.
        self.resource_category_id = resource_category_id
        # A list of resource owner IDs for cross-account resource queries. If you omit this parameter, the API returns resources from the current account.
        self.resource_owner_ids = resource_owner_ids
        # The ID of the resource\\"s region. If you omit this parameter, the API returns resources from all regions.
        self.resource_region_id = resource_region_id

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

        if self.resource_owner_ids is not None:
            result['ResourceOwnerIds'] = self.resource_owner_ids

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceOwnerIds') is not None:
            self.resource_owner_ids = m.get('ResourceOwnerIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        return self

