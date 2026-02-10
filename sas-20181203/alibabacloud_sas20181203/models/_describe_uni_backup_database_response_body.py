# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeUniBackupDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        database_list: List[main_models.DescribeUniBackupDatabaseResponseBodyDatabaseList] = None,
        page_info: main_models.DescribeUniBackupDatabaseResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of the information about the databases.
        self.database_list = database_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.database_list:
            for v1 in self.database_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabaseList'] = []
        if self.database_list is not None:
            for k1 in self.database_list:
                result['DatabaseList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_list = []
        if m.get('DatabaseList') is not None:
            for k1 in m.get('DatabaseList'):
                temp_model = main_models.DescribeUniBackupDatabaseResponseBodyDatabaseList()
                self.database_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeUniBackupDatabaseResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUniBackupDatabaseResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUniBackupDatabaseResponseBodyDatabaseList(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        created_by_product: str = None,
        database_name: str = None,
        database_type: str = None,
        database_version: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_uuid: str = None,
        policy_id: int = None,
        status: str = None,
    ):
        # The status of the anti-ransomware agent. Valid values:
        # 
        # *   **UNKNOWN**: unknown
        # *   **INSTALLED**: installed
        # *   **INSTALL_FAILED**: installation failed
        # *   **UNINSTALL_FAILED**: uninstallation failed
        self.agent_status = agent_status
        # The service from which the database is created. Valid values:
        # 
        # *   **HBR**: HBR
        # *   **AEGIS**: Security Center
        self.created_by_product = created_by_product
        # The name of the database.
        self.database_name = database_name
        # The type of the database. Valid values:
        # 
        # *   **MYSQL**
        # *   **MSSQL**
        # *   **Oracle**
        self.database_type = database_type
        # The version of the database engine.
        self.database_version = database_version
        # The ID of the server.
        self.instance_id = instance_id
        # The name of the instance to which the database belongs.
        self.instance_name = instance_name
        # The UUID of the Hybrid Backup Recovery (HBR) agent that is used to back up the data of the database.
        self.instance_uuid = instance_uuid
        # The ID of the anti-ransomware policy.
        self.policy_id = policy_id
        # The status of the ECS instance. Valid values:
        # 
        # *   **Stopped**
        # *   **Running**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.created_by_product is not None:
            result['CreatedByProduct'] = self.created_by_product

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.database_version is not None:
            result['DatabaseVersion'] = self.database_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_uuid is not None:
            result['InstanceUuid'] = self.instance_uuid

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('CreatedByProduct') is not None:
            self.created_by_product = m.get('CreatedByProduct')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('DatabaseVersion') is not None:
            self.database_version = m.get('DatabaseVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceUuid') is not None:
            self.instance_uuid = m.get('InstanceUuid')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

