# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateCategoryProductsRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        product_ids: List[str] = None,
    ):
        # The operation type for the bulk operation. This parameter specifies whether to add the API products specified by productIds to the category or remove them from the category. The valid values are not declared in the API definition.
        self.action = action
        # The list of API product IDs to be processed. Each element is the primary ID of an API product resource.
        self.product_ids = product_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.product_ids is not None:
            result['productIds'] = self.product_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('productIds') is not None:
            self.product_ids = m.get('productIds')

        return self

