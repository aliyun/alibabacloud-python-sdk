# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkipPreCheckRequest(DaraModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        skip: bool = None,
        skip_pre_check_items: str = None,
        skip_pre_check_names: str = None,
    ):
        # The ID of the data migration, data synchronization, or change tracking task.
        # 
        # This parameter is required.
        self.dts_job_id = dts_job_id
        # The precheck task ID. You can call the **DescribePreCheckStatus** operation to query the task ID.
        self.job_id = job_id
        # The region ID of the DTS instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to skip the precheck item. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.skip = skip
        # The shortened name of the precheck item. Valid values:
        # 
        # *   **["CHECK_SAME_OBJ"]**: object name conflict.
        # *   **["CHECK_SAME_USER"]**: username conflict.
        # *   **["CHECK_SRC"]**: source database version.
        # *   **["CHECK_TOPOLOGY"]**: topology. For more information about the topologies supported by Data Transmission Service (DTS), see [Synchronization topologies](https://help.aliyun.com/document_detail/124115.html).
        # *   **["CHECK_SERVER_ID"]**: the server ID of the source database.
        # *   **["CHECK_DEST_TABLE_EMPTY"]**: existence of objects in the destination database.
        # 
        # > Separate multiple item names with commas (,). Example: **["CHECK_SRC","CHECK_SAME_OBJ"]**.
        self.skip_pre_check_items = skip_pre_check_items
        # The precheck item name. This parameter corresponds to **SkipPreCheckItems**. Valid values:
        # 
        # *   **["CHECK_SAME_OBJ_DETAIL"]**: object name conflict.
        # *   **["CHECK_SAME_USER_DETAIL"]**: username conflict.
        # *   **["CHECK_SRC_DETAIL"]**: source database version.
        # *   **["CHECK_TOPOLOGY_DETAIL"]**: topology. For more information about the topologies supported by DTS, see [Synchronization topologies](https://help.aliyun.com/document_detail/124115.html).
        # *   **["CHECK_SERVER_ID_DETAIL"]**: the server ID of the source database.
        # *   **["CHECK_DEST_TABLE_EMPTY_DETAIL"]**: empty tables in the destination database.
        # 
        # > Separate multiple item names with commas (,). Example: **["CHECK_SRC_DETAIL","CHECK_SAME_OBJ_DETAIL"]**.
        self.skip_pre_check_names = skip_pre_check_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.skip_pre_check_items is not None:
            result['SkipPreCheckItems'] = self.skip_pre_check_items

        if self.skip_pre_check_names is not None:
            result['SkipPreCheckNames'] = self.skip_pre_check_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SkipPreCheckItems') is not None:
            self.skip_pre_check_items = m.get('SkipPreCheckItems')

        if m.get('SkipPreCheckNames') is not None:
            self.skip_pre_check_names = m.get('SkipPreCheckNames')

        return self

