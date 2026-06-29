# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class Job(DaraModel):
    def __init__(
        self,
        creator: main_models.SimpleUser = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        job_id: str = None,
        job_result: main_models.JobJobResult = None,
        job_type: str = None,
        status: str = None,
    ):
        # Job creator.
        self.creator = creator
        # Creation Time.
        self.gmt_create_time = gmt_create_time
        # Updated At.
        self.gmt_modified_time = gmt_modified_time
        # Job ID.
        self.job_id = job_id
        # Task Result.
        self.job_result = job_result
        # Task Type. Currently, only DOWNLOWD_MARKRESULT_FLOW is supported.
        self.job_type = job_type
        # Job status. Possible values:
        # - init: initialization
        # - running: running
        # - pause: pause
        # - stop: stopped
        # - succ: Succeeded
        # - fail: failed
        self.status = status

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.job_result:
            self.job_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_result is not None:
            result['JobResult'] = self.job_result.to_map()

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = main_models.SimpleUser()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobResult') is not None:
            temp_model = main_models.JobJobResult()
            self.job_result = temp_model.from_map(m.get('JobResult'))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class JobJobResult(DaraModel):
    def __init__(
        self,
        result_link: str = None,
    ):
        # Return value link, which is the OSS path where the annotation results are stored.
        self.result_link = result_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_link is not None:
            result['ResultLink'] = self.result_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultLink') is not None:
            self.result_link = m.get('ResultLink')

        return self

