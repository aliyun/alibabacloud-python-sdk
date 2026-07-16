# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelTranslationTaskRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        task_id: str = None,
    ):
        self.apikey = apikey
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

