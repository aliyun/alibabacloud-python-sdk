# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class SkuSaleInfoListResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sku_sale_infos: List[main_models.SkuSaleInfo] = None,
    ):
        self.request_id = request_id
        self.sku_sale_infos = sku_sale_infos

    def validate(self):
        if self.sku_sale_infos:
            for v1 in self.sku_sale_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['skuSaleInfos'] = []
        if self.sku_sale_infos is not None:
            for k1 in self.sku_sale_infos:
                result['skuSaleInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.sku_sale_infos = []
        if m.get('skuSaleInfos') is not None:
            for k1 in m.get('skuSaleInfos'):
                temp_model = main_models.SkuSaleInfo()
                self.sku_sale_infos.append(temp_model.from_map(k1))

        return self

