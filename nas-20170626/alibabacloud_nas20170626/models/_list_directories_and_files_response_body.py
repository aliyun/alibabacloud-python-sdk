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
        # The details about the files or directories.
        self.entries = entries
        # A pagination token. It can be used in the next request to retrieve a new page of results.
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
        owner: str = None,
        retrieve_time: str = None,
        size: int = None,
        storage_type: str = None,
        type: str = None,
    ):
        # The time when the file was queried.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.atime = atime
        # The time when the raw data was modified.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.ctime = ctime
        # The ID of the directory or file.
        self.file_id = file_id
        # Indicates whether the directory contains files stored in the Archive storage class.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the Archive storage class.
        # *   false: The directory does not contain files stored in the Archive storage class.
        self.has_archive_file = has_archive_file
        # Indicates whether the directory contains files stored in the IA storage class.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the IA storage class.
        # *   false: The directory does not contain files stored in the IA storage class.
        self.has_infrequent_access_file = has_infrequent_access_file
        # The file or directory inode.
        self.inode = inode
        # The time when the file was modified.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.mtime = mtime
        # The name of the file or directory.
        self.name = name
        # The ID of the portable account. This parameter is returned and valid only if the value of the ProtocolType parameter is SMB and RAM-based access control is enabled.
        self.owner = owner
        # The time when the last data retrieval task was run.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.retrieve_time = retrieve_time
        # The size of the file.
        # 
        # Unit: bytes.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        self.size = size
        # The storage class.
        # 
        # This parameter is returned and valid only if the value of the Type parameter is File.
        # 
        # Valid values:
        # 
        # *   InfrequentAccess: the IA storage class.
        # *   Archive: the Archive storage class.
        self.storage_type = storage_type
        # The type of the query result.
        # 
        # Valid values:
        # 
        # *   File
        # *   Directory
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

