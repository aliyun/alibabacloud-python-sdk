# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVulScanTasksRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        match_mode: str = None,
        page_size: int = None,
        scheduled_strategy_id: str = None,
        status: str = None,
        task_ids: List[str] = None,
        task_name: str = None,
        task_type: str = None,
        user_group_id: str = None,
    ):
        # The page number of the current page in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Filters by the matching mode of the effective scope. Valid values:
        # - **UserGroupAll**: applies to all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: applies only to users within specified user groups.
        self.match_mode = match_mode
        # The number of entries per page in a paged query. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the vulnerability scheduled scan policy. This parameter is used to filter tasks triggered by the specified policy. Valid values are obtained from:
        # - [ListVulScanScheduledStrategies](~~ListVulScanScheduledStrategies~~): lists vulnerability scheduled scan policies.
        # - [CreateVulScanScheduledStrategy](~~CreateVulScanScheduledStrategy~~): creates a vulnerability scheduled scan policy.
        self.scheduled_strategy_id = scheduled_strategy_id
        # Filters by task status. Valid values:
        # - **Running**: the task is in progress and still within the validity period.
        # - **Expired**: the task has expired and exceeded the validity period.
        # - **Canceled**: the task has been canceled.
        self.status = status
        # The vulnerability scanning task IDs used for filtering. A maximum of 100 IDs can be specified. Duplicate IDs are not allowed.
        self.task_ids = task_ids
        # The task name. Fuzzy match is supported. The name can be up to 128 characters in length.
        self.task_name = task_name
        # Filters by task type. Valid values:
        # - **Instant**: an instant task created by CreateVulScanTask.
        # - **Scheduled**: a scheduled task automatically created by a vulnerability scheduled scan policy on a periodic basis.
        self.task_type = task_type
        # The user group ID. This parameter is used to filter records whose effective scope includes the specified user group. Valid values are obtained from:
        # - [ListUserGroups](~~ListUserGroups~~): lists user groups.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scheduled_strategy_id is not None:
            result['ScheduledStrategyId'] = self.scheduled_strategy_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScheduledStrategyId') is not None:
            self.scheduled_strategy_id = m.get('ScheduledStrategyId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

