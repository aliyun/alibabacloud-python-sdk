# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAntiVirusRealTimeDefenceStrategyRequest(DaraModel):
    def __init__(
        self,
        high_risk_operation: str = None,
        low_risk_operation: str = None,
        match_mode: str = None,
        max_cpu_usage: int = None,
        mid_risk_operation: str = None,
        scan_targets: List[str] = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The action to take on high-risk virus files. Required when configuring the real-time defense policy for the first time. Valid values:
        # - **Quarantine**: Quarantines quarantined file.
        # - **Notify**: Reports an alert only without taking action on quarantined file.
        self.high_risk_operation = high_risk_operation
        # The action to take on low-risk virus files. Required when configuring the real-time defense policy for the first time. Valid values:
        # - **Quarantine**: Quarantines quarantined file.
        # - **Notify**: Reports an alert only without taking action on quarantined file.
        # - **None**: Takes no action.
        self.low_risk_operation = low_risk_operation
        # The matching mode for the effective scope. Required when configuring the real-time defense policy for the first time. Valid values:
        # - **UserGroupAll**: Applies to all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: Applies only to users in specified user groups. UserGroupIds is required in this case.
        self.match_mode = match_mode
        # The maximum percentage of endpoint CPU that real-time defense can consume. Valid values: 0 to 100. When configuring for the first time, the value is stored as 0 but takes effect as 30.
        self.max_cpu_usage = max_cpu_usage
        # The action to take on medium-risk virus files. Required when configuring the real-time defense policy for the first time. Valid values:
        # - **Quarantine**: Quarantines quarantined file.
        # - **Notify**: Reports an alert only without taking action on quarantined file.
        self.mid_risk_operation = mid_risk_operation
        # The collection of virus types to be handled by real-time defense. Duplicates are not allowed. Required when configuring the real-time defense policy for the first time. When the policy already exists, this parameter performs a full replacement. The collection you pass in replaces the existing configuration.
        self.scan_targets = scan_targets
        # The enabling status. Required when configuring the real-time defense policy for the first time. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The collection of user group IDs to which the policy applies. Required when MatchMode is set to UserGroupNormal. Not allowed when MatchMode is set to UserGroupAll. At least 1 and at most 100 entries are allowed. Duplicates are not allowed. When MatchMode is UserGroupNormal, you must pass in the complete user group collection on every call, even when modifying only other parameters.
        self.user_group_ids = user_group_ids
        # The exception user list. Users in this list are excluded from real-time defense. A maximum of 1000 entries are allowed. Duplicates are not allowed. This parameter performs a full replacement. The list you pass in replaces the existing list.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.scan_targets is not None:
            result['ScanTargets'] = self.scan_targets

        if self.status is not None:
            result['Status'] = self.status

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('ScanTargets') is not None:
            self.scan_targets = m.get('ScanTargets')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

