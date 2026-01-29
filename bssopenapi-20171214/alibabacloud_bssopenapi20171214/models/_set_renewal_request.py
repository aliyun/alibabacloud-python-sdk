# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetRenewalRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        renewal_period: int = None,
        renewal_period_unit: str = None,
        renewal_status: str = None,
        subscription_type: str = None,
    ):
        # The ID of the instance. You can enable auto-renewal for up to 100 subscription instances at a time. Separate multiple instance IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        self.owner_id = owner_id
        # The code of the service.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The auto-renewal period. Valid values:
        # 
        # *   1
        # *   2
        # *   3
        # *   6
        # *   12
        # 
        # >  This parameter is required if the RenewalStatus parameter is set to AutoRenewal.
        self.renewal_period = renewal_period
        # The unit of the auto-renewal period. Valid values:
        # 
        # *   M: months
        # *   Y: years
        # 
        # >  This parameter is required if the RenewalStatus parameter is set to AutoRenewal.
        self.renewal_period_unit = renewal_period_unit
        # The status of renewal. Valid values:
        # 
        # *   AutoRenewal: The instance is automatically renewed.
        # *   ManualRenewal: The instance is manually renewed.
        # *   NotRenewal: The instance is not renewed.
        # 
        # This parameter is required.
        self.renewal_status = renewal_status
        # The billing method. Valid values:
        # 
        # *   Subscription: subscription
        # *   PayAsYouGo: pay-as-you-go
        self.subscription_type = subscription_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.renewal_period is not None:
            result['RenewalPeriod'] = self.renewal_period

        if self.renewal_period_unit is not None:
            result['RenewalPeriodUnit'] = self.renewal_period_unit

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RenewalPeriod') is not None:
            self.renewal_period = m.get('RenewalPeriod')

        if m.get('RenewalPeriodUnit') is not None:
            self.renewal_period_unit = m.get('RenewalPeriodUnit')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

