# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQueryOptimizeExecErrorSampleRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        instance_id: str = None,
        sql_id: str = None,
        time: str = None,
    ):
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PolarDBMySQL**
        # *   **PostgreSQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The SQL template ID. You can call the [GetQueryOptimizeExecErrorStats](https://help.aliyun.com/document_detail/405235.html) operation to obtain the SQL template ID.
        # 
        # This parameter is required.
        self.sql_id = sql_id
        # The date to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.time = time

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

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

