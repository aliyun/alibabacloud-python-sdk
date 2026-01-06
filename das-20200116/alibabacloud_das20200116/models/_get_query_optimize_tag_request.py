# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQueryOptimizeTagRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        instance_id: str = None,
        sql_id: str = None,
    ):
        # The database engine. Valid values:
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL
        # *   **PolarDBMySQL**: PolarDB for MySQL
        # *   **PostgreSQL**: ApsaraDB RDS for PostgreSQL
        # 
        # This parameter is required.
        self.engine = engine
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The SQL template ID. You can call the [GetQueryOptimizeDataStats](https://help.aliyun.com/document_detail/405261.html) operation to query the SQL template ID.
        # 
        # This parameter is required.
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        return self

