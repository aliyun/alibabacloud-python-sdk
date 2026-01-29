# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePricingModuleRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        self.owner_id = owner_id
        # The service code. You can query the service code by calling the **QueryProductList** operation.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service. You can query the service type by calling the **QueryProductList** operation.
        self.product_type = product_type
        # The billing method. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        # 
        # This parameter is required.
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

