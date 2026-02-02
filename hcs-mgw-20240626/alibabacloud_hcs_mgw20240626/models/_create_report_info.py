# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReportInfo(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        runtime_id: int = None,
        version: str = None,
    ):
        self.job_name = job_name
        self.runtime_id = runtime_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

