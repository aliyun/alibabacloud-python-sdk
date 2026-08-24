# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVirusScanScheduledStrategiesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        performance_modes: List[str] = None,
        scan_modes: List[str] = None,
        status: str = None,
        strategy_ids: List[str] = None,
        strategy_name: str = None,
        user_group_id: str = None,
    ):
        # The page number of the current page in paging. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page in paging. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The collection of scan performance modes. Duplicate values are not allowed.
        self.performance_modes = performance_modes
        # The collection of scan path scopes. Duplicate values are not allowed.
        self.scan_modes = scan_modes
        # Filters policies by enabled status. Valid values:
        # - **Enabled**: enabled.
        # - **Disabled**: disabled.
        self.status = status
        # The collection of virus scheduled scan policy IDs. Duplicate values are not allowed.
        self.strategy_ids = strategy_ids
        # The policy name. Fuzzy match is supported. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-).
        self.strategy_name = strategy_name
        # The user group ID. This parameter is used to filter policies whose effective scope includes the specified user group. You can obtain the value from:
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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.performance_modes is not None:
            result['PerformanceModes'] = self.performance_modes

        if self.scan_modes is not None:
            result['ScanModes'] = self.scan_modes

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_ids is not None:
            result['StrategyIds'] = self.strategy_ids

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PerformanceModes') is not None:
            self.performance_modes = m.get('PerformanceModes')

        if m.get('ScanModes') is not None:
            self.scan_modes = m.get('ScanModes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyIds') is not None:
            self.strategy_ids = m.get('StrategyIds')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

