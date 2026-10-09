# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMasterSpecRequest(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        effective_time: str = None,
        master_aispec: str = None,
        master_cu: int = None,
        resource_group_id: str = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The effective period of the specification change. Valid values: 
        # - **Immediately** (default): The change takes effect immediately.
        # - **MaintainTime**: The change takes effect during the maintenance window of the instance.
        self.effective_time = effective_time
        # If you want to change the master node to a MasterAI node, specify this parameter.
        # 
        # > - This parameter and MasterCU cannot be specified at the same time.
        # >- Only specific regions and zones support changing the master node to a MasterAI node.
        # >- Only AnalyticDB for PostgreSQL V7.0 Basic Edition instances support MasterAI nodes.
        # >- You can view all valid values of this parameter on the specification change page for the master node.
        self.master_aispec = master_aispec
        # The master resources. Valid values: 
        # - 2 CU 
        # - 4 CU 
        # - 8 CU 
        # - 16 CU 
        # - 32 CU 
        # > Master resources greater than 8 CU incur additional fees.
        self.master_cu = master_cu
        # The ID of the resource group to which the instance belongs. For information about how to obtain the resource group ID, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
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

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

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

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('MasterAISpec') is not None:
            self.master_aispec = m.get('MasterAISpec')

        if m.get('MasterCU') is not None:
            self.master_cu = m.get('MasterCU')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

