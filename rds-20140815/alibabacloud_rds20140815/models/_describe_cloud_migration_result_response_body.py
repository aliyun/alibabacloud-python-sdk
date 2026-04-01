# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudMigrationResultResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeCloudMigrationResultResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_size: int = None,
    ):
        # The details about the cloud migration task.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeCloudMigrationResultResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeCloudMigrationResultResponseBodyItems(DaraModel):
    def __init__(
        self,
        detail: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        migrate_stage: str = None,
        replication_info: str = None,
        replication_state: str = None,
        source_account: str = None,
        source_category: str = None,
        source_ip_address: str = None,
        source_password: str = None,
        source_port: int = None,
        switch_time: str = None,
        target_eip: str = None,
        target_instance_name: str = None,
        task_id: int = None,
        task_name: str = None,
    ):
        # The details about the migration task.
        self.detail = detail
        # The time when the task was created.
        self.gmt_created = gmt_created
        # The time when the task was modified.
        self.gmt_modified = gmt_modified
        # The migration phase of the migration task.
        # 
        # *   **precheck**: precheck
        # *   **basebackup**: full data backup
        # *   **startup**: link establishment
        # *   **increment**: incremental data synchronization
        # *   **switch**: cloud migration-triggered switchover
        # *   **success**: cloud migration completed
        self.migrate_stage = migrate_stage
        # The information about the replication link.
        self.replication_info = replication_info
        # The status of data replication.
        # 
        # *   **unstarted**
        # *   **catchup**
        # *   **streaming**
        # *   **disconnect**
        # *   **finish**
        self.replication_state = replication_state
        # The username.
        self.source_account = source_account
        # The environment in which the self-managed PostgreSQL instance runs.
        # 
        # *   **idcOnVpc**: The self-managed PostgreSQL instance resides in a data center. The data center can communicate with the VPC to which the ApsaraDB RDS for PostgreSQL instance belongs.
        # *   **ecsOnVpc**: The self-managed PostgreSQL instance resides on an ECS instance.
        self.source_category = source_category
        # The private IP address that is used to connect to the self-managed PostgreSQL instance.
        self.source_ip_address = source_ip_address
        # The password.
        self.source_password = source_password
        # The port number that is used to connect to the self-managed PostgreSQL instance.
        self.source_port = source_port
        # The time when the switchover was performed.
        self.switch_time = switch_time
        # A reserved parameter. The return value of this parameter is empty.
        self.target_eip = target_eip
        # The ID of the destination instance.
        self.target_instance_name = target_instance_name
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.migrate_stage is not None:
            result['MigrateStage'] = self.migrate_stage

        if self.replication_info is not None:
            result['ReplicationInfo'] = self.replication_info

        if self.replication_state is not None:
            result['ReplicationState'] = self.replication_state

        if self.source_account is not None:
            result['SourceAccount'] = self.source_account

        if self.source_category is not None:
            result['SourceCategory'] = self.source_category

        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address

        if self.source_password is not None:
            result['SourcePassword'] = self.source_password

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        if self.target_eip is not None:
            result['TargetEip'] = self.target_eip

        if self.target_instance_name is not None:
            result['TargetInstanceName'] = self.target_instance_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MigrateStage') is not None:
            self.migrate_stage = m.get('MigrateStage')

        if m.get('ReplicationInfo') is not None:
            self.replication_info = m.get('ReplicationInfo')

        if m.get('ReplicationState') is not None:
            self.replication_state = m.get('ReplicationState')

        if m.get('SourceAccount') is not None:
            self.source_account = m.get('SourceAccount')

        if m.get('SourceCategory') is not None:
            self.source_category = m.get('SourceCategory')

        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')

        if m.get('SourcePassword') is not None:
            self.source_password = m.get('SourcePassword')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        if m.get('TargetEip') is not None:
            self.target_eip = m.get('TargetEip')

        if m.get('TargetInstanceName') is not None:
            self.target_instance_name = m.get('TargetInstanceName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

