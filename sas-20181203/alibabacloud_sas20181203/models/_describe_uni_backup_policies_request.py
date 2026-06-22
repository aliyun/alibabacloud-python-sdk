# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUniBackupPoliciesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        policy_name: str = None,
    ):
        # The page number from which to start displaying query results. Default value: **1**, which indicates that query results are displayed starting from page 1.
        self.current_page = current_page
        # The maximum number of entries to display per page for a paginated query. The default number of entries per page is 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # > We recommend that you do not leave PageSize empty.
        self.page_size = page_size
        # The name of the database anti-ransomware backup policy.
        self.policy_name = policy_name

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

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

