# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CountJobByConditionRequest(DaraModel):
    def __init__(
        self,
        dest_db_type: str = None,
        group_id: str = None,
        job_type: str = None,
        params: str = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        src_db_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The type of the destination database.
        self.dest_db_type = dest_db_type
        # The ID of the DTS task.
        self.group_id = group_id
        # The type of the DTS task. Valid values:
        # 
        # *   **MIGRATION**: data migration task
        # *   **SYNC**: data synchronization task
        # *   **SUBSCRIBE**: change tracking task
        self.job_type = job_type
        # The content of the query condition, which corresponds to the value of the JobType parameter.
        self.params = params
        # One of the query conditions. The ID of the region. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region = region
        # The ID of the region in which the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group ID, global parameter that does not need to be passed in by the current API.
        self.resource_group_id = resource_group_id
        # The type of the source database.
        self.src_db_type = src_db_type
        # The status of the DTS task.
        # 
        # Valid values for a data migration task:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is in precheck.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **PreCheckPass**: The task passed the precheck.
        # *   **NotConfigured**: The task is not configured.
        # *   **Migrating**: The task is in progress.
        # *   **Suspending**: The task is paused.
        # *   **MigrationFailed**: The task failed to migrate data.
        # *   **Finished**: The task is complete.
        # *   **Retrying**: The task is being retried.
        # *   **Upgrade**: The task is being upgraded.
        # *   **Locked**: The task is locked.
        # *   **Downgrade**: The task is being downgraded.
        # 
        # Valid values for a data synchronization task:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is in precheck.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **PreCheckPass**: The task passed the precheck.
        # *   **NotConfigured**: The task is not configured.
        # *   **Initializing**: The task is performing initial synchronization.
        # *   **InitializeFailed**: Initial synchronization failed.
        # *   **Synchronizing**: The task is in progress.
        # *   **Failed**: The task failed to synchronize data.
        # *   **Suspending**: The task is paused.
        # *   **Modifying**: The objects in the task are being modified.
        # *   **Finished**: The task is complete.
        # *   **Retrying**: The task is being retried.
        # *   **Upgrade**: The task is being upgraded.
        # *   **Locked**: The task is locked.
        # *   **Downgrade**: The task is being downgraded.
        # 
        # Valid values for a change tracking task:
        # 
        # *   **NotConfigured**: The task is not configured.
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is in precheck.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **PreCheckPass**: The task passed the precheck.
        # *   **Starting**: The task is being started.
        # *   **Normal**: The task is running as expected.
        # *   **Retrying**: The task is being retried.
        # *   **Abnormal**: The task is not running as expected.
        # *   **Upgrade**: The task is being upgraded.
        # *   **Locked**: The task is locked.
        # *   **Downgrade**: The task is being downgraded.
        self.status = status
        # The content of the query condition. Valid values:
        # 
        # *   **name**: the name of the task
        # *   **rds**: the ID of the destination instance
        # *   **instance**: the ID of the Data Transmission Service (DTS) instance
        # *   **srcRds**: the ID of the source instance
        # 
        # > The value of this parameter corresponds to the value of the **JobType** parameter.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_db_type is not None:
            result['DestDbType'] = self.dest_db_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.params is not None:
            result['Params'] = self.params

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.src_db_type is not None:
            result['SrcDbType'] = self.src_db_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestDbType') is not None:
            self.dest_db_type = m.get('DestDbType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SrcDbType') is not None:
            self.src_db_type = m.get('SrcDbType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

