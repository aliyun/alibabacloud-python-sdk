# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListVirusScanTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.ListVirusScanTasksResponseBodyTasks] = None,
        total_num: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of virus scan tasks.
        self.tasks = tasks
        # The total number of virus scan tasks.
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
                temp_model = main_models.ListVirusScanTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListVirusScanTasksResponseBodyTasks(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        custom_match_group: List[main_models.ListVirusScanTasksResponseBodyTasksCustomMatchGroup] = None,
        end_time: int = None,
        high_risk_operation: str = None,
        low_risk_operation: str = None,
        match_mode: str = None,
        match_target_infos: List[main_models.ListVirusScanTasksResponseBodyTasksMatchTargetInfos] = None,
        max_cpu_usage: int = None,
        mid_risk_operation: str = None,
        performance_mode: str = None,
        scan_mode: str = None,
        scan_path: List[str] = None,
        scan_targets: List[str] = None,
        status: int = None,
        task_description: str = None,
        task_id: str = None,
        whitelist: List[str] = None,
    ):
        # The time when the task was created, in the yyyy-MM-dd HH:mm:ss format. The time is in the UTC+8 time zone.
        self.create_time = create_time
        # The effective scope specified by organizational structure.
        self.custom_match_group = custom_match_group
        # The time when the task expires, in seconds-level UNIX timestamp format.
        self.end_time = end_time
        # The action to take on high-risk virus files. Valid values:
        # - **Quarantine**: Quarantine quarantined file.
        # - **Notify**: Report an alert only without taking action on quarantined file.
        self.high_risk_operation = high_risk_operation
        # The action to take on low-risk virus files. Valid values:
        # - **Quarantine**: Quarantine quarantined file.
        # - **Notify**: Report an alert only without taking action on quarantined file.
        # - **None**: Take no action.
        self.low_risk_operation = low_risk_operation
        # The matching mode for the effective scope. Valid values:
        # - **UserGroupAll**: Applies to all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: Applies only to users in specified user groups.
        self.match_mode = match_mode
        # The collection of user groups to which the task applies.
        self.match_target_infos = match_target_infos
        # The maximum percentage of endpoint CPU usage allowed during scanning.
        self.max_cpu_usage = max_cpu_usage
        # The action to take on medium-risk virus files. Valid values:
        # - **Quarantine**: Quarantine quarantined file.
        # - **Notify**: Report an alert only without taking action on quarantined file.
        self.mid_risk_operation = mid_risk_operation
        # The scan performance schema pattern. Valid values:
        # - **SecurityFirst**: Security first. The default CPU usage upper limit is 50%.
        # - **Balance**: Balanced. The default CPU usage upper limit is 30%.
        # - **ExperienceFirst**: Experience first. The default CPU usage upper limit is 15%.
        self.performance_mode = performance_mode
        # The scan path scope. Valid values:
        # - **Quick**: Quick scan. Only scans critical system directories and common risk locations.
        # - **Full**: Full scan.
        # - **Custom**: Custom path scan.
        self.scan_mode = scan_mode
        # The collection of custom scan paths.
        self.scan_path = scan_path
        # The collection of virus types to be handled in this scan.
        self.scan_targets = scan_targets
        # The task status. Valid values:
        # - **0**: Not canceled.
        # - **1**: Canceled.
        self.status = status
        # The description of the task.
        self.task_description = task_description
        # The ID of the virus scan task.
        self.task_id = task_id
        # The list of exempted users.
        self.whitelist = whitelist

    def validate(self):
        if self.custom_match_group:
            for v1 in self.custom_match_group:
                 if v1:
                    v1.validate()
        if self.match_target_infos:
            for v1 in self.match_target_infos:
                 if v1:
                    v1.validate()

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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.high_risk_operation is not None:
            result['HighRiskOperation'] = self.high_risk_operation

        if self.low_risk_operation is not None:
            result['LowRiskOperation'] = self.low_risk_operation

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        result['MatchTargetInfos'] = []
        if self.match_target_infos is not None:
            for k1 in self.match_target_infos:
                result['MatchTargetInfos'].append(k1.to_map() if k1 else None)

        if self.max_cpu_usage is not None:
            result['MaxCpuUsage'] = self.max_cpu_usage

        if self.mid_risk_operation is not None:
            result['MidRiskOperation'] = self.mid_risk_operation

        if self.performance_mode is not None:
            result['PerformanceMode'] = self.performance_mode

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.scan_path is not None:
            result['ScanPath'] = self.scan_path

        if self.scan_targets is not None:
            result['ScanTargets'] = self.scan_targets

        if self.status is not None:
            result['Status'] = self.status

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        if self.task_id is not None:
            result['TaskId'] = self.task_id

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
                temp_model = main_models.ListVirusScanTasksResponseBodyTasksCustomMatchGroup()
                self.custom_match_group.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HighRiskOperation') is not None:
            self.high_risk_operation = m.get('HighRiskOperation')

        if m.get('LowRiskOperation') is not None:
            self.low_risk_operation = m.get('LowRiskOperation')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        self.match_target_infos = []
        if m.get('MatchTargetInfos') is not None:
            for k1 in m.get('MatchTargetInfos'):
                temp_model = main_models.ListVirusScanTasksResponseBodyTasksMatchTargetInfos()
                self.match_target_infos.append(temp_model.from_map(k1))

        if m.get('MaxCpuUsage') is not None:
            self.max_cpu_usage = m.get('MaxCpuUsage')

        if m.get('MidRiskOperation') is not None:
            self.mid_risk_operation = m.get('MidRiskOperation')

        if m.get('PerformanceMode') is not None:
            self.performance_mode = m.get('PerformanceMode')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('ScanPath') is not None:
            self.scan_path = m.get('ScanPath')

        if m.get('ScanTargets') is not None:
            self.scan_targets = m.get('ScanTargets')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class ListVirusScanTasksResponseBodyTasksMatchTargetInfos(DaraModel):
    def __init__(
        self,
        target_id: str = None,
        target_name: str = None,
    ):
        # The ID of the user group.
        self.target_id = target_id
        # The name of the user group.
        self.target_name = target_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        return self

class ListVirusScanTasksResponseBodyTasksCustomMatchGroup(DaraModel):
    def __init__(
        self,
        group: List[str] = None,
        idp_id: str = None,
    ):
        # The collection of organizational structure nodes.
        self.group = group
        # The ID of the identity provider.
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

