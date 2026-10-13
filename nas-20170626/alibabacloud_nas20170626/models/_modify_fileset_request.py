# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFilesetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection: bool = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        fset_id: str = None,
    ):
        # Ensures the idempotence of the request. Generate a parameter value from your client to ensure that the value is unique across different requests.
        # 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may vary for each API request.
        self.client_token = client_token
        # The release protection property of the instance. Specifies whether the instance can be released by using the console or the [DeleteFileset](https://help.aliyun.com/document_detail/2402263.html) operation.
        # 
        # 
        # 
        # -   true: Enables release protection for the instance.
        # -   false: Disables release protection for the instance.
        # 
        # > This property only restricts manual release operations and does not take effect on system-initiated release operations.
        self.deletion_protection = deletion_protection
        # The description of the fileset.
        self.description = description
        # Specifies whether to perform a dry run for this modification request.
        # 
        # A dry run checks parameter validity and inventory without actually modifying the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without modifying the instance. The check items include whether required parameters are specified, request format, business limits, and NAS inventory. If the check fails, the corresponding error is returned. If the check passes, HTTP status code 200 is returned.
        # - false (default): Sends a normal request. After the check passes, the instance is directly modified.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-099394bd928c****.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya****.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # Fileset ID。
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

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

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

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        return self

