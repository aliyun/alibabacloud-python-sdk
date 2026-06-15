# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListDirectoriesAndFilesResponseBody(DaraModel):
    def __init__(
        self,
        entries: List[main_models.ListDirectoriesAndFilesResponseBodyEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of directory and file entries.
        self.entries = entries
        # The pagination token. If the response is truncated, include this token in the next request to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            for v1 in self.entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entries'] = []
        if self.entries is not None:
            for k1 in self.entries:
                result['Entries'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k1 in m.get('Entries'):
                temp_model = main_models.ListDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDirectoriesAndFilesResponseBodyEntries(DaraModel):
    def __init__(
        self,
        atime: str = None,
        ctime: str = None,
        file_id: str = None,
        has_archive_file: str = None,
        has_infrequent_access_file: bool = None,
        inode: str = None,
        mtime: str = None,
        name: str = None,
        offline_duration: int = None,
        offline_unchanged_duration: int = None,
        owner: str = None,
        retrieve_time: str = None,
        size: int = None,
        storage_type: str = None,
        type: str = None,
    ):
        # The last access time (atime) of the file.
        # 
        # The time is in the ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # This parameter is returned only when `Type` is `File`.
        self.atime = atime
        # The metadata change time (ctime) of the file.
        # 
        # The time is in the ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # This parameter is returned only when `Type` is `File`.
        self.ctime = ctime
        # The ID of the file or directory.
        self.file_id = file_id
        # Specifies whether the directory contains any archive files.
        # 
        # This parameter is returned only when `Type` is `Directory`.
        # 
        # Valid values:
        # 
        # - `true`: Yes
        # 
        # - `false`: No
        self.has_archive_file = has_archive_file
        # Specifies whether the directory contains any infrequent access files.
        # 
        # This parameter is returned only when `Type` is `Directory`.
        # 
        # Valid values:
        # 
        # - `true`: Yes
        # 
        # - `false`: No
        self.has_infrequent_access_file = has_infrequent_access_file
        # The inode of the file or directory.
        self.inode = inode
        # The last modification time (mtime) of the file.
        # 
        # The time is in the ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # This parameter is returned only when `Type` is `File`.
        self.mtime = mtime
        # The name of the file or directory.
        self.name = name
        self.offline_duration = offline_duration
        self.offline_unchanged_duration = offline_unchanged_duration
        # The owner of the file or directory. This parameter is returned only when `ProtocolType` is `SMB` and access control is enabled.
        self.owner = owner
        # The last data retrieval time.
        # 
        # The time is in the ISO 8601 format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # This parameter is returned only when `Type` is `File`.
        self.retrieve_time = retrieve_time
        # The size of the file, in bytes.
        # 
        # This parameter is returned only when `Type` is `File`.
        # 
        # This value is returned and is meaningful only when Type is File.
        self.size = size
        # The storage class of the file.
        # 
        # This parameter is returned only when `Type` is `File`.
        # 
        # Valid values:
        # 
        # - `InfrequentAccess`
        # 
        # - `Archive`
        self.storage_type = storage_type
        # The type of the entry.
        # 
        # Valid values:
        # 
        # - `File`: a file
        # 
        # - `Directory`: a directory
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.atime is not None:
            result['Atime'] = self.atime

        if self.ctime is not None:
            result['Ctime'] = self.ctime

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.has_archive_file is not None:
            result['HasArchiveFile'] = self.has_archive_file

        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file

        if self.inode is not None:
            result['Inode'] = self.inode

        if self.mtime is not None:
            result['Mtime'] = self.mtime

        if self.name is not None:
            result['Name'] = self.name

        if self.offline_duration is not None:
            result['OfflineDuration'] = self.offline_duration

        if self.offline_unchanged_duration is not None:
            result['OfflineUnchangedDuration'] = self.offline_unchanged_duration

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.retrieve_time is not None:
            result['RetrieveTime'] = self.retrieve_time

        if self.size is not None:
            result['Size'] = self.size

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Atime') is not None:
            self.atime = m.get('Atime')

        if m.get('Ctime') is not None:
            self.ctime = m.get('Ctime')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('HasArchiveFile') is not None:
            self.has_archive_file = m.get('HasArchiveFile')

        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')

        if m.get('Inode') is not None:
            self.inode = m.get('Inode')

        if m.get('Mtime') is not None:
            self.mtime = m.get('Mtime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfflineDuration') is not None:
            self.offline_duration = m.get('OfflineDuration')

        if m.get('OfflineUnchangedDuration') is not None:
            self.offline_unchanged_duration = m.get('OfflineUnchangedDuration')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

