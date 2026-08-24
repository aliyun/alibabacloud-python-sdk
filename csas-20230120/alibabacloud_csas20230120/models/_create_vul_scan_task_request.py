# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVulScanTaskRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        match_mode: str = None,
        task_description: str = None,
        task_name: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The task expiration time, in seconds-level UNIX timestamp. After this time is reached, endpoints no longer pull and execute this task, and incomplete scans are not continued.
        self.end_timestamp = end_timestamp
        # The matching mode for the effective scope. Valid values:
        # 
        # - **UserGroupAll**: Takes effect for all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: Takes effect only for users in specified user groups. In this case, UserGroupIds is required.
        # 
        # This parameter is required.
        self.match_mode = match_mode
        # The task description.
        self.task_description = task_description
        # The task name. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The collection of user group IDs for which the task takes effect. This parameter is required when MatchMode is set to UserGroupNormal and cannot be specified when MatchMode is set to UserGroupAll. The collection must contain at least 1 and at most 100 entries. Duplicate values are not allowed.
        self.user_group_ids = user_group_ids
        # The list of exempt usernames. Users in this list are excluded from this scan. The list can contain up to 1000 entries. Duplicate values are not allowed.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

