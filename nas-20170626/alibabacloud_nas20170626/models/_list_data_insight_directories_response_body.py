# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListDataInsightDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        directory: main_models.ListDataInsightDirectoriesResponseBodyDirectory = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.directory = directory
        self.file_system_id = file_system_id
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            temp_model = main_models.ListDataInsightDirectoriesResponseBodyDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataInsightDirectoriesResponseBodyDirectory(DaraModel):
    def __init__(
        self,
        dir_capacity: int = None,
        dir_capacity_offline: int = None,
        dir_capacity_online: int = None,
        file_count: int = None,
        file_count_offline: int = None,
        file_count_online: int = None,
        sub_directories: List[main_models.ListDataInsightDirectoriesResponseBodyDirectorySubDirectories] = None,
    ):
        self.dir_capacity = dir_capacity
        self.dir_capacity_offline = dir_capacity_offline
        self.dir_capacity_online = dir_capacity_online
        self.file_count = file_count
        self.file_count_offline = file_count_offline
        self.file_count_online = file_count_online
        self.sub_directories = sub_directories

    def validate(self):
        if self.sub_directories:
            for v1 in self.sub_directories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dir_capacity is not None:
            result['DirCapacity'] = self.dir_capacity

        if self.dir_capacity_offline is not None:
            result['DirCapacityOffline'] = self.dir_capacity_offline

        if self.dir_capacity_online is not None:
            result['DirCapacityOnline'] = self.dir_capacity_online

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.file_count_offline is not None:
            result['FileCountOffline'] = self.file_count_offline

        if self.file_count_online is not None:
            result['FileCountOnline'] = self.file_count_online

        result['SubDirectories'] = []
        if self.sub_directories is not None:
            for k1 in self.sub_directories:
                result['SubDirectories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirCapacity') is not None:
            self.dir_capacity = m.get('DirCapacity')

        if m.get('DirCapacityOffline') is not None:
            self.dir_capacity_offline = m.get('DirCapacityOffline')

        if m.get('DirCapacityOnline') is not None:
            self.dir_capacity_online = m.get('DirCapacityOnline')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('FileCountOffline') is not None:
            self.file_count_offline = m.get('FileCountOffline')

        if m.get('FileCountOnline') is not None:
            self.file_count_online = m.get('FileCountOnline')

        self.sub_directories = []
        if m.get('SubDirectories') is not None:
            for k1 in m.get('SubDirectories'):
                temp_model = main_models.ListDataInsightDirectoriesResponseBodyDirectorySubDirectories()
                self.sub_directories.append(temp_model.from_map(k1))

        return self

class ListDataInsightDirectoriesResponseBodyDirectorySubDirectories(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        dir_capacity: int = None,
        dir_capacity_offline: int = None,
        dir_capacity_online: int = None,
        dir_level: int = None,
        dir_name: str = None,
        file_count: int = None,
        file_count_offline: int = None,
        file_count_online: int = None,
        last_access_time: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.dir_capacity = dir_capacity
        self.dir_capacity_offline = dir_capacity_offline
        self.dir_capacity_online = dir_capacity_online
        self.dir_level = dir_level
        self.dir_name = dir_name
        self.file_count = file_count
        self.file_count_offline = file_count_offline
        self.file_count_online = file_count_online
        self.last_access_time = last_access_time
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.dir_capacity is not None:
            result['DirCapacity'] = self.dir_capacity

        if self.dir_capacity_offline is not None:
            result['DirCapacityOffline'] = self.dir_capacity_offline

        if self.dir_capacity_online is not None:
            result['DirCapacityOnline'] = self.dir_capacity_online

        if self.dir_level is not None:
            result['DirLevel'] = self.dir_level

        if self.dir_name is not None:
            result['DirName'] = self.dir_name

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.file_count_offline is not None:
            result['FileCountOffline'] = self.file_count_offline

        if self.file_count_online is not None:
            result['FileCountOnline'] = self.file_count_online

        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DirCapacity') is not None:
            self.dir_capacity = m.get('DirCapacity')

        if m.get('DirCapacityOffline') is not None:
            self.dir_capacity_offline = m.get('DirCapacityOffline')

        if m.get('DirCapacityOnline') is not None:
            self.dir_capacity_online = m.get('DirCapacityOnline')

        if m.get('DirLevel') is not None:
            self.dir_level = m.get('DirLevel')

        if m.get('DirName') is not None:
            self.dir_name = m.get('DirName')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('FileCountOffline') is not None:
            self.file_count_offline = m.get('FileCountOffline')

        if m.get('FileCountOnline') is not None:
            self.file_count_online = m.get('FileCountOnline')

        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

