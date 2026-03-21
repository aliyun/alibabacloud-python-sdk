# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class CreateMultiOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        order_items: List[main_models.CreateMultiOrderShrinkRequestOrderItems] = None,
        order_type: str = None,
        properties_shrink: str = None,
        reseller_owner_uid: int = None,
    ):
        self.order_items = order_items
        self.order_type = order_type
        self.properties_shrink = properties_shrink
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        if self.order_items:
            for v1 in self.order_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OrderItems'] = []
        if self.order_items is not None:
            for k1 in self.order_items:
                result['OrderItems'].append(k1.to_map() if k1 else None)

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_items = []
        if m.get('OrderItems') is not None:
            for k1 in m.get('OrderItems'):
                temp_model = main_models.CreateMultiOrderShrinkRequestOrderItems()
                self.order_items.append(temp_model.from_map(k1))

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

class CreateMultiOrderShrinkRequestOrderItems(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        buy_change: bool = None,
        components: List[main_models.CreateMultiOrderShrinkRequestOrderItemsComponents] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.amount = amount
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.buy_change = buy_change
        self.components = components
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.resource_ids = resource_ids
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.buy_change is not None:
            result['BuyChange'] = self.buy_change

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BuyChange') is not None:
            self.buy_change = m.get('BuyChange')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.CreateMultiOrderShrinkRequestOrderItemsComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class CreateMultiOrderShrinkRequestOrderItemsComponents(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

