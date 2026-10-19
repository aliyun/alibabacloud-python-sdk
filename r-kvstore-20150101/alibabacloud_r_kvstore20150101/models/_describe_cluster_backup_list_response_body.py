# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterBackupListResponseBody(DaraModel):
    def __init__(
        self,
        cluster_backups: List[main_models.DescribeClusterBackupListResponseBodyClusterBackups] = None,
        free_size: int = None,
        full_storage_size: int = None,
        log_storage_size: int = None,
        max_results: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The list of cluster backup sets. A cluster backup set contains the backup sets of all nodes in the cluster.
        self.cluster_backups = cluster_backups
        # <props="china">The free backup quota of the instance. Unit: bytes. The free quota is equal to the default memory capacity of the instance type. For more information, see the notice on backup commercialization. Full backups and log backups share this free quota. When you change the instance type, the free quota of the instance changes accordingly.
        # <props="intl">This parameter is not in effect. Ignore this parameter.
        self.free_size = free_size
        # The size of full backup files for the current instance. Unit: bytes. Full backups are generated from daily scheduled backups, manual backups, and backups generated during cache analysis.
        # > This value is independent of the number and size of backup sets returned in the current request. It represents the total size of all valid full backups for the instance.
        self.full_storage_size = full_storage_size
        # The size of the instance log backup files for the current instance. Unit: bytes. This value is valid only when the flashback feature is enabled.
        # > This value is independent of the number and size of backup sets in the current response. It represents the total size of all valid instance log backups for the current instance.
        self.log_storage_size = log_storage_size
        # The maximum number of records returned by the current request.
        self.max_results = max_results
        # The page number, which is the same as the request parameter.
        self.page_number = page_number
        # The maximum number of records per page, which is the same as the request parameter.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_backups:
            for v1 in self.cluster_backups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterBackups'] = []
        if self.cluster_backups is not None:
            for k1 in self.cluster_backups:
                result['ClusterBackups'].append(k1.to_map() if k1 else None)

        if self.free_size is not None:
            result['FreeSize'] = self.free_size

        if self.full_storage_size is not None:
            result['FullStorageSize'] = self.full_storage_size

        if self.log_storage_size is not None:
            result['LogStorageSize'] = self.log_storage_size

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_backups = []
        if m.get('ClusterBackups') is not None:
            for k1 in m.get('ClusterBackups'):
                temp_model = main_models.DescribeClusterBackupListResponseBodyClusterBackups()
                self.cluster_backups.append(temp_model.from_map(k1))

        if m.get('FreeSize') is not None:
            self.free_size = m.get('FreeSize')

        if m.get('FullStorageSize') is not None:
            self.full_storage_size = m.get('FullStorageSize')

        if m.get('LogStorageSize') is not None:
            self.log_storage_size = m.get('LogStorageSize')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterBackupListResponseBodyClusterBackups(DaraModel):
    def __init__(
        self,
        backups: List[main_models.DescribeClusterBackupListResponseBodyClusterBackupsBackups] = None,
        cluster_backup_end_time: str = None,
        cluster_backup_id: str = None,
        cluster_backup_mode: str = None,
        cluster_backup_size: str = None,
        cluster_backup_start_time: str = None,
        cluster_backup_status: str = None,
        expect_expire_time: str = None,
        is_avail: int = None,
        progress: str = None,
        shard_class_memory: int = None,
    ):
        # The collection of backup sets for all child nodes under a single cluster backup set.
        self.backups = backups
        # The end time of the cluster backup. The time is in the YYYY-MM-DDTHH:mm:ssZ format and displayed in UTC.
        self.cluster_backup_end_time = cluster_backup_end_time
        # The cluster backup set ID.
        self.cluster_backup_id = cluster_backup_id
        # The cluster backup mode.
        self.cluster_backup_mode = cluster_backup_mode
        # The size of the cluster backup set.
        self.cluster_backup_size = cluster_backup_size
        # The start time of the cluster backup. The time is in the YYYY-MM-DDTHH:mm:ssZ format and displayed in UTC.
        self.cluster_backup_start_time = cluster_backup_start_time
        # The status of the cluster backup set. Valid values:
        # - OK: The backup is successful.
        # - RUNNING: The backup is in progress.
        # - Other values: The backup failed.
        self.cluster_backup_status = cluster_backup_status
        # The expiration time of the backup set. The time is in the yyyy-MM-ddTHH:mmZ format and displayed in UTC.
        self.expect_expire_time = expect_expire_time
        # Indicates whether the cluster backup set is valid. The value is 0 if the backup sets of child nodes are incomplete or failed.
        self.is_avail = is_avail
        # The backup progress. This parameter is returned only for backups that are in progress.
        self.progress = progress
        # The memory size of a single DB node when the full backup is created. Unit: MB.
        self.shard_class_memory = shard_class_memory

    def validate(self):
        if self.backups:
            for v1 in self.backups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backups'] = []
        if self.backups is not None:
            for k1 in self.backups:
                result['Backups'].append(k1.to_map() if k1 else None)

        if self.cluster_backup_end_time is not None:
            result['ClusterBackupEndTime'] = self.cluster_backup_end_time

        if self.cluster_backup_id is not None:
            result['ClusterBackupId'] = self.cluster_backup_id

        if self.cluster_backup_mode is not None:
            result['ClusterBackupMode'] = self.cluster_backup_mode

        if self.cluster_backup_size is not None:
            result['ClusterBackupSize'] = self.cluster_backup_size

        if self.cluster_backup_start_time is not None:
            result['ClusterBackupStartTime'] = self.cluster_backup_start_time

        if self.cluster_backup_status is not None:
            result['ClusterBackupStatus'] = self.cluster_backup_status

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.shard_class_memory is not None:
            result['ShardClassMemory'] = self.shard_class_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backups = []
        if m.get('Backups') is not None:
            for k1 in m.get('Backups'):
                temp_model = main_models.DescribeClusterBackupListResponseBodyClusterBackupsBackups()
                self.backups.append(temp_model.from_map(k1))

        if m.get('ClusterBackupEndTime') is not None:
            self.cluster_backup_end_time = m.get('ClusterBackupEndTime')

        if m.get('ClusterBackupId') is not None:
            self.cluster_backup_id = m.get('ClusterBackupId')

        if m.get('ClusterBackupMode') is not None:
            self.cluster_backup_mode = m.get('ClusterBackupMode')

        if m.get('ClusterBackupSize') is not None:
            self.cluster_backup_size = m.get('ClusterBackupSize')

        if m.get('ClusterBackupStartTime') is not None:
            self.cluster_backup_start_time = m.get('ClusterBackupStartTime')

        if m.get('ClusterBackupStatus') is not None:
            self.cluster_backup_status = m.get('ClusterBackupStatus')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ShardClassMemory') is not None:
            self.shard_class_memory = m.get('ShardClassMemory')

        return self

class DescribeClusterBackupListResponseBodyClusterBackupsBackups(DaraModel):
    def __init__(
        self,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_intranet_download_url: str = None,
        backup_name: str = None,
        backup_size: str = None,
        backup_start_time: str = None,
        backup_status: str = None,
        engine: str = None,
        extra_info: main_models.DescribeClusterBackupListResponseBodyClusterBackupsBackupsExtraInfo = None,
        instance_name: str = None,
        is_avail: str = None,
        recover_config_mode: str = None,
    ):
        # The public download URL of the backup file.
        self.backup_download_url = backup_download_url
        # The end time of the backup. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format and displayed in UTC.
        self.backup_end_time = backup_end_time
        # The ID of the backup file.
        self.backup_id = backup_id
        # The internal download URL of the backup file.
        # > You can use this URL to download the backup file from an ECS instance that is connected to the current instance. Both instances must reside in the same VPC.
        self.backup_intranet_download_url = backup_intranet_download_url
        # The backup name.
        self.backup_name = backup_name
        # The size of the backup file. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format and displayed in UTC.
        self.backup_start_time = backup_start_time
        # The backup status. Valid values:
        # * **OK**: The backup is successful.
        # * **ERROR**: The backup failed.
        self.backup_status = backup_status
        # The database engine type. The value is fixed as **redis**.
        self.engine = engine
        # The additional information.
        self.extra_info = extra_info
        # The name of the instance.
        self.instance_name = instance_name
        # Indicates whether the backup set is available. Valid values:
        # * **0**: unavailable.
        # * **1**: available.
        self.is_avail = is_avail
        # This parameter is not in effect. Ignore this parameter.
        self.recover_config_mode = recover_config_mode

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url

        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url

        if self.backup_name is not None:
            result['BackupName'] = self.backup_name

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        if self.recover_config_mode is not None:
            result['RecoverConfigMode'] = self.recover_config_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')

        if m.get('BackupName') is not None:
            self.backup_name = m.get('BackupName')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExtraInfo') is not None:
            temp_model = main_models.DescribeClusterBackupListResponseBodyClusterBackupsBackupsExtraInfo()
            self.extra_info = temp_model.from_map(m.get('ExtraInfo'))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        if m.get('RecoverConfigMode') is not None:
            self.recover_config_mode = m.get('RecoverConfigMode')

        return self

class DescribeClusterBackupListResponseBodyClusterBackupsBackupsExtraInfo(DaraModel):
    def __init__(
        self,
        custins_db_version: str = None,
    ):
        # The database engine version.
        self.custins_db_version = custins_db_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custins_db_version is not None:
            result['CustinsDbVersion'] = self.custins_db_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustinsDbVersion') is not None:
            self.custins_db_version = m.get('CustinsDbVersion')

        return self

