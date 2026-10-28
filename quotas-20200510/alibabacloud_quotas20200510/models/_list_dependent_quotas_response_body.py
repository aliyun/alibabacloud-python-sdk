# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListDependentQuotasResponseBody(DaraModel):
    def __init__(
        self,
        quotas: List[main_models.ListDependentQuotasResponseBodyQuotas] = None,
        request_id: str = None,
    ):
        # The list of quotas on which the target quota depends.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListDependentQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDependentQuotasResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.ListDependentQuotasResponseBodyQuotasDimensions] = None,
        product_code: str = None,
        quota_action_code: str = None,
        scale: float = None,
    ):
        # The quota dimensions on which the target quota depends.
        self.dimensions = dimensions
        # The abbreviated name of the cloud service.
        self.product_code = product_code
        # The ID of the quota on which the target quota depends.
        self.quota_action_code = quota_action_code
        # The ratio between the target quota and the dependent quota.
        self.scale = scale

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.scale is not None:
            result['Scale'] = self.scale

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.ListDependentQuotasResponseBodyQuotasDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('Scale') is not None:
            self.scale = m.get('Scale')

        return self

class ListDependentQuotasResponseBodyQuotasDimensions(DaraModel):
    def __init__(
        self,
        dependent_dimension: List[str] = None,
        dimension_key: str = None,
        dimension_values: List[str] = None,
    ):
        # The quota dimension on which the dependent dimension of the target quota depends.
        self.dependent_dimension = dependent_dimension
        # The key of the quota dimension on which the target quota depends.
        self.dimension_key = dimension_key
        # The value of the quota dimension on which the dependent dimension of the target quota depends.
        self.dimension_values = dimension_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependent_dimension is not None:
            result['DependentDimension'] = self.dependent_dimension

        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key

        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimension') is not None:
            self.dependent_dimension = m.get('DependentDimension')

        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')

        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')

        return self

