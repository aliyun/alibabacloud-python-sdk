# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopGroupSessionsRequest(DaraModel):
    def __init__(
        self,
        desktop_group_ids: List[str] = None,
        desktop_group_name: str = None,
        end_time: str = None,
        end_user_id: str = None,
        fill_terminal_info: bool = None,
        language: str = None,
        max_results: int = None,
        next_token: str = None,
        own_type: int = None,
        region_id: str = None,
        session_status: str = None,
        start_time: str = None,
    ):
        # The IDs of shared desktop groups.
        self.desktop_group_ids = desktop_group_ids
        # The name of the shared desktop.
        self.desktop_group_name = desktop_group_name
        # The end of the time range to query.
        self.end_time = end_time
        # The user ID of the terminal that connects to the session.
        self.end_user_id = end_user_id
        # Whether to supplement terminal information.
        self.fill_terminal_info = fill_terminal_info
        # The language of the response.
        self.language = language
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The type of the session.
        # 
        # Valid values:
        # 
        # *   0: single-session
        # *   1: multi-session
        self.own_type = own_type
        # The ID of the region. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        self.region_id = region_id
        # The status of the session.
        # 
        # Valid values:
        # 
        # *   Connected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Disconnected
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.session_status = session_status
        # The beginning of the time range to query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.fill_terminal_info is not None:
            result['FillTerminalInfo'] = self.fill_terminal_info

        if self.language is not None:
            result['Language'] = self.language

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.own_type is not None:
            result['OwnType'] = self.own_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_status is not None:
            result['SessionStatus'] = self.session_status

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FillTerminalInfo') is not None:
            self.fill_terminal_info = m.get('FillTerminalInfo')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

