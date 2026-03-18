# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class UpdateComputeSubQuotaRequest(DaraModel):
    def __init__(
        self,
        sub_quota_info_list: List[main_models.UpdateComputeSubQuotaRequestSubQuotaInfoList] = None,
    ):
        self.sub_quota_info_list = sub_quota_info_list

    def validate(self):
        if self.sub_quota_info_list:
            for v1 in self.sub_quota_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k1 in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k1 in m.get('subQuotaInfoList'):
                temp_model = main_models.UpdateComputeSubQuotaRequestSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k1))

        return self

class UpdateComputeSubQuotaRequestSubQuotaInfoList(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        parameter: main_models.UpdateComputeSubQuotaRequestSubQuotaInfoListParameter = None,
        type: str = None,
    ):
        # This parameter is required.
        self.nick_name = nick_name
        self.parameter = parameter
        self.type = type

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

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')

        if m.get('parameter') is not None:
            temp_model = main_models.UpdateComputeSubQuotaRequestSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m.get('parameter'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateComputeSubQuotaRequestSubQuotaInfoListParameter(DaraModel):
    def __init__(
        self,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        self.enable_priority = enable_priority
        self.force_reserved_min = force_reserved_min
        # This parameter is required.
        self.max_cu = max_cu
        # This parameter is required.
        self.min_cu = min_cu
        self.scheduler_type = scheduler_type
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority

        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min

        if self.max_cu is not None:
            result['maxCU'] = self.max_cu

        if self.min_cu is not None:
            result['minCU'] = self.min_cu

        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type

        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')

        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')

        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')

        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')

        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')

        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')

        return self

