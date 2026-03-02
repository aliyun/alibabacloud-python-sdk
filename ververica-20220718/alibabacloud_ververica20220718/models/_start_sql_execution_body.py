# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartSqlExecutionBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        sql_file_id: str = None,
        sql_script: str = None,
    ):
        self.description = description
        self.sql_file_id = sql_file_id
        self.sql_script = sql_script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.sql_file_id is not None:
            result['sqlFileId'] = self.sql_file_id

        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('sqlFileId') is not None:
            self.sql_file_id = m.get('sqlFileId')

        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')

        return self

