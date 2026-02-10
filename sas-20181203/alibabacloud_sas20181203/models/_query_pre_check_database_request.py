# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPreCheckDatabaseRequest(DaraModel):
    def __init__(
        self,
        instance_uuid: str = None,
        task_id: str = None,
        uni_region_id: str = None,
    ):
        # The UUID of the agent that is used to back up the data of the database.
        # 
        # > You can call the [DescribeUniBackupDatabase](~~DescribeUniBackupDatabase~~) operation to query the UUID.
        self.instance_uuid = instance_uuid
        # The ID of the database precheck task.
        # 
        # > You can call the [StartPreCheckDatabase](~~StartPreCheckDatabase~~) operation to query the ID of the database precheck task.
        self.task_id = task_id
        # The region ID of the server that hosts the database.
        # 
        # This parameter is required.
        self.uni_region_id = uni_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uni_region_id is not None:
            result['UniRegionId'] = self.uni_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UniRegionId') is not None:
            self.uni_region_id = m.get('UniRegionId')

        return self

