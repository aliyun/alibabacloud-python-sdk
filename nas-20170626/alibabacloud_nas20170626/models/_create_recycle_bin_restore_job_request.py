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
        # Generate a value from your client to ensure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # >If you do not specify ClientToken, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The FileId of the file or directory to restore.
        # 
        # You can call the [ListRecycledDirectoriesAndFiles](https://help.aliyun.com/document_detail/2412174.html) operation to query the FileId of deleted data.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The file system ID. **Required**.
        # 
        # **How to obtain**:
        # - Call [DescribeFileSystems](https://www.alibabacloud.com/help/en/nas/developer-reference/api-nas-2017-06-26-describefilesystems) to query the file system list and obtain the FileSystemId.
        # - Call [CreateFileSystem](https://www.alibabacloud.com/help/en/nas/developer-reference/api-nas-2017-06-26-createfilesystem) to create a file system and obtain the FileSystemId from the response.
        # 
        # **Usage notes**:
        # - This operation applies only to General-purpose NAS file systems.
        # - Before calling this operation, make sure that the recycle bin feature is enabled for the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The FileId of the directory to which the file is restored.
        # 
        # - You can call the [ListRecentlyRecycledDirectories](https://help.aliyun.com/document_detail/2412173.html) operation to query the TargetFileId of directories from which files have been deleted.
        # 
        # - You can call the [ListDirectoriesAndFiles](https://help.aliyun.com/document_detail/2412163.html) operation to query the TargetFileId of existing directories in the file system.
        # 
        # **Special notes**:
        # - The FileId of the root directory of a file system is fixed to `2`. You can directly use this value as the TargetFileId to restore a file to the root directory without querying.
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

