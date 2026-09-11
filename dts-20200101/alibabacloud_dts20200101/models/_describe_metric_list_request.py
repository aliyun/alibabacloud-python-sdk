# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricListRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        client_token: str = None,
        dts_job_id: str = None,
        end_time: int = None,
        env: str = None,
        metric_name: str = None,
        metric_type: str = None,
        owner_id: str = None,
        param: str = None,
        period: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # Ensures the idempotency of the request. Generate a parameter value from your client to make sure that the value is unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the data migration or data synchronization task.
        self.dts_job_id = dts_job_id
        # The end timestamp, in milliseconds.
        self.end_time = end_time
        # Default value: **ALIYUN**.
        self.env = env
        # - **InternetOut**: outbound Internet traffic, in bytes.
        # - **diskusage_utilization**: disk usage.
        # - **IntranetInRate**: inbound internal network traffic, in bytes.
        # - **InternetIn**: inbound Internet traffic, in bytes.
        # - **cpu_total**: CPU utilization.
        # - **memory_usedutilization**: memory utilization.
        # - **IntranetOutRate**: outbound internal network traffic, in bytes.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # Specifies whether to query a cluster or a node. Valid values:
        # - **CLUSTER**: cluster.
        # - **NODE**: node.
        self.metric_type = metric_type
        self.owner_id = owner_id
        # The observation value. If **MetricType** is set to **NODE**, the value is **nodeid**.
        # 
        # This parameter is required.
        self.param = param
        # The observation interval in seconds. The minimum interval is 15 seconds.
        self.period = period
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The start timestamp, in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.env is not None:
            result['Env'] = self.env

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id

        if self.param is not None:
            result['Param'] = self.param

        if self.period is not None:
            result['Period'] = self.period

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

