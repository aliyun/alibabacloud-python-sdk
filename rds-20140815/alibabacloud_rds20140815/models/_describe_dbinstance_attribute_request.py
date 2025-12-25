# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        expired: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # >Notice: Do not query the details of multiple instances at a time by using multiple instance IDs. Otherwise, the query times out and fails.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether the instance expires. Valid values:
        # 
        # *   **True**
        # *   **False**
        self.expired = expired
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

