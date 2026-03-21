# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeMultiPriceRequest(DaraModel):
    def __init__(
        self,
        order_items: List[main_models.DescribeMultiPriceRequestOrderItems] = None,
        order_type: str = None,
        package_code: str = None,
        reseller_owner_uid: int = None,
    ):
        self.order_items = order_items
        self.order_type = order_type
        self.package_code = package_code
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

        if self.package_code is not None:
            result['PackageCode'] = self.package_code

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_items = []
        if m.get('OrderItems') is not None:
            for k1 in m.get('OrderItems'):
                temp_model = main_models.DescribeMultiPriceRequestOrderItems()
                self.order_items.append(temp_model.from_map(k1))

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PackageCode') is not None:
            self.package_code = m.get('PackageCode')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

class DescribeMultiPriceRequestOrderItems(DaraModel):
    def __init__(
        self,
        amount: int = None,
        components: List[main_models.DescribeMultiPriceRequestOrderItemsComponents] = None,
        instance_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        saving_plan_period: str = None,
    ):
        self.amount = amount
        self.components = components
        self.instance_ids = instance_ids
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.saving_plan_period = saving_plan_period

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

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

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

        if self.saving_plan_period is not None:
            result['SavingPlanPeriod'] = self.saving_plan_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeMultiPriceRequestOrderItemsComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

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

        if m.get('SavingPlanPeriod') is not None:
            self.saving_plan_period = m.get('SavingPlanPeriod')

        return self

class DescribeMultiPriceRequestOrderItemsComponents(DaraModel):
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

