# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListRemoteADBDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data_source_items: main_models.ListRemoteADBDataSourcesResponseBodyDataSourceItems = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # Returns the successfully added data sharing service data.
        self.data_source_items = data_source_items
        # Request ID.
        self.request_id = request_id
        # Task ID.
        self.task_id = task_id

    def validate(self):
        if self.data_source_items:
            self.data_source_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_items is not None:
            result['DataSourceItems'] = self.data_source_items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceItems') is not None:
            temp_model = main_models.ListRemoteADBDataSourcesResponseBodyDataSourceItems()
            self.data_source_items = temp_model.from_map(m.get('DataSourceItems'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ListRemoteADBDataSourcesResponseBodyDataSourceItems(DaraModel):
    def __init__(
        self,
        remote_data_sources: List[main_models.ListRemoteADBDataSourcesResponseBodyDataSourceItemsRemoteDataSources] = None,
    ):
        self.remote_data_sources = remote_data_sources

    def validate(self):
        if self.remote_data_sources:
            for v1 in self.remote_data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RemoteDataSources'] = []
        if self.remote_data_sources is not None:
            for k1 in self.remote_data_sources:
                result['RemoteDataSources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remote_data_sources = []
        if m.get('RemoteDataSources') is not None:
            for k1 in m.get('RemoteDataSources'):
                temp_model = main_models.ListRemoteADBDataSourcesResponseBodyDataSourceItemsRemoteDataSources()
                self.remote_data_sources.append(temp_model.from_map(k1))

        return self

class ListRemoteADBDataSourcesResponseBodyDataSourceItemsRemoteDataSources(DaraModel):
    def __init__(
        self,
        data_source_name: str = None,
        description: str = None,
        id: int = None,
        local_database: str = None,
        local_instance_name: str = None,
        manager_user_name: str = None,
        region_id: str = None,
        remote_database: str = None,
        remote_instance_name: str = None,
        status: str = None,
        user_name: str = None,
    ):
        # Data source name
        self.data_source_name = data_source_name
        # Description.
        self.description = description
        # ID.
        self.id = id
        # Local database name
        self.local_database = local_database
        # Local instance name
        self.local_instance_name = local_instance_name
        # Manager user name
        self.manager_user_name = manager_user_name
        # Region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) API to view available region IDs.
        self.region_id = region_id
        # Remote database name
        self.remote_database = remote_database
        # Remote instance name
        self.remote_instance_name = remote_instance_name
        # Data source status
        self.status = status
        # User name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.local_database is not None:
            result['LocalDatabase'] = self.local_database

        if self.local_instance_name is not None:
            result['LocalInstanceName'] = self.local_instance_name

        if self.manager_user_name is not None:
            result['ManagerUserName'] = self.manager_user_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remote_database is not None:
            result['RemoteDatabase'] = self.remote_database

        if self.remote_instance_name is not None:
            result['RemoteInstanceName'] = self.remote_instance_name

        if self.status is not None:
            result['Status'] = self.status

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LocalDatabase') is not None:
            self.local_database = m.get('LocalDatabase')

        if m.get('LocalInstanceName') is not None:
            self.local_instance_name = m.get('LocalInstanceName')

        if m.get('ManagerUserName') is not None:
            self.manager_user_name = m.get('ManagerUserName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoteDatabase') is not None:
            self.remote_database = m.get('RemoteDatabase')

        if m.get('RemoteInstanceName') is not None:
            self.remote_instance_name = m.get('RemoteInstanceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

