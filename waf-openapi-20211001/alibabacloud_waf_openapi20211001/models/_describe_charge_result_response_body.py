# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeChargeResultResponseBody(DaraModel):
    def __init__(
        self,
        module_details: List[main_models.DescribeChargeResultResponseBodyModuleDetails] = None,
        request_id: str = None,
        total_credit: float = None,
        total_se_cu: float = None,
    ):
        # The calculation results.
        self.module_details = module_details
        # The request ID.
        self.request_id = request_id
        # The total number of calculated Credits.
        self.total_credit = total_credit
        # The total number of calculated SeCUs.
        self.total_se_cu = total_se_cu

    def validate(self):
        if self.module_details:
            for v1 in self.module_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleDetails'] = []
        if self.module_details is not None:
            for k1 in self.module_details:
                result['ModuleDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_credit is not None:
            result['TotalCredit'] = self.total_credit

        if self.total_se_cu is not None:
            result['TotalSeCu'] = self.total_se_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_details = []
        if m.get('ModuleDetails') is not None:
            for k1 in m.get('ModuleDetails'):
                temp_model = main_models.DescribeChargeResultResponseBodyModuleDetails()
                self.module_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCredit') is not None:
            self.total_credit = m.get('TotalCredit')

        if m.get('TotalSeCu') is not None:
            self.total_se_cu = m.get('TotalSeCu')

        return self

class DescribeChargeResultResponseBodyModuleDetails(DaraModel):
    def __init__(
        self,
        credit: float = None,
        module_code: str = None,
        se_cu: float = None,
    ):
        # The number of Credits for the pricing module.
        self.credit = credit
        # The pricing module identifier.
        self.module_code = module_code
        # The number of SeCUs for the pricing module.
        self.se_cu = se_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit is not None:
            result['Credit'] = self.credit

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.se_cu is not None:
            result['SeCu'] = self.se_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credit') is not None:
            self.credit = m.get('Credit')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('SeCu') is not None:
            self.se_cu = m.get('SeCu')

        return self

