# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatabaseSummary(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        database_name: str = None,
        generated_date: str = None,
        location: str = None,
        obj_type_archive_size: int = None,
        obj_type_cold_archive_size: int = None,
        obj_type_ia_size: int = None,
        obj_type_standard_size: int = None,
        partition_count: int = None,
        table_count: int = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
        total_meta_size_in_bytes: int = None,
    ):
        # Creation timestamp in milliseconds
        self.created_at = created_at
        # 库名 - Database name
        self.database_name = database_name
        # Last profile update date in format yyyyMMdd
        self.generated_date = generated_date
        # Storage location URI
        self.location = location
        self.obj_type_archive_size = obj_type_archive_size
        self.obj_type_cold_archive_size = obj_type_cold_archive_size
        self.obj_type_ia_size = obj_type_ia_size
        self.obj_type_standard_size = obj_type_standard_size
        self.partition_count = partition_count
        # Total storage in bytes
        self.table_count = table_count
        self.total_file_count = total_file_count
        # Total file count
        self.total_file_size_in_bytes = total_file_size_in_bytes
        self.total_meta_size_in_bytes = total_meta_size_in_bytes

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

        if self.location is not None:
            result['location'] = self.location

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

        if self.table_count is not None:
            result['tableCount'] = self.table_count

        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count

        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes

        if self.total_meta_size_in_bytes is not None:
            result['totalMetaSizeInBytes'] = self.total_meta_size_in_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('generatedDate') is not None:
            self.generated_date = m.get('generatedDate')

        if m.get('location') is not None:
            self.location = m.get('location')

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

        if m.get('tableCount') is not None:
            self.table_count = m.get('tableCount')

        if m.get('totalFileCount') is not None:
            self.total_file_count = m.get('totalFileCount')

        if m.get('totalFileSizeInBytes') is not None:
            self.total_file_size_in_bytes = m.get('totalFileSizeInBytes')

        if m.get('totalMetaSizeInBytes') is not None:
            self.total_meta_size_in_bytes = m.get('totalMetaSizeInBytes')

        return self

