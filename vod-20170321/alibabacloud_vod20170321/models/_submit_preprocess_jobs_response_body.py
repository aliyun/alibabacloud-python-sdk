# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SubmitPreprocessJobsResponseBody(DaraModel):
    def __init__(
        self,
        preprocess_jobs: main_models.SubmitPreprocessJobsResponseBodyPreprocessJobs = None,
        request_id: str = None,
    ):
        self.preprocess_jobs = preprocess_jobs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.preprocess_jobs:
            self.preprocess_jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.preprocess_jobs is not None:
            result['PreprocessJobs'] = self.preprocess_jobs.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreprocessJobs') is not None:
            temp_model = main_models.SubmitPreprocessJobsResponseBodyPreprocessJobs()
            self.preprocess_jobs = temp_model.from_map(m.get('PreprocessJobs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SubmitPreprocessJobsResponseBodyPreprocessJobs(DaraModel):
    def __init__(
        self,
        preprocess_job: List[main_models.SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob] = None,
    ):
        self.preprocess_job = preprocess_job

    def validate(self):
        if self.preprocess_job:
            for v1 in self.preprocess_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreprocessJob'] = []
        if self.preprocess_job is not None:
            for k1 in self.preprocess_job:
                result['PreprocessJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.preprocess_job = []
        if m.get('PreprocessJob') is not None:
            for k1 in m.get('PreprocessJob'):
                temp_model = main_models.SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob()
                self.preprocess_job.append(temp_model.from_map(k1))

        return self

class SubmitPreprocessJobsResponseBodyPreprocessJobsPreprocessJob(DaraModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

