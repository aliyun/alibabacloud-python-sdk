# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListMigrationsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMigrationsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListMigrationsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMigrationsResponseBodyData(DaraModel):
    def __init__(
        self,
        migrations: List[main_models.ListMigrationsResponseBodyDataMigrations] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of migration tasks.
        self.migrations = migrations
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.migrations:
            for v1 in self.migrations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Migrations'] = []
        if self.migrations is not None:
            for k1 in self.migrations:
                result['Migrations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migrations = []
        if m.get('Migrations') is not None:
            for k1 in m.get('Migrations'):
                temp_model = main_models.ListMigrationsResponseBodyDataMigrations()
                self.migrations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMigrationsResponseBodyDataMigrations(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        create_user_name: str = None,
        description: str = None,
        download_url: str = None,
        id: int = None,
        message: str = None,
        migration_type: str = None,
        name: str = None,
        package_type: str = None,
        project_id: int = None,
        status: str = None,
        tenant_id: int = None,
        update_time: int = None,
        update_user: str = None,
        update_user_name: str = None,
    ):
        # The time when the migration task was created.
        self.create_time = create_time
        # The ID of the user who created the migration task.
        self.create_user = create_user
        # The name of the user who created the migration task.
        self.create_user_name = create_user_name
        # The description of the export task.
        self.description = description
        # The URL that is used to download the package of the export task. You can use the URL to download the package of the export task.
        self.download_url = download_url
        # The primary key ID.
        self.id = id
        # The error message returned.
        self.message = message
        # The type of the migration task. Valid values:
        # 
        # *   IMPORT
        # *   EXPORT
        self.migration_type = migration_type
        # The name of the migration task.
        self.name = name
        # The type of the import or export package. Valid values:
        # 
        # *   DWMA (standard format)
        # *   DATAWORKS_MODEL (standard format)
        # *   DATAWORKS_V2 (Apsara Stack DataWorks V3.6.1 to V3.11)
        # *   DATAWORKS_V3 (Apsara Stack DataWorks V3.12 and later)
        # 
        # The DWMA and DATAWORKS_MODEL types are interchangeable.
        self.package_type = package_type
        # The ID of the DataWorks workspace to which the task belongs.
        self.project_id = project_id
        # The status of the migration task. Valid values:
        # 
        # *   INIT: The migration task is in the initial state.
        # *   EDITING: The migration task is being edited.
        # *   RUNNING: The migration task is running.
        # *   FAILURE: The migration task fails to run.
        # *   SUCCESS: The migration task is successfully run.
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The time when the migration task was last updated.
        self.update_time = update_time
        # The ID of the user who last updated the migration task.
        self.update_user = update_user
        # The name of the user who last updated the migration task.
        self.update_user_name = update_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type

        if self.name is not None:
            result['Name'] = self.name

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')

        return self

