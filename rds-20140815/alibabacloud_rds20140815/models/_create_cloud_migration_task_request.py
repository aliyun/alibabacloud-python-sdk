# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudMigrationTaskRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        resource_owner_id: int = None,
        source_account: str = None,
        source_category: str = None,
        source_ip_address: str = None,
        source_password: str = None,
        source_port: int = None,
        task_name: str = None,
    ):
        # The ID of the destination instance. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.resource_owner_id = resource_owner_id
        # The username of the account that is used to connect to the self-managed PostgreSQL instance. Enter the username of the account that you created in the [Create an account for cloud migration on a self-managed PostgreSQL instance](https://help.aliyun.com/document_detail/369500.html) topic.
        # 
        # This parameter is required.
        self.source_account = source_account
        # The environment in which the self-managed PostgreSQL instance runs.
        # 
        # *   **idcOnVpc**: The self-managed PostgreSQL instance resides in a data center. The data center can communicate with the VPC to which the ApsaraDB RDS for PostgreSQL instance belongs.
        # *   **ecsOnVpc**: The self-managed PostgreSQL instance resides on an ECS instance.
        # 
        # This parameter is required.
        self.source_category = source_category
        # The private or public IP address that is used to connect to the self-managed PostgreSQL instance.
        # 
        # *   If the self-managed PostgreSQL instance resides on an Elastic Compute Service (ECS) instance, enter the private IP address of the ECS instance. For more information about how to obtain the private IP address of an ECS instance, see [View IP addresses](https://help.aliyun.com/document_detail/273914.html).
        # *   If the self-managed PostgreSQL instance resides in a data center, enter the private IP address of the data center.
        # 
        # This parameter is required.
        self.source_ip_address = source_ip_address
        # The password of the account that is used to connect to the self-managed PostgreSQL instance. Enter the password of the account that you created in the [Create an account for cloud migration on a self-managed PostgreSQL instance](https://help.aliyun.com/document_detail/369500.html) topic.
        # 
        # This parameter is required.
        self.source_password = source_password
        # The port number that is used to connect to the self-managed PostgreSQL instance. You can run the `netstat -a | grep PGSQL` command to obtain the port number.
        # 
        # This parameter is required.
        self.source_port = source_port
        # The name of the task. If you do not specify this parameter, ApsaraDB RDS automatically generates a name for the cloud migration task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

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

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

