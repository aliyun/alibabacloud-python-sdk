# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAccountFactoryBaselineItemsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        names: List[str] = None,
        next_token: str = None,
        region_id: str = None,
        type: str = None,
        versions: List[str] = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The names of the baseline items.
        self.names = names
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The type of the baseline items.
        self.type = type
        # The versions of the baseline items.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.names is not None:
            result['Names'] = self.names

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        if self.versions is not None:
            result['Versions'] = self.versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        return self

