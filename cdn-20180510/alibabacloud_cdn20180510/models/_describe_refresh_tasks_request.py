# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRefreshTasksRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        object_path: str = None,
        object_type: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        security_token: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The accelerated domain name. You can specify only one accelerated domain name in each call. By default, this operation queries the status of tasks for all accelerated domain names.
        self.domain_name = domain_name
        # The end time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The path of the object. The path is used as a condition for exact matching.
        self.object_path = object_path
        # The type of the task. Valid values:
        # 
        # *   **file**: refreshes one or more files.
        # *   **directory**: refreshes files in specific directories.
        # *   **regex**: refreshes content based on a regular expression.
        # *   **preload**: prefetches one or more files.
        # 
        # > If you set the **DomainName** or **Status** parameter, you must also set the **ObjectType** parameter.
        self.object_type = object_type
        self.owner_id = owner_id
        # The number of the page to return. Valid values: **1** to **100000**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **20**. Maximum value: **100**. Valid values: **1** to **100**.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.security_token = security_token
        # The start of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The status of the task. Valid values:
        # 
        # *   **Complete**: The task is complete.
        # *   **Refreshing**: The task is in progress.
        # *   **Failed**: The task failed.
        self.status = status
        # The ID of the task that you want to query.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.object_path is not None:
            result['ObjectPath'] = self.object_path

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

