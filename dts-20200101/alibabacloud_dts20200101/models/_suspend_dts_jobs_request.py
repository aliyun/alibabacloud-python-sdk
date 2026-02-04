# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SuspendDtsJobsRequest(DaraModel):
    def __init__(
        self,
        dts_job_ids: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the data migration or data synchronization task.
        # 
        # > 
        # *   For multiple tasks, separate them with commas (,).
        # *   You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_ids = dts_job_ids
        # The ID of the region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource GroupId
        self.resource_group_id = resource_group_id
        # Whether it is a seamless integration (Zero-ETL) task, the value can be:
        # - **false**: No. - **true**: Yes.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_ids is not None:
            result['DtsJobIds'] = self.dts_job_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobIds') is not None:
            self.dts_job_ids = m.get('DtsJobIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

