# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListDatasetJobsResponseBody(DaraModel):
    def __init__(
        self,
        dataset_jobs: List[main_models.DatasetJob] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The jobs in the dataset.
        self.dataset_jobs = dataset_jobs
        # The request ID.
        self.request_id = request_id
        # The total number of jobs.
        self.total_count = total_count

    def validate(self):
        if self.dataset_jobs:
            for v1 in self.dataset_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatasetJobs'] = []
        if self.dataset_jobs is not None:
            for k1 in self.dataset_jobs:
                result['DatasetJobs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dataset_jobs = []
        if m.get('DatasetJobs') is not None:
            for k1 in m.get('DatasetJobs'):
                temp_model = main_models.DatasetJob()
                self.dataset_jobs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

