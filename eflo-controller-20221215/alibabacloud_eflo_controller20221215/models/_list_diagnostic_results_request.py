# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiagnosticResultsRequest(DaraModel):
    def __init__(
        self,
        diag_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # Type of diagnosis, indicating which diagnostic rules are hit.
        self.diag_type = diag_type
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default value is 20.
        # - If the set value is greater than 100, the default value is 100.
        self.max_results = max_results
        # NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diag_type is not None:
            result['DiagType'] = self.diag_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagType') is not None:
            self.diag_type = m.get('DiagType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

