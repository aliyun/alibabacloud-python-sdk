# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListSecretParametersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The number of entries per page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the parameter. **You can enter a keyword to query parameter names in fuzzy match mode.
        self.name = name
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The path of the parameter. For example, if the name of a parameter is /path/path1/Myparameter, the path of the parameter is /path/path1/.
        self.path = path
        # Specifies whether to query parameters from all levels of directories in the specified path. Default value: false.
        self.recursive = recursive
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The field used to sort the query results. Valid values:
        # 
        # *   Name
        # *   CreatedDate
        self.sort_field = sort_field
        # The order in which the entries are sorted. Valid values:
        # 
        # *   Ascending
        # *   Descending (Default)
        self.sort_order = sort_order
        # The tags of the parameter.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.path is not None:
            result['Path'] = self.path

        if self.recursive is not None:
            result['Recursive'] = self.recursive

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

