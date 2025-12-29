# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterBackupsResponseBody(DaraModel):
    def __init__(
        self,
        cluster_backups: List[main_models.DescribeClusterBackupsResponseBodyClusterBackups] = None,
        max_results: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The cluster backup sets. A cluster backup file contains the backup sets of each node.
        self.cluster_backups = cluster_backups
        # The maximum number of entries returned.
        self.max_results = max_results
        # The page number of the page returned.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the request.
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
                temp_model = main_models.DescribeClusterBackupsResponseBodyClusterBackups()
                self.cluster_backups.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClusterBackupsResponseBodyClusterBackups(DaraModel):
    def __init__(
        self,
        attach_log_status: str = None,
        backup_expire_time: str = None,
        backups: List[main_models.DescribeClusterBackupsResponseBodyClusterBackupsBackups] = None,
        cluster_backup_end_time: str = None,
        cluster_backup_id: str = None,
        cluster_backup_mode: str = None,
        cluster_backup_size: str = None,
        cluster_backup_start_time: str = None,
        cluster_backup_status: str = None,
        engine_version: str = None,
        extra_info: main_models.DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo = None,
        is_avail: int = None,
        progress: str = None,
    ):
        # The backup status. Valid values:
        # 
        # *   **init**: The backup is being initialized.
        # *   **No_Need**: Log backup is not performed.
        # *   **Running**: Log backup is being performed.
        # *   **Ready**: Log backup is complete.
        # *   **Failed**: Log backup failed.
        # 
        # >  If the **ClusterBackupStatus** parameter is set to OK, full backup is successful. If you want to perform point-in-time-restoration on an instance for which log backup is enabled or to implement consistency restoration, make sure that log backup is complete.
        self.attach_log_status = attach_log_status
        self.backup_expire_time = backup_expire_time
        # The collection of the backup sets of each child node in a cluster backup set.
        self.backups = backups
        # The end of the time range within which the cluster backup is performed.
        self.cluster_backup_end_time = cluster_backup_end_time
        # The backup set ID.
        self.cluster_backup_id = cluster_backup_id
        # The cluster backup mode.
        self.cluster_backup_mode = cluster_backup_mode
        # The size of the cluster backup set. Unit: bytes.
        self.cluster_backup_size = cluster_backup_size
        # The beginning of the time range within which the cluster backup is performed.
        self.cluster_backup_start_time = cluster_backup_start_time
        # The status of the cluster backup set.
        self.cluster_backup_status = cluster_backup_status
        # Version of the backuped instance.
        # 
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        self.engine_version = engine_version
        # The additional information in the JSON format.
        self.extra_info = extra_info
        # Indicates whether the cluster backup sets take effect. Valid values:
        # 
        # *   **1**: The cluster backup sets take effect.
        # *   **0**: The backup sets of child nodes are incomplete or fail.
        self.is_avail = is_avail
        # The progress of the backup task. Unit: %. The progress is returned only for running backup tasks.
        self.progress = progress

    def validate(self):
        if self.backups:
            for v1 in self.backups:
                 if v1:
                    v1.validate()
        if self.extra_info:
            self.extra_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_log_status is not None:
            result['AttachLogStatus'] = self.attach_log_status

        if self.backup_expire_time is not None:
            result['BackupExpireTime'] = self.backup_expire_time

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

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        if self.progress is not None:
            result['Progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachLogStatus') is not None:
            self.attach_log_status = m.get('AttachLogStatus')

        if m.get('BackupExpireTime') is not None:
            self.backup_expire_time = m.get('BackupExpireTime')

        self.backups = []
        if m.get('Backups') is not None:
            for k1 in m.get('Backups'):
                temp_model = main_models.DescribeClusterBackupsResponseBodyClusterBackupsBackups()
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

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExtraInfo') is not None:
            temp_model = main_models.DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo()
            self.extra_info = temp_model.from_map(m.get('ExtraInfo'))

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        return self

class DescribeClusterBackupsResponseBodyClusterBackupsExtraInfo(DaraModel):
    def __init__(
        self,
        registry_from_history: str = None,
    ):
        # Indicates whether the cluster backups are migrated from the historical backup sets. If the value of this parameter is **1**, the cluster backups are migrated from the historical backup sets.
        self.registry_from_history = registry_from_history

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registry_from_history is not None:
            result['RegistryFromHistory'] = self.registry_from_history

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistryFromHistory') is not None:
            self.registry_from_history = m.get('RegistryFromHistory')

        return self

class DescribeClusterBackupsResponseBodyClusterBackupsBackups(DaraModel):
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
        extra_info: main_models.DescribeClusterBackupsResponseBodyClusterBackupsBackupsExtraInfo = None,
        instance_name: str = None,
        is_avail: str = None,
    ):
        # The URL that is used to download the backup set over the Internet. If the backup set cannot be downloaded, an empty string is returned.
        self.backup_download_url = backup_download_url
        # The end time of the backup. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.backup_end_time = backup_end_time
        # The ID of the backup set.
        self.backup_id = backup_id
        # The URL that is used to download the backup set over an internal network. If the backup set cannot be downloaded, null is returned.
        self.backup_intranet_download_url = backup_intranet_download_url
        # The backup name.
        self.backup_name = backup_name
        # The size of the backup file. Unit: bytes.
        self.backup_size = backup_size
        # The start time of the backup. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.backup_start_time = backup_start_time
        # The status of the backup task. Valid values:
        # 
        # *   **Success**: The backup task is successful.
        # *   **Failed**: The backup task failed.
        self.backup_status = backup_status
        # The information of the node associated with the backup.
        self.extra_info = extra_info
        # The shard name.
        self.instance_name = instance_name
        # Indicates whether the backup set is available. Valid values:
        # 
        # *   **0**: unavailable
        # *   **1**: available
        self.is_avail = is_avail

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

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

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

        if m.get('ExtraInfo') is not None:
            temp_model = main_models.DescribeClusterBackupsResponseBodyClusterBackupsBackupsExtraInfo()
            self.extra_info = temp_model.from_map(m.get('ExtraInfo'))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        return self

class DescribeClusterBackupsResponseBodyClusterBackupsBackupsExtraInfo(DaraModel):
    def __init__(
        self,
        instance_class: str = None,
        node_id: str = None,
        node_type: str = None,
        storage_size: str = None,
    ):
        # The instance type of the node.
        self.instance_class = instance_class
        # The node ID.
        self.node_id = node_id
        # The node type.
        self.node_type = node_type
        # The storage capacity of the node. Unit: MB.
        self.storage_size = storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        return self

