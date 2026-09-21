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
        # The value must be 1 to 300 characters in length.
        self.comments = comments
        # The database engine. Valid values:
        # 
        # - **MySQL**: RDS MySQL
        # - **PolarDBMySQL**: PolarDB for MySQL
        # - **PostgreSQL**: RDS PostgreSQL
        # 
        # This parameter is required.
        self.engine = engine
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The SQL template ID. You can call the [GetQueryOptimizeDataStats](https://help.aliyun.com/document_detail/405261.html) operation to query SQL template IDs. You can specify multiple template IDs separated by commas (,) to add tags in batches.
        # 
        # This parameter is required.
        self.sql_ids = sql_ids
        # The status of the **Tags** request parameter.
        # 
        # - **0**: Clears all tags for the SQL template IDs specified by **SqlIds** and ignores the **Tags** parameter.
        # - **1**: Sets the tags for the SQL template IDs specified by **SqlIds** to the values specified by **Tags**.
        # 
        # This parameter is required.
        self.status = status
        # The SQL tag. You can specify multiple values separated by commas (,).
        # 
        # - **DAS_IMPORTANT**: important SQL.
        # - **DAS_NOT_IMPORTANT**: unimportant SQL.
        # - **USER_IGNORE**: optimization not required.
        # - **DAS_IN_PLAN**: scheduled for optimization.
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

