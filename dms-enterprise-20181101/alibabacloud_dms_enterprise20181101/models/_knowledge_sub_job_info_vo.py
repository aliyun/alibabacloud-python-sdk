# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KnowledgeSubJobInfoVO(DaraModel):
    def __init__(
        self,
        err_message: str = None,
        job_type: str = None,
        name: str = None,
        progress: int = None,
        status: str = None,
        sub_job_id: int = None,
    ):
        self.err_message = err_message
        self.job_type = job_type
        self.name = name
        self.progress = progress
        self.status = status
        self.sub_job_id = sub_job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.name is not None:
            result['Name'] = self.name

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_job_id is not None:
            result['SubJobId'] = self.sub_job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubJobId') is not None:
            self.sub_job_id = m.get('SubJobId')

        return self

