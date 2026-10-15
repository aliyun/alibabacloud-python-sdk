# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetSubscriptionPriceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        module_list: List[main_models.GetSubscriptionPriceRequestModuleList] = None,
        order_type: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        quantity: int = None,
        region: str = None,
        service_period_quantity: int = None,
        service_period_unit: str = None,
        subscription_type: str = None,
    ):
        # The ID of the instance for which you want to inquire about the price. This parameter is required in upgrade scenarios to obtain the configurations of the instance before the upgrade.
        self.instance_id = instance_id
        # The list of pricing modules.
        # 
        # This parameter is required.
        self.module_list = module_list
        # The order type. Valid values:
        # - NewOrder: new purchase.
        # - Renewal: renewal.
        # - Upgrade: upgrade.
        # 
        # This parameter is required.
        self.order_type = order_type
        self.owner_id = owner_id
        # The product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The product type. Whether this parameter is required depends on the price inquiry documentation of the specific product.
        self.product_type = product_type
        # The quantity.
        self.quantity = quantity
        # The region ID of the instance.
        self.region = region
        # The service period.
        self.service_period_quantity = service_period_quantity
        # The unit of the service period. Valid values:
        # - Year: years.
        # - Month: months.
        self.service_period_unit = service_period_unit
        # The subscription type. Valid value: Subscription (subscription).
        # 
        # This parameter is required.
        self.subscription_type = subscription_type

    def validate(self):
        if self.module_list:
            for v1 in self.module_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['ModuleList'] = []
        if self.module_list is not None:
            for k1 in self.module_list:
                result['ModuleList'].append(k1.to_map() if k1 else None)

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region is not None:
            result['Region'] = self.region

        if self.service_period_quantity is not None:
            result['ServicePeriodQuantity'] = self.service_period_quantity

        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.module_list = []
        if m.get('ModuleList') is not None:
            for k1 in m.get('ModuleList'):
                temp_model = main_models.GetSubscriptionPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k1))

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServicePeriodQuantity') is not None:
            self.service_period_quantity = m.get('ServicePeriodQuantity')

        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

class GetSubscriptionPriceRequestModuleList(DaraModel):
    def __init__(
        self,
        config: str = None,
        module_code: str = None,
        module_status: int = None,
        tag: str = None,
    ):
        # The configuration of the nth pricing module. Valid values of n: 1 to 50. Format: AA:aa,BB:bb. AA and BB are the identifiers of the pricing module attributes, and aa and bb are the attribute values of the pricing module attributes.
        # 
        # This parameter is required.
        self.config = config
        # The identifier of the nth pricing module.
        # 
        # This parameter is required.
        self.module_code = module_code
        # The change status of the pricing module for this inquiry. This parameter is required only when the order type is Upgrade. Valid values:
        # - 1: add.
        # - 2: modify. If the configuration of the pricing module changes in an upgrade scenario, you must explicitly specify this value.
        # 
        # Default value: 1.
        self.module_status = module_status
        # The identifier of the specified resource. This parameter is required only for the upgrade and configuration change of specific products. For example, if you change the configuration of a cloud disk, you can use Tag to identify the ID of the specific cloud disk.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

