# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudMigrationResultRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_owner_id: int = None,
        source_ip_address: str = None,
        source_port: int = None,
        task_id: int = None,
        task_name: str = None,
    ):
        # The target instance ID. You can invoke the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        # The internal IP address of the self-managed PostgreSQL database.
        # 
        # - For a one-click cloud migration of a self-managed PostgreSQL database on an ECS instance, set this parameter to the private IP address of the ECS instance. For more information, see [View IP addresses](https://help.aliyun.com/document_detail/273914.html).
        # - For a one-click cloud migration of a self-managed PostgreSQL database in an IDC, set this parameter to the internal IP address of the IDC.
        self.source_ip_address = source_ip_address
        # The port of the self-managed PostgreSQL database. You can run the netstat -a | grep PGSQL command to query the port.
        self.source_port = source_port
        # The task ID. You can obtain the task ID from the response of the CreateCloudMigrationTask operation when you create an RDS PostgreSQL cloud migration task.
        self.task_id = task_id
        # The task name. You can obtain the task name from the response of the CreateCloudMigrationTask operation when you create an RDS PostgreSQL cloud migration task.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

