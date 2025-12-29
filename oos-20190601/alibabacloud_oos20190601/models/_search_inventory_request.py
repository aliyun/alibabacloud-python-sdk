# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class SearchInventoryRequest(DaraModel):
    def __init__(
        self,
        aggregator: List[str] = None,
        filter: List[main_models.SearchInventoryRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The information about aggregators. You can use one or more aggregators to query the aggregate information of an instance. Valid values:
        # 
        # *   ACS:Application.Name
        # *   ACS:Application.Version
        self.aggregator = aggregator
        # The filter rules for the component.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id

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
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.SearchInventoryRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class SearchInventoryRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # The name of the component property. Valid values of N: 1 to 5. Different components have different property names. You can call the [GetInventorySchema](https://api.aliyun.com/#/?product=oos\\&version=2019-06-01\\&api=GetInventorySchema) operation to query the property names of different components. For example, the ACS:InstanceInformation component has the InstanceId property. Therefore, you can set this parameter to ACS:InstanceInformation.InstanceId.
        self.name = name
        # The comparison operator that is used to filter property values. Valid values of N: 1 to 5. Valid values:
        # 
        # *   Equal
        # *   NotEqual
        # *   BeginWith
        # *   LessThan
        # *   GreaterThan
        self.operator = operator
        # The property values to query.
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

