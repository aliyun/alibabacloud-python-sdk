# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SubmitTranscodeJobsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_jobs: main_models.SubmitTranscodeJobsResponseBodyTranscodeJobs = None,
        transcode_task_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.transcode_jobs = transcode_jobs
        # The ID of the transcoding task that was submitted.
        self.transcode_task_id = transcode_task_id

    def validate(self):
        if self.transcode_jobs:
            self.transcode_jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.transcode_jobs is not None:
            result['TranscodeJobs'] = self.transcode_jobs.to_map()

        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TranscodeJobs') is not None:
            temp_model = main_models.SubmitTranscodeJobsResponseBodyTranscodeJobs()
            self.transcode_jobs = temp_model.from_map(m.get('TranscodeJobs'))

        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')

        return self

class SubmitTranscodeJobsResponseBodyTranscodeJobs(DaraModel):
    def __init__(
        self,
        transcode_job: List[main_models.SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob] = None,
    ):
        self.transcode_job = transcode_job

    def validate(self):
        if self.transcode_job:
            for v1 in self.transcode_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TranscodeJob'] = []
        if self.transcode_job is not None:
            for k1 in self.transcode_job:
                result['TranscodeJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.transcode_job = []
        if m.get('TranscodeJob') is not None:
            for k1 in m.get('TranscodeJob'):
                temp_model = main_models.SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob()
                self.transcode_job.append(temp_model.from_map(k1))

        return self

class SubmitTranscodeJobsResponseBodyTranscodeJobsTranscodeJob(DaraModel):
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

