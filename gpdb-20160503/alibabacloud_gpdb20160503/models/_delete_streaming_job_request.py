# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStreamingJobRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        job_id: int = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

