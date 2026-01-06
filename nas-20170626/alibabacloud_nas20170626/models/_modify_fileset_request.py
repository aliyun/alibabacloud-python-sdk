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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable deletion protection to allow you to release the fileset by using the console or by calling the [DeleteFileset](https://help.aliyun.com/document_detail/2402263.html) operation. Valid values:
        # 
        # *   true: enables release protection.
        # *   false: disables release protection.
        # 
        # > This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The fileset description.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is modified and no fees incurred.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, service limits, and Apsara File Storage NAS (NAS) inventory data. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the specified fileset is modified.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
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

