# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class SkuSaleInfoListQuery(DaraModel):
    def __init__(
        self,
        division_code: str = None,
        purchaser_id: str = None,
        sku_query_params: List[main_models.SkuQueryParam] = None,
    ):
        self.division_code = division_code
        # This parameter is required.
        self.purchaser_id = purchaser_id
        # This parameter is required.
        self.sku_query_params = sku_query_params

    def validate(self):
        if self.sku_query_params:
            for v1 in self.sku_query_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.division_code is not None:
            result['divisionCode'] = self.division_code

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        result['skuQueryParams'] = []
        if self.sku_query_params is not None:
            for k1 in self.sku_query_params:
                result['skuQueryParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('divisionCode') is not None:
            self.division_code = m.get('divisionCode')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        self.sku_query_params = []
        if m.get('skuQueryParams') is not None:
            for k1 in m.get('skuQueryParams'):
                temp_model = main_models.SkuQueryParam()
                self.sku_query_params.append(temp_model.from_map(k1))

        return self

