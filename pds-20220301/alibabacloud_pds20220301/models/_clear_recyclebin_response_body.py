# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearRecyclebinResponseBody(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # You can call the GetAsyncTask operation to query the information about the asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        return self

