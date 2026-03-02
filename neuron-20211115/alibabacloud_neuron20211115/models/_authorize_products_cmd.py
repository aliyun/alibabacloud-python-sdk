# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeProductsCmd(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        product_ids: List[int] = None,
    ):
        self.company_id = company_id
        self.product_ids = product_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.product_ids is not None:
            result['productIds'] = self.product_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('productIds') is not None:
            self.product_ids = m.get('productIds')

        return self

