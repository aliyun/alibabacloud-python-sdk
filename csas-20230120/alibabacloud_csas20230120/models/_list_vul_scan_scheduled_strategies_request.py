# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVulScanScheduledStrategiesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        match_mode: str = None,
        page_size: int = None,
        status: str = None,
        strategy_ids: List[str] = None,
        strategy_name: str = None,
        user_group_id: str = None,
    ):
        # The page number of the current page in a paging query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Filters by the matching mode of the effective scope. Valid values:
        # - **UserGroupAll**: Takes effect for all users under the current Alibaba Cloud account.
        # - **UserGroupNormal**: Takes effect only for users in specified user groups.
        self.match_mode = match_mode
        # The number of entries per page in a paging query. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Filters by enabled status. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The IDs of scheduled vulnerability scan policies used for filtering. A maximum of 100 IDs can be specified. Duplicate IDs are not allowed.
        self.strategy_ids = strategy_ids
        # The policy name. Fuzzy match is supported. The name can be up to 128 characters in length.
        self.strategy_name = strategy_name
        # The user group ID. Used to filter records whose effective scope includes the specified user group. You can obtain the value from the following operation:
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

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyIds') is not None:
            self.strategy_ids = m.get('StrategyIds')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

