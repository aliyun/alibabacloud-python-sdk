# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskFromResourceImportRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        export_task_id: str = None,
        export_version: str = None,
        task_name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.export_task_id = export_task_id
        # This parameter is required.
        self.export_version = export_version
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id

        if self.export_version is not None:
            result['exportVersion'] = self.export_version

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')

        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

