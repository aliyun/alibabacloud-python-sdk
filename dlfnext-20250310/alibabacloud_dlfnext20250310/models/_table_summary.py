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
        last_requester: str = None,
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
        top_requester: str = None,
        total_file_access_num: int = None,
        total_file_access_num_30d: int = None,
        total_file_access_num_7d: int = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
        total_meta_file_count: int = None,
        total_meta_size_in_bytes: int = None,
        unaccessed_std_ia_partition_count_180d: int = None,
        unaccessed_std_partition_count_30d: int = None,
        updated_at: int = None,
    ):
        # The timestamp, in milliseconds, indicating when the table was created.
        self.created_at = created_at
        # The name of the database.
        self.database_name = database_name
        # The generation date of the storage summary.
        self.generated_date = generated_date
        # The timestamp, in milliseconds, indicating when the table data was last accessed.
        self.last_access_time = last_access_time
        self.last_requester = last_requester
        # The total size of data files in the Archive storage class, in bytes.
        self.obj_type_archive_size = obj_type_archive_size
        # The total size of data files in the Cold Archive storage class, in bytes.
        self.obj_type_cold_archive_size = obj_type_cold_archive_size
        # The total size of data files in the Infrequent Access storage class, in bytes.
        self.obj_type_ia_size = obj_type_ia_size
        # The total size of data files in the Standard storage class, in bytes.
        self.obj_type_standard_size = obj_type_standard_size
        # The total number of partitions in the table.
        self.partition_count = partition_count
        # The storage location of the table.
        self.path = path
        # The storage action parameters.
        self.storage_action_params = storage_action_params
        self.storage_action_timestamp = storage_action_timestamp
        # The storage class.
        self.storage_class = storage_class
        # The name of the table.
        self.table_name = table_name
        self.top_requester = top_requester
        # Total file access count.
        self.total_file_access_num = total_file_access_num
        # Total file access count over the last 30 days.
        self.total_file_access_num_30d = total_file_access_num_30d
        # Total file access count over the last 7 days.
        self.total_file_access_num_7d = total_file_access_num_7d
        # The total number of files in the table.
        self.total_file_count = total_file_count
        # The total storage capacity of the table, in bytes.
        self.total_file_size_in_bytes = total_file_size_in_bytes
        # The total number of metadata files.
        self.total_meta_file_count = total_meta_file_count
        # The total size of metadata files, in bytes.
        self.total_meta_size_in_bytes = total_meta_size_in_bytes
        # The number of Standard or Infrequent Access partitions unaccessed in the last 180 days.
        self.unaccessed_std_ia_partition_count_180d = unaccessed_std_ia_partition_count_180d
        # The number of Standard partitions unaccessed in the last 30 days.
        self.unaccessed_std_partition_count_30d = unaccessed_std_partition_count_30d
        # The update time.
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

        if self.last_requester is not None:
            result['lastRequester'] = self.last_requester

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

        if self.top_requester is not None:
            result['topRequester'] = self.top_requester

        if self.total_file_access_num is not None:
            result['totalFileAccessNum'] = self.total_file_access_num

        if self.total_file_access_num_30d is not None:
            result['totalFileAccessNum30d'] = self.total_file_access_num_30d

        if self.total_file_access_num_7d is not None:
            result['totalFileAccessNum7d'] = self.total_file_access_num_7d

        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count

        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes

        if self.total_meta_file_count is not None:
            result['totalMetaFileCount'] = self.total_meta_file_count

        if self.total_meta_size_in_bytes is not None:
            result['totalMetaSizeInBytes'] = self.total_meta_size_in_bytes

        if self.unaccessed_std_ia_partition_count_180d is not None:
            result['unaccessedStdIaPartitionCount180d'] = self.unaccessed_std_ia_partition_count_180d

        if self.unaccessed_std_partition_count_30d is not None:
            result['unaccessedStdPartitionCount30d'] = self.unaccessed_std_partition_count_30d

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

        if m.get('lastRequester') is not None:
            self.last_requester = m.get('lastRequester')

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

        if m.get('topRequester') is not None:
            self.top_requester = m.get('topRequester')

        if m.get('totalFileAccessNum') is not None:
            self.total_file_access_num = m.get('totalFileAccessNum')

        if m.get('totalFileAccessNum30d') is not None:
            self.total_file_access_num_30d = m.get('totalFileAccessNum30d')

        if m.get('totalFileAccessNum7d') is not None:
            self.total_file_access_num_7d = m.get('totalFileAccessNum7d')

        if m.get('totalFileCount') is not None:
            self.total_file_count = m.get('totalFileCount')

        if m.get('totalFileSizeInBytes') is not None:
            self.total_file_size_in_bytes = m.get('totalFileSizeInBytes')

        if m.get('totalMetaFileCount') is not None:
            self.total_meta_file_count = m.get('totalMetaFileCount')

        if m.get('totalMetaSizeInBytes') is not None:
            self.total_meta_size_in_bytes = m.get('totalMetaSizeInBytes')

        if m.get('unaccessedStdIaPartitionCount180d') is not None:
            self.unaccessed_std_ia_partition_count_180d = m.get('unaccessedStdIaPartitionCount180d')

        if m.get('unaccessedStdPartitionCount30d') is not None:
            self.unaccessed_std_partition_count_30d = m.get('unaccessedStdPartitionCount30d')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

