# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class TableSummary(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        database_name: str = None,
        generated_date: str = None,
        last_access_time: int = None,
        obj_type_archive_size: int = None,
        obj_type_cold_archive_size: int = None,
        obj_type_ia_size: int = None,
        obj_type_standard_size: int = None,
        partition_count: int = None,
        path: str = None,
        storage_action_params: Dict[str, str] = None,
        storage_action_timestamp: int = None,
        storage_class: str = None,
        table_name: str = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
        updated_at: int = None,
    ):
        # Latest snapshot storage size
        self.created_at = created_at
        # Database name
        self.database_name = database_name
        self.generated_date = generated_date
        self.last_access_time = last_access_time
        self.obj_type_archive_size = obj_type_archive_size
        self.obj_type_cold_archive_size = obj_type_cold_archive_size
        self.obj_type_ia_size = obj_type_ia_size
        self.obj_type_standard_size = obj_type_standard_size
        # Creation timestamp in milliseconds
        self.partition_count = partition_count
        self.path = path
        self.storage_action_params = storage_action_params
        self.storage_action_timestamp = storage_action_timestamp
        self.storage_class = storage_class
        # Table name
        self.table_name = table_name
        # 30-day access count
        self.total_file_count = total_file_count
        self.total_file_size_in_bytes = total_file_size_in_bytes
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.generated_date is not None:
            result['generatedDate'] = self.generated_date

        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time

        if self.obj_type_archive_size is not None:
            result['objTypeArchiveSize'] = self.obj_type_archive_size

        if self.obj_type_cold_archive_size is not None:
            result['objTypeColdArchiveSize'] = self.obj_type_cold_archive_size

        if self.obj_type_ia_size is not None:
            result['objTypeIaSize'] = self.obj_type_ia_size

        if self.obj_type_standard_size is not None:
            result['objTypeStandardSize'] = self.obj_type_standard_size

        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count

        if self.path is not None:
            result['path'] = self.path

        if self.storage_action_params is not None:
            result['storageActionParams'] = self.storage_action_params

        if self.storage_action_timestamp is not None:
            result['storageActionTimestamp'] = self.storage_action_timestamp

        if self.storage_class is not None:
            result['storageClass'] = self.storage_class

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count

        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('generatedDate') is not None:
            self.generated_date = m.get('generatedDate')

        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')

        if m.get('objTypeArchiveSize') is not None:
            self.obj_type_archive_size = m.get('objTypeArchiveSize')

        if m.get('objTypeColdArchiveSize') is not None:
            self.obj_type_cold_archive_size = m.get('objTypeColdArchiveSize')

        if m.get('objTypeIaSize') is not None:
            self.obj_type_ia_size = m.get('objTypeIaSize')

        if m.get('objTypeStandardSize') is not None:
            self.obj_type_standard_size = m.get('objTypeStandardSize')

        if m.get('partitionCount') is not None:
            self.partition_count = m.get('partitionCount')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('storageActionParams') is not None:
            self.storage_action_params = m.get('storageActionParams')

        if m.get('storageActionTimestamp') is not None:
            self.storage_action_timestamp = m.get('storageActionTimestamp')

        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('totalFileCount') is not None:
            self.total_file_count = m.get('totalFileCount')

        if m.get('totalFileSizeInBytes') is not None:
            self.total_file_size_in_bytes = m.get('totalFileSizeInBytes')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

