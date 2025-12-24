# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoadBalancerInstanceChargeTypeRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_charge_type: str = None,
        internet_charge_type: str = None,
        load_balancer_id: str = None,
        load_balancer_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The maximum bandwidth of the Internet-facing CLB instance that is billed on a pay-by-bandwidth basis.
        # 
        # You do not need to set this parameter. The metering method of Internet data transfer for pay-by-LCU instances supports only pay-by-traffic.
        self.bandwidth = bandwidth
        # The metering method of the instance after the change.
        # 
        # Valid value: **PayByCLCU**. Only pay-by-LCU is supported.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The metering method of Internet data transfer after the change.
        # 
        # Valid value: **paybytraffic**.
        # 
        # > *   If the value of the **InstanceChargeType** parameter is set to **PayByCLCU**, only pay-by-data-transfer is supported.
        # >*   When you change the metering method, the new metering method takes effect at 00:00:00 the next day.
        self.internet_charge_type = internet_charge_type
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The specification of the CLB instance.
        # 
        # You do not need to set this parameter. For pay-as-you-go CLB instances, you can only change the metering method from pay-by-specification to pay-by-LCU. You cannot change the metering method from pay-by-LCU to pay-by-specification.
        self.load_balancer_spec = load_balancer_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the CLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

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
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

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

