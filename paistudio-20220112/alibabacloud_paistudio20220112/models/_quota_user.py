# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QuotaUser(DaraModel):
    def __init__(
        self,
        resources: main_models.QuotaUserResources = None,
        user_id: str = None,
        username: str = None,
        workload_count: int = None,
    ):
        self.resources = resources
        self.user_id = user_id
        self.username = username
        self.workload_count = workload_count

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        if self.workload_count is not None:
            result['WorkloadCount'] = self.workload_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resources') is not None:
            temp_model = main_models.QuotaUserResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkloadCount') is not None:
            self.workload_count = m.get('WorkloadCount')

        return self

class QuotaUserResources(DaraModel):
    def __init__(
        self,
        submitted: main_models.ResourceAmount = None,
        used: main_models.ResourceAmount = None,
    ):
        self.submitted = submitted
        self.used = used

    def validate(self):
        if self.submitted:
            self.submitted.validate()
        if self.used:
            self.used.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.submitted is not None:
            result['Submitted'] = self.submitted.to_map()

        if self.used is not None:
            result['Used'] = self.used.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Submitted') is not None:
            temp_model = main_models.ResourceAmount()
            self.submitted = temp_model.from_map(m.get('Submitted'))

        if m.get('Used') is not None:
            temp_model = main_models.ResourceAmount()
            self.used = temp_model.from_map(m.get('Used'))

        return self

