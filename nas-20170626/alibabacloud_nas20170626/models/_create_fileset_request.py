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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId may be different for each API request.
        self.client_token = client_token
        # The release protection property of the instance. Specifies whether the instance can be released by using the console or the [DeleteFileset](https://help.aliyun.com/document_detail/2402263.html) operation.
        # 
        # - true: Enables release protection for the instance.
        # - false (default): Disables release protection for the instance.
        # 
        # > This property only restricts manual release operations and does not take effect on system-initiated release operations.
        self.deletion_protection = deletion_protection
        # The description of the fileset.
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter or Chinese character and cannot start with http:// or https://.
        # - The description can contain digits, colons (:), underscores (_), or hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run for this request.
        # 
        # A dry run checks parameter validity and resource availability without actually creating the instance or incurring charges.
        # 
        # Valid values:
        # 
        # - true: Sends a dry run request without creating the instance. The check items include required parameters, request format, business restrictions, and NAS inventory. If the check fails, the corresponding error is returned. If the check succeeds, HTTP status code 200 is returned, but FsetId is empty.
        # - false (default): Sends a normal request. After the check succeeds, the instance is created.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - CPFS: The ID must start with `cpfs-`, such as cpfs-099394bd928c\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the fileset to create.
        # 
        # - Path restrictions for CPFS:
        #   - The parent directory of the specified directory must be an existing directory in the file system.
        #   - The path must be 2 to 1,024 characters in length.
        #   - The specified directory must start and end with a forward slash (/).
        # - Path restrictions for CPFS for Lingjun:
        #   - The path must be 2 to 1,024 characters in length.
        #   - The specified directory must start and end with a forward slash (/).
        #   - The fileset path must be a new path and cannot be an existing path. Renaming a fileset path is not supported, and the path cannot be a symbolic link.
        #   - The maximum depth of a fileset path is 8 levels, with the root directory / as level 0. For example, a fileset path of /test/aaa/ccc/ has a depth of 3 levels.
        #   - If the fileset path contains multiple directory levels, the parent directory must be an existing directory.
        #   - Nesting filesets within a fileset is not supported. If a parent directory is already specified as a fileset, its subdirectories cannot be specified as filesets. Only one quota is supported for each fileset path.
        #   - The total path length cannot exceed 990 characters.
        # 
        # This parameter is required.
        self.file_system_path = file_system_path
        # The quota information.
        # > This parameter is supported only for CPFS for Lingjun 2.7.0 and later.
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
        # The file count limit of the quota. Valid values:
        # 
        # - Minimum value: 10,000.
        # 
        # - Maximum value: 10,000,000,000.
        self.file_count_limit = file_count_limit
        # The total capacity limit of the quota. Unit: bytes.
        # 
        # Valid values:
        # 
        # - Minimum value: 10,737,418,240 (10 GiB).
        # 
        # - Increment: 1,073,741,824 (1 GiB).
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

