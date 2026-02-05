# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobDataParsingTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        job_file_path: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.job_file_path = job_file_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')

        return self

