# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApprovalProcessesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        policy_id: str = None,
        policy_type: str = None,
        process_ids: List[str] = None,
        process_name: str = None,
        sase_user_id: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        self.policy_id = policy_id
        self.policy_type = policy_type
        self.process_ids = process_ids
        self.process_name = process_name
        self.sase_user_id = sase_user_id
        self.username = username

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

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.process_ids is not None:
            result['ProcessIds'] = self.process_ids

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('ProcessIds') is not None:
            self.process_ids = m.get('ProcessIds')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

