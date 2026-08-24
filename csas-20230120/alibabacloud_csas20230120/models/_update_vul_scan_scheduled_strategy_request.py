# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateVulScanScheduledStrategyRequest(DaraModel):
    def __init__(
        self,
        match_mode: str = None,
        priority: int = None,
        scan_begin_time: str = None,
        scan_end_time: str = None,
        scan_frequency: str = None,
        scan_interval: str = None,
        status: str = None,
        strategy_description: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The matching mode for the effective scope. Valid values:
        # - **UserGroupAll**: The policy takes effect on all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: The policy takes effect only on users in specified user groups. In this case, UserGroupIds is required.
        self.match_mode = match_mode
        # The policy priority. A smaller value indicates a higher priority. Valid values: 1 to 100.
        self.priority = priority
        # The start hour during which the scan can be triggered. The value is an integer hour. Valid values: 0 to 23, inclusive. This field is not a timestamp.
        self.scan_begin_time = scan_begin_time
        # The end hour during which the scan can be triggered. The value is an integer hour. Valid values: 1 to 24, exclusive. The value must be greater than ScanBeginTime. This field is not a timestamp.
        self.scan_end_time = scan_end_time
        # The unit of the trigger cycle. Valid values:
        # - **day**: by day.
        # - **week**: by week.
        self.scan_frequency = scan_frequency
        # The interval number of the trigger cycle. This parameter works together with ScanFrequency to determine the trigger cycle. Valid values: 1 to 30. For example, if ScanFrequency is set to week and ScanInterval is set to 1, the scan is triggered once a week.
        self.scan_interval = scan_interval
        # The enabling status. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The policy description.
        self.strategy_description = strategy_description
        # The ID of the vulnerability scheduled scan policy to modify. You can obtain the value from the following operations:
        # - [ListVulScanScheduledStrategies](~~ListVulScanScheduledStrategies~~): Lists vulnerability scheduled scan policies.
        # - [CreateVulScanScheduledStrategy](~~CreateVulScanScheduledStrategy~~): Creates a vulnerability scheduled scan policy.
        # 
        # This parameter is required.
        self.strategy_id = strategy_id
        # The policy name. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.strategy_name = strategy_name
        # The collection of user group IDs for the effective scope. This parameter is required when the effective scope is UserGroupNormal and must not be specified when the effective scope is UserGroupAll. The collection must contain at least 1 and at most 100 entries, and duplicates are not allowed. The collection you specify fully replaces the existing user groups of the policy.
        self.user_group_ids = user_group_ids
        # The list of exempted users. Users in this list are not scanned by this policy. The list can contain up to 1000 entries and duplicates are not allowed. This parameter performs a full overwrite. The list you specify replaces the existing list of the policy.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.scan_begin_time is not None:
            result['ScanBeginTime'] = self.scan_begin_time

        if self.scan_end_time is not None:
            result['ScanEndTime'] = self.scan_end_time

        if self.scan_frequency is not None:
            result['ScanFrequency'] = self.scan_frequency

        if self.scan_interval is not None:
            result['ScanInterval'] = self.scan_interval

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ScanBeginTime') is not None:
            self.scan_begin_time = m.get('ScanBeginTime')

        if m.get('ScanEndTime') is not None:
            self.scan_end_time = m.get('ScanEndTime')

        if m.get('ScanFrequency') is not None:
            self.scan_frequency = m.get('ScanFrequency')

        if m.get('ScanInterval') is not None:
            self.scan_interval = m.get('ScanInterval')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

