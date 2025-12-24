# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUsersInGroupRequest(DaraModel):
    def __init__(
        self,
        connect_state: int = None,
        desktop_group_id: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        org_id: str = None,
        query_user_detail: bool = None,
        region_id: str = None,
    ):
        # The status of the desktop connection for the end user.
        # 
        # Valid values:
        # 
        # - 0: Disconnected.
        # - 1: Connected.
        self.connect_state = connect_state
        # The ID of the cloud computer share.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The ID of the authorized user.
        self.end_user_id = end_user_id
        # The IDs of the authorized users.
        self.end_user_ids = end_user_ids
        # The query string for fuzzy match. If you specify this parameter, the system returns all results that contain the string.
        self.filter = filter
        # The number of entries to return on each page.
        # 
        # *   Maximum value: 100.
        # *   Default value: 10.
        self.max_results = max_results
        # The token that determines the start point of the next query. If this parameter is left empty, all results are returned.
        self.next_token = next_token
        # The ID of the organization to which the end user belongs.
        self.org_id = org_id
        # Specifies whether to query user details.
        # 
        # Valid values:
        # 
        # *   true (default)
        # *   false
        self.query_user_detail = query_user_detail
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_state is not None:
            result['ConnectState'] = self.connect_state

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.query_user_detail is not None:
            result['QueryUserDetail'] = self.query_user_detail

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectState') is not None:
            self.connect_state = m.get('ConnectState')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('QueryUserDetail') is not None:
            self.query_user_detail = m.get('QueryUserDetail')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

