# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitorDataRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        end_time: str = None,
        instance_id: str = None,
        length: str = None,
        metric_name: str = None,
        next_token: str = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The end of the time range to query. The following formats are supported:
        # 
        # - UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 January 1, 1970.
        # 
        # - Time format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # > The interval between the start time and the end time is less than or equal to 31 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries per page. Valid values: 1 to 1440.
        self.length = length
        # The name of the metric. Valid values:
        # 
        # - MEMORY_ACTUALUSEDSPACE: the memory usage. Unit: bytes.
        # 
        # - DISKUSAGE_USED: the disk usage. Unit: bytes.
        # 
        # - CPU_UTILIZATION: the CPU usage, in percentage.
        # 
        # - VPC_PUBLICIP_INTERNETOUT_RATE: the outbound bandwidth. Unit: bits/s.
        # 
        # - VPC_PUBLICIP_INTERNETIN_RATE: the inbound bandwidth. Unit: bits/s.
        # 
        # - DISK_READ_IOPS: the read IOPS of the disk. Unit: count/s.
        # 
        # - DISK_WRITE_IOPS: the write IOPS of the disk. Unit: count/s.
        # 
        # - FLOW_USED: the traffic usage. Unit: bytes.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The interval at which the monitoring data is queried. Valid values: 60, 300, and 900. Unit: seconds.
        # 
        # > If MetricName is set to FLOW_USED, set Period to 3600 (one hour). In other cases, set Period based on your business requirements.
        # 
        # This parameter is required.
        self.period = period
        # The region ID of the simple application server. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. The following formats are supported:
        # 
        # - UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 January 1, 1970.
        # 
        # - Time format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # > * The specified time range includes the end time and excludes the start time. The start time must be earlier than the end time.
        # >
        # > * The interval between the start time and the end time is less than or equal to 31 days.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

