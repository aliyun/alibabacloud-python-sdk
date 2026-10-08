# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateReplicationLinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dry_run: bool = None,
        replicator_account: str = None,
        replicator_password: str = None,
        source_address: str = None,
        source_category: str = None,
        source_instance_name: str = None,
        source_instance_region_id: str = None,
        source_port: int = None,
        target_address: str = None,
        task_id: int = None,
        task_name: str = None,
    ):
        # The instance ID of the disaster recovery instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to perform a dry run for creating the synchronization link of the disaster recovery instance. Valid values:
        # 
        # - **true**: Executes a dry run without creating the instance. The system checks items such as request parameters, request format, business limits, and inventory.
        # - **false** (default): Sends a normal request and creates the instance after the check is passed.
        # 
        # This parameter is required.
        self.dry_run = dry_run
        # The database account used for data synchronization.
        self.replicator_account = replicator_account
        # The password of the synchronization account.
        self.replicator_password = replicator_password
        # The endpoint of the PostgreSQL source instance or the IP address of the SQL Server source instance.
        self.source_address = source_address
        # The category of the source instance. Valid values:
        # - **other**: Other. (**Not supported for SQL Server.**)
        # - **aliyunRDS**: ApsaraDB RDS instance.
        self.source_category = source_category
        # The name of the source instance. This parameter is required when **SourceCategory** is set to **aliyunRDS**.
        self.source_instance_name = source_instance_name
        # The region ID of the source instance. This parameter is required when **SourceCategory** is set to **aliyunRDS**.
        self.source_instance_region_id = source_instance_region_id
        # The port of the source instance.
        self.source_port = source_port
        # The IP address of the SQL Server disaster recovery instance.
        self.target_address = target_address
        # The ID of a successful dry run task.
        self.task_id = task_id
        # The name of the dry run task. You can specify a custom name. If you do not specify this parameter, the system automatically generates a name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.replicator_account is not None:
            result['ReplicatorAccount'] = self.replicator_account

        if self.replicator_password is not None:
            result['ReplicatorPassword'] = self.replicator_password

        if self.source_address is not None:
            result['SourceAddress'] = self.source_address

        if self.source_category is not None:
            result['SourceCategory'] = self.source_category

        if self.source_instance_name is not None:
            result['SourceInstanceName'] = self.source_instance_name

        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.target_address is not None:
            result['TargetAddress'] = self.target_address

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ReplicatorAccount') is not None:
            self.replicator_account = m.get('ReplicatorAccount')

        if m.get('ReplicatorPassword') is not None:
            self.replicator_password = m.get('ReplicatorPassword')

        if m.get('SourceAddress') is not None:
            self.source_address = m.get('SourceAddress')

        if m.get('SourceCategory') is not None:
            self.source_category = m.get('SourceCategory')

        if m.get('SourceInstanceName') is not None:
            self.source_instance_name = m.get('SourceInstanceName')

        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('TargetAddress') is not None:
            self.target_address = m.get('TargetAddress')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

