# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApsWebhookRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        job_type: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # **JobType**\\
        # Job type. SLS or OSS Export Task: ResultExport.
        self.job_type = job_type
        # The region ID.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

