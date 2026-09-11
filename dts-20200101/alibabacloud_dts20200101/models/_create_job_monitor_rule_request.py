# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobMonitorRuleRequest(DaraModel):
    def __init__(
        self,
        delay_rule_time: int = None,
        dts_job_id: str = None,
        notice_value: int = None,
        period: int = None,
        phone: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        times: int = None,
        type: str = None,
    ):
        # The threshold for triggering an alert.
        # 
        # - If **Type** is set to **delay**, the unit is seconds and the value must be an integer. Set the threshold based on your business requirements. A value of 10 or greater is recommended to avoid alert fluctuations caused by network issues or database loads.
        # 
        # - If **Type** is set to **full_timeout**, the unit is hours and the value must be an integer.
        # 
        # > This parameter is required when **Type** is set to **delay** or **full_timeout** and **State** is set to **Y**.
        self.delay_rule_time = delay_rule_time
        # The ID of the data migration, data synchronization, or change tracking task. You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to obtain the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The alert threshold.
        self.notice_value = notice_value
        # The statistical period of the incremental verification task. Unit: minutes.
        # 
        # > Valid values: 1, 5, 10, and 30.
        self.period = period
        # The mobile phone numbers of alert contacts, separated by commas (,).
        # >-  This parameter is supported only on the China site (aliyun.com) and only for the Chinese mainland mobile phone numbers. A maximum of 10 mobile phone numbers can be specified.
        # - The international site does not support SMS-based alerting. You can only [set alert rules for DTS tasks through the CloudMonitor monitoring platform](https://help.aliyun.com/document_detail/175876.html).
        self.phone = phone
        # The region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to enable the alert rule. Valid values:
        # 
        # - **Y**: Enable the alert rule.
        # - **N**: Disable the alert rule.
        # 
        # Default value: **Y**.
        self.state = state
        # The number of statistical periods for the incremental verification task.
        self.times = times
        # The type of the alert metric. Valid values:
        # - **delay**: the **Latency** metric.
        # - **error**: the **Migration Status** metric.
        # - **full_timeout**: the **Full Migration Duration** metric.
        # 
        # Default value: **error**. This parameter must be manually specified.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.notice_value is not None:
            result['NoticeValue'] = self.notice_value

        if self.period is not None:
            result['Period'] = self.period

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        if self.times is not None:
            result['Times'] = self.times

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('NoticeValue') is not None:
            self.notice_value = m.get('NoticeValue')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Times') is not None:
            self.times = m.get('Times')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

