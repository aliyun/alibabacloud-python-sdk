# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceDescriptionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        resource_group_id: str = None,
    ):
        # The description of the instance.
        # 
        # The description must be 2 to 256 characters in length. It cannot start with http:// or https://.
        # 
        # This parameter is required.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is no longer used.
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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

