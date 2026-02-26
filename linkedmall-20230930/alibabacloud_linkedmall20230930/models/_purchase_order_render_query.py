# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class PurchaseOrderRenderQuery(DaraModel):
    def __init__(
        self,
        buyer_id: str = None,
        delivery_address: main_models.AddressInfo = None,
        ext_info: Dict[str, Any] = None,
        product_list: List[main_models.OrderRenderProductDTO] = None,
    ):
        # This parameter is required.
        self.buyer_id = buyer_id
        # This parameter is required.
        self.delivery_address = delivery_address
        self.ext_info = ext_info
        # This parameter is required.
        self.product_list = product_list

    def validate(self):
        if self.delivery_address:
            self.delivery_address.validate()
        if self.product_list:
            for v1 in self.product_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id

        if self.delivery_address is not None:
            result['deliveryAddress'] = self.delivery_address.to_map()

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        result['productList'] = []
        if self.product_list is not None:
            for k1 in self.product_list:
                result['productList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')

        if m.get('deliveryAddress') is not None:
            temp_model = main_models.AddressInfo()
            self.delivery_address = temp_model.from_map(m.get('deliveryAddress'))

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        self.product_list = []
        if m.get('productList') is not None:
            for k1 in m.get('productList'):
                temp_model = main_models.OrderRenderProductDTO()
                self.product_list.append(temp_model.from_map(k1))

        return self

