# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnvironmentMetricTargetsRequest(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        job_name: str = None,
        region_id: str = None,
    ):
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The job name.
        self.job_name = job_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

