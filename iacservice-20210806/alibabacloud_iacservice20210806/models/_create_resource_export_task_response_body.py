# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id

        if self.export_version is not None:
            result['exportVersion'] = self.export_version

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')

        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

