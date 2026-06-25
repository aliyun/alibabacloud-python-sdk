# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateProductOrdersRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        products: List[main_models.CreateProductOrdersRequestProducts] = None,
    ):
        # Specifies whether to automatically pay for all products listed in the Products parameter.
        # 
        # - true: Enables automatic payment.
        # 
        # - false: Disables automatic payment.
        self.auto_pay = auto_pay
        # The list of products to purchase.
        self.products = products

    def validate(self):
        if self.products:
            for v1 in self.products:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        result['Products'] = []
        if self.products is not None:
            for k1 in self.products:
                result['Products'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        self.products = []
        if m.get('Products') is not None:
            for k1 in m.get('Products'):
                temp_model = main_models.CreateProductOrdersRequestProducts()
                self.products.append(temp_model.from_map(k1))

        return self

class CreateProductOrdersRequestProducts(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        charge_type: str = None,
        duration: int = None,
        instance_properties: List[main_models.CreateProductOrdersRequestProductsInstanceProperties] = None,
        order_type: str = None,
        pricing_cycle: str = None,
        product_code: str = None,
    ):
        # Specifies whether to enable auto-renewal.
        # 
        # - true: Enables auto-renewal.
        # 
        # - false: Disables auto-renewal.
        self.auto_renew = auto_renew
        # The billing method. Currently, only POSTPAY is supported.
        self.charge_type = charge_type
        # The subscription duration. This parameter is used with PricingCycle. Currently, only a value of 1 is supported.
        self.duration = duration
        # The list of instance properties.
        # 
        # - DataWorks_share:
        #   [ {
        #   "Code": "region",
        #   "Value": "cn-shanghai"
        #   }
        #   ]
        # 
        # - OSS_share:
        #   [ {
        #   "Code": "commodity_type",
        #   "Value": "oss",
        #   "Name": "Object Storage Service"
        #   },
        #   {
        #   "Code": "ord_time",
        #   "Value": "1:Hour",
        #   "Name": "1 Hour"
        #   }
        #   ]
        # 
        # - PAI_share: None
        # 
        # - MaxCompute_share for accounts in mainland China:
        #   [
        #   {
        #   "Code": "region",
        #   "Value": "cn-hangzhou"
        #   },
        #   {
        #   "Code": "odps_specification_type",
        #   "Value": "OdpsStandard"
        #   },
        #   {
        #   "Code": "ord_time",
        #   "Value": "1:Hour"
        #   }
        #   ]
        # 
        # - MaxCompute_share for accounts outside mainland China:
        #   [
        #   {
        #   "Code": "region",
        #   "Value": "cn-hangzhou"
        #   },
        #   {
        #   "Code": "ord_time",
        #   "Value": "1:Hour"
        #   }
        #   ]
        self.instance_properties = instance_properties
        # The order type. Currently, only BUY is supported.
        self.order_type = order_type
        # The billing cycle. The following values are supported:
        # 
        # - Month: Monthly billing. Only DataWorks_share supports this value.
        # 
        # - Hour: Hourly billing. Only OSS_share and MaxCompute_share support this value.
        self.pricing_cycle = pricing_cycle
        # The product code. The following codes are supported:
        # 
        # - DataWorks_share: The pay-as-you-go DataWorks product.
        # 
        # - MaxCompute_share: The pay-as-you-go MaxCompute product.
        # 
        # - PAI_share: The pay-as-you-go PAI product.
        # 
        # - OSS_share: The pay-as-you-go OSS product.
        self.product_code = product_code

    def validate(self):
        if self.instance_properties:
            for v1 in self.instance_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.duration is not None:
            result['Duration'] = self.duration

        result['InstanceProperties'] = []
        if self.instance_properties is not None:
            for k1 in self.instance_properties:
                result['InstanceProperties'].append(k1.to_map() if k1 else None)

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        self.instance_properties = []
        if m.get('InstanceProperties') is not None:
            for k1 in m.get('InstanceProperties'):
                temp_model = main_models.CreateProductOrdersRequestProductsInstanceProperties()
                self.instance_properties.append(temp_model.from_map(k1))

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

class CreateProductOrdersRequestProductsInstanceProperties(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        value: str = None,
    ):
        # The code of the instance property.
        self.code = code
        # The name of the instance property.
        self.name = name
        # The value of the instance property.
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

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

