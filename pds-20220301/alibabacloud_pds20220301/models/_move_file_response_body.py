# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveFileResponseBody(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        exist: bool = None,
        file_id: str = None,
        file_name: str = None,
        revision_id: str = None,
        updated_at: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # If an empty string is returned, the file is moved.
        # 
        # If a non-empty string is returned, an asynchronous task is required. You can call the GetAsyncTask operation to obtain the information about an asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # Indicates whether the file already exists in the destination directory.
        self.exist = exist
        # The file ID.
        self.file_id = file_id
        self.file_name = file_name
        self.revision_id = revision_id
        self.updated_at = updated_at

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

        if self.exist is not None:
            result['exist'] = self.exist

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('exist') is not None:
            self.exist = m.get('exist')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

