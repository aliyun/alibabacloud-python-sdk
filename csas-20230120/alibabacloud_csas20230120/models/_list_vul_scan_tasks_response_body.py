# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVulScanTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.ListVulScanTasksResponseBodyTasks] = None,
        total_num: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of vulnerability scanning tasks.
        self.tasks = tasks
        # The total number of vulnerability scanning tasks that match the query conditions.
        self.total_num = total_num

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ListVulScanTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListVulScanTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        custom_match_group: List[main_models.ListVulScanTasksResponseBodyTasksCustomMatchGroup] = None,
        end_timestamp: int = None,
        match_mode: str = None,
        match_target_ids: List[str] = None,
        scheduled_strategy_id: str = None,
        status: str = None,
        target_device_count: main_models.ListVulScanTasksResponseBodyTasksTargetDeviceCount = None,
        task_description: str = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
        vul_count: int = None,
        whitelist: List[str] = None,
    ):
        # The task creation time, in seconds-level UNIX timestamp.
        self.create_time = create_time
        # The effective scope specified by organizational structure. An empty list is returned if no organizational structure is configured.
        self.custom_match_group = custom_match_group
        # The task expiration time, in seconds-level UNIX timestamp. After this time, endpoints no longer pull and execute this task.
        self.end_timestamp = end_timestamp
        # The matching mode of the effective scope. Valid values:
        # - **UserGroupAll**: applies to all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: applies only to users within specified user groups.
        self.match_mode = match_mode
        # The collection of effective user group IDs. An empty list is returned when MatchMode is UserGroupAll.
        self.match_target_ids = match_target_ids
        # The ID of the vulnerability scheduled scan policy that triggered this task. An empty string is returned when TaskType is Instant.
        self.scheduled_strategy_id = scheduled_strategy_id
        # The task status. Valid values:
        # - **Running**: the task is in progress and still within the validity period.
        # - **Expired**: the task has expired and exceeded the validity period.
        # - **Canceled**: the task has been canceled.
        self.status = status
        # The execution statistics of this task on user endpoint devices within the effective scope.
        self.target_device_count = target_device_count
        # The task description. An empty string is returned if no description is specified.
        self.task_description = task_description
        # The vulnerability scanning task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The task type. Valid values:
        # - **Instant**: an instant task created by CreateVulScanTask.
        # - **Scheduled**: a scheduled task automatically created by a vulnerability scheduled scan policy on a periodic basis.
        self.task_type = task_type
        # The total number of vulnerabilities detected by this task.
        self.vul_count = vul_count
        # The list of exempted users. Users in this list are excluded from the scan. An empty list is returned if no exemption is configured.
        self.whitelist = whitelist

    def validate(self):
        if self.custom_match_group:
            for v1 in self.custom_match_group:
                 if v1:
                    v1.validate()
        if self.target_device_count:
            self.target_device_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['CustomMatchGroup'] = []
        if self.custom_match_group is not None:
            for k1 in self.custom_match_group:
                result['CustomMatchGroup'].append(k1.to_map() if k1 else None)

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.match_target_ids is not None:
            result['MatchTargetIds'] = self.match_target_ids

        if self.scheduled_strategy_id is not None:
            result['ScheduledStrategyId'] = self.scheduled_strategy_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target_device_count is not None:
            result['TargetDeviceCount'] = self.target_device_count.to_map()

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.custom_match_group = []
        if m.get('CustomMatchGroup') is not None:
            for k1 in m.get('CustomMatchGroup'):
                temp_model = main_models.ListVulScanTasksResponseBodyTasksCustomMatchGroup()
                self.custom_match_group.append(temp_model.from_map(k1))

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MatchTargetIds') is not None:
            self.match_target_ids = m.get('MatchTargetIds')

        if m.get('ScheduledStrategyId') is not None:
            self.scheduled_strategy_id = m.get('ScheduledStrategyId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetDeviceCount') is not None:
            temp_model = main_models.ListVulScanTasksResponseBodyTasksTargetDeviceCount()
            self.target_device_count = temp_model.from_map(m.get('TargetDeviceCount'))

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class ListVulScanTasksResponseBodyTasksTargetDeviceCount(DaraModel):
    def __init__(
        self,
        ack_count: int = None,
        fail_count: int = None,
        start_count: int = None,
        success_count: int = None,
    ):
        # The number of user endpoint devices that have acknowledged receipt of this task.
        self.ack_count = ack_count
        # The number of user endpoint devices on which the scan failed.
        self.fail_count = fail_count
        # The number of user endpoint devices currently executing the scan. This value is calculated by subtracting SuccessCount and FailCount from AckCount.
        self.start_count = start_count
        # The number of user endpoint devices on which the scan succeeded.
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_count is not None:
            result['AckCount'] = self.ack_count

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.start_count is not None:
            result['StartCount'] = self.start_count

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckCount') is not None:
            self.ack_count = m.get('AckCount')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('StartCount') is not None:
            self.start_count = m.get('StartCount')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

class ListVulScanTasksResponseBodyTasksCustomMatchGroup(DaraModel):
    def __init__(
        self,
        group: List[str] = None,
        idp_id: str = None,
    ):
        # The collection of organizational structure nodes.
        self.group = group
        # The identity provider ID.
        self.idp_id = idp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        return self

