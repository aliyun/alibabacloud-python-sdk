# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMigrationSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMigrationSummaryResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the migration task.
        self.data = data
        # The request ID. You can use the request ID to query logs and troubleshoot issues.
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
            temp_model = main_models.GetMigrationSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMigrationSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        create_user: str = None,
        download_url: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        migration_id: int = None,
        name: str = None,
        op_user: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # The ID of the user who created the task.
        self.create_user = create_user
        # The URL that is used to download the package of the export task. You can use the URL to download the package of the export task.
        self.download_url = download_url
        # The time when the task was created.
        self.gmt_create = gmt_create
        # The time when the task was modified.
        self.gmt_modified = gmt_modified
        # The task ID.
        self.migration_id = migration_id
        # The task name.
        self.name = name
        # The ID of the user who managed the task.
        self.op_user = op_user
        # The ID of the DataWorks workspace to which the migration task belongs.
        self.project_id = project_id
        # The status of the migration task. Valid values:
        # 
        # *   INIT
        # *   EDITING
        # *   IMPORTING
        # *   IMPORT_ERROR
        # *   IMPORT_SUCCESS
        # *   EXPORTING
        # *   EXPORT_ERROR
        # *   EXPORT_SUCCESS
        # *   REVOKED
        # *   PARTIAL_SUCCESS
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.migration_id is not None:
            result['MigrationId'] = self.migration_id

        if self.name is not None:
            result['Name'] = self.name

        if self.op_user is not None:
            result['OpUser'] = self.op_user

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MigrationId') is not None:
            self.migration_id = m.get('MigrationId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpUser') is not None:
            self.op_user = m.get('OpUser')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

