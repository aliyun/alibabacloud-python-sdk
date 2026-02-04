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
        # The specific throttling configuration.
        # 
        # *   **dts.datamove.blaster.qps.max**: The rate at which queries are made to the source database per second.
        # *   **dts.datamove.source.rps.max**: The number of rows that are fully synchronized or migrated per second.
        # *   **dts.datamove.source.bps.max**: the amount of data processed per second for full synchronization or migration. Unit: MB.
        # 
        # > 
        # 
        # *   If you set the **JobCode** parameter to **03**, you need to specify **true** for the **EnableLimit** parameter. Otherwise, the configuration cannot take effect.
        # 
        # *   If you set the **JobCode** parameter to **04** or **07**, you only need to specify the **dts.datamove.source.rps.max** and **dts.datamove.source.bps.max** parameters.
        # *   A value of \\*\\*-1\\*\\* indicates no rate limit.
        self.config_list = config_list
        # The ID of the data migration or synchronization task.
        # 
        # >  You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # Specifies whether to enable throttling for data synchronization or migration. Valid values: **true** and **false**.
        # 
        # >  Only needs to be configured when the **JobCode** parameter is set to **03**.
        self.enable_limit = enable_limit
        # The task type. Valid values:
        # 
        # *   **03**: a full data synchronization or full data migration task.
        # *   **04**: an incremental data migration task.
        # *   **07**: an incremental data synchronization task.
        # 
        # This parameter is required.
        self.job_code = job_code
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
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

