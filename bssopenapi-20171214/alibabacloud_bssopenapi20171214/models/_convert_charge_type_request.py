# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertChargeTypeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_id: int = None,
        period: int = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # The subscription duration. Unit: months. This parameter is required if you switch the billing method to subscription. Valid values:
        # 
        # *   1 to 9
        # *   12
        # *   24
        # *   36
        self.period = period
        # The code of the service to which the instance belongs.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service to which the instance belongs.
        self.product_type = product_type
        # The billing method of the instance. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        # 
        # >  After the call is successful, the billing method of the instance is switched.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

