# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetProductQuotaDimensionRequest(DaraModel):
    def __init__(
        self,
        dependent_dimensions: List[main_models.GetProductQuotaDimensionRequestDependentDimensions] = None,
        dimension_key: str = None,
        product_code: str = None,
    ):
        # The quota dimensions on which the target quota dimension depends.
        self.dependent_dimensions = dependent_dimensions
        # The key of the target quota dimension.
        # 
        # > If the target quota dimension has dependent quota dimensions, you must specify the keys and values of the dependent quota dimensions at the same time.
        self.dimension_key = dimension_key
        # The abbreviation of the cloud service.
        # 
        # > For more information about how to obtain the abbreviation of a cloud service, see the ProductCode parameter in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code

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

        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dependent_dimensions = []
        if m.get('DependentDimensions') is not None:
            for k1 in m.get('DependentDimensions'):
                temp_model = main_models.GetProductQuotaDimensionRequestDependentDimensions()
                self.dependent_dimensions.append(temp_model.from_map(k1))

        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

class GetProductQuotaDimensionRequestDependentDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension on which the target quota dimension depends.
        # 
        # > - The value of N depends on the number of quota dimensions on which the target quota dimension depends.
        # > - You must specify the key and value of a dependent quota dimension at the same time.
        self.key = key
        # The value of the quota dimension on which the target quota dimension depends.
        # 
        # > - The value of N depends on the number of quota dimensions on which the target quota dimension depends.
        # > - You must specify the key and value of a dependent quota dimension at the same time.
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

