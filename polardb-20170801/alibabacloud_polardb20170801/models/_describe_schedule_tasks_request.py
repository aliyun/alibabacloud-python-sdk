# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScheduleTasksRequest(DaraModel):
    def __init__(
        self,
        dbcluster_description: str = None,
        dbcluster_id: str = None,
        order_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        planned_end_time: str = None,
        planned_start_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        task_action: str = None,
    ):
        # The description of the cluster.
        self.dbcluster_description = dbcluster_description
        # The cluster ID.
        # 
        # > 
        # 
        # *   You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the information of all PolarDB clusters that are deployed in a specific region, such as the cluster IDs.
        # 
        # *   If you do not specify this parameter, all scheduled tasks on your clusters are queried.
        self.dbcluster_id = dbcluster_id
        # The ID of the order.
        # 
        # >  The order ID can contain only digits.
        self.order_id = order_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the page to return. Set this parameter to an integer that is greater than 0. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: **30**, **50**, and **100**. Default value: 30.
        self.page_size = page_size
        # The latest start time of the task that you specified when you created the scheduled task. The time is displayed in UTC.
        self.planned_end_time = planned_end_time
        # The earliest start time of the task that you specified when you created the scheduled task. The time is displayed in UTC.
        self.planned_start_time = planned_start_time
        # The ID of the region.
        # 
        # > 
        # 
        # *   You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the region information of all clusters in a specific account.
        # 
        # *   If you do not specify this parameter, scheduled tasks on your clusters that are deployed in all regions are queried.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The state of the tasks that you want to query. Valid values:
        # 
        # *   **pending**: The tasks are pending execution.
        # *   **executing**: The tasks are being executed.
        # *   **failure**: The tasks failed and need to be run again.
        # *   **finish**: The tasks are complete.
        # *   **cancel**: The tasks are canceled.
        # *   **expired**: The tasks are expired. The tasks are not started within the time periods that are specified to start the tasks.
        # *   **rollback**: The tasks are being rolled back.
        # 
        # >  If you do not specify this parameter, all scheduled tasks in all states are queried.
        self.status = status
        # The type of scheduled tasks that you want to query. Valid values:
        # 
        # *   **CreateDBNodes**
        # *   **ModifyDBNodeClass**
        # *   **UpgradeDBClusterVersion**
        # *   **ModifyDBClusterPrimaryZone**
        # 
        # > 
        # 
        # *   If you specify the `PlannedStartTime` parameter when you call the four preceding operations, the details of each task are returned. Otherwise, an empty string is returned for the `TimerInfos` parameter.
        # 
        # *   If you do not specify this parameter, all types of scheduled tasks on you clusters are queried.
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.planned_end_time is not None:
            result['PlannedEndTime'] = self.planned_end_time

        if self.planned_start_time is not None:
            result['PlannedStartTime'] = self.planned_start_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlannedEndTime') is not None:
            self.planned_end_time = m.get('PlannedEndTime')

        if m.get('PlannedStartTime') is not None:
            self.planned_start_time = m.get('PlannedStartTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        return self

