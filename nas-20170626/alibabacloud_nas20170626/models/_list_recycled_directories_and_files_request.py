# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecycledDirectoriesAndFilesRequest(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_system_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The FileId of the directory to query.
        # 
        # If the recycle bin is empty, you can call this operation with FileId=2 (root directory inode) to verify the reachability of the operation or query the recycle bin content under the root directory. You can obtain other valid FileId values by calling the [ListRecentlyRecycledDirectories](https://help.aliyun.com/document_detail/2412173.html) operation.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The number of files or directories returned per query.
        # 
        # Valid values: 10 to 1000.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The pagination token for the next page. You do not need to specify this parameter for the first query.
        # 
        # If a single query does not return all files and directories, a non-empty NextToken is returned. You can specify the correct NextToken in subsequent queries to continue listing.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

