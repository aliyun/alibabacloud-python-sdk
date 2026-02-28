# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeFaultDiagnosisFactorDistributionStatResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[main_models.DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList] = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list

    def validate(self):
        if self.stat_list:
            for v1 in self.stat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatList'] = []
        if self.stat_list is not None:
            for k1 in self.stat_list:
                result['StatList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stat_list = []
        if m.get('StatList') is not None:
            for k1 in m.get('StatList'):
                temp_model = main_models.DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k1))

        return self

class DescribeFaultDiagnosisFactorDistributionStatResponseBodyStatList(DaraModel):
    def __init__(
        self,
        factor_id: str = None,
        user_count: int = None,
        user_ratio: float = None,
    ):
        self.factor_id = factor_id
        self.user_count = user_count
        self.user_ratio = user_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factor_id is not None:
            result['FactorId'] = self.factor_id

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        if self.user_ratio is not None:
            result['UserRatio'] = self.user_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FactorId') is not None:
            self.factor_id = m.get('FactorId')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        if m.get('UserRatio') is not None:
            self.user_ratio = m.get('UserRatio')

        return self

