# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListDatasetJobConfigsResponseBody(DaraModel):
    def __init__(
        self,
        dataset_job_configs: List[main_models.DatasetJobConfig] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The dataset job configurations.
        self.dataset_job_configs = dataset_job_configs
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.dataset_job_configs:
            for v1 in self.dataset_job_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatasetJobConfigs'] = []
        if self.dataset_job_configs is not None:
            for k1 in self.dataset_job_configs:
                result['DatasetJobConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_job_configs = []
        if m.get('DatasetJobConfigs') is not None:
            for k1 in m.get('DatasetJobConfigs'):
                temp_model = main_models.DatasetJobConfig()
                self.dataset_job_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

