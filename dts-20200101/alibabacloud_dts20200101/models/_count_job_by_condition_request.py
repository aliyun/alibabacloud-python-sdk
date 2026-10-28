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
        # The ID of the parent task for a distributed synchronization task.
        self.group_id = group_id
        # The task type. Valid values:
        # 
        # - **MIGRATION**: data migration.
        # - **SYNC**: data synchronization.
        # - **SUBSCRIBE**: change tracking.
        self.job_type = job_type
        # The query value, which corresponds to JobType.
        self.params = params
        # The region ID, which is one of the filter conditions. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region = region
        # The ID of the region where the DTS instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. This is a global parameter and is not required for this operation.
        self.resource_group_id = resource_group_id
        # The type of the source database.
        self.src_db_type = src_db_type
        # The DTS instance status. Valid values:
        # 
        # Status of a data migration task:
        # - **NotStarted**: not started.
        # - **Prechecking**: performing a precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **PreCheckPass**: precheck passed.
        # - **NotConfigured**: not configured.
        # - **Migrating**: migrating data.
        # - **Suspending**: being paused.
        # - **MigrationFailed**: migration failed.
        # - **Finished**: completed.
        # - **Retrying**: being retried.
        # - **Upgrade**: being upgraded.
        # - **Locked**: locked.
        # - **Downgrade**: being downgraded.
        # 
        # Status of a data synchronization task:
        # - **NotStarted**: not started.
        # - **Prechecking**: performing a precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **PreCheckPass**: precheck passed.
        # - **NotConfigured**: not configured.
        # - **Initializing**: performing initial synchronization.
        # - **InitializeFailed**: initial synchronization failed.
        # - **Synchronizing**: synchronizing data.
        # - **Failed**: synchronization failed.
        # - **Suspending**: being paused.
        # - **Modifying**: modifying sub-objects.
        # - **Finished**: completed.
        # - **Retrying**: being retried.
        # - **Upgrade**: being upgraded.
        # - **Locked**: locked.
        # - **Downgrade**: being downgraded.
        # 
        # Status of a change tracking task:
        # - **NotConfigured**: not configured.
        # - **NotStarted**: not started.
        # - **Prechecking**: performing a precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **PreCheckPass**: precheck passed.
        # - **Starting**: being started.
        # - **Normal**: normal.
        # - **Retrying**: being retried.
        # - **Abnormal**: abnormal.
        # - **Upgrade**: being upgraded.
        # - **Locked**: locked.
        # - **Downgrade**: being downgraded.
        self.status = status
        # Specifies the query type. Valid values:  
        # - **name**: queries by job name.  
        # - **rds**: queries by destination instance ID.  
        # - **instance**: queries by DTS instance ID.
        # - **srcRds**: queries by source instance ID.
        # 
        # > This parameter corresponds to the query value and **JobType**.
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

