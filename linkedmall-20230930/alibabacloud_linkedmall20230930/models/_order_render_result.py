# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class OrderRenderResult(DaraModel):
    def __init__(
        self,
        can_sell: bool = None,
        delivery_info_list: List[main_models.DeliveryInfo] = None,
        ext_info: Dict[str, Any] = None,
        message: str = None,
        product_list: List[main_models.OrderProductResult] = None,
    ):
        self.can_sell = can_sell
        self.delivery_info_list = delivery_info_list
        self.ext_info = ext_info
        self.message = message
        self.product_list = product_list

    def validate(self):
        if self.delivery_info_list:
            for v1 in self.delivery_info_list:
                 if v1:
                    v1.validate()
        if self.product_list:
            for v1 in self.product_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        result['deliveryInfoList'] = []
        if self.delivery_info_list is not None:
            for k1 in self.delivery_info_list:
                result['deliveryInfoList'].append(k1.to_map() if k1 else None)

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        if self.message is not None:
            result['message'] = self.message

        result['productList'] = []
        if self.product_list is not None:
            for k1 in self.product_list:
                result['productList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        self.delivery_info_list = []
        if m.get('deliveryInfoList') is not None:
            for k1 in m.get('deliveryInfoList'):
                temp_model = main_models.DeliveryInfo()
                self.delivery_info_list.append(temp_model.from_map(k1))

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.product_list = []
        if m.get('productList') is not None:
            for k1 in m.get('productList'):
                temp_model = main_models.OrderProductResult()
                self.product_list.append(temp_model.from_map(k1))

        return self

