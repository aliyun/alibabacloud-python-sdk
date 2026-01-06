# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListRecycledDirectoriesAndFilesResponseBody(DaraModel):
    def __init__(
        self,
        entries: List[main_models.ListRecycledDirectoriesAndFilesResponseBodyEntries] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about files or directories in the recycle bin.
        self.entries = entries
        # A pagination token.
        # 
        # If all the files and directories are incompletely returned in a query, the return value of the NextToken parameter is not empty. In this case, you can specify a valid value for the NextToken parameter to continue the query.
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
                temp_model = main_models.ListRecycledDirectoriesAndFilesResponseBodyEntries()
                self.entries.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRecycledDirectoriesAndFilesResponseBodyEntries(DaraModel):
    def __init__(
        self,
        atime: str = None,
        ctime: str = None,
        delete_time: str = None,
        file_id: str = None,
        inode: str = None,
        mtime: str = None,
        name: str = None,
        size: int = None,
        type: str = None,
    ):
        # The time when the file or directory was last accessed.
        self.atime = atime
        # The time when the metadata was last modified.
        self.ctime = ctime
        # The time when the file or directory was deleted.
        self.delete_time = delete_time
        # The IDs of the files or directories.
        self.file_id = file_id
        # The inode of the file or directory.
        self.inode = inode
        # The time when the file or directory was last modified.
        self.mtime = mtime
        # The name of the file or directory before it was deleted.
        self.name = name
        # The size of the file. Unit: bytes.
        # 
        # The value 0 is returned for this parameter if Directory is returned for the Type parameter.
        self.size = size
        # The type of the returned object. Valid values:
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

        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.inode is not None:
            result['Inode'] = self.inode

        if self.mtime is not None:
            result['MTime'] = self.mtime

        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ATime') is not None:
            self.atime = m.get('ATime')

        if m.get('CTime') is not None:
            self.ctime = m.get('CTime')

        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Inode') is not None:
            self.inode = m.get('Inode')

        if m.get('MTime') is not None:
            self.mtime = m.get('MTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

