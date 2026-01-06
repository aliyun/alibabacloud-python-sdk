# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartApsJobRequest(DaraModel):
    def __init__(
        self,
        aps_job_id: str = None,
        region_id: str = None,
    ):
        # The job ID.
        # 
        # This parameter is required.
        self.aps_job_id = aps_job_id
        # The region ID
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aps_job_id is not None:
            result['ApsJobId'] = self.aps_job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsJobId') is not None:
            self.aps_job_id = m.get('ApsJobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

