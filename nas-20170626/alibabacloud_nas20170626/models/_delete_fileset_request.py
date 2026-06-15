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
        # A client-generated token that you can use to ensure the idempotence of the request. The ClientToken must be unique across requests.
        # 
        # The ClientToken can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the ClientToken. The request ID is unique for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run for the request.
        # 
        # A dry run checks for issues such as parameter validity and resource availability, but does not delete the fileset.
        # 
        # Valid values:
        # 
        # - true: Sends a check request and does not delete the fileset. The system checks for required parameters, request format, and business limits. If the check fails, an error is returned. If the check passes, an HTTP 200 OK status code is returned.
        # 
        # - false (Default): Sends a normal request and deletes the fileset after the check passes.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-099394bd928c\\*\\*\\*\\*.
        # 
        # - CPFS for AI and HPC: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
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

