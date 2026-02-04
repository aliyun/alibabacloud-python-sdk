# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkipFullJobTableRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_progress_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the DTS task. The DTS task can be a data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The ID of the primary key.
        self.job_progress_id = job_progress_id
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to query only zero-extract, transform, load (ETL) integration tasks. Valid values:
        # 
        # *   **true**: yes.
        # *   **false**: no.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.job_progress_id is not None:
            result['JobProgressId'] = self.job_progress_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('JobProgressId') is not None:
            self.job_progress_id = m.get('JobProgressId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

