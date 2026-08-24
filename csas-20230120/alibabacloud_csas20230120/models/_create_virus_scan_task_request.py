# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateVirusScanTaskRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        high_risk_operation: str = None,
        low_risk_operation: str = None,
        match_mode: str = None,
        max_cpu_usage: int = None,
        mid_risk_operation: str = None,
        performance_mode: str = None,
        scan_mode: str = None,
        scan_path: List[str] = None,
        scan_targets: List[str] = None,
        task_description: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The task expiration time, in seconds-level UNIX timestamp. After this time, endpoints no longer pull and execute this task. If this parameter is not specified or the specified time is earlier than the current time, the value defaults to the current time plus 24 hours.
        self.end_time = end_time
        # The action to take on high-risk virus files. Valid values:
        # - **Quarantine**: quarantine quarantined file.
        # - **Notify**: report an alert only without taking action on quarantined file.
        # 
        # This parameter is required.
        self.high_risk_operation = high_risk_operation
        # The action to take on low-risk virus files. Valid values:
        # - **Quarantine**: quarantine quarantined file.
        # - **Notify**: report an alert only without taking action on quarantined file.
        # - **None**: take no action.
        # 
        # This parameter is required.
        self.low_risk_operation = low_risk_operation
        # The matching mode for the effective scope. Valid values:
        # - **UserGroupAll**: applies to all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: applies only to users in specified user groups. UserGroupIds is required when this value is specified.
        # 
        # This parameter is required.
        self.match_mode = match_mode
        # The maximum percentage of endpoint CPU usage during scanning. Valid values: 0 to 100. If this parameter is not specified or is set to 0, the default value is determined by PerformanceMode: 50 for SecurityFirst, 30 for Balance, and 15 for ExperienceFirst.
        self.max_cpu_usage = max_cpu_usage
        # The action to take on medium-risk virus files. Valid values:
        # - **Quarantine**: quarantine quarantined file.
        # - **Notify**: report an alert only without taking action on quarantined file.
        # 
        # This parameter is required.
        self.mid_risk_operation = mid_risk_operation
        # The scan performance pattern. Valid values:
        # - **SecurityFirst**: security first. The default CPU usage limit is 50%.
        # - **Balance**: balanced. The default CPU usage limit is 30%.
        # - **ExperienceFirst**: experience first. The default CPU usage limit is 15%.
        # 
        # This parameter is required.
        self.performance_mode = performance_mode
        # The scan path scope. Valid values:
        # - **Quick**: quick scan. Only system critical directories and common risk locations are scanned.
        # - **Full**: full disk scan.
        # - **Custom**: custom path scan. ScanPath is required when this value is specified.
        # 
        # This parameter is required.
        self.scan_mode = scan_mode
        # The collection of custom scan paths. This parameter is required when ScanMode is set to Custom and cannot be specified when ScanMode is set to Quick or Full. A maximum of 100 paths can be specified. Duplicate values are not allowed.
        self.scan_path = scan_path
        # The collection of virus types to be handled in this scan. At least one type must be specified. Duplicate values are not allowed.
        # 
        # This parameter is required.
        self.scan_targets = scan_targets
        # The task description. The description can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, spaces, periods (.), commas (,), semicolons (;), forward slashes (/), at signs (@), hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.task_description = task_description
        # The collection of user group IDs to which the task applies. This parameter is required when MatchMode is set to UserGroupNormal and cannot be specified when MatchMode is set to UserGroupAll. At least 1 and at most 100 IDs can be specified. Duplicate values are not allowed.
        self.user_group_ids = user_group_ids
        # The list of exempt users. Users in this list do not execute this scan task. A maximum of 1000 users can be specified. Duplicate values are not allowed.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.high_risk_operation is not None:
            result['HighRiskOperation'] = self.high_risk_operation

        if self.low_risk_operation is not None:
            result['LowRiskOperation'] = self.low_risk_operation

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

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

        if self.task_description is not None:
            result['TaskDescription'] = self.task_description

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HighRiskOperation') is not None:
            self.high_risk_operation = m.get('HighRiskOperation')

        if m.get('LowRiskOperation') is not None:
            self.low_risk_operation = m.get('LowRiskOperation')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

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

        if m.get('TaskDescription') is not None:
            self.task_description = m.get('TaskDescription')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

