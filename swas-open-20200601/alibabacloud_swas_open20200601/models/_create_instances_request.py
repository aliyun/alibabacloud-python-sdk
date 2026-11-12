# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstancesRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        client_token: str = None,
        data_disk_size: int = None,
        image_id: str = None,
        period: int = None,
        plan_id: str = None,
        region_id: str = None,
    ):
        # The number of Simple Application Server instances to create. Valid values: 1 to 20.
        # 
        # Default value: 1.
        self.amount = amount
        # Specifies whether to enable auto-renewal upon expiration. Valid values:
        # 
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is disabled.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. This parameter is required only when AutoRenew is set to true. Unit: months. Valid values: 1, 3, 6, 12, 24, and 36.
        self.auto_renew_period = auto_renew_period
        # The billing method. Set the value to PrePaid. Currently, only the subscription billing method is supported.
        # 
        # Default value: PrePaid.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The size of the data cloud disk to be mounted. Unit: GB. Valid values: 0 to 16380. The value must be a multiple of 20.
        # 
        # <props="china">
        # - A value of 0 indicates that no data cloud disk is mounted.
        # 
        # - If the selected plan uses a PL0 ESSD, the minimum size of the data cloud disk is 40 GB.
        # 
        # - If the selected plan uses a standard SSD, the minimum size of the data cloud disk is 20 GB.
        # 
        # 
        # 
        # <props="intl">
        # - A value of 0 indicates that no data cloud disk is mounted.
        # 
        # - If the selected plan uses a standard SSD, the minimum size of the data cloud disk is 20 GB.
        # 
        # 
        # 
        # Default value: 0.
        self.data_disk_size = data_disk_size
        # The image ID. You can call the [ListImages](https://help.aliyun.com/document_detail/189313.html) operation to query available image IDs in a specified region.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The subscription period of the resource. Unit: months. Valid values: 1, 3, 6, 12, 24, and 36.
        # 
        # This parameter is required.
        self.period = period
        # The plan ID. You can call the [ListPlans](https://help.aliyun.com/document_detail/189314.html) operation to query all plans in a specified region.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.period is not None:
            result['Period'] = self.period

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

