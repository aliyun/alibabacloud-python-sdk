# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class UploadMediaByURLResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upload_jobs: List[main_models.UploadMediaByURLResponseBodyUploadJobs] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the upload job.
        self.upload_jobs = upload_jobs

    def validate(self):
        if self.upload_jobs:
            for v1 in self.upload_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UploadJobs'] = []
        if self.upload_jobs is not None:
            for k1 in self.upload_jobs:
                result['UploadJobs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.upload_jobs = []
        if m.get('UploadJobs') is not None:
            for k1 in m.get('UploadJobs'):
                temp_model = main_models.UploadMediaByURLResponseBodyUploadJobs()
                self.upload_jobs.append(temp_model.from_map(k1))

        return self

class UploadMediaByURLResponseBodyUploadJobs(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        source_url: str = None,
    ):
        # The ID of the upload job.
        self.job_id = job_id
        # The URL of the source file that is uploaded in the upload job.
        self.source_url = source_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.source_url is not None:
            result['SourceURL'] = self.source_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SourceURL') is not None:
            self.source_url = m.get('SourceURL')

        return self

