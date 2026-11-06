# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeFileSystemsResponseBody(DaraModel):
    def __init__(
        self,
        bucket_id: str = None,
        file_count: int = None,
        file_system_id: str = None,
        file_systems: List[main_models.DescribeFileSystemsResponseBodyFileSystems] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The bucket ID.
        self.bucket_id = bucket_id
        # The total number of files that match the conditions.
        self.file_count = file_count
        # The file system ID.
        self.file_system_id = file_system_id
        # The list of files.
        self.file_systems = file_systems
        # Indicates whether the results are truncated. If true, you can use NextToken to retrieve subsequent results.
        self.is_truncated = is_truncated
        # The maximum number of records returned for this request.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.file_systems:
            for v1 in self.file_systems:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_id is not None:
            result['BucketId'] = self.bucket_id

        if self.file_count is not None:
            result['FileCount'] = self.file_count

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        result['FileSystems'] = []
        if self.file_systems is not None:
            for k1 in self.file_systems:
                result['FileSystems'].append(k1.to_map() if k1 else None)

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketId') is not None:
            self.bucket_id = m.get('BucketId')

        if m.get('FileCount') is not None:
            self.file_count = m.get('FileCount')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k1 in m.get('FileSystems'):
                temp_model = main_models.DescribeFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k1))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFileSystemsResponseBodyFileSystems(DaraModel):
    def __init__(
        self,
        capacity: str = None,
        file_name: str = None,
        last_modified: str = None,
        storage_type: str = None,
    ):
        # The file capacity.
        self.capacity = capacity
        # The file name.
        self.file_name = file_name
        # The last modified time of the file, in RFC 3339 UTC format.
        self.last_modified = last_modified
        # The storage type of the file.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

