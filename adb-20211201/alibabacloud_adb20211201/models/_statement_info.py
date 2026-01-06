# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StatementInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        completed_time_in_mills: int = None,
        output: str = None,
        process: float = None,
        started_time_in_mills: int = None,
        state: str = None,
        statement_id: str = None,
    ):
        self.code = code
        self.completed_time_in_mills = completed_time_in_mills
        self.output = output
        self.process = process
        self.started_time_in_mills = started_time_in_mills
        self.state = state
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.completed_time_in_mills is not None:
            result['CompletedTimeInMills'] = self.completed_time_in_mills

        if self.output is not None:
            result['Output'] = self.output

        if self.process is not None:
            result['Process'] = self.process

        if self.started_time_in_mills is not None:
            result['StartedTimeInMills'] = self.started_time_in_mills

        if self.state is not None:
            result['State'] = self.state

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompletedTimeInMills') is not None:
            self.completed_time_in_mills = m.get('CompletedTimeInMills')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('StartedTimeInMills') is not None:
            self.started_time_in_mills = m.get('StartedTimeInMills')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        return self

