# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetResourcesRequest(DaraModel):
    def __init__(
        self,
        filter: Dict[str, Any] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The filter conditions for resources.
        # 
        # Specify multiple key-value pairs in JSON format to filter resources. If a List or Get operation for a cloud product supports filtering by specific properties, you can use those properties as filter conditions for this parameter.
        # 
        # > The supported filter fields may vary for different resource types. For more information about the supported fields, see the OpenAPI documentation for the specific resource.
        # 
        # For example, DBInstance resources support filtering by the `EditionType` and `PaymentType` fields.
        self.filter = filter
        # The maximum number of records to return on each page for a paged query. Maximum value: 100.
        self.max_results = max_results
        # The pagination token.
        # 
        # - You do not need to specify this parameter for the first query. The system returns data from the first page.
        # 
        # - For subsequent queries, set this parameter to the nextToken value returned from the previous call.
        # 
        # > If this parameter contains only digits, Cloud Control API treats it as the `PageNumber` for paging.
        self.next_token = next_token
        # The region ID. This parameter is required if the cloud product is region-specific.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

