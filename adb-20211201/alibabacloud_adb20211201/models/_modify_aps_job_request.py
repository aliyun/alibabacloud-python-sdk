# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApsJobRequest(DaraModel):
    def __init__(
        self,
        aps_job_id: str = None,
        db_list: str = None,
        partition_list: str = None,
        region_id: str = None,
    ):
        # The job ID.
        # 
        # This parameter is required.
        self.aps_job_id = aps_job_id
        # The objects to be synchronized.
        # 
        # This parameter is required.
        self.db_list = db_list
        # The partitions.
        self.partition_list = partition_list
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
        if self.aps_job_id is not None:
            result['ApsJobId'] = self.aps_job_id

        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.partition_list is not None:
            result['PartitionList'] = self.partition_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApsJobId') is not None:
            self.aps_job_id = m.get('ApsJobId')

        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('PartitionList') is not None:
            self.partition_list = m.get('PartitionList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

