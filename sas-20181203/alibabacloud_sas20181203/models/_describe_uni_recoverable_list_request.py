# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUniRecoverableListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        database: str = None,
        page_size: int = None,
        policy_id: int = None,
    ):
        # The number of the page from which query results start to be displayed. Default value: **1**. This value indicates that the results start from page 1.
        self.current_page = current_page
        # The database name.
        self.database = database
        # The maximum number of entries to display per page in a paged query. The default number of entries per page is 20. If PageSize is left empty, 20 entries are returned by default.
        # > Set PageSize to a non-empty value.
        self.page_size = page_size
        # The ID of the anti-ransomware backup policy for the database.
        # >Call the [DescribeUniBackupPolicies](~~DescribeUniBackupPolicies~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.database is not None:
            result['Database'] = self.database

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

