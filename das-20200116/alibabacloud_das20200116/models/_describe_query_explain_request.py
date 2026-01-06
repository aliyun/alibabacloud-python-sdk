# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQueryExplainRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        instance_id: str = None,
        node_id: str = None,
        schema: str = None,
        sql: str = None,
    ):
        self.db_name = db_name
        # This parameter is required.
        self.instance_id = instance_id
        self.node_id = node_id
        self.schema = schema
        # This parameter is required.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.sql is not None:
            result['Sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        return self

