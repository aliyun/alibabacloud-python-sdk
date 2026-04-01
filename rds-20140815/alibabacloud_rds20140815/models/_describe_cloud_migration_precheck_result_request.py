# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudMigrationPrecheckResultRequest(DaraModel):
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
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The page number. Pages start from page 1. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Valid values: **30** to **100**. Default value: 30.
        # 
        # This parameter is required.
        self.page_size = page_size
        self.resource_owner_id = resource_owner_id
        # The private or public IP address that is used to connect to the self-managed PostgreSQL instance.
        # 
        # *   If the self-managed PostgreSQL instance resides on an Elastic Compute Service (ECS) instance, enter the private IP address of the ECS instance. For more information about how to obtain the private IP address of an ECS instance, see [View IP addresses](https://help.aliyun.com/document_detail/273914.html).
        # *   If the self-managed PostgreSQL instance resides in an on-premises data center, enter the private IP address of the on-premises data center.
        self.source_ip_address = source_ip_address
        # The port number that is used to connect to the self-managed PostgreSQL instance. You can run the netstat -a | grep PGSQL command to obtain the port number.
        self.source_port = source_port
        # The task ID. You can obtain the task ID from the response that is returned after you call the CreateCloudMigrationPrecheckTask operation to create the task.
        self.task_id = task_id
        # The task name. You can obtain the task name from the response that is returned after you call the CreateCloudMigrationPrecheckTask operation to create the task.
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

