# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SimpleQueryResponseBody(DaraModel):
    def __init__(
        self,
        aggregations: List[main_models.SimpleQueryResponseBodyAggregations] = None,
        files: List[main_models.File] = None,
        next_token: str = None,
        request_id: str = None,
        total_hits: int = None,
    ):
        # The list of aggregation field information. This parameter is returned only when Aggregations in the request is not empty.
        self.aggregations = aggregations
        # The list of file information. This parameter is returned only when Aggregations in the request is empty.
        self.files = files
        # The token used for pagination when the total number of files exceeds the value of MaxResults.
        # 
        # When you list file information next time, set NextToken to this value to return the remaining results.
        # 
        # This parameter has a value only when not all files are returned.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of matched records.
        self.total_hits = total_hits

    def validate(self):
        if self.aggregations:
            for v1 in self.aggregations:
                 if v1:
                    v1.validate()
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Aggregations'] = []
        if self.aggregations is not None:
            for k1 in self.aggregations:
                result['Aggregations'].append(k1.to_map() if k1 else None)

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_hits is not None:
            result['TotalHits'] = self.total_hits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregations = []
        if m.get('Aggregations') is not None:
            for k1 in m.get('Aggregations'):
                temp_model = main_models.SimpleQueryResponseBodyAggregations()
                self.aggregations.append(temp_model.from_map(k1))

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.File()
                self.files.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalHits') is not None:
            self.total_hits = m.get('TotalHits')

        return self

class SimpleQueryResponseBodyAggregations(DaraModel):
    def __init__(
        self,
        field: str = None,
        groups: List[main_models.SimpleQueryResponseBodyAggregationsGroups] = None,
        operation: str = None,
        value: float = None,
    ):
        # The name of the aggregation field.
        self.field = field
        # The list of grouping and aggregation results. This parameter is returned only when an Operation of the group type exists in Aggregations of the request.
        self.groups = groups
        # The aggregation operation for the aggregation field.
        self.operation = operation
        # The statistical result of the aggregation.
        self.value = value

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.SimpleQueryResponseBodyAggregationsGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SimpleQueryResponseBodyAggregationsGroups(DaraModel):
    def __init__(
        self,
        count: int = None,
        value: str = None,
    ):
        # The total count of the grouping and aggregation.
        self.count = count
        # The value of the grouping and aggregation.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

