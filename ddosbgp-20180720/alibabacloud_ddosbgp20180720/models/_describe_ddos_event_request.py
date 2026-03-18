# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDdosEventRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        ip: str = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end time of the DDoS attack events to query. This value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Anti-DDoS Origin instance to query.
        # 
        # >  You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all Anti-DDoS Origin instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The attacked IP address to query.
        self.ip = ip
        # The page number.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region where the Anti-DDoS Origin instance resides.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the Anti-DDoS Origin instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The start time of the DDoS attack events to query. This value is a UNIX timestamp. Unit: seconds.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

