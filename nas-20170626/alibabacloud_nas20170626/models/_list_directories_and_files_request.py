# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDirectoriesAndFilesRequest(DaraModel):
    def __init__(
        self,
        directory_only: bool = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        path: str = None,
        storage_type: str = None,
    ):
        # Whether to list only directories.
        # 
        # Valid values:
        # 
        # - `false` (default): Lists both directories and files.
        # 
        # - `true`: Lists only directories.
        # 
        # > If you set `StorageType` to `All`, you must set `DirectoryOnly` to `true`.
        self.directory_only = directory_only
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The maximum number of directories or files to return per page.
        # 
        # Value range: 10–128
        # 
        # Default value: 100
        self.max_results = max_results
        # A continuation token used to retrieve the next page of results when the response is truncated.
        self.next_token = next_token
        # The absolute path of the directory.
        # 
        # The path must start with a forward slash (/) and exist on the mount target.
        # 
        # This parameter is required.
        self.path = path
        # The storage type.
        # 
        # - `InfrequentAccess`: infrequent access.
        # 
        # - `Archive`: archive storage.
        # 
        # - `All`: all storage types.
        # 
        # > If you set `StorageType` to `All`, you must set `DirectoryOnly` to `true`.
        # 
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_only is not None:
            result['DirectoryOnly'] = self.directory_only

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.path is not None:
            result['Path'] = self.path

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryOnly') is not None:
            self.directory_only = m.get('DirectoryOnly')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

