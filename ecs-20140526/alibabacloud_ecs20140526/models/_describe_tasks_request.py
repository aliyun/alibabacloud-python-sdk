# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeTasksRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
        task_action: str = None,
        task_group_id: str = None,
        task_ids: str = None,
        task_status: str = None,
    ):
        # The end of the creation time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the results.
        # 
        # Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. Valid values of N: 1 to 100.
        self.resource_ids = resource_ids
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the creation time range to query. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The name of the API operation associated with the task. Valid values:
        # 
        # - ImportImage: import an image.
        # - ExportImage: export an image.
        # - RedeployInstance: redeploy an ECS instance.
        # - ModifyDiskSpec: change the cloud disk type.
        # - ArchiveSnapshot: archive a snapshot.
        self.task_action = task_action
        # The task group ID.
        # 
        # > This parameter is in invitational preview. When this parameter is specified, other query conditions do not take effect.
        self.task_group_id = task_group_id
        # The task IDs. You can specify up to 100 task IDs at a time. Separate multiple IDs with commas (,).
        self.task_ids = task_ids
        # The task status. Valid values:
        # 
        # - Finished: The task is complete.
        # - Processing: The task is running.
        # - Failed: The task has failed.
        # 
        # Default value: null.
        # 
        # > Only tasks in the Finished, Processing, or Failed state can be queried. Other values do not take effect.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        if self.task_group_id is not None:
            result['TaskGroupId'] = self.task_group_id

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        if m.get('TaskGroupId') is not None:
            self.task_group_id = m.get('TaskGroupId')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

