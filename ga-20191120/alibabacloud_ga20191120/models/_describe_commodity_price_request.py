# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeCommodityPriceRequest(DaraModel):
    def __init__(
        self,
        orders: List[main_models.DescribeCommodityPriceRequestOrders] = None,
        promotion_option_no: str = None,
        region_id: str = None,
    ):
        # The commodity orders.
        # 
        # This parameter is required.
        self.orders = orders
        # The coupon code.
        # 
        # >  This parameter is unavailable on the China site (aliyun.com).
        self.promotion_option_no = promotion_option_no
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.orders:
            for v1 in self.orders:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Orders'] = []
        if self.orders is not None:
            for k1 in self.orders:
                result['Orders'].append(k1.to_map() if k1 else None)

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.orders = []
        if m.get('Orders') is not None:
            for k1 in m.get('Orders'):
                temp_model = main_models.DescribeCommodityPriceRequestOrders()
                self.orders.append(temp_model.from_map(k1))

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeCommodityPriceRequestOrders(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        components: List[main_models.DescribeCommodityPriceRequestOrdersComponents] = None,
        duration: int = None,
        order_type: str = None,
        pricing_cycle: str = None,
        quantity: int = None,
    ):
        # The billing method. Set the value to **PREPAY**, which specifies the subscription billing method.
        self.charge_type = charge_type
        # The commodity code.
        # 
        # Valid values on the China site (aliyun.com):
        # 
        # *   **ga_gapluspre_public_cn**: GA instance.
        # *   **ga_plusbwppre_public_cn**: basic bandwidth plan.
        # 
        # Valid values on the international site (alibabacloud.com):
        # 
        # *   **ga_pluspre_public_intl**: GA instance.
        # *   **ga_bwppreintl_public_intl:** basic bandwidth plan.
        self.commodity_code = commodity_code
        # The information about commodity modules.
        # 
        # The information varies based on the commodity module.
        self.components = components
        # The subscription duration.
        # 
        # *   Valid values if you set **PricingCycle** to **Month**: **1** to **9**.
        # *   Valid values if you set **PricingCycle** to **Year**: **1** to **3**.
        self.duration = duration
        # The type of the order. Valid values:
        # 
        # *   **BUY**: purchase order.
        # *   **RENEW**: renewal order.
        # *   **UPGRADE**: upgrade order.
        self.order_type = order_type
        # The billing cycle. Valid values:
        # 
        # *   **Month**
        # *   **Year**
        self.pricing_cycle = pricing_cycle
        # The number of instances that you want to purchase.
        self.quantity = quantity

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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeCommodityPriceRequestOrdersComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

class DescribeCommodityPriceRequestOrdersComponents(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        properties: List[main_models.DescribeCommodityPriceRequestOrdersComponentsProperties] = None,
    ):
        # The code of the commodity module.
        # 
        # The information varies based on the commodity module. Examples: **instance** (GA instance) and **ord_time** (subscription duration).
        self.component_code = component_code
        # The attributes of commodity modules.
        # 
        # The information varies based on the commodity module.
        self.properties = properties

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.DescribeCommodityPriceRequestOrdersComponentsProperties()
                self.properties.append(temp_model.from_map(k1))

        return self

class DescribeCommodityPriceRequestOrdersComponentsProperties(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The code of the attribute of the commodity module.
        # 
        # The information varies based on the commodity module. Examples: **instance** (GA instance) and **ord_time** (subscription duration).
        self.code = code
        # The value of the attribute.
        # 
        # The information varies based on the commodity module. Examples: **instance_fee** (GA instance fee) and **1:Month** (one-month subscription).
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

