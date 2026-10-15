# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        logistics: str = None,
        owner_id: int = None,
        parameter: List[main_models.CreateInstanceRequestParameter] = None,
        period: int = None,
        pricing_cycle: int = None,
        product_code: str = None,
        product_type: str = None,
        renew_period: int = None,
        renewal_status: str = None,
        subscription_type: str = None,
    ):
        # The client idempotency token. The server checks whether a request with the same ClientToken has been made. If yes, the server returns the result of the previous call.
        self.client_token = client_token
        # The logistics address for this order. This parameter is typically valid for orders of physical products.
        self.logistics = logistics
        self.owner_id = owner_id
        # The list of modules.
        self.parameter = parameter
        # The subscription period. Unit: months. For yearly subscription products, specify a multiple of 12.
        self.period = period
        # The unit of the subscription period.
        # 
        # - PricingCycle=1: The unit of the subscription period is year.
        # 
        # - PricingCycle=2: The unit of the subscription period is month.
        # 
        # - PricingCycle=3: The unit of the subscription period is day.
        # 
        # Default value: PricingCycle=2.
        # 
        # This parameter is applicable only to specific product types (ProductType is ddos_originpre_public_cn, ddosDip, ddoscoo, ddos_originpre_public_intl, ddosDip_intl, or ddoscoo_intl).
        self.pricing_cycle = pricing_cycle
        # The product code. You can call the **QueryProductList** operation to query the product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The product type.
        self.product_type = product_type
        # The auto-renewal epoch. Unit: months.
        # > This parameter is required when you set **RenewalStatus** to **AutoRenewal** in Settings.
        self.renew_period = renew_period
        # The auto-renewal status. Valid values:
        # - AutoRenewal: auto-renewal is enabled.
        # - ManualRenewal: manual renewal.
        # 
        # Default value: ManualRenewal.
        self.renewal_status = renewal_status
        # The billing method. Valid values:
        # - Subscription: subscription.
        # - PayAsYouGo: pay-as-you-go.
        # 
        # This parameter is required.
        self.subscription_type = subscription_type

    def validate(self):
        if self.parameter:
            for v1 in self.parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.logistics is not None:
            result['Logistics'] = self.logistics

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Parameter'] = []
        if self.parameter is not None:
            for k1 in self.parameter:
                result['Parameter'].append(k1.to_map() if k1 else None)

        if self.period is not None:
            result['Period'] = self.period

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Logistics') is not None:
            self.logistics = m.get('Logistics')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.parameter = []
        if m.get('Parameter') is not None:
            for k1 in m.get('Parameter'):
                temp_model = main_models.CreateInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k1))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

class CreateInstanceRequestParameter(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The code of the Nth module property. Valid values of N: 1 to 100. If multiple module properties exist, concatenate them in the format of N=1, 2, 3...N.
        # 
        # This parameter is required.
        self.code = code
        # The value of the Nth module property. Valid values of N: 1 to 100.
        # 
        # This parameter is required.
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

