# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQueryOptimizeTagRequest(DaraModel):
    def __init__(
        self,
        comments: str = None,
        engine: str = None,
        instance_id: str = None,
        sql_ids: str = None,
        status: int = None,
        tags: str = None,
    ):
        # The remarks.
        # 
        # The remarks can be 1 to 300 characters in length.
        self.comments = comments
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
        # The SQL template IDs. You can call the [GetQueryOptimizeExecErrorStats](https://help.aliyun.com/document_detail/405261.html) operation to obtain the SQL template ID. Separate multiple SQL template IDs with commas (,).
        # 
        # This parameter is required.
        self.sql_ids = sql_ids
        # The status of **Tags**. Valid values:
        # 
        # *   **0**: removes all tags added to the SQL templates that are specified by **SqlIds** and leaves **Tags** empty.
        # *   **1**: adds the tags specified by **Tags** to the SQL templates that are specified by **SqlIds**.
        # 
        # This parameter is required.
        self.status = status
        # The SQL tags. Separate multiple SQL tags with commas (,). Valid values:
        # 
        # *   **DAS_IMPORTANT**: The SQL template is important.
        # *   **DAS_NOT_IMPORTANT**: The SQL template is unimportant.
        # *   **USER_IGNORE**: The scheduling of the SQL template does not need to be optimized.
        # *   **DAS_IN_PLAN**: The scheduling of the SQL template needs to be optimized.
        # 
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sql_ids is not None:
            result['SqlIds'] = self.sql_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SqlIds') is not None:
            self.sql_ids = m.get('SqlIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

