# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoadBalancerInternetSpecRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        bandwidth: int = None,
        internet_charge_type: str = None,
        load_balancer_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to automatically pay the subscription fee of the Internet-facing CLB instance. Valid values:
        # 
        # *   **true**: enables automatic payments. This is the default value.
        # *   **false**: disables automatic payment. You must complete the payment in Order Center.
        self.auto_pay = auto_pay
        # The maximum bandwidth of the Internet-facing CLB instance that uses the pay-by-bandwidth metering method. Unit: Mbit/s.
        # 
        # Valid values: **1 to 5000**. The maximum bandwidth varies based on the region where the CLB instance is created.****
        # 
        # >  You do not need to specify this parameter if you set **InternetChargeType** to **paybytraffic** (pay-by-data-transfer).
        self.bandwidth = bandwidth
        # The metering method of the Internet-facing CLB instance. Valid values:
        # 
        # *   **paybybandwidth**: pay-by-bandwidth
        # *   **paybytraffic**: pay-by-data-transfer
        self.internet_charge_type = internet_charge_type
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
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

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

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

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

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

