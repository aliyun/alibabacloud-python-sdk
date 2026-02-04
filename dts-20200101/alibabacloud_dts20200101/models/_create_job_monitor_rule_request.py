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
        # *   If **Type** is set to **delay**, the threshold must be an integer in units of seconds. You can specify the threshold based on your business requirements. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds.
        # *   If **Type** is set to **full_timeout**, the threshold must be an integer in units of hours.
        # 
        # > This parameter is required if **Type** is set to **delay** or **full_timeout** and **State** is set to **Y**.
        self.delay_rule_time = delay_rule_time
        # The ID of the data migration, data synchronization, or change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The alert threshold.
        self.notice_value = notice_value
        # The statistical period of the incremental data verification task. Unit: minutes.
        # 
        # > Valid values: 1, 3, 5, and 30.
        self.period = period
        # The mobile numbers that receive alert notifications. Separate multiple mobile numbers with commas (,).
        # 
        # > 
        # 
        # *   This parameter is available only for users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers.
        # 
        # *   Users of the international site (alibabacloud.com) cannot receive notifications on alerts by using mobile numbers, but can configure alert rules for DTS tasks in the CloudMonitor console. For more information, see [Configure alert rules for DTS tasks in the CloudMonitor console](https://help.aliyun.com/document_detail/175876.html).
        self.phone = phone
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to enable the alert rule. Valid values:
        # 
        # *   **Y**: enables the alert rule.
        # *   **N**: disables the alert rule.
        # 
        # Default value: **Y**.
        self.state = state
        # The number of statistical periods of the incremental data verification task.
        self.times = times
        # The metric that is used to monitor the task. Valid values:
        # 
        # *   **delay**: the **Latency** metric.
        # *   **error**: the **Status** metric.
        # *   **full_timeout**: the **Full Timeout** metric.
        # 
        # Default value: **error**. You must manually set this value.
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

