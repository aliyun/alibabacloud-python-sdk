# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ResourceDiagnosisDetail(DaraModel):
    def __init__(
        self,
        exceed_resources: List[str] = None,
        limit: main_models.ResourceAmount = None,
        status: str = None,
        used: main_models.ResourceAmount = None,
        workload_ids: List[str] = None,
    ):
        self.exceed_resources = exceed_resources
        self.limit = limit
        self.status = status
        self.used = used
        self.workload_ids = workload_ids

    def validate(self):
        if self.limit:
            self.limit.validate()
        if self.used:
            self.used.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exceed_resources is not None:
            result['ExceedResources'] = self.exceed_resources

        if self.limit is not None:
            result['Limit'] = self.limit.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.used is not None:
            result['Used'] = self.used.to_map()

        if self.workload_ids is not None:
            result['WorkloadIds'] = self.workload_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceedResources') is not None:
            self.exceed_resources = m.get('ExceedResources')

        if m.get('Limit') is not None:
            temp_model = main_models.ResourceAmount()
            self.limit = temp_model.from_map(m.get('Limit'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Used') is not None:
            temp_model = main_models.ResourceAmount()
            self.used = temp_model.from_map(m.get('Used'))

        if m.get('WorkloadIds') is not None:
            self.workload_ids = m.get('WorkloadIds')

        return self

