# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TableCompactionHistory(DaraModel):
    def __init__(
        self,
        after_files_count: int = None,
        after_files_size: int = None,
        before_files_count: int = None,
        before_files_last_creation_time: int = None,
        before_files_size: int = None,
        catalog_id: str = None,
        commit_time: int = None,
        snapshot_id: int = None,
        table_id: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.after_files_count = after_files_count
        self.after_files_size = after_files_size
        self.before_files_count = before_files_count
        self.before_files_last_creation_time = before_files_last_creation_time
        self.before_files_size = before_files_size
        self.catalog_id = catalog_id
        self.commit_time = commit_time
        self.snapshot_id = snapshot_id
        self.table_id = table_id
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_files_count is not None:
            result['afterFilesCount'] = self.after_files_count

        if self.after_files_size is not None:
            result['afterFilesSize'] = self.after_files_size

        if self.before_files_count is not None:
            result['beforeFilesCount'] = self.before_files_count

        if self.before_files_last_creation_time is not None:
            result['beforeFilesLastCreationTime'] = self.before_files_last_creation_time

        if self.before_files_size is not None:
            result['beforeFilesSize'] = self.before_files_size

        if self.catalog_id is not None:
            result['catalogId'] = self.catalog_id

        if self.commit_time is not None:
            result['commitTime'] = self.commit_time

        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id

        if self.table_id is not None:
            result['tableId'] = self.table_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('afterFilesCount') is not None:
            self.after_files_count = m.get('afterFilesCount')

        if m.get('afterFilesSize') is not None:
            self.after_files_size = m.get('afterFilesSize')

        if m.get('beforeFilesCount') is not None:
            self.before_files_count = m.get('beforeFilesCount')

        if m.get('beforeFilesLastCreationTime') is not None:
            self.before_files_last_creation_time = m.get('beforeFilesLastCreationTime')

        if m.get('beforeFilesSize') is not None:
            self.before_files_size = m.get('beforeFilesSize')

        if m.get('catalogId') is not None:
            self.catalog_id = m.get('catalogId')

        if m.get('commitTime') is not None:
            self.commit_time = m.get('commitTime')

        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

