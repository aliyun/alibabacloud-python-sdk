# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetProductQuotaDimensionResponseBody(DaraModel):
    def __init__(
        self,
        quota_dimension: main_models.GetProductQuotaDimensionResponseBodyQuotaDimension = None,
        request_id: str = None,
    ):
        # The details of the quota dimension.
        self.quota_dimension = quota_dimension
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.quota_dimension:
            self.quota_dimension.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaDimension') is not None:
            temp_model = main_models.GetProductQuotaDimensionResponseBodyQuotaDimension()
            self.quota_dimension = temp_model.from_map(m.get('QuotaDimension'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProductQuotaDimensionResponseBodyQuotaDimension(DaraModel):
    def __init__(
        self,
        dependent_dimensions: List[str] = None,
        dimension_key: str = None,
        dimension_value_detail: List[main_models.GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail] = None,
        dimension_values: List[str] = None,
        name: str = None,
    ):
        # The quota dimensions of the cloud service on which the target quota depends.
        self.dependent_dimensions = dependent_dimensions
        # The key of the quota dimension. Valid values:
        # - regionId: region
        # 
        # - zoneId: zone
        # 
        # - chargeType: billing method
        # 
        # - networkType: network type
        # 
        # - resourceType: resource type
        self.dimension_key = dimension_key
        # The details of the quota dimension value.
        self.dimension_value_detail = dimension_value_detail
        # The list of quota dimension values.
        self.dimension_values = dimension_values
        # The name of the quota dimension.
        self.name = name

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
                temp_model = main_models.GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail()
                self.dimension_value_detail.append(temp_model.from_map(k1))

        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the quota dimension value.
        self.name = name
        # The value of the quota dimension.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

