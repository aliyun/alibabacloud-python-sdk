# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSensitiveStatisticRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        start_time: int = None,
        statistic_type: str = None,
    ):
        # The hybrid cloud cluster ID.
        # > This parameter applies only to hybrid cloud scenarios. You can call [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) to obtain hybrid cloud cluster information.
        self.cluster_id = cluster_id
        # The end of the time range to query, in UNIX timestamp (UTC) format. Unit: seconds.
        # 
        # > Only data within the last month can be queried. **StartTime** cannot be earlier than one month before the current time. The query fails if the value is out of the supported range.
        # > This parameter is optional. Default value: the current time.
        self.end_time = end_time
        # The ID of the WAF instance.
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number to return in a paged query. Default value: **1**, which indicates the first page.
        self.page_number = page_number
        # The number of entries per page in a paged query. Default value: **10**, which indicates 10 entries per page.
        self.page_size = page_size
        # The region where the WAF instance is deployed. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The beginning of the time range to query, in UNIX timestamp (UTC) format. Unit: seconds.
        # 
        # > Only data within the last month can be queried. **StartTime** cannot be earlier than one month before the current time. The query fails if the value is out of the supported range.
        # > This parameter is optional. Default value: one month before the current time.
        self.start_time = start_time
        # The type of data statistics. Valid values:
        # - **ip**: IP address statistics.
        # - **host**: domain name statistics.
        # - **sensitive_code**: sensitive data type statistics.
        # - **api**: sensitive data API statistics.
        self.statistic_type = statistic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statistic_type is not None:
            result['StatisticType'] = self.statistic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisticType') is not None:
            self.statistic_type = m.get('StatisticType')

        return self

