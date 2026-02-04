# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewInstanceRequest(DaraModel):
    def __init__(
        self,
        buy_count: str = None,
        charge_type: str = None,
        dts_job_id: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The subscription duration of the DTS instance after renewal. Default value: 1.
        # 
        # *   If **Period** is set to **Year**, the valid values are **1 to 5**.
        # *   If **Period** is set to **Month**, the valid values are **1 to 60**.
        self.buy_count = buy_count
        # The billing method of the DTS instance. Set the value to **PREPAY**, which specifies the subscription billing method.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The ID of the data synchronization or change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The billing cycle of the DTS instance after renewal. Valid values:
        # 
        # *   **Year**
        # *   **Month** (default)
        self.period = period
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

