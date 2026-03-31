# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class UpdateComputeQuotaPlanRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        quota: main_models.UpdateComputeQuotaPlanRequestQuota = None,
    ):
        # The name of quota plan.
        # 
        # This parameter is required.
        self.name = name
        # The parameters of quota plan.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.quota is not None:
            result['quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('quota') is not None:
            temp_model = main_models.UpdateComputeQuotaPlanRequestQuota()
            self.quota = temp_model.from_map(m.get('quota'))

        return self

class UpdateComputeQuotaPlanRequestQuota(DaraModel):
    def __init__(
        self,
        parameter: main_models.UpdateComputeQuotaPlanRequestQuotaParameter = None,
        sub_quota_info_list: List[main_models.UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoList] = None,
    ):
        # The parameters of level-1 quota.
        self.parameter = parameter
        # The list of level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list

    def validate(self):
        if self.parameter:
            self.parameter.validate()
        if self.sub_quota_info_list:
            for v1 in self.sub_quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()

        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k1 in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameter') is not None:
            temp_model = main_models.UpdateComputeQuotaPlanRequestQuotaParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k1))

        return self

class UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        parameter: main_models.UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter = None,
    ):
        # The nickname of the level-2 quota.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The parameters of the level-2 quota.
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick_name is not None:
            result['nickName'] = self.nick_name

        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            temp_model = main_models.UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        return self

class UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter(DaraModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        # The value of elastic Reserved CUs.
        # > The total number of elastically reserved CUs in all the level-2 quotas is equal to the number of elastically reserved CUs in the level-1 quota.
        # 
        # This parameter is required.
        self.elastic_reserved_cu = elastic_reserved_cu
        # The value of maxCU in Reserved CUs.
        # > The value of maxCU must be less than or equal to the value of maxCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        # > 
        # >- The total value of minCU in all the level-2 quotas is equal to the value of minCU in the level-1 quota.
        # >- The value of minCU must be less than or equal to the value of maxCU in the level-2 quota and less than or equal to the value of minCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu

        if self.max_cu is not None:
            result['maxCU'] = self.max_cu

        if self.min_cu is not None:
            result['minCU'] = self.min_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')

        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')

        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')

        return self

class UpdateComputeQuotaPlanRequestQuotaParameter(DaraModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
    ):
        # The value of elastic Reserved CUs in the level-1 quota.
        # > The default value is 0. The maximum value of this parameter must be equal to the number of subscription-based reserved CUs and cannot exceed 10,000 CUs.
        # 
        # This parameter is required.
        self.elastic_reserved_cu = elastic_reserved_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')

        return self

