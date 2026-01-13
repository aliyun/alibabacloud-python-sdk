# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTaskCodesRequest(DaraModel):
    def __init__(
        self,
        gen_num: int = None,
        product_namespace: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.gen_num = gen_num
        # This parameter is required.
        self.product_namespace = product_namespace
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gen_num is not None:
            result['genNum'] = self.gen_num

        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('genNum') is not None:
            self.gen_num = m.get('genNum')

        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

