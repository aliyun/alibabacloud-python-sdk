# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDlpOutboundLogsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        log_id: str = None,
        page_size: int = None,
        policy_action: str = None,
        src_file_name: str = None,
        start_time: int = None,
        sub_channel_type: str = None,
        user_name: str = None,
    ):
        # The current page number, starting from 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end time of the query. UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The log ID.
        self.log_id = log_id
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The policy action. Single-value exact match.
        self.policy_action = policy_action
        # The original file name. Fuzzy match.
        self.src_file_name = src_file_name
        # The start time of the query. UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The secondary channel ID in the format of `PrimaryChannelID.SubChannelID`. Separate multiple values with commas.
        self.sub_channel_type = sub_channel_type
        # The username. Exact match.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action

        if self.src_file_name is not None:
            result['SrcFileName'] = self.src_file_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_channel_type is not None:
            result['SubChannelType'] = self.sub_channel_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')

        if m.get('SrcFileName') is not None:
            self.src_file_name = m.get('SrcFileName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubChannelType') is not None:
            self.sub_channel_type = m.get('SubChannelType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

