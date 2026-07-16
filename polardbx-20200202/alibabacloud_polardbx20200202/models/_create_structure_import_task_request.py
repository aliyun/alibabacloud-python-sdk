# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStructureImportTaskRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        slink_task_id: str = None,
    ):
        # The configuration information.
        self.config = config
        # The instance ID. > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the details of all instances in the specified region, including instance IDs.
        self.dbinstance_name = dbinstance_name
        # The region in which the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the target task. > You can call the [DescribeSlinkTasks](https://help.aliyun.com/document_detail/196830.html) operation to query the execution status of the target task, including the task ID.
        # 
        # This parameter is required.
        self.slink_task_id = slink_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        return self

