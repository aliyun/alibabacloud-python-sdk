# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApiMeteringRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        product_code: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.page_num = page_num
        self.product_code = product_code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.product_code is not None:
            result['productCode'] = self.product_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

