# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ResumeJobsRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_id: List[str] = None,
        job_reference_id: List[str] = None,
        scenario_id: str = None,
    ):
        # This parameter is required.
        self.all = all
        # This parameter is required.
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.job_reference_id = job_reference_id
        self.scenario_id = scenario_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_reference_id is not None:
            result['JobReferenceId'] = self.job_reference_id

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobReferenceId') is not None:
            self.job_reference_id = m.get('JobReferenceId')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        return self

