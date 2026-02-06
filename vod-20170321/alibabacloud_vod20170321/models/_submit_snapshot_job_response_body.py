# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SubmitSnapshotJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_job: main_models.SubmitSnapshotJobResponseBodySnapshotJob = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the snapshot job.
        self.snapshot_job = snapshot_job

    def validate(self):
        if self.snapshot_job:
            self.snapshot_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_job is not None:
            result['SnapshotJob'] = self.snapshot_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotJob') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJob()
            self.snapshot_job = temp_model.from_map(m.get('SnapshotJob'))

        return self

class SubmitSnapshotJobResponseBodySnapshotJob(DaraModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The ID of the snapshot job.
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

