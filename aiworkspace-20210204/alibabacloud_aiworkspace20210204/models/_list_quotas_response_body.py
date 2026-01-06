# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListQuotasResponseBody(DaraModel):
    def __init__(
        self,
        quotas: List[main_models.ListQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned quotas.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id
        # The number of quotas that meet the filter conditions.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotasResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        mode: str = None,
        name: str = None,
        product_code: str = None,
        quota_type: str = None,
        specs: List[main_models.ListQuotasResponseBodyQuotasSpecs] = None,
    ):
        # The alias of the quota.
        self.display_name = display_name
        # The quota ID.
        self.id = id
        # The billing method. Valid values:
        # 
        # *   isolate: subscription
        # *   share: pay-as-you-go
        self.mode = mode
        # The quota name.
        self.name = name
        # The product code. Valid values:
        # 
        # *   PAI_isolate: CPU subscription resource groups of PAI
        # *   PAI_share: GPU pay-as-you-go resource groups of PAI
        self.product_code = product_code
        # The quota type. Valid value:
        # 
        # PAI: indicates GPU resource groups of MaxCompute.
        self.quota_type = quota_type
        # The quota specifications.
        self.specs = specs

    def validate(self):
        if self.specs:
            for v1 in self.specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        result['Specs'] = []
        if self.specs is not None:
            for k1 in self.specs:
                result['Specs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        self.specs = []
        if m.get('Specs') is not None:
            for k1 in m.get('Specs'):
                temp_model = main_models.ListQuotasResponseBodyQuotasSpecs()
                self.specs.append(temp_model.from_map(k1))

        return self

class ListQuotasResponseBodyQuotasSpecs(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The specification name.
        self.name = name
        # The specification type. The parameter can be left empty.
        self.type = type
        # The specification value.
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

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

