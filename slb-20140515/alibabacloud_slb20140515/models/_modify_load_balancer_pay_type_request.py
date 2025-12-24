# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoadBalancerPayTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        duration: int = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # >  This parameter is valid only when the `PayType` parameter is set to **PrePay**. This parameter is valid only for pay-as-you-go instances.
        self.auto_pay = auto_pay
        # The subscription duration.
        # 
        # *   If **PricingCycle** is set to **month**, the valid values are **1** to **9**.
        # *   If **PricingCycle** is set to **year**, the valid values are **1** to **3**.
        # 
        # >  This parameter is valid only when the **PayType** parameter is set to **PrePay**. This parameter is valid only for pay-as-you-go instances.
        self.duration = duration
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the CLB instance. Valid values:
        # 
        # *   **PayOnDemand** (default): pay-as-you-go
        # 
        # To change the billing method of a pay-as-you-go CLB instance to subscription, you must set the parameter to **PrePay**. In addition, the previous billing method of the CLB instance must be **PayOnDemand**.
        self.pay_type = pay_type
        # The billing cycle.
        # 
        # Valid values: **year** and **month**.
        # 
        # >  This parameter is valid only when the **PayType** parameter is set to **PrePay**. This parameter is valid only for pay-as-you-go instances.
        self.pricing_cycle = pricing_cycle
        # The ID of the region where the CLB instance is deployed.
        # 
        # You can query the region ID from the [Regions and zones](https://help.aliyun.com/document_detail/40654.html) list or by calling the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

