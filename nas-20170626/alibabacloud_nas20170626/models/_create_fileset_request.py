# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateFilesetRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection: bool = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        file_system_path: str = None,
        quota: main_models.CreateFilesetRequestQuota = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to enable deletion protection to allow you to release the fileset by using the console or by calling the [DeleteFileset](https://help.aliyun.com/document_detail/2402263.html) operation.
        # 
        # *   true: enables release protection.
        # *   false (default): disables release protection.
        # 
        # >  This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The description of the fileset.
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The name must start with a letter and cannot start with http:// or https://.
        # *   The description can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no fileset is created and no fee is incurred.
        # 
        # Valid value:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, service limits, and available Apsara File Storage NAS (NAS) resources. Otherwise, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FsetId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a fileset is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for Lingjun file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the fileset.
        # 
        # *   CPFS path limits.
        # 
        #     *   The parent directory of the path that you specify must be an existing directory in the file system.
        #     *   The path must be 2 to 1024 characters in length.
        #     *   The path must start and end with a forward slash (/).
        # 
        # *   Path limit of CPFS for Lingjun
        # 
        #     *   The path must be 2 to 1024 characters in length.
        #     *   The path must start and end with a forward slash (/).
        #     *   The fileset path must be a new path and cannot be an existing path. Fileset paths cannot be renamed and cannot be symbolic links.
        #     *   The maximum depth supported by a fileset path is eight levels. The depth of the root directory / is 0 levels. For example, the fileset path /test/aaa/ccc/ has three levels.
        #     *   If the fileset path is a multi-level path, the parent directory must be an existing directory.
        #     *   Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset. A fileset path supports only one quota.
        #     *   The path cannot exceed 990 characters in length.
        # 
        # This parameter is required.
        self.file_system_path = file_system_path
        # The quota information.
        # 
        # >  Only CPFS for Lingjun V2.7.0 and later support this parameter.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

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

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

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

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('Quota') is not None:
            temp_model = main_models.CreateFilesetRequestQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        return self

class CreateFilesetRequestQuota(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        # The file quantity quota. Valid values:
        # 
        # *   Minimum value: 100000.
        # *   Maximum value: 10000000000.
        self.file_count_limit = file_count_limit
        # The total quota capacity limit. Unit: bytes.
        # 
        # Valid values:
        # 
        # *   Minimum value: 10,737,418,240 (10 GiB).
        # *   Step size: 1073741824 (1 GiB).
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

