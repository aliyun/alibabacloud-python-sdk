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
        # The client token that is used to ensure the idempotence of the request. The server checks whether a request that uses the same client token has been received. If a request that uses the same client token has been received, the server returns the same request result as the previous request.
        self.client_token = client_token
        # The logistics address of this order. This parameter is generally valid for physical orders.
        self.logistics = logistics
        self.owner_id = owner_id
        # The details of the modules.
        self.parameter = parameter
        # The subscription duration. Unit: month. The value must be an integral multiple of 12.
        # 
        # >  This parameter is required if you create a subscription instance.
        self.period = period
        # The cycle type of the prepaid period
        # - PricingCycle=1 indicates that the unit of the prepaid period is in years; 
        # - PricingCycle=2 indicates that the unit of the prepaid period is in months; 
        # - PricingCycle=3 indicates that the unit of the prepaid period is in days;
        # - Default value: PricingCycle=2
        # 
        # Applicable only to certain product types (ProductType being ddos_originpre_public_cn, ddosDip, ddoscoo, ddos_originpre_public_intl, ddosDip_intl, ddoscoo_intl)
        self.pricing_cycle = pricing_cycle
        # The code of the service to which the instance belongs. You can query the service code by calling the **QueryProductList** operation or viewing **Codes of Alibaba Cloud Services**.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The auto-renewal period. Unit: month.
        # 
        # >  This parameter is required if the **RenewalStatus** parameter is set to **AutoRenewal**.
        self.renew_period = renew_period
        # The renewal method. Valid values:
        # 
        # *   AutoRenewal: The instance is automatically renewed.
        # *   ManualRenewal: The instance is manually renewed.
        # 
        # Default value: ManualRenewal.
        self.renewal_status = renewal_status
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method.
        # *   PayAsYouGo: the pay-as-you-go billing method.
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
        # The code property of the Nth module. Value of N: 1 to 100. If multiple module property parameters are involved, concatenate multiple parameters based on the value of N in sequence.
        # 
        # This parameter is required.
        self.code = code
        # The value property of the Nth module. Value of N: 1 to 100.
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

