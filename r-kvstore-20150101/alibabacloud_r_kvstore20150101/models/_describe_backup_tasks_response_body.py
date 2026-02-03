# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupTasksResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeBackupTasksResponseBodyAccessDeniedDetail = None,
        backup_jobs: List[main_models.DescribeBackupTasksResponseBodyBackupJobs] = None,
        instance_id: str = None,
        request_id: str = None,
    ):
        # The following parameters are no longer used. Ignore the parameters.
        self.access_denied_detail = access_denied_detail
        # The details of the backup tasks.
        self.backup_jobs = backup_jobs
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.backup_jobs:
            for v1 in self.backup_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        result['BackupJobs'] = []
        if self.backup_jobs is not None:
            for k1 in self.backup_jobs:
                result['BackupJobs'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeBackupTasksResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        self.backup_jobs = []
        if m.get('BackupJobs') is not None:
            for k1 in m.get('BackupJobs'):
                temp_model = main_models.DescribeBackupTasksResponseBodyBackupJobs()
                self.backup_jobs.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupTasksResponseBodyBackupJobs(DaraModel):
    def __init__(
        self,
        backup_job_id: int = None,
        backup_progress_status: str = None,
        job_mode: str = None,
        node_id: str = None,
        process: str = None,
        progress: str = None,
        start_time: str = None,
        task_action: str = None,
    ):
        # The ID of the backup task.
        self.backup_job_id = backup_job_id
        # The state of the backup task. Valid values:
        # 
        # *   **NoStart**: The backup task is not started.
        # *   **Preparing**: The backup task is being prepared.
        # *   **Waiting**: The backup task is pending.
        # *   **Uploading**: The system is uploading the backup file.
        # *   **Checking**: The system is checking the uploaded backup file.
        # *   **Finished**: The backup task is completed.
        self.backup_progress_status = backup_progress_status
        # The backup mode. Valid values:
        # 
        # *   **Automated**: automatic backup
        # *   **Manual**: manual backup
        self.job_mode = job_mode
        # The ID of the data node.
        self.node_id = node_id
        # The progress of the backup task in percentage.
        self.process = process
        # The backup progress.
        self.progress = progress
        # The start time of the backup task. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The type of the backup task. Valid values:
        # 
        # *   **TempBackupTask**: The backup task was manually performed.
        # *   **NormalBackupTask**: The backup task was automatically performed.
        self.task_action = task_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_job_id is not None:
            result['BackupJobID'] = self.backup_job_id

        if self.backup_progress_status is not None:
            result['BackupProgressStatus'] = self.backup_progress_status

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.process is not None:
            result['Process'] = self.process

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_action is not None:
            result['TaskAction'] = self.task_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupJobID') is not None:
            self.backup_job_id = m.get('BackupJobID')

        if m.get('BackupProgressStatus') is not None:
            self.backup_progress_status = m.get('BackupProgressStatus')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')

        return self

class DescribeBackupTasksResponseBodyAccessDeniedDetail(DaraModel):
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

