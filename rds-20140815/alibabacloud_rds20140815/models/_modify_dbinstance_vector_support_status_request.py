# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceVectorSupportStatusRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        status: str = None,
    ):
        # Instance ID. You can obtain it by invoking DescribeDBInstances.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The status of the vector storage toggle. Valid values:
        # 
        # - **ON**: Enabled.
        # - **OFF**: Disabled.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

