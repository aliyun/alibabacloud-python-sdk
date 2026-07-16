# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecycleBinDeleteJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        file_id: str = None,
        file_system_id: str = None,
    ):
        # Ensures the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure that the value is unique among different requests. The value of ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # >If you do not specify ClientToken, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The FileId of the file or directory that you want to permanently delete.
        # 
        # You can call the [ListRecycledDirectoriesAndFiles](https://help.aliyun.com/document_detail/2412174.html) operation to query the FileId of deleted data.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

