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
        # The product information.
        self.order_items = order_items
        # The order type.
        self.order_type = order_type
        # The package code. You do not need to specify this parameter for non-package types.
        self.package_code = package_code
        # The user ID for resource ownership in the reseller pattern. You do not need to specify this parameter in the non-reseller pattern.
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
        data: str = None,
        instance_ids: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        saving_plan_period: str = None,
    ):
        # The purchase quantity.
        self.amount = amount
        # The list of product modules.
        self.components = components
        self.data = data
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The subscription duration. Valid values:
        # 
        # - If PeriodUnit is set to Year: 1, 2, or 3.
        # 
        # - If PeriodUnit is set to Month: 1, 2, 3, or 6.
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The list of resource IDs.
        self.resource_ids = resource_ids
        # The resource type.
        # > This parameter is case-sensitive. Make sure that the spelling is correct.
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

        if self.data is not None:
            result['Data'] = self.data

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

        if m.get('Data') is not None:
            self.data = m.get('Data')

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
        # The key of the module.
        self.key = key
        # The value of the module.
        # 
        # The following example values and valid values are for the Enterprise Edition monthly duration package:
        # 
        # - RegionId: cn-shanghai
        # - InstanceType: eds.enterprise_office.4c8g
        # - DurationType (hours): Valid values: 
        #    - 120
        #    - 250
        # - OsType: Valid values: 
        #    - Windows
        #    - Linux
        # - RootDiskSize (GiB): 80
        # - RootDiskCategory: Valid values: 
        #    - cloud_efficiency: ultra cloud disk
        #    - cloud_auto: ESSD AutoPL cloud disk
        #    - cloud_essd: enhanced standard SSD. Only specific instance types support this value.
        # - RootPerformanceLevel: Valid values: 
        #    - PL0
        #    - PL1
        #    - PL2
        #    - PL3
        # - DataDiskSize (GiB): same as RootDiskSize
        # - DataDiskCategory: same as RootDiskCategory
        # - DataPerformanceLevel: same as RootPerformanceLevel
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

