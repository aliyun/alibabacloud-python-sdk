# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocParsingResultRequest(DaraModel):
    def __init__(
        self,
        return_format: str = None,
        task_id: str = None,
    ):
        # - The document parsing result supports two formats: markdown and json.
        # - By default, the result is returned in markdown format.
        self.return_format = return_format
        # - Task ID.
        # - The taskId is obtained from the SubmitDocParsingTaskAdvance or SubmitDocParsingTask interfaces.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.return_format is not None:
            result['returnFormat'] = self.return_format

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('returnFormat') is not None:
            self.return_format = m.get('returnFormat')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

