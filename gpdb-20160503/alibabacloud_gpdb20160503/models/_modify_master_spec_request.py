# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMasterSpecRequest(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        master_aispec: str = None,
        master_cu: int = None,
        resource_group_id: str = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter must be specified if you want to change coordinator nodes to AI coordinator nodes.
        # >-  You cannot specify the MasterAISpec and MasterCU parameters at the same time.
        # >- You can change coordinator nodes to AI coordinator nodes only in specific regions and zones.
        # >- Only AnalyticDB for PostgreSQL V7.0 instances of Basic Edition support AI coordinator nodes.
        # >- You can view the valid values of this parameter on the configuration change page of coordinator nodes.
        self.master_aispec = master_aispec
        # The specifications of coordinator node resources. Valid values:
        # 
        # *   2 CU
        # *   4 CU
        # *   8 CU
        # *   16 CU
        # *   32 CU
        # 
        # >  You are charged for coordinator node resources of more than 8 compute units (CUs).
        self.master_cu = master_cu
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.master_aispec is not None:
            result['MasterAISpec'] = self.master_aispec

        if self.master_cu is not None:
            result['MasterCU'] = self.master_cu

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('MasterAISpec') is not None:
            self.master_aispec = m.get('MasterAISpec')

        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

