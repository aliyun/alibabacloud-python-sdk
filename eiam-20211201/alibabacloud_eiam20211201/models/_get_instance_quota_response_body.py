# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: main_models.GetInstanceQuotaResponseBodyQuota = None,
        request_id: str = None,
    ):
        self.quota = quota
        self.request_id = request_id

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = main_models.GetInstanceQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceQuotaResponseBodyQuota(DaraModel):
    def __init__(
        self,
        quota_key: str = None,
        quota_value: int = None,
    ):
        # Quota 配额的Key，同请求参数
        self.quota_key = quota_key
        # Quota 配额的值。
        self.quota_value = quota_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota_key is not None:
            result['QuotaKey'] = self.quota_key

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaKey') is not None:
            self.quota_key = m.get('QuotaKey')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        return self

