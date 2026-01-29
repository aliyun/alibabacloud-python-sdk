# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        owner_id: int = None,
        product_code: str = None,
        product_type: str = None,
        region: str = None,
        renew_status: str = None,
        subscription_type: str = None,
    ):
        # The ID of the instance. Separate multiple IDs with commas (,). A maximum of 100 IDs can be specified.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # This parameter is required.
        self.owner_id = owner_id
        # The code of the service.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The type of the service.
        self.product_type = product_type
        # The region in which the instance resides.
        self.region = region
        # The method that is used to renew the instance. Valid values:
        # 
        # AutoRenewal: automatically renews the instance.
        # 
        # ManualRenewal: manually renews the instance.
        # 
        # NotRenewal: does not renew the instance.
        self.renew_status = renew_status
        # The billing method. Valid values:
        # 
        # Subscription: the subscription billing method.
        # 
        # PayAsYouGo: the pay-as-you-go billing method.
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
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region is not None:
            result['Region'] = self.region

        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

