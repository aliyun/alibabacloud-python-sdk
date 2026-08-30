# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDomainAccessLogsRequest(DaraModel):
    def __init__(
        self,
        block_action: str = None,
        current_page: int = None,
        department: str = None,
        end_time: int = None,
        page_size: int = None,
        policy_type: str = None,
        remote_host: str = None,
        start_time: int = None,
        user_name: str = None,
    ):
        # The action taken upon a rule hit. Exact match is used. Valid values:
        # 
        # - Audit: Audit.
        # - Observe: Observe only.
        # - WhiteList: Allowed by whitelist.
        # - Block: Blocked.
        # - Redirect: Redirected to a prompt page.
        self.block_action = block_action
        # The current page number.
        self.current_page = current_page
        # The department. Exact match is used.
        self.department = department
        # The end time of the query. This value is a UNIX timestamp in seconds.
        self.end_time = end_time
        # The number of entries per page in paging. Valid values: 1 to 1000.
        self.page_size = page_size
        # The policy type used to filter results.
        self.policy_type = policy_type
        # The destination domain name accessed. Exact match is used.
        self.remote_host = remote_host
        # The start time of the query. This value is a UNIX timestamp in seconds.
        self.start_time = start_time
        # The username. Exact match is used.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_action is not None:
            result['BlockAction'] = self.block_action

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.remote_host is not None:
            result['RemoteHost'] = self.remote_host

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockAction') is not None:
            self.block_action = m.get('BlockAction')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RemoteHost') is not None:
            self.remote_host = m.get('RemoteHost')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

