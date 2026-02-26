# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class OrderLineResult(DaraModel):
    def __init__(
        self,
        eticket_infos: List[main_models.EticketInfo] = None,
        logistics_status: str = None,
        number: str = None,
        order_id: str = None,
        order_line_id: str = None,
        order_line_status: str = None,
        pay_fee: int = None,
        product_id: str = None,
        product_pic: str = None,
        product_title: str = None,
        sku_id: str = None,
        sku_title: str = None,
    ):
        self.eticket_infos = eticket_infos
        self.logistics_status = logistics_status
        self.number = number
        self.order_id = order_id
        self.order_line_id = order_line_id
        self.order_line_status = order_line_status
        self.pay_fee = pay_fee
        self.product_id = product_id
        self.product_pic = product_pic
        self.product_title = product_title
        # skuId
        self.sku_id = sku_id
        self.sku_title = sku_title

    def validate(self):
        if self.eticket_infos:
            for v1 in self.eticket_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['eticketInfos'] = []
        if self.eticket_infos is not None:
            for k1 in self.eticket_infos:
                result['eticketInfos'].append(k1.to_map() if k1 else None)

        if self.logistics_status is not None:
            result['logisticsStatus'] = self.logistics_status

        if self.number is not None:
            result['number'] = self.number

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.order_line_id is not None:
            result['orderLineId'] = self.order_line_id

        if self.order_line_status is not None:
            result['orderLineStatus'] = self.order_line_status

        if self.pay_fee is not None:
            result['payFee'] = self.pay_fee

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_pic is not None:
            result['productPic'] = self.product_pic

        if self.product_title is not None:
            result['productTitle'] = self.product_title

        if self.sku_id is not None:
            result['skuId'] = self.sku_id

        if self.sku_title is not None:
            result['skuTitle'] = self.sku_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eticket_infos = []
        if m.get('eticketInfos') is not None:
            for k1 in m.get('eticketInfos'):
                temp_model = main_models.EticketInfo()
                self.eticket_infos.append(temp_model.from_map(k1))

        if m.get('logisticsStatus') is not None:
            self.logistics_status = m.get('logisticsStatus')

        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('orderLineId') is not None:
            self.order_line_id = m.get('orderLineId')

        if m.get('orderLineStatus') is not None:
            self.order_line_status = m.get('orderLineStatus')

        if m.get('payFee') is not None:
            self.pay_fee = m.get('payFee')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productPic') is not None:
            self.product_pic = m.get('productPic')

        if m.get('productTitle') is not None:
            self.product_title = m.get('productTitle')

        if m.get('skuId') is not None:
            self.sku_id = m.get('skuId')

        if m.get('skuTitle') is not None:
            self.sku_title = m.get('skuTitle')

        return self

