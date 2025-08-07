# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import Dict


class PartitionSummary(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        database_name: str = None,
        last_access_time: int = None,
        partition_name: str = None,
        storage_action_params: Dict[str, str] = None,
        storage_action_timestamp: int = None,
        storage_class: str = None,
        table_name: str = None,
        total_file_count: int = None,
        total_file_size_in_bytes: int = None,
        updated_at: int = None,
    ):
        # Partition creation timestamp in milliseconds
        self.created_at = created_at
        # Database name
        self.database_name = database_name
        # Total files in partition
        self.last_access_time = last_access_time
        # Partition identifier
        self.partition_name = partition_name
        self.storage_action_params = storage_action_params
        self.storage_action_timestamp = storage_action_timestamp
        self.storage_class = storage_class
        # Table name
        self.table_name = table_name
        # 24h access count
        self.total_file_count = total_file_count
        # Last data access timestamp in milliseconds
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

        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time

        if self.partition_name is not None:
            result['partitionName'] = self.partition_name

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

        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')

        if m.get('partitionName') is not None:
            self.partition_name = m.get('partitionName')

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

