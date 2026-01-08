# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAclCheckQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: main_models.DescribeAclCheckQuotaResponseBodyQuota = None,
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
            temp_model = main_models.DescribeAclCheckQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAclCheckQuotaResponseBodyQuota(DaraModel):
    def __init__(
        self,
        available_quota: int = None,
        consumed_quota: int = None,
        total_quota: int = None,
        update_time: str = None,
    ):
        self.available_quota = available_quota
        self.consumed_quota = consumed_quota
        self.total_quota = total_quota
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_quota is not None:
            result['AvailableQuota'] = self.available_quota

        if self.consumed_quota is not None:
            result['ConsumedQuota'] = self.consumed_quota

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableQuota') is not None:
            self.available_quota = m.get('AvailableQuota')

        if m.get('ConsumedQuota') is not None:
            self.consumed_quota = m.get('ConsumedQuota')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

