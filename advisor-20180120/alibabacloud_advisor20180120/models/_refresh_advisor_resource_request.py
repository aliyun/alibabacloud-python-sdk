# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshAdvisorResourceRequest(DaraModel):
    def __init__(
        self,
        product: str = None,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.product = product
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product is not None:
            result['Product'] = self.product

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

