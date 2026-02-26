# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class Shop(DaraModel):
    def __init__(
        self,
        cooperation_shops: List[main_models.CooperationShop] = None,
        distributor_id: str = None,
        end_date: str = None,
        purchaser_id: str = None,
        request_id: str = None,
        shop_id: str = None,
        shop_name: str = None,
        shop_type: str = None,
        start_date: str = None,
        status: str = None,
    ):
        self.cooperation_shops = cooperation_shops
        self.distributor_id = distributor_id
        self.end_date = end_date
        self.purchaser_id = purchaser_id
        self.request_id = request_id
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.shop_type = shop_type
        self.start_date = start_date
        self.status = status

    def validate(self):
        if self.cooperation_shops:
            for v1 in self.cooperation_shops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cooperationShops'] = []
        if self.cooperation_shops is not None:
            for k1 in self.cooperation_shops:
                result['cooperationShops'].append(k1.to_map() if k1 else None)

        if self.distributor_id is not None:
            result['distributorId'] = self.distributor_id

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        if self.shop_name is not None:
            result['shopName'] = self.shop_name

        if self.shop_type is not None:
            result['shopType'] = self.shop_type

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cooperation_shops = []
        if m.get('cooperationShops') is not None:
            for k1 in m.get('cooperationShops'):
                temp_model = main_models.CooperationShop()
                self.cooperation_shops.append(temp_model.from_map(k1))

        if m.get('distributorId') is not None:
            self.distributor_id = m.get('distributorId')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')

        if m.get('shopType') is not None:
            self.shop_type = m.get('shopType')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

