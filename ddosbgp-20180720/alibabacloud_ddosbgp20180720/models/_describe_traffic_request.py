# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrafficRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        flow_type: str = None,
        instance_id: str = None,
        interval: int = None,
        ip: str = None,
        ipnet: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # If you do not specify this parameter, the current system time is used as the end time.
        self.end_time = end_time
        # The type of the traffic statistics to query. Valid values:
        # 
        # *   **max**: the peak traffic within the specified interval.
        # *   **avg**: the average traffic within the specified interval.
        # 
        # Enumerated values:
        # 
        # *   all
        # *   avg
        # *   max
        self.flow_type = flow_type
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # If you specify an on-demand instance, you must configure the **Interval** parameter.
        self.instance_id = instance_id
        # The interval at which the traffic statistics are calculated. Unit: seconds. Default value: **5**.
        self.interval = interval
        # The public IP address of the asset to query. If you do not specify this parameter, the traffic statistics of all public IP addresses that are protected by the Anti-DDoS Origin instance are queried.
        # 
        # >  The public IP address must be a protected object of the Anti-DDoS Origin instance. You can call the [DescribePackIpList](https://help.aliyun.com/document_detail/118701.html) operation to query all protected objects of the Anti-DDoS Origin instance.
        self.ip = ip
        # The Classless Inter-Domain Routing (CIDR) block of the on-demand instance that you want to query.
        self.ipnet = ipnet
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ipnet is not None:
            result['Ipnet'] = self.ipnet

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Ipnet') is not None:
            self.ipnet = m.get('Ipnet')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

