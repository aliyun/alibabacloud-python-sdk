# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomScenePoliciesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policy_id: int = None,
    ):
        # The number of the page to return. Valid values: **1 to 100000**.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. Valid values: **5**, **10**, or **20**.
        self.page_size = page_size
        # The rule ID.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

