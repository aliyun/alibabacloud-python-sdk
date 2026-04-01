# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeReplicationLinkLogsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        items: List[main_models.DescribeReplicationLinkLogsResponseBodyItems] = None,
        request_id: str = None,
        total_size: int = None,
    ):
        # The ID of the instance.
        self.dbinstance_id = dbinstance_id
        # The items.
        self.items = items
        # The request ID.
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeReplicationLinkLogsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeReplicationLinkLogsResponseBodyItems(DaraModel):
    def __init__(
        self,
        detail: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        replication_info: str = None,
        replication_state: str = None,
        replicator_account: str = None,
        replicator_password: str = None,
        source_address: str = None,
        source_category: str = None,
        source_port: int = None,
        target_instance_id: str = None,
        task_id: int = None,
        task_name: str = None,
        task_stage: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The details of the task.
        self.detail = detail
        # The creation time. The time is displayed in UTC.
        self.gmt_created = gmt_created
        # The modification time. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The synchronization information. This parameter is a reserved parameter.
        self.replication_info = replication_info
        # The status of the synchronization. Valid values:
        # 
        # *   **steaming**: The synchronization is in progress.
        # *   **finish**: The synchronization is complete.
        # *   **disconnect**: The synchronization is disconnected.
        self.replication_state = replication_state
        # The account of the database that is used for data synchronization.
        self.replicator_account = replicator_account
        # The password of the account.
        self.replicator_password = replicator_password
        # The endpoint of the source instance.
        self.source_address = source_address
        # The type of the source instance. Valid values:
        # 
        # *   other: other instances
        # *   aliyunRDS: an ApsaraDB RDS instance
        self.source_category = source_category
        # The port number of the source instance.
        self.source_port = source_port
        # The destination instance ID.
        self.target_instance_id = target_instance_id
        # The ID of the task.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The stage of the task. Valid values:
        # 
        # *   **precheck**: the precheck stage.
        # *   **basebackup**: the basic backup stage.
        # *   **startup**: the startup stage.
        # *   **increment**: the incremental synchronization stage.
        self.task_stage = task_stage
        # The status of the task. Valid values:
        # 
        # *   **success**
        # *   **failure**
        # *   **running**
        self.task_status = task_status
        # The type of the task. Valid values:
        # 
        # *   **create**: creates a synchronization link.
        # *   **create-dryrun**: performs a precheck before a synchronization link is created.
        self.task_type = task_type

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

        if self.replication_info is not None:
            result['ReplicationInfo'] = self.replication_info

        if self.replication_state is not None:
            result['ReplicationState'] = self.replication_state

        if self.replicator_account is not None:
            result['ReplicatorAccount'] = self.replicator_account

        if self.replicator_password is not None:
            result['ReplicatorPassword'] = self.replicator_password

        if self.source_address is not None:
            result['SourceAddress'] = self.source_address

        if self.source_category is not None:
            result['SourceCategory'] = self.source_category

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_stage is not None:
            result['TaskStage'] = self.task_stage

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ReplicationInfo') is not None:
            self.replication_info = m.get('ReplicationInfo')

        if m.get('ReplicationState') is not None:
            self.replication_state = m.get('ReplicationState')

        if m.get('ReplicatorAccount') is not None:
            self.replicator_account = m.get('ReplicatorAccount')

        if m.get('ReplicatorPassword') is not None:
            self.replicator_password = m.get('ReplicatorPassword')

        if m.get('SourceAddress') is not None:
            self.source_address = m.get('SourceAddress')

        if m.get('SourceCategory') is not None:
            self.source_category = m.get('SourceCategory')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStage') is not None:
            self.task_stage = m.get('TaskStage')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

