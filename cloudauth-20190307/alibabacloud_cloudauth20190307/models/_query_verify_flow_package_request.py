# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryVerifyFlowPackageRequest(DaraModel):
    def __init__(
        self,
        product_type: str = None,
    ):
        # Product type:
        # - **FINANCE_VERIFY**: Financial Grade Real Person Verification
        # - **SMART_VERIFY**: Enhanced Real Person Verification (discontinued)
        # - **FACE_VERIFY**: Real Person Verification (discontinued)
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

