# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogStoreLogsTask(DaraModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        from_: int = None,
        progress: int = None,
        query: str = None,
        task_id: str = None,
        to: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.from_ = from_
        self.progress = progress
        self.query = query
        self.task_id = task_id
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.from_ is not None:
            result['from'] = self.from_

        if self.progress is not None:
            result['progress'] = self.progress

        if self.query is not None:
            result['query'] = self.query

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

