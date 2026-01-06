# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SparkBatchSQLStatement(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        code: str = None,
        end_time: int = None,
        error: str = None,
        result: str = None,
        result_uri: str = None,
        start_time: int = None,
        state: str = None,
        statement_id: str = None,
    ):
        self.app_id = app_id
        self.code = code
        self.end_time = end_time
        self.error = error
        self.result = result
        self.result_uri = result_uri
        self.start_time = start_time
        self.state = state
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error is not None:
            result['Error'] = self.error

        if self.result is not None:
            result['Result'] = self.result

        if self.result_uri is not None:
            result['ResultUri'] = self.result_uri

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ResultUri') is not None:
            self.result_uri = m.get('ResultUri')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        return self

