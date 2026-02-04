# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetServiceQuotaResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        service_quota: main_models.GetServiceQuotaResponseBodyServiceQuota = None,
    ):
        self.request_id = request_id
        self.service_quota = service_quota

    def validate(self):
        if self.service_quota:
            self.service_quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_quota is not None:
            result['ServiceQuota'] = self.service_quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceQuota') is not None:
            temp_model = main_models.GetServiceQuotaResponseBodyServiceQuota()
            self.service_quota = temp_model.from_map(m.get('ServiceQuota'))

        return self

class GetServiceQuotaResponseBodyServiceQuota(DaraModel):
    def __init__(
        self,
        quota_type: str = None,
        quota_value: int = None,
        used_quota_value: int = None,
    ):
        # Quota 配额的唯一标识。
        self.quota_type = quota_type
        # Quota 配额的值。
        self.quota_value = quota_value
        # Quota 配额的当前用量。
        self.used_quota_value = used_quota_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        if self.used_quota_value is not None:
            result['UsedQuotaValue'] = self.used_quota_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        if m.get('UsedQuotaValue') is not None:
            self.used_quota_value = m.get('UsedQuotaValue')

        return self

