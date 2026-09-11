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
        # The ID of the precheck task. You can call **DescribePreCheckStatus** to query the ID.
        self.job_id = job_id
        # The region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to suppress the precheck item. Valid values:
        # 
        # - **true**: Suppress the precheck item.
        # - **false**: Unsuppress the precheck item.
        # 
        # This parameter is required.
        self.skip = skip
        # The abbreviated names of the precheck items to suppress or unsuppress. Valid values:
        # 
        # - **["CHECK_SAME_OBJ"]**: check for objects with the same name.
        # - **["CHECK_SAME_USER"]**: check for accounts with different names.
        # - **["CHECK_SRC"]**: source database version check.
        # - **["CHECK_TOPOLOGY"]**: topology version check. For the topology versions supported by DTS, see [Topology overview](https://help.aliyun.com/document_detail/124115.html).
        # - **["CHECK_SERVER_ID"]**: source database server_id check.
        # - **["CHECK_DEST_TABLE_EMPTY"]**: destination database object existence check.
        # - **["CHECK_SUPER_AUTH_DEST"]**: destination database super account permission check.
        # 
        # > Separate multiple item names with commas (,), for example, **["CHECK_SRC","CHECK_SAME_OBJ"]**.
        self.skip_pre_check_items = skip_pre_check_items
        # The full names of the precheck items to suppress or unsuppress. This parameter corresponds to the **SkipPreCheckItems** parameter. Valid values:
        # 
        # - **["CHECK_SAME_OBJ_DETAIL"]**: check for objects with the same name.
        # - **["CHECK_SAME_USER_DETAIL"]**: check for accounts with different names.
        # - **["CHECK_SRC_DETAIL"]**: source database version check.
        # - **["CHECK_TOPOLOGY_DETAIL"]**: topology version check. For the topology versions supported by DTS, see [Topology overview](https://help.aliyun.com/document_detail/124115.html).
        # - **["CHECK_SERVER_ID_DETAIL"]**: source database server_id check.
        # - **["CHECK_DEST_TABLE_EMPTY_DETAIL"]**: check whether the destination database tables are empty.
        # - **["CHECK_SUPER_AUTH_DEST_DETAIL"]**: check the super account permissions of the destination database.
        # 
        # > Separate multiple item names with commas (,), for example, **["CHECK_SRC_DETAIL","CHECK_SAME_OBJ_DETAIL"]**.
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

