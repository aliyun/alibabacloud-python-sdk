# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribePolicyBindingsRequest(DaraModel):
    def __init__(
        self,
        data_source_ids: List[str] = None,
        filters: List[main_models.DescribePolicyBindingsRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        policy_id: str = None,
        source_type: str = None,
    ):
        # List of data source IDs.
        self.data_source_ids = data_source_ids
        # Query filters.
        self.filters = filters
        # Number of results per query.
        # 
        # Range: 10~100. Default: 10.
        self.max_results = max_results
        # Token required to fetch the next page of policy and data source associations.
        self.next_token = next_token
        # Policy ID.
        self.policy_id = policy_id
        # Data source type. Possible values:
        # * **UDM_ECS**: Indicates ECS full machine backup.
        self.source_type = source_type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_ids is not None:
            result['DataSourceIds'] = self.data_source_ids

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceIds') is not None:
            self.data_source_ids = m.get('DataSourceIds')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribePolicyBindingsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribePolicyBindingsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # Key in the query filter. Possible values include:
        # 
        # - **PolicyId**: Backup policy ID
        # - **DataSourceId**: ECS instance ID
        # - **DataSourceType**: Data source type
        self.key = key
        # Matching method. Default is IN. This refers to the matching operation (Operator) supported by the Key and Value in the filter. Possible values include:
        # 
        # - **EQUAL**: Equal to
        # - **NOT_EQUAL**: Not equal to
        # - **GREATER_THAN**: Greater than
        # - **GREATER_THAN_OR_EQUAL**: Greater than or equal to
        # - **LESS_THAN**: Less than
        # - **LESS_THAN_OR_EQUAL**: Less than or equal to
        # - **BETWEEN**: Range, where value is a JSON array `[lower_bound, upper_bound]`.
        # - **IN**: In the set, where value is an array.
        self.operator = operator
        # Values to be matched in the query filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

