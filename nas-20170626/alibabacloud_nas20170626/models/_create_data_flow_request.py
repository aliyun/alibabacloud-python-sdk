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
        # The automatic update interval. CPFS checks whether data is updated in the directory at the interval specified by this parameter. If data is updated, CPFS starts an automatic update task. Unit: minutes.
        # 
        # Valid values: 10 to 525600. Default value: 10.
        # 
        # >  This parameter takes effect only for CPFS file systems.
        self.auto_refresh_interval = auto_refresh_interval
        # The automatic update policy. The updated data in the source storage is imported into the CPFS file system based on the policy.
        # 
        # *   None (default): Updated data in the source storage is not automatically imported into the CPFS file system. You can run a data flow task to import the updated data from the source storage.
        # *   ImportChanged: Updated data in the source storage is automatically imported into the CPFS file system.
        # 
        # >  This parameter takes effect only for CPFS file systems.
        self.auto_refresh_policy = auto_refresh_policy
        # The automatic update configurations.
        # 
        # >  This parameter takes effect only for CPFS file systems.
        self.auto_refreshs = auto_refreshs
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure the idempotence?](https://help.aliyun.com/document_detail/25693.html)
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The value of RequestId may be different for each API request.
        self.client_token = client_token
        # The description of the dataflow.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   The description must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # Specifies whether to perform a dry run.
        # 
        # During the dry run, the system checks whether the request parameters are valid and whether the requested resources are available. During the dry run, no file system is created and no fee is incurred.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run. The system checks the required parameters, request syntax, limits, and available NAS resources. If the request fails the dry run, an error message is returned. If the request passes the dry run, the HTTP status code 200 is returned. No value is returned for the FileSystemId parameter.
        # *   false (default): performs a dry run and sends the request. If the request passes the dry run, a file system is created.
        self.dry_run = dry_run
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for Lingjun file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The directory in the CPFS for LINGJUN file system. Limits:
        # 
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be an existing directory in the CPFS for LINGJUN file system.
        # *   The directory must be 1 to 1023 characters in length.
        # *   The directory must be encoded in UTF-8.
        # 
        # >  This parameter is required for CPFS for LINGJUN file systems.
        self.file_system_path = file_system_path
        # The fileset ID.
        # 
        # >  This parameter is required for CPFS file systems.
        self.fset_id = fset_id
        # The type of security mechanism for the source storage. This parameter must be specified if the source storage is accessed with a security mechanism. Valid values:
        # 
        # *   None (default): The source storage can be accessed without a security mechanism.
        # *   SSL: The source storage must be accessed with an SSL certificate.
        self.source_security_type = source_security_type
        # The access path of the source storage. Format: `<storage type>://[<account id>:]<path>`.
        # 
        # Parameters:
        # 
        # *   storage type: Only OSS is supported.
        # 
        # *   account id (optional): the UID of the account of the source storage. This parameter is required when you use OSS buckets across accounts.
        # 
        # *   path: the name of the OSS bucket. Limits:
        # 
        #     *   The name can contain only lowercase letters, digits, and hyphens (-). The name must start and end with a lowercase letter or digit.
        #     *   The name can be up to 128 characters in length.
        #     *   The name must be encoded in UTF-8.
        # 
        # > *   The OSS bucket must be an existing bucket in the region.
        # > *   Only CPFS for LINGJUN V2.6.0 and later support the account id parameter.
        # 
        # This parameter is required.
        self.source_storage = source_storage
        # The access path in the bucket of the source storage. Limits:
        # 
        # *   The path must start and end with a forward slash (/).
        # *   The path is case-sensitive.
        # *   The path must be 1 to 1023 characters in length.
        # *   The path must be encoded in UTF-8.
        # 
        # >  This parameter is required for CPFS for LINGJUN file systems.
        self.source_storage_path = source_storage_path
        # The maximum data flow throughput. Unit: MB/s. Valid values:
        # 
        # *   600
        # *   1200
        # *   1500
        # 
        # >  The data flow throughput must be less than the I/O throughput of the file system. This parameter is required for CPFS file systems.
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
        # The automatic update directory. CPFS registers the data update event in the source storage, and automatically checks whether the source data in the directory is updated and imports the updated data.
        # 
        # This parameter is empty by default. Updated data in the source storage is not automatically imported into the CPFS file system. You must import the updated data by running a manual task.
        # 
        # Limits:
        # 
        # *   The directory must be 2 to 1,024 characters in length.
        # *   The directory must be encoded in UTF-8.
        # *   The directory must start and end with a forward slash (/).
        # *   The directory must be an existing directory in the CPFS file system and must be in a fileset where the data flow is enabled.
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

