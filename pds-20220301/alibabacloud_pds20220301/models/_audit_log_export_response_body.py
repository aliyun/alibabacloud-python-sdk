# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuditLogExportResponseBody(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
    ):
        # The ID of the asynchronous task used to export audit logs.
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')

        return self

