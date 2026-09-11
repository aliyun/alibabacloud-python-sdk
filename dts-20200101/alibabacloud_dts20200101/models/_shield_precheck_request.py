# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShieldPrecheckRequest(DaraModel):
    def __init__(
        self,
        dts_instance_id: str = None,
        precheck_items: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the data migration or synchronization instance. You can call the **DescribeMigrationJobs** or DescribeSynchronizationJobs operation to query the instance ID.
        # 
        # This parameter is required.
        self.dts_instance_id = dts_instance_id
        # The precheck items to skip. Separate multiple items with commas (,). Valid values:
        # 
        # - **CHECK_SAME_OBJ**: checks whether objects with the same name exist.
        # - **CHECK_SAME_USER**: checks whether accounts with different names exist.
        # - **CHECK_SRC**: checks the source database version.
        # - **CHECK_TOPOLOGY**: checks the topology version.
        # > For the topology versions supported by DTS, see [Topology overview](https://help.aliyun.com/document_detail/124115.html).
        # - **CHECK_SERVER_ID**: checks the server_id of the source database.
        # 
        # This parameter is required.
        self.precheck_items = precheck_items
        # The ID of the region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
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
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.precheck_items is not None:
            result['PrecheckItems'] = self.precheck_items

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('PrecheckItems') is not None:
            self.precheck_items = m.get('PrecheckItems')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

