# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListOpsItemsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListOpsItemsShrinkRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_tags_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The filter rules for the component.
        self.filter = filter
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The information about resource tags.
        self.resource_tags_shrink = resource_tags_shrink
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_tags_shrink is not None:
            result['ResourceTags'] = self.resource_tags_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListOpsItemsShrinkRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceTags') is not None:
            self.resource_tags_shrink = m.get('ResourceTags')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

class ListOpsItemsShrinkRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter.
        self.name = name
        # The comparison operator that is used to filter property values.
        self.operator = operator
        # The parameter values of the filter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

