# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class ProductSaleInfoListResult(DaraModel):
    def __init__(
        self,
        product_sale_infos: List[main_models.ProductSaleInfo] = None,
        request_id: str = None,
    ):
        self.product_sale_infos = product_sale_infos
        self.request_id = request_id

    def validate(self):
        if self.product_sale_infos:
            for v1 in self.product_sale_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['productSaleInfos'] = []
        if self.product_sale_infos is not None:
            for k1 in self.product_sale_infos:
                result['productSaleInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_sale_infos = []
        if m.get('productSaleInfos') is not None:
            for k1 in m.get('productSaleInfos'):
                temp_model = main_models.ProductSaleInfo()
                self.product_sale_infos.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

