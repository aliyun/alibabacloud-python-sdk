# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoadBalancerInstanceSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        load_balancer_id: str = None,
        load_balancer_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **true**: automatically completes the payment.
        # *   **false** (default): If you select this option, you must complete the payment in the Order Center.
        # 
        # > This parameter takes effect only for subscription instances.
        self.auto_pay = auto_pay
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The specification of the CLB instance. Valid values:
        # 
        # *   **slb.s1.small**
        # *   **slb.s2.small**
        # *   **slb.s2.medium**
        # *   **slb.s3.small**
        # *   **slb.s3.medium**
        # *   **slb.s3.large**
        # 
        # The specifications available vary by region. For more information about the specifications, see [High-performance CLB instance](https://help.aliyun.com/document_detail/85931.html).
        # 
        # > When you switch a shared-resource CLB instance to a high-performance CLB instance, your service may be interrupted for 10 to 30 seconds. We recommend that you modify the specification during off-peak hours or use Alibaba Cloud DNS to schedule your workloads to another CLB instance before you modify the specification.
        # 
        # This parameter is required.
        self.load_balancer_spec = load_balancer_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the CLB instance.
        # 
        # You can query the region ID from the [Regions and zones](https://help.aliyun.com/document_detail/40654.html) list or by calling the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation.
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

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

