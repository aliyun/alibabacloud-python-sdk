# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportTaskDTO(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        error: str = None,
        filename: str = None,
        finished_at: int = None,
        id: str = None,
        max_rows: int = None,
        progress: int = None,
        status: str = None,
        total: int = None,
        type: str = None,
    ):
        self.created_at = created_at
        self.error = error
        self.filename = filename
        self.finished_at = finished_at
        self.id = id
        self.max_rows = max_rows
        self.progress = progress
        self.status = status
        self.total = total
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.error is not None:
            result['error'] = self.error

        if self.filename is not None:
            result['filename'] = self.filename

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.id is not None:
            result['id'] = self.id

        if self.max_rows is not None:
            result['maxRows'] = self.max_rows

        if self.progress is not None:
            result['progress'] = self.progress

        if self.status is not None:
            result['status'] = self.status

        if self.total is not None:
            result['total'] = self.total

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('filename') is not None:
            self.filename = m.get('filename')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('maxRows') is not None:
            self.max_rows = m.get('maxRows')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

