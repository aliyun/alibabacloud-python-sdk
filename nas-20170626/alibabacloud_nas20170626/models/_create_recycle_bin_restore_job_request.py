# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecycleBinRestoreJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        file_id: str = None,
        file_system_id: str = None,
        target_file_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the file or directory that you want to restore.
        # 
        # You can call the [ListRecycledDirectoriesAndFiles](https://help.aliyun.com/document_detail/2412174.html) operation to query the FileId of the deleted data.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the directory to which the file is restored.
        # 
        # *   You can call the [ListRecentlyRecycledDirectories](https://help.aliyun.com/document_detail/2412173.html) operation to query the TargetFileId for recently deleted directories.
        # *   You can call the [ListDirectoriesAndFiles](https://help.aliyun.com/document_detail/2412163.html) operation to query the TargetFileId for existing directories.
        # 
        # This parameter is required.
        self.target_file_id = target_file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.target_file_id is not None:
            result['TargetFileId'] = self.target_file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('TargetFileId') is not None:
            self.target_file_id = m.get('TargetFileId')

        return self

