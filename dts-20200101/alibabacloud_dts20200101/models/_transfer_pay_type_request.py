# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferPayTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        buy_count: str = None,
        charge_type: str = None,
        dts_job_id: str = None,
        instance_class: str = None,
        max_du: int = None,
        min_du: int = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # Specifies whether to automatically renew the DTS instance when it expires. Valid values:
        # 
        # *   **false**: does not automatically renew the DTS instance when it expires. This is the default value.
        # *   **true**: automatically renews the DTS instance when it expires.
        self.auto_pay = auto_pay
        # The subscription length.
        # 
        # *   If the **Period** parameter is set to **Year**, the value range is **1** to **5**.
        # *   If the **Period** parameter is set to **Month**, the value range is **1** to **60**.
        # 
        # >  You must specify this parameter only if you set the **ChargeType** parameter to **PrePaid**.
        self.buy_count = buy_count
        # The new billing method. Valid values:
        # 
        # *   **PrePaid**: subscription.
        # *   **PostPaid**: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The ID of the data synchronization or change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The new instance class of the DTS instance. You can call the [DescribeDtsJobDetail](https://help.aliyun.com/document_detail/208925.html) operation to query the original instance class of the DTS instance.
        # 
        # *   DTS supports the following instance classes for a data migration instance: **xxlarge**, **xlarge**, **large**, **medium**, and **small**.
        # *   DTS supports the following instance classes for a data synchronization instance: **large**, **medium**, **small**, and **micro**.
        # 
        # > For more information about the test performance of each instance class, see [Specifications of data migration instances](https://help.aliyun.com/document_detail/26606.html) and [Specifications of data synchronization channels](https://help.aliyun.com/document_detail/26605.html).
        self.instance_class = instance_class
        # The maximum number of DUs in a serverless instance. Valid values: 2, 4, 8, and 16.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.max_du = max_du
        # The minimum number of DTS Units (DUs) in a serverless instance. Valid values: 1, 2, 4, 8, and 16.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.min_du = min_du
        # The billing cycle of the subscription instance. Valid values:
        # 
        # *   **Year**
        # *   **Month** (default value)
        # 
        # >  You must specify this parameter only if you set the **ChargeType** parameter to **PrePaid**.
        self.period = period
        # The ID of the region where the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

