# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTopRiskyResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        resource_category_id: str = None,
        resource_owner_ids_shrink: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource category.
        self.resource_category_id = resource_category_id
        self.resource_owner_ids_shrink = resource_owner_ids_shrink
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_category_id is not None:
            result['ResourceCategoryId'] = self.resource_category_id

        if self.resource_owner_ids_shrink is not None:
            result['ResourceOwnerIds'] = self.resource_owner_ids_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCategoryId') is not None:
            self.resource_category_id = m.get('ResourceCategoryId')

        if m.get('ResourceOwnerIds') is not None:
            self.resource_owner_ids_shrink = m.get('ResourceOwnerIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

