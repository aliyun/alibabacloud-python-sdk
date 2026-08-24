# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAntiVirusRealTimeDefenceStrategyResponseBody(DaraModel):
    def __init__(
        self,
        high_risk_operation: str = None,
        low_risk_operation: str = None,
        match_mode: str = None,
        mid_risk_operation: str = None,
        request_id: str = None,
        scan_targets: List[str] = None,
        status: str = None,
        strategy_id: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The action to take on high-risk virus files. Valid values:
        # - **Quarantine**: Quarantines quarantined file.
        # - **Notify**: Reports an alert only without taking action on quarantined file. Quarantine is returned if no real-time defense policy has been configured.
        self.high_risk_operation = high_risk_operation
        # The action to take on low-risk virus files. Valid values:
        # - **Quarantine**: Quarantines quarantined file.
        # - **Notify**: Reports an alert only without taking action on quarantined file.
        # - **None**: Takes no action. None is returned if no real-time defense policy has been configured.
        self.low_risk_operation = low_risk_operation
        # The matching mode for the effective scope. Valid values:
        # - **UserGroupAll**: Applies to all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: Applies only to users in specified user groups. An empty string is returned if no real-time defense policy has been configured.
        self.match_mode = match_mode
        # The action to take on medium-risk virus files. Valid values:
        # - **Quarantine**: Quarantines quarantined file.
        # - **Notify**: Reports an alert only without taking action on quarantined file. Notify is returned if no real-time defense policy has been configured.
        self.mid_risk_operation = mid_risk_operation
        # The request ID.
        self.request_id = request_id
        # The collection of virus types to be handled by real-time defense. An empty list is returned if no real-time defense policy has been configured.
        self.scan_targets = scan_targets
        # The enabling status. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled. This value is returned if no real-time defense policy has been configured.
        self.status = status
        # The real-time defense policy ID. An empty string is returned if no real-time defense policy has been configured.
        self.strategy_id = strategy_id
        # The collection of user group IDs to which the policy applies. An empty list is returned when MatchMode is set to UserGroupAll.
        self.user_group_ids = user_group_ids
        # The exception user list. Users in this list are excluded from real-time defense. An empty list is returned if no exception users are configured.
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

        if self.mid_risk_operation is not None:
            result['MidRiskOperation'] = self.mid_risk_operation

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_targets is not None:
            result['ScanTargets'] = self.scan_targets

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

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

        if m.get('MidRiskOperation') is not None:
            self.mid_risk_operation = m.get('MidRiskOperation')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanTargets') is not None:
            self.scan_targets = m.get('ScanTargets')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

