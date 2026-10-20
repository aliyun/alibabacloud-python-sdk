# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CacheLoadTaskInfo(DaraModel):
    def __init__(
        self,
        catalog_id: str = None,
        completed_files: int = None,
        database: str = None,
        enumerated_files: int = None,
        enumeration_done: bool = None,
        extra_options: Dict[str, str] = None,
        failed_files: int = None,
        last_error: str = None,
        loaded_bytes: int = None,
        path: str = None,
        started_at: int = None,
        status: str = None,
        table: str = None,
        task_id: str = None,
        task_updated_at: int = None,
        total_bytes: int = None,
        total_files: int = None,
    ):
        # The data catalog ID.
        self.catalog_id = catalog_id
        # The number of files with completed cache loading.
        self.completed_files = completed_files
        # The database name.
        self.database = database
        # The number of enumerated files.
        self.enumerated_files = enumerated_files
        # The file enumeration completion status.
        self.enumeration_done = enumeration_done
        # The additional parameters.
        self.extra_options = extra_options
        # The number of files with failed cache loading.
        self.failed_files = failed_files
        # The most recent error message, which is empty when the status is normal.
        self.last_error = last_error
        # The number of bytes loaded into the cache.
        self.loaded_bytes = loaded_bytes
        # The storage location.
        self.path = path
        # The start time of the task execution, in milliseconds.
        self.started_at = started_at
        # The task execution status.
        self.status = status
        # The table name.
        self.table = table
        # The task ID.
        self.task_id = task_id
        # The task update time, in milliseconds.
        self.task_updated_at = task_updated_at
        # The total number of bytes.
        self.total_bytes = total_bytes
        # The total number of files.
        self.total_files = total_files

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.completed_files is not None:
            result['completedFiles'] = self.completed_files

        if self.database is not None:
            result['database'] = self.database

        if self.enumerated_files is not None:
            result['enumeratedFiles'] = self.enumerated_files

        if self.enumeration_done is not None:
            result['enumerationDone'] = self.enumeration_done

        if self.extra_options is not None:
            result['extraOptions'] = self.extra_options

        if self.failed_files is not None:
            result['failedFiles'] = self.failed_files

        if self.last_error is not None:
            result['lastError'] = self.last_error

        if self.loaded_bytes is not None:
            result['loadedBytes'] = self.loaded_bytes

        if self.path is not None:
            result['path'] = self.path

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.table is not None:
            result['table'] = self.table

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_updated_at is not None:
            result['taskUpdatedAt'] = self.task_updated_at

        if self.total_bytes is not None:
            result['totalBytes'] = self.total_bytes

        if self.total_files is not None:
            result['totalFiles'] = self.total_files

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('completedFiles') is not None:
            self.completed_files = m.get('completedFiles')

        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('enumeratedFiles') is not None:
            self.enumerated_files = m.get('enumeratedFiles')

        if m.get('enumerationDone') is not None:
            self.enumeration_done = m.get('enumerationDone')

        if m.get('extraOptions') is not None:
            self.extra_options = m.get('extraOptions')

        if m.get('failedFiles') is not None:
            self.failed_files = m.get('failedFiles')

        if m.get('lastError') is not None:
            self.last_error = m.get('lastError')

        if m.get('loadedBytes') is not None:
            self.loaded_bytes = m.get('loadedBytes')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskUpdatedAt') is not None:
            self.task_updated_at = m.get('taskUpdatedAt')

        if m.get('totalBytes') is not None:
            self.total_bytes = m.get('totalBytes')

        if m.get('totalFiles') is not None:
            self.total_files = m.get('totalFiles')

        return self

