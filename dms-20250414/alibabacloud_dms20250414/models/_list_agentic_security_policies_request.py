# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticSecurityPoliciesRequest(DaraModel):
    def __init__(
        self,
        include_archived: bool = None,
        page: int = None,
        policy_status: str = None,
        size: int = None,
    ):
        # Specifies whether to include archived policies in the query scope of user policies. Valid values:
        # - true: Includes archived policies.
        # - false: Does not include archived policies.
        # Default value: false. When querying archived policies, do not specify PolicyStatus. If ON or OFF is specified, only user policies in the corresponding state are returned. This parameter does not affect system default policies.
        self.include_archived = include_archived
        # The page number of the user policies to query. Pages start from 1. Default value: 1. Only user policies are paginated. System default policies are returned separately in each call.
        self.page = page
        # The filter condition for the user policy status. Valid values: ON (enabled) and OFF (disabled). If this parameter is not specified or contains only whitespace characters, policies are not filtered by status. You cannot specify ARCHIVED. To query archived user policies, do not specify this parameter and set IncludeArchived to true. This parameter does not affect system default policies.
        self.policy_status = policy_status
        # The number of user policies to query on each page. Valid values: 1 to 100. Default value: 20. In addition, each call returns up to Size enabled system default policies. Therefore, the number of items in the returned Data may be greater than Size.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_archived is not None:
            result['IncludeArchived'] = self.include_archived

        if self.page is not None:
            result['Page'] = self.page

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeArchived') is not None:
            self.include_archived = m.get('IncludeArchived')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

