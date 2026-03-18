# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOpEntitiesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        op_action: int = None,
        order_by: str = None,
        order_dir: str = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end time. Operation logs that were generated before this time are queried.**** The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance to query.
        # 
        # > You can call the [DescribeInstanceList](https://help.aliyun.com/document_detail/118698.html) operation to query the IDs of all instances.
        self.instance_id = instance_id
        # The type of the operation. Valid values:
        # 
        # *   **3**: Add an IP address to the instance.
        # *   **4**: Remove an IP address from the instance.
        # *   **5**: Downgrade the instance.
        # *   **6**: Deactivate blackhole filtering.
        # *   **7**: Reset the number of times that you can deactivate blackhole filtering.
        # *   **8**: Restore the mitigation capability.
        # *   **9**: Add an asset group.
        # *   **10**: Remove an asset group.
        # *   **11**: Enable the metering method of daily 95th percentile for the burstable clean bandwidth feature.
        # *   **12**: Enable the metering method of monthly 95th percentile for the burstable clean bandwidth feature.
        # *   **13**: Periodically switch between the metering methods of daily 95th percentile and monthly 95th percentile for the burstable clean bandwidth feature.
        # *   **14**: Disable the metering method of daily 95th percentile for the burstable clean bandwidth feature.
        # *   **15**: Disable the metering method of monthly 95th percentile for the burstable clean bandwidth feature.
        # *   **16**: Disable burstable clean bandwidth due to overdue payments.
        # *   **17**: Disable burstable clean bandwidth due to instance expiration.
        self.op_action = op_action
        # The sorting method of operation logs. Set the value to **opdate**, which indicates sorting based on the operation time.
        self.order_by = order_by
        # The sort order of operation logs. Valid values:
        # 
        # *   **ASC**: the ascending order.
        # *   **DESC**: the descending order.
        # 
        # Default value: **DESC**.
        self.order_dir = order_dir
        # The number of entries per page. Maximum value: 50.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region where the instance resides.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/118703.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs in Resource Management.
        # 
        # If you do not specify this parameter, the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The start time. Operation logs that were generated after this time are queried.**** The value is a UNIX timestamp. Unit: milliseconds.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.op_action is not None:
            result['OpAction'] = self.op_action

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_dir is not None:
            result['OrderDir'] = self.order_dir

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
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderDir') is not None:
            self.order_dir = m.get('OrderDir')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

