# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai20240521 import models as main_models
from darabonba.model import DaraModel

class QuotaDetails(DaraModel):
    def __init__(
        self,
        actual_min_quota: main_models.ResourceAmount = None,
        desired_min_quota: main_models.ResourceAmount = None,
        requested_quota: main_models.ResourceAmount = None,
        used_quota: main_models.ResourceAmount = None,
    ):
        self.actual_min_quota = actual_min_quota
        self.desired_min_quota = desired_min_quota
        self.requested_quota = requested_quota
        self.used_quota = used_quota

    def validate(self):
        if self.actual_min_quota:
            self.actual_min_quota.validate()
        if self.desired_min_quota:
            self.desired_min_quota.validate()
        if self.requested_quota:
            self.requested_quota.validate()
        if self.used_quota:
            self.used_quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_min_quota is not None:
            result['ActualMinQuota'] = self.actual_min_quota.to_map()

        if self.desired_min_quota is not None:
            result['DesiredMinQuota'] = self.desired_min_quota.to_map()

        if self.requested_quota is not None:
            result['RequestedQuota'] = self.requested_quota.to_map()

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualMinQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.actual_min_quota = temp_model.from_map(m.get('ActualMinQuota'))

        if m.get('DesiredMinQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.desired_min_quota = temp_model.from_map(m.get('DesiredMinQuota'))

        if m.get('RequestedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.requested_quota = temp_model.from_map(m.get('RequestedQuota'))

        if m.get('UsedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.used_quota = temp_model.from_map(m.get('UsedQuota'))

        return self

