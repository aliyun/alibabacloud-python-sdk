# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupMachineStatusResponseBody(DaraModel):
    def __init__(
        self,
        backup_machine_status: main_models.DescribeBackupMachineStatusResponseBodyBackupMachineStatus = None,
        request_id: str = None,
    ):
        # The backup status of the server.
        self.backup_machine_status = backup_machine_status
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_machine_status:
            self.backup_machine_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_machine_status is not None:
            result['BackupMachineStatus'] = self.backup_machine_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupMachineStatus') is not None:
            temp_model = main_models.DescribeBackupMachineStatusResponseBodyBackupMachineStatus()
            self.backup_machine_status = temp_model.from_map(m.get('BackupMachineStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupMachineStatusResponseBodyBackupMachineStatus(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_status: str = None,
        client_version: str = None,
        error_code: str = None,
        error_list: List[main_models.DescribeBackupMachineStatusResponseBodyBackupMachineStatusErrorList] = None,
        instance_id: str = None,
        region_id: str = None,
        saved_backup_count: int = None,
        service_status: str = None,
        status: str = None,
        uuid: str = None,
        vault_id: str = None,
    ):
        # The ID of the anti-ransomware agent.
        self.client_id = client_id
        # The status of the anti-ransomware agent. Valid values:
        # 
        # *   **ONLINE**: normal
        # *   **CLIENT_CONNECTION_ERROR**: abnormal
        # *   **UNINSTALLING**: being uninstalled
        # *   **UNINSTALL_FAILED**: failed to be uninstalled
        # *   **UPGRADING**: being upgraded
        # *   **UPGRADE_FAILED**: failed to be upgraded
        self.client_status = client_status
        # The version of the anti-ransomware agent.
        self.client_version = client_version
        # The error code returned.
        self.error_code = error_code
        # An array that consists of the error information reported by the backup server.
        self.error_list = error_list
        # The ID of the server.
        self.instance_id = instance_id
        # The ID of the region in which the server resides.
        self.region_id = region_id
        # The number of backup versions.
        self.saved_backup_count = saved_backup_count
        # The status of the anti-ransomware service. Valid values:
        # *   **SERVICE_EXCEPTION**: Service exception
        # *   **RESTORING**: Restoring
        # *   **BACKING_UP**: Backup in process
        self.service_status = service_status
        # The status of the anti-ransomware agent. Valid values:
        # 
        # *   **NOT_INSTALLED**: not installed
        # *   **CLIENT_CONNECTION_ERROR**: abnormal
        # *   **ACTIVATED**: normal
        self.status = status
        # The UUID of the server.
        self.uuid = uuid
        # The ID of the backup vault in which the backup data is stored.
        self.vault_id = vault_id

    def validate(self):
        if self.error_list:
            for v1 in self.error_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        result['ErrorList'] = []
        if self.error_list is not None:
            for k1 in self.error_list:
                result['ErrorList'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.saved_backup_count is not None:
            result['SavedBackupCount'] = self.saved_backup_count

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        self.error_list = []
        if m.get('ErrorList') is not None:
            for k1 in m.get('ErrorList'):
                temp_model = main_models.DescribeBackupMachineStatusResponseBodyBackupMachineStatusErrorList()
                self.error_list.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SavedBackupCount') is not None:
            self.saved_backup_count = m.get('SavedBackupCount')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class DescribeBackupMachineStatusResponseBodyBackupMachineStatusErrorList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_status: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_status = error_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_status is not None:
            result['ErrorStatus'] = self.error_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorStatus') is not None:
            self.error_status = m.get('ErrorStatus')

        return self

