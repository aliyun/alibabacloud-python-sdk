# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListProductQuotaDimensionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_dimensions: List[main_models.ListProductQuotaDimensionsResponseBodyQuotaDimensions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned for this query.
        self.max_results = max_results
        # The pagination token that indicates the position of the returned data. If this parameter is not returned, it indicates that all data has been queried.
        self.next_token = next_token
        # The quota dimensions.
        self.quota_dimensions = quota_dimensions
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned for this request.
        self.total_count = total_count

    def validate(self):
        if self.quota_dimensions:
            for v1 in self.quota_dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k1 in self.quota_dimensions:
                result['QuotaDimensions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k1 in m.get('QuotaDimensions'):
                temp_model = main_models.ListProductQuotaDimensionsResponseBodyQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProductQuotaDimensionsResponseBodyQuotaDimensions(DaraModel):
    def __init__(
        self,
        dependent_dimensions: List[str] = None,
        dimension_key: str = None,
        dimension_value_detail: List[main_models.ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail] = None,
        dimension_values: List[str] = None,
        name: str = None,
        requisite: bool = None,
    ):
        # The quota dimensions on which the target quota dimension depends.
        self.dependent_dimensions = dependent_dimensions
        # The key of the quota dimension. Valid values:
        # 
        # - regionId: the region ID.
        # 
        # - zoneId: the zone ID.
        # 
        # - chargeType: the billing method.
        # 
        # - networkType: the network type.
        # 
        # - resourceType: the resource type.
        self.dimension_key = dimension_key
        # The details of the quota dimension value.
        self.dimension_value_detail = dimension_value_detail
        # The list of quota dimension values.
        self.dimension_values = dimension_values
        # The name of the quota dimension.
        self.name = name
        # Specifies whether the quota dimension is required when you query quota dimensions. Valid values:
        # 
        # - true: The quota dimension is required.
        # 
        # - false: The quota dimension is optional.
        self.requisite = requisite

    def validate(self):
        if self.dimension_value_detail:
            for v1 in self.dimension_value_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions

        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key

        result['DimensionValueDetail'] = []
        if self.dimension_value_detail is not None:
            for k1 in self.dimension_value_detail:
                result['DimensionValueDetail'].append(k1.to_map() if k1 else None)

        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values

        if self.name is not None:
            result['Name'] = self.name

        if self.requisite is not None:
            result['Requisite'] = self.requisite

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')

        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')

        self.dimension_value_detail = []
        if m.get('DimensionValueDetail') is not None:
            for k1 in m.get('DimensionValueDetail'):
                temp_model = main_models.ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail()
                self.dimension_value_detail.append(temp_model.from_map(k1))

        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Requisite') is not None:
            self.requisite = m.get('Requisite')

        return self

class ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail(DaraModel):
    def __init__(
        self,
        dependent_dimensions: List[main_models.ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetailDependentDimensions] = None,
        name: str = None,
        value: str = None,
    ):
        # The quota dimensions on which the target quota dimension depends.
        self.dependent_dimensions = dependent_dimensions
        # The name of the quota dimension value.
        self.name = name
        # The value of the quota dimension.
        self.value = value

    def validate(self):
        if self.dependent_dimensions:
            for v1 in self.dependent_dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DependentDimensions'] = []
        if self.dependent_dimensions is not None:
            for k1 in self.dependent_dimensions:
                result['DependentDimensions'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dependent_dimensions = []
        if m.get('DependentDimensions') is not None:
            for k1 in m.get('DependentDimensions'):
                temp_model = main_models.ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetailDependentDimensions()
                self.dependent_dimensions.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetailDependentDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension on which the target quota dimension depends.
        self.key = key
        # The value of the quota dimension on which the target quota dimension depends.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

