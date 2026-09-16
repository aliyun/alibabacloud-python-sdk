# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryLumaWithSQLRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        max_rows: int = None,
        sql: str = None,
    ):
        # The name of the Agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # Rows exceeding this limit are truncated. The IsTruncated field in the response indicates whether truncation occurred.
        self.max_rows = max_rows
        # Only query statements are supported.
        # 
        # This parameter is required.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.max_rows is not None:
            result['MaxRows'] = self.max_rows

        if self.sql is not None:
            result['Sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('MaxRows') is not None:
            self.max_rows = m.get('MaxRows')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        return self

