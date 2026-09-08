# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetAgentJobResponseBody(DaraModel):
    def __init__(
        self,
        job: main_models.GetAgentJobResponseBodyJob = None,
        request_id: str = None,
    ):
        # The task information.
        self.job = job
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Job') is not None:
            temp_model = main_models.GetAgentJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAgentJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        output: str = None,
        status: str = None,
    ):
        # The task ID.
        self.job_id = job_id
        # The task output JSON string. Different tasks return different structures, which are defined by the business side.
        self.output = output
        # The task status. Valid values:
        # 
        # - Created
        # - Queuing
        # - Executing
        # - Finished
        # - Failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.output is not None:
            result['Output'] = self.output

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

