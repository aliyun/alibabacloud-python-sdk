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
        # The ID of the change tracking instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        # 
        # >  You must specify at least one of the **DtsInstanceId** and **DtsJobId** parameters.
        # 
        # This parameter is required.
        self.dts_instance_id = dts_instance_id
        # The precheck items that you want to ignore. Separate multiple items with commas (,). Valid values:
        #  
        # *   **CHECK_SAME_OBJ**: schema name conflict
        #  
        # *   **CHECK_SAME_USER**: multiple usernames for one instance
        #  
        # *   **CHECK_SRC**: source database version
        #  
        # *   **CHECK_TOPOLOGY**: topology
        #  
        # > For more information about the topologies supported by DTS, see [Synchronization topologies](https://help.aliyun.com/document_detail/124115.html).
        #  
        # *   **CHECK_SERVER_ID**: value of server_id in the source database
        # 
        # This parameter is required.
        self.precheck_items = precheck_items
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

