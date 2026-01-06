# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class GetDirectoryOrFilePropertiesResponseBody(DaraModel):
    def __init__(
        self,
        entry: main_models.GetDirectoryOrFilePropertiesResponseBodyEntry = None,
        request_id: str = None,
    ):
        # The details about the file or directory.
        self.entry = entry
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entry:
            self.entry.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry is not None:
            result['Entry'] = self.entry.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            temp_model = main_models.GetDirectoryOrFilePropertiesResponseBodyEntry()
            self.entry = temp_model.from_map(m.get('Entry'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDirectoryOrFilePropertiesResponseBodyEntry(DaraModel):
    def __init__(
        self,
        atime: str = None,
        ctime: str = None,
        has_archive_file: bool = None,
        has_infrequent_access_file: bool = None,
        inode: str = None,
        mtime: str = None,
        name: str = None,
        retrieve_time: str = None,
        size: int = None,
        storage_type: str = None,
        type: str = None,
    ):
        # The time when the file was queried.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.atime = atime
        # The time when the metadata was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.ctime = ctime
        # Indicates whether the directory contains files stored in the Archive storage class.
        # 
        # This parameter is returned only if the Type parameter is set to Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the Archive storage class.
        # *   false: The directory does not contain files stored in the Archive storage class.
        self.has_archive_file = has_archive_file
        # Indicates whether the directory contains files stored in the IA storage medium.
        # 
        # This parameter is returned only if the value of the Type parameter is Directory.
        # 
        # Valid values:
        # 
        # *   true: The directory contains files stored in the IA storage medium.
        # *   false: The directory does not contain files stored in the IA storage medium.
        self.has_infrequent_access_file = has_infrequent_access_file
        # The file or directory inode.
        self.inode = inode
        # The time when the file was modified.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.mtime = mtime
        # The name of the file or directory.
        self.name = name
        # The time when the last data retrieval task was run.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.retrieve_time = retrieve_time
        # The size of the file.
        # 
        # Unit: bytes.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        self.size = size
        # The storage class of the file.
        # 
        # This parameter is returned only if the value of the Type parameter is File.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose NAS file system
        # *   InfrequentAccess: the IA storage class.
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
            result['ATime'] = self.atime

        if self.ctime is not None:
            result['CTime'] = self.ctime

        if self.has_archive_file is not None:
            result['HasArchiveFile'] = self.has_archive_file

        if self.has_infrequent_access_file is not None:
            result['HasInfrequentAccessFile'] = self.has_infrequent_access_file

        if self.inode is not None:
            result['Inode'] = self.inode

        if self.mtime is not None:
            result['MTime'] = self.mtime

        if self.name is not None:
            result['Name'] = self.name

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
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')

        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')

        if m.get('HasArchiveFile') is not None:
            self.has_archive_file = m.get('HasArchiveFile')

        if m.get('HasInfrequentAccessFile') is not None:
            self.has_infrequent_access_file = m.get('HasInfrequentAccessFile')

        if m.get('Inode') is not None:
            self.inode = m.get('Inode')

        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RetrieveTime') is not None:
            self.retrieve_time = m.get('RetrieveTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

