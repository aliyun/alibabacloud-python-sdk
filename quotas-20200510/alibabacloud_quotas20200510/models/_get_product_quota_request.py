# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class GetProductQuotaRequest(DaraModel):
    def __init__(
        self,
        dimensions: List[main_models.GetProductQuotaRequestDimensions] = None,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        # The quota dimensions.
        # The properties of the quota item. The combination of dimensions and QuotaActionCode determines a unique quota item.
        # > Dimensions are required for some cloud services. You can call the [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) operation to query the quota dimensions of a cloud service and check whether a dimension is required. The Requisite response parameter indicates whether the dimension is required.
        self.dimensions = dimensions
        # The abbreviated name of the cloud service.
        # 
        # > For more information about how to obtain the abbreviated name of a cloud service, see the ProductCode parameter in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota ID.
        # 
        # > For more information about how to obtain the quota ID of a specified cloud service, see the QuotaActionCode parameter in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.quota_action_code = quota_action_code

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.GetProductQuotaRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        return self

class GetProductQuotaRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > You must specify both Dimensions.N.Key and Dimensions.N.Value. The value range of N depends on the number of dimensions supported by the cloud service. You can call the [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) operation to query the quota dimensions supported by the cloud service. The length of the returned array is the maximum value of N.
        self.key = key
        # The value of the quota dimension.
        # 
        # > You must specify both Dimensions.N.Key and Dimensions.N.Value. The value range of N depends on the number of dimensions supported by the cloud service. You can call the [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) operation to query the quota dimensions supported by the cloud service. The length of the returned array is the maximum value of N.
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

