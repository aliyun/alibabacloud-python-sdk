# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDynamicConfigRequest(DaraModel):
    def __init__(
        self,
        config_list: str = None,
        dts_job_id: str = None,
        enable_limit: bool = None,
        job_code: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The rate limit configurations.
        # 
        # - **dts.datamove.blaster.qps.max**: the queries per second (QPS) for querying the source database.
        # - **dts.datamove.source.rps.max**: the records per second (RPS) for full data synchronization or migration.
        # - **dts.datamove.source.bps.max**: the data volume per second for full data synchronization or migration. Unit: bytes per second.
        # 
        # > - If **JobCode** is set to **03**, you must set **EnableLimit** to **true** for the three parameters to take effect.
        # - If **JobCode** is set to **04** or **07**, you only need to configure **dts.datamove.source.rps.max** and **dts.datamove.source.bps.max**.
        # - A value of **-1** indicates that no rate limit is applied.
        self.config_list = config_list
        # The ID of the data synchronization or migration task.
        # 
        # > You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to obtain the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # Specifies whether to limit the migration rate of the full data synchronization or migration task. Valid values: **true** and **false**.
        # 
        # > This parameter is required only when **JobCode** is set to **03**.
        self.enable_limit = enable_limit
        # The task code. Valid values:
        # 
        # - **03**: full data synchronization or migration task.
        # - **04**: incremental data migration task.
        # - **07**: incremental data synchronization task.
        # 
        # This parameter is required.
        self.job_code = job_code
        # The ID of the region where the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_list is not None:
            result['ConfigList'] = self.config_list

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.enable_limit is not None:
            result['EnableLimit'] = self.enable_limit

        if self.job_code is not None:
            result['JobCode'] = self.job_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            self.config_list = m.get('ConfigList')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EnableLimit') is not None:
            self.enable_limit = m.get('EnableLimit')

        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

