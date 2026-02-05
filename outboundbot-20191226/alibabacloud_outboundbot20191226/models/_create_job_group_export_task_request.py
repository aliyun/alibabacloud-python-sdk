# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateJobGroupExportTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        option: List[str] = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.option = option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.option is not None:
            result['Option'] = self.option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        return self

