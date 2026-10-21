# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateDataFlowRequest(DaraModel):
    def __init__(
        self,
        auto_refresh_interval: int = None,
        auto_refresh_policy: str = None,
        auto_refreshs: List[main_models.CreateDataFlowRequestAutoRefreshs] = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_id: str = None,
        source_security_type: str = None,
        source_storage: str = None,
        source_storage_path: str = None,
        throughput: int = None,
    ):
        # The auto-refresh interval. General-purpose CPFS checks whether data updates exist in the directory at this interval. If data updates exist, an auto-refresh task is started. Unit: minutes.
        # 
        # Valid values: 10 to 525600. Default value: 10.
        # > This parameter takes effect only when the file system type is General-purpose CPFS.
        self.auto_refresh_interval = auto_refresh_interval
        # The auto-refresh policy. This policy determines how data updates from the source storage are imported to General-purpose CPFS.
        # 
        # - None: Data updates from the source storage are not automatically imported to General-purpose CPFS. You can use a data flow task to import the updates. This is the default value.
        # - ImportChanged: Data updates from the source storage are automatically imported to General-purpose CPFS.
        # > This parameter takes effect only when the file system type is General-purpose CPFS.
        self.auto_refresh_policy = auto_refresh_policy
        # The auto-refresh configurations.
        # > This parameter takes effect only when the file system type is General-purpose CPFS.
        self.auto_refreshs = auto_refreshs
        # The client token that is used to ensure the idempotence of the request. You can generate the token on your client to ensure that the token is unique across different requests.
        # 
        # The client token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        # 
        # > If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # The description of the data flow. 
        # 
        # Limits:
        # 
        # - The description must be 2 to 128 characters in length.
        # - The description must start with a letter and cannot start with `http://` or `https://`.
        # - The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run on the creation request.
        # 
        # A dry run helps you check parameter validity and resource availability without actually creating the instance or incurring fees.
        # 
        # Valid values:
        # 
        # - true: A dry run is performed and no instance is created. The system checks whether required parameters are specified, the request format, business limits, and NAS resource availability. If the request fails the dry run, an error is returned. If the request passes the dry run, the HTTP status code 200 is returned, but the FileSystemId parameter is empty.
        # - false: A regular request is sent. If the request passes the dry run, the instance is created. This is the default value.
        self.dry_run = dry_run
        # The file system ID.
        # 
        # - General-purpose CPFS: The ID must start with `cpfs-`, such as cpfs-125487\\*\\*\\*\\*.
        # 
        # - CPFS for Lingjun: The ID must start with `bmcpfs-`, such as bmcpfs-0015\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directory in the CPFS for Lingjun file system. Limits:
        # 
        # - The directory must start and end with a forward slash (/).
        # 
        # - The directory must already exist in the CPFS for Lingjun file system.
        # 
        # - The directory must be 1 to 1,023 characters in length.
        # 
        # - The directory must be encoded in UTF-8.
        # 
        # > This parameter is required when the file system type is CPFS for Lingjun.
        self.file_system_path = file_system_path
        # The fileset ID.
        # > This parameter is required when the file system type is General-purpose CPFS.
        self.fset_id = fset_id
        # The security protection type of the source storage. If the source storage must be accessed through security protection, specify the security protection type. Valid values:
        # 
        # - None: The source storage does not require security protection for access. This is the default value.
        # - SSL: Access is protected by an SSL certificate.
        self.source_security_type = source_security_type
        # The access address of the source storage. Format: `<storage type>://[<account id>:]<path>`.
        # 
        # Where:
        # 
        # - storage type: Only oss is supported.
        # - account id: Optional. The UID of the account to which the source storage belongs. This parameter is required when you use a cross-account OSS bucket.
        # - path: The name of the OSS bucket. Limits:
        # 
        #     - The name can contain only lowercase letters, digits, and hyphens (-), and must start and end with a lowercase letter or a digit.
        # 
        #     - The name can be up to 128 characters in length.
        # 
        #     - The name must be encoded in UTF-8.
        # 
        # > - The OSS bucket must already exist in the region.
        # > - The account id parameter is supported only in CPFS for Lingjun 2.6.0 and later.
        # 
        # This parameter is required.
        self.source_storage = source_storage
        # The access path in the source storage bucket. Limits:
        # 
        # - The path must start and end with a forward slash (/).
        # 
        # - The path is case-sensitive.
        # 
        # - The path must be 1 to 1,023 characters in length.
        # 
        # - The path must be encoded in UTF-8.
        # 
        # > This parameter is required when the file system type is CPFS for Lingjun.
        self.source_storage_path = source_storage_path
        # The maximum transmission bandwidth of the data flow. Unit: MB/s. Valid values: 
        # 
        # - 600
        # - 1200
        # - 1500
        # 
        # > The transmission bandwidth of the data flow must be less than the I/O bandwidth of the file system.
        # > This parameter is required when the file system type is General-purpose CPFS.
        self.throughput = throughput

    def validate(self):
        if self.auto_refreshs:
            for v1 in self.auto_refreshs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_refresh_interval is not None:
            result['AutoRefreshInterval'] = self.auto_refresh_interval

        if self.auto_refresh_policy is not None:
            result['AutoRefreshPolicy'] = self.auto_refresh_policy

        result['AutoRefreshs'] = []
        if self.auto_refreshs is not None:
            for k1 in self.auto_refreshs:
                result['AutoRefreshs'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        if self.source_security_type is not None:
            result['SourceSecurityType'] = self.source_security_type

        if self.source_storage is not None:
            result['SourceStorage'] = self.source_storage

        if self.source_storage_path is not None:
            result['SourceStoragePath'] = self.source_storage_path

        if self.throughput is not None:
            result['Throughput'] = self.throughput

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRefreshInterval') is not None:
            self.auto_refresh_interval = m.get('AutoRefreshInterval')

        if m.get('AutoRefreshPolicy') is not None:
            self.auto_refresh_policy = m.get('AutoRefreshPolicy')

        self.auto_refreshs = []
        if m.get('AutoRefreshs') is not None:
            for k1 in m.get('AutoRefreshs'):
                temp_model = main_models.CreateDataFlowRequestAutoRefreshs()
                self.auto_refreshs.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        if m.get('SourceSecurityType') is not None:
            self.source_security_type = m.get('SourceSecurityType')

        if m.get('SourceStorage') is not None:
            self.source_storage = m.get('SourceStorage')

        if m.get('SourceStoragePath') is not None:
            self.source_storage_path = m.get('SourceStoragePath')

        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')

        return self

class CreateDataFlowRequestAutoRefreshs(DaraModel):
    def __init__(
        self,
        refresh_path: str = None,
    ):
        # The auto-refresh directory. General-purpose CPFS registers data modification events of the source storage, checks whether the source data in this directory is updated, and automatically imports the updated data.
        # 
        # By default, this parameter is empty. Data updates in the source storage are not automatically imported to General-purpose CPFS. You must create a manual task to import the updates.
        # 
        # Limits:
        # 
        # - The directory must be 2 to 1,024 characters in length.
        # - The directory must be encoded in UTF-8.
        # - The directory must start and end with a forward slash (/).
        # - The directory must already exist in General-purpose CPFS and must be located in the fileset directory of the data flow.
        self.refresh_path = refresh_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refresh_path is not None:
            result['RefreshPath'] = self.refresh_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshPath') is not None:
            self.refresh_path = m.get('RefreshPath')

        return self

