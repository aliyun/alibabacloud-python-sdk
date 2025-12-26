# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListQuotaWorkloadsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        workloads: List[main_models.QueueInfo] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.workloads = workloads

    def validate(self):
        if self.workloads:
            for v1 in self.workloads:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Workloads'] = []
        if self.workloads is not None:
            for k1 in self.workloads:
                result['Workloads'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.workloads = []
        if m.get('Workloads') is not None:
            for k1 in m.get('Workloads'):
                temp_model = main_models.QueueInfo()
                self.workloads.append(temp_model.from_map(k1))

        return self

