# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class PurchaseOrderRenderResult(DaraModel):
    def __init__(
        self,
        address_list: List[main_models.AddressInfo] = None,
        can_sell: bool = None,
        ext_info: Dict[str, Any] = None,
        message: str = None,
        order_list: List[main_models.OrderRenderResult] = None,
        request_id: str = None,
        unsellable_order_list: List[main_models.OrderRenderResult] = None,
    ):
        self.address_list = address_list
        self.can_sell = can_sell
        self.ext_info = ext_info
        self.message = message
        self.order_list = order_list
        self.request_id = request_id
        self.unsellable_order_list = unsellable_order_list

    def validate(self):
        if self.address_list:
            for v1 in self.address_list:
                 if v1:
                    v1.validate()
        if self.order_list:
            for v1 in self.order_list:
                 if v1:
                    v1.validate()
        if self.unsellable_order_list:
            for v1 in self.unsellable_order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['addressList'] = []
        if self.address_list is not None:
            for k1 in self.address_list:
                result['addressList'].append(k1.to_map() if k1 else None)

        if self.can_sell is not None:
            result['canSell'] = self.can_sell

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        if self.message is not None:
            result['message'] = self.message

        result['orderList'] = []
        if self.order_list is not None:
            for k1 in self.order_list:
                result['orderList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['unsellableOrderList'] = []
        if self.unsellable_order_list is not None:
            for k1 in self.unsellable_order_list:
                result['unsellableOrderList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_list = []
        if m.get('addressList') is not None:
            for k1 in m.get('addressList'):
                temp_model = main_models.AddressInfo()
                self.address_list.append(temp_model.from_map(k1))

        if m.get('canSell') is not None:
            self.can_sell = m.get('canSell')

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.order_list = []
        if m.get('orderList') is not None:
            for k1 in m.get('orderList'):
                temp_model = main_models.OrderRenderResult()
                self.order_list.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.unsellable_order_list = []
        if m.get('unsellableOrderList') is not None:
            for k1 in m.get('unsellableOrderList'):
                temp_model = main_models.OrderRenderResult()
                self.unsellable_order_list.append(temp_model.from_map(k1))

        return self

