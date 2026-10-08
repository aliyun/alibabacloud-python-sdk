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
        # The ID of the target instance. You can invoke the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.resource_owner_id = resource_owner_id
        # The username. The database account created in the [Create a migration account](https://help.aliyun.com/document_detail/369500.html) step.
        # 
        # This parameter is required.
        self.source_account = source_account
        # The category of the source instance.
        # 
        # - **aliyunRDS**: ApsaraDB RDS instance.
        # - **other**: other.
        # 
        # This parameter is required.
        self.source_category = source_category
        # The internal or public IP address of the self-managed PostgreSQL database.
        # 
        # - To migrate a self-managed PostgreSQL database on an ECS instance to the cloud, set this parameter to the private IP address of the ECS instance. For more information about how to obtain the IP address, see [View IP addresses](https://help.aliyun.com/document_detail/98677.html).
        # - To migrate a self-managed PostgreSQL database in an Internet Data Center (IDC) to the cloud, set this parameter to the internal IP address of the IDC.
        # 
        # This parameter is required.
        self.source_ip_address = source_ip_address
        # The password. The password of the database account created in the [Create a migration account](https://help.aliyun.com/document_detail/369500.html) step.
        # 
        # This parameter is required.
        self.source_password = source_password
        # The port of the self-managed PostgreSQL database. You can run the `netstat -a | grep PGSQL` command to view the port.
        # 
        # This parameter is required.
        self.source_port = source_port
        # The task name. You can specify a custom name. If you do not specify this parameter, the system automatically generates a name.
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

