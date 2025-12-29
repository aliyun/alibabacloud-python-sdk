# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInventorySchemaRequest(DaraModel):
    def __init__(
        self,
        aggregator: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        type_name: str = None,
    ):
        # Specifies whether to return only properties that support the aggregate feature in the configuration list. Valid values:
        # 
        # *   true: only returns properties that support the aggregate feature in the configuration list.
        # *   false: returns all properties in the configuration list.
        self.aggregator = aggregator
        # The number of entries per page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The configuration list type name. Valid values:
        # 
        # *   ACS:InstanceInformation
        # *   ACS:Application
        # *   ACS:File
        # *   ACS:Network
        # *   ACS:WindowsRole
        # *   ACS:Service
        # *   ACS:WindowsUpdate
        # *   ACS:WindowsRegistry
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

