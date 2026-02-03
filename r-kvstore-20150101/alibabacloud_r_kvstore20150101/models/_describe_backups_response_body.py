# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeBackupsResponseBodyAccessDeniedDetail = None,
        backups: main_models.DescribeBackupsResponseBodyBackups = None,
        free_size: int = None,
        full_storage_size: int = None,
        log_storage_size: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The following parameters are no longer used. Ignore the parameters.
        self.access_denied_detail = access_denied_detail
        # The queried backup sets.
        self.backups = backups
        # This parameter does not take effect. Ignore this parameter.
        self.free_size = free_size
        # The size of the full backup file of the instance. Unit: bytes. Full backups originate from scheduled backups, manual backups, and backups generated during cache analysis.
        # 
        # >  The value of this parameter is independent of the number and size of the returned backup sets. Instead, it reflects the total size of all valid full backups of the instance.
        self.full_storage_size = full_storage_size
        # The size of the log backup file of the instance. Unit: bytes. This value is valid only when flashback is enabled.
        # 
        # >  The value of this parameter is independent of the number and size of the returned backup sets. Instead, it reflects the total size of all valid log backups of the instance.
        self.log_storage_size = log_storage_size
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of backup files that were returned.
        self.total_count = total_count

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.backups:
            self.backups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.backups is not None:
            result['Backups'] = self.backups.to_map()

        if self.free_size is not None:
            result['FreeSize'] = self.free_size

        if self.full_storage_size is not None:
            result['FullStorageSize'] = self.full_storage_size

        if self.log_storage_size is not None:
            result['LogStorageSize'] = self.log_storage_size

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Backups') is not None:
            temp_model = main_models.DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m.get('Backups'))

        if m.get('FreeSize') is not None:
            self.free_size = m.get('FreeSize')

        if m.get('FullStorageSize') is not None:
            self.full_storage_size = m.get('FullStorageSize')

        if m.get('LogStorageSize') is not None:
            self.log_storage_size = m.get('LogStorageSize')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupsResponseBodyBackups(DaraModel):
    def __init__(
        self,
        backup: List[main_models.DescribeBackupsResponseBodyBackupsBackup] = None,
    ):
        self.backup = backup

    def validate(self):
        if self.backup:
            for v1 in self.backup:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backup'] = []
        if self.backup is not None:
            for k1 in self.backup:
                result['Backup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k1 in m.get('Backup'):
                temp_model = main_models.DescribeBackupsResponseBodyBackupsBackup()
                self.backup.append(temp_model.from_map(k1))

        return self

class DescribeBackupsResponseBodyBackupsBackup(DaraModel):
    def __init__(
        self,
        backup_dbnames: str = None,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_id: int = None,
        backup_intranet_download_url: str = None,
        backup_job_id: int = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        engine_version: str = None,
        expect_expire_time: str = None,
        node_instance_id: str = None,
        recover_config_mode: str = None,
    ):
        # The names of the databases that are backed up. The default value is **all**, which indicates that all databases are backed up.
        self.backup_dbnames = backup_dbnames
        # The public download URL of the backup file.
        self.backup_download_url = backup_download_url
        # The end time of the backup.
        self.backup_end_time = backup_end_time
        # The ID of the backup file.
        self.backup_id = backup_id
        # The internal download URL of the backup file.
        # 
        # >  You can use this URL to download the backup file from an Elastic Compute Service (ECS) instance that is connected to the Tair instance. The ECS instance must belong to the same classic network or reside in the same virtual private cloud (VPC) as the Tair instance.
        self.backup_intranet_download_url = backup_intranet_download_url
        # The ID of the backup task.
        self.backup_job_id = backup_job_id
        # The backup method. Valid values:
        # 
        # *   **Logical**
        # *   **Physical**
        self.backup_method = backup_method
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The size of the backup file.
        self.backup_size = backup_size
        # The start time of the backup.
        self.backup_start_time = backup_start_time
        # The status of the backup. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        self.backup_status = backup_status
        # The backup type. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementalBackup**
        self.backup_type = backup_type
        # The engine version (major version) of the instance.
        self.engine_version = engine_version
        self.expect_expire_time = expect_expire_time
        # The node ID.
        # 
        # >  If the instance uses the standard architecture, this parameter returns the instance ID.
        self.node_instance_id = node_instance_id
        # If the backup includes account information, kernel parameters and whitelist details.
        self.recover_config_mode = recover_config_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames

        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url

        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url

        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id

        if self.recover_config_mode is not None:
            result['RecoverConfigMode'] = self.recover_config_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')

        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')

        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')

        if m.get('RecoverConfigMode') is not None:
            self.recover_config_mode = m.get('RecoverConfigMode')

        return self

class DescribeBackupsResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # This parameter is no longer used. Ignore this parameter.
        self.auth_action = auth_action
        # This parameter is no longer used. Ignore this parameter.
        self.auth_principal_display_name = auth_principal_display_name
        # This parameter is no longer used. Ignore this parameter.
        self.auth_principal_owner_id = auth_principal_owner_id
        # This parameter is no longer used. Ignore this parameter.
        self.auth_principal_type = auth_principal_type
        # This parameter is no longer used. Ignore this parameter.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # This parameter is no longer used. Ignore this parameter.
        self.no_permission_type = no_permission_type
        # This parameter is no longer used. Ignore this parameter.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

