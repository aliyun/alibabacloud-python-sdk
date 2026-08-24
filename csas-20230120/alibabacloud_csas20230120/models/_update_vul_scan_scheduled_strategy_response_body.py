# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateVulScanScheduledStrategyResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        custom_match_group: List[main_models.UpdateVulScanScheduledStrategyResponseBodyCustomMatchGroup] = None,
        last_trigger_time: int = None,
        match_mode: str = None,
        match_target_ids: List[str] = None,
        priority: int = None,
        request_id: str = None,
        scan_begin_time: int = None,
        scan_end_time: int = None,
        scan_frequency: str = None,
        scan_interval: int = None,
        status: str = None,
        strategy_description: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        whitelist: List[str] = None,
    ):
        # The time when the policy was created, in seconds-level UNIX timestamp.
        self.create_time = create_time
        # The effective scope specified by organizational structure. An empty list is returned if the scope is not configured by organizational structure.
        self.custom_match_group = custom_match_group
        # The time when the policy last triggered a scan, in seconds-level UNIX timestamp. The value 0 is returned if the policy has never been triggered.
        self.last_trigger_time = last_trigger_time
        # The matching mode for the effective scope. Valid values:
        # - **UserGroupAll**: The policy takes effect on all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: The policy takes effect only on users in specified user groups.
        self.match_mode = match_mode
        # The collection of user group IDs for the effective scope. An empty list is returned when MatchMode is set to UserGroupAll.
        self.match_target_ids = match_target_ids
        # The policy priority. A smaller value indicates a higher priority. Valid values: 1 to 100.
        self.priority = priority
        # The request ID.
        self.request_id = request_id
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
        # The vulnerability scheduled scan policy ID.
        self.strategy_id = strategy_id
        # The policy name.
        self.strategy_name = strategy_name
        # The list of exempted users. Users in this list are not scanned by this policy. An empty list is returned if no exemption is configured.
        self.whitelist = whitelist

    def validate(self):
        if self.custom_match_group:
            for v1 in self.custom_match_group:
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

        if self.last_trigger_time is not None:
            result['LastTriggerTime'] = self.last_trigger_time

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.match_target_ids is not None:
            result['MatchTargetIds'] = self.match_target_ids

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.UpdateVulScanScheduledStrategyResponseBodyCustomMatchGroup()
                self.custom_match_group.append(temp_model.from_map(k1))

        if m.get('LastTriggerTime') is not None:
            self.last_trigger_time = m.get('LastTriggerTime')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MatchTargetIds') is not None:
            self.match_target_ids = m.get('MatchTargetIds')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class UpdateVulScanScheduledStrategyResponseBodyCustomMatchGroup(DaraModel):
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

