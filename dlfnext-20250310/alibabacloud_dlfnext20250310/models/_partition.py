# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import Dict, Any


class Partition(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        done: bool = None,
        file_count: int = None,
        file_size_in_bytes: int = None,
        last_file_creation_time: int = None,
        record_count: int = None,
        spec: Dict[str, Any] = None,
        storage_action: str = None,
        storage_action_timestamp: int = None,
        storage_class: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.done = done
        self.file_count = file_count
        self.file_size_in_bytes = file_size_in_bytes
        self.last_file_creation_time = last_file_creation_time
        self.record_count = record_count
        self.spec = spec
        self.storage_action = storage_action
        self.storage_action_timestamp = storage_action_timestamp
        self.storage_class = storage_class
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.done is not None:
            result['done'] = self.done

        if self.file_count is not None:
            result['fileCount'] = self.file_count

        if self.file_size_in_bytes is not None:
            result['fileSizeInBytes'] = self.file_size_in_bytes

        if self.last_file_creation_time is not None:
            result['lastFileCreationTime'] = self.last_file_creation_time

        if self.record_count is not None:
            result['recordCount'] = self.record_count

        if self.spec is not None:
            result['spec'] = self.spec

        if self.storage_action is not None:
            result['storageAction'] = self.storage_action

        if self.storage_action_timestamp is not None:
            result['storageActionTimestamp'] = self.storage_action_timestamp

        if self.storage_class is not None:
            result['storageClass'] = self.storage_class

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('done') is not None:
            self.done = m.get('done')

        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')

        if m.get('fileSizeInBytes') is not None:
            self.file_size_in_bytes = m.get('fileSizeInBytes')

        if m.get('lastFileCreationTime') is not None:
            self.last_file_creation_time = m.get('lastFileCreationTime')

        if m.get('recordCount') is not None:
            self.record_count = m.get('recordCount')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        if m.get('storageAction') is not None:
            self.storage_action = m.get('storageAction')

        if m.get('storageActionTimestamp') is not None:
            self.storage_action_timestamp = m.get('storageActionTimestamp')

        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

