# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartSqlExecutionResult(DaraModel):
    def __init__(
        self,
        newly_created: bool = None,
        sql_execution_id: str = None,
        success: bool = None,
    ):
        self.newly_created = newly_created
        self.sql_execution_id = sql_execution_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.newly_created is not None:
            result['newlyCreated'] = self.newly_created

        if self.sql_execution_id is not None:
            result['sqlExecutionId'] = self.sql_execution_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newlyCreated') is not None:
            self.newly_created = m.get('newlyCreated')

        if m.get('sqlExecutionId') is not None:
            self.sql_execution_id = m.get('sqlExecutionId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

