# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFilesetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run for this deletion request.
        # 
        # A dry run checks parameter validity and resource availability without actually deleting the instance.
        # 
        # Valid values:
        # 
        # - true: Sends a check request without deleting the instance. The check items include whether required parameters are specified, the request format, and business limitations. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # 
        # - false (default): Sends a normal request. After the check passes, the instance is directly deleted.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-099394bd928c****.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya****.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The fileset ID.
        # 
        # This parameter is required.
        self.fset_id = fset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        return self

