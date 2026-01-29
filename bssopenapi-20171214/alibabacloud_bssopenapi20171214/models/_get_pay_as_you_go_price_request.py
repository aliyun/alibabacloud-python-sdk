# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetPayAsYouGoPriceRequest(DaraModel):
    def __init__(
        self,
        module_list: List[main_models.GetPayAsYouGoPriceRequestModuleList] = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        region: str = None,
        subscription_type: str = None,
    ):
        # The details of pricing modules.
        # 
        # This parameter is required.
        self.module_list = module_list
        self.owner_id = owner_id
        # The code of the service.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The ID of the region in which the instance resides.
        self.region = region
        # The billing method. Set the value to PayAsYouGo.
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
        result['ModuleList'] = []
        if self.module_list is not None:
            for k1 in self.module_list:
                result['ModuleList'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region is not None:
            result['Region'] = self.region

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_list = []
        if m.get('ModuleList') is not None:
            for k1 in m.get('ModuleList'):
                temp_model = main_models.GetPayAsYouGoPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

class GetPayAsYouGoPriceRequestModuleList(DaraModel):
    def __init__(
        self,
        config: str = None,
        module_code: str = None,
        price_type: str = None,
    ):
        # The configuration of the Nth pricing module. Valid values of N: 1 to 50. Format: AA:aa,BB:bb. The values of AA and BB are the property IDs of the pricing module. The values of aa and bb are the property values of the pricing module.
        # 
        # >  You can call the [DescribePricingModule](https://help.aliyun.com/document_detail/96469.html) operation to obtain the configuration parameters of the pricing module.
        # 
        # This parameter is required.
        self.config = config
        # The code of the Nth pricing module.
        # 
        # >  You can call the [DescribePricingModule](https://help.aliyun.com/document_detail/96469.html) operation to obtain the module code.
        # 
        # This parameter is required.
        self.module_code = module_code
        # The price type of the Nth pricing module. Valid values:
        # 
        # *   Hour: hourly price
        # *   Usage: usage price
        # *   Month: monthly price
        # *   Year: annual price
        # 
        # >  You can call the [DescribePricingModule](https://help.aliyun.com/document_detail/96469.html) operation to obtain the configuration parameters of the pricing module.
        # 
        # This parameter is required.
        self.price_type = price_type

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

        if self.price_type is not None:
            result['PriceType'] = self.price_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')

        return self

