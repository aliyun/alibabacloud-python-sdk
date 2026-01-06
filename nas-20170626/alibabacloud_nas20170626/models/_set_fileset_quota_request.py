# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetFilesetQuotaRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        file_count_limit: int = None,
        file_system_id: str = None,
        fset_id: str = None,
        size_limit: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. The dry run checks parameter validity and prerequisites. The dry run does not delete the specified quota or incur fees.
        # 
        # Valid values:
        # 
        # *   true: performs only a dry run. The system checks the required parameters, request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the HTTP status code 200 is returned.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, the quota is deleted.
        self.dry_run = dry_run
        # The number of files of the quota. Valid values:
        # 
        # *   Minimum value: 10,000.
        # *   Maximum value: 10,000,000,000.
        # 
        # >  If you do not specify this parameter, the number of files is unlimited.
        self.file_count_limit = file_count_limit
        # The ID of the CPFS for LINGJUN file system. The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The fileset ID.
        # 
        # This parameter is required.
        self.fset_id = fset_id
        # The total capacity of the quota. Unit: bytes.
        # 
        # Valid values:
        # 
        # *   Minimum value: 10,737,418,240 (10 GiB).
        # *   Step size: 1,073,741,824 (1 GiB).
        # 
        # >  If you do not specify this parameter, the capacity is unlimited.
        self.size_limit = size_limit

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

        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

