# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListModelTemplateResourceGroupRequest(DaraModel):
    def __init__(
        self,
        model_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_ids: List[str] = None,
    ):
        # The ID of the model group.
        # 
        # This parameter is required.
        self.model_template_id = model_template_id
        # The page number. Pages start from page 1. Both 0 and 1 return the same result.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of resource group IDs.
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        return self

