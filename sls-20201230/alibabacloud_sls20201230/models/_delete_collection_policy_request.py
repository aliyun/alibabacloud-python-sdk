# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCollectionPolicyRequest(DaraModel):
    def __init__(
        self,
        data_code: str = None,
        product_code: str = None,
    ):
        self.data_code = data_code
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_code is not None:
            result['dataCode'] = self.data_code

        if self.product_code is not None:
            result['productCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataCode') is not None:
            self.data_code = m.get('dataCode')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        return self

