# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class GetFlinkAiServiceFreeQuotaResponseBody(DaraModel):
    def __init__(
        self,
        flink_ai_free_quota_dto: main_models.GetFlinkAiServiceFreeQuotaResponseBodyFlinkAiFreeQuotaDTO = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The Flink AI free quota data transfer object.
        self.flink_ai_free_quota_dto = flink_ai_free_quota_dto
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.flink_ai_free_quota_dto:
            self.flink_ai_free_quota_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flink_ai_free_quota_dto is not None:
            result['FlinkAiFreeQuotaDTO'] = self.flink_ai_free_quota_dto.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlinkAiFreeQuotaDTO') is not None:
            temp_model = main_models.GetFlinkAiServiceFreeQuotaResponseBodyFlinkAiFreeQuotaDTO()
            self.flink_ai_free_quota_dto = temp_model.from_map(m.get('FlinkAiFreeQuotaDTO'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFlinkAiServiceFreeQuotaResponseBodyFlinkAiFreeQuotaDTO(DaraModel):
    def __init__(
        self,
        free_quota: float = None,
        used_quota_details: List[main_models.GetFlinkAiServiceFreeQuotaResponseBodyFlinkAiFreeQuotaDTOUsedQuotaDetails] = None,
    ):
        # The total free quota.
        self.free_quota = free_quota
        # The list of used quota details for each usage type.
        self.used_quota_details = used_quota_details

    def validate(self):
        if self.used_quota_details:
            for v1 in self.used_quota_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.free_quota is not None:
            result['FreeQuota'] = self.free_quota

        result['UsedQuotaDetails'] = []
        if self.used_quota_details is not None:
            for k1 in self.used_quota_details:
                result['UsedQuotaDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FreeQuota') is not None:
            self.free_quota = m.get('FreeQuota')

        self.used_quota_details = []
        if m.get('UsedQuotaDetails') is not None:
            for k1 in m.get('UsedQuotaDetails'):
                temp_model = main_models.GetFlinkAiServiceFreeQuotaResponseBodyFlinkAiFreeQuotaDTOUsedQuotaDetails()
                self.used_quota_details.append(temp_model.from_map(k1))

        return self

class GetFlinkAiServiceFreeQuotaResponseBodyFlinkAiFreeQuotaDTOUsedQuotaDetails(DaraModel):
    def __init__(
        self,
        amount: float = None,
        usage_type: str = None,
    ):
        # The used quota for this usage type.
        self.amount = amount
        # The usage type.
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

