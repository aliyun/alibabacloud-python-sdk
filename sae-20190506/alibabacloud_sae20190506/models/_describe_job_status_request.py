# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobStatusRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        job_id: str = None,
    ):
        # The ID of the job template.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The job ID.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

