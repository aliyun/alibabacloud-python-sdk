# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBandwidthLimitationRequest(DaraModel):
    def __init__(
        self,
        instance_charge_type: str = None,
        instance_type: str = None,
        operation_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_strategy: str = None,
    ):
        # The billing method of the instance. For more information, see [Billing overview](https://help.aliyun.com/document_detail/25398.html). Valid values:
        # 
        # - PrePaid: subscription.
        # - PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        self.instance_charge_type = instance_charge_type
        # The instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The operation type for querying public bandwidth limits. Valid values:
        # 
        # - Upgrade: upgrades the public bandwidth.
        # - Downgrade: downgrades the public bandwidth.
        # - Create: creates an ECS instance.
        # 
        # Default value: Create.
        self.operation_type = operation_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the target region. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        # 
        # > When you set the OperationType parameter to Upgrade or Downgrade, the ResourceId parameter is required.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The bidding strategy for pay-as-you-go instances. Valid values:
        # 
        # - NoSpot: a regular pay-as-you-go instance.
        # - SpotWithPriceLimit: a preemptible instance with a user-defined maximum hourly price.
        # - SpotAsPriceGo: a preemptible instance priced at the market price at the time of purchase.
        # 
        # Default value: NoSpot.
        # 
        # > The SpotStrategy parameter takes effect only when the InstanceChargeType parameter is set to PostPaid.
        self.spot_strategy = spot_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        return self

