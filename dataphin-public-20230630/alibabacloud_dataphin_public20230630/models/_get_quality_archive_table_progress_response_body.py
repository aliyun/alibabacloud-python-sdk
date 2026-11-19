# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualityArchiveTableProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQualityArchiveTableProgressResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The progress details of the asynchronous task.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetQualityArchiveTableProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityArchiveTableProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        archive_table_id: int = None,
        archive_table_name: str = None,
        error_message: str = None,
        status: str = None,
    ):
        # The ID of the archive table. This parameter is returned after the task succeeds and can be used to switch the active table later.
        self.archive_table_id = archive_table_id
        # The full name of the archive table. This parameter is returned after the task succeeds. When a table is created, the _exception_data suffix is automatically appended to the name.
        self.archive_table_name = archive_table_name
        # The cause of the task failure. This parameter is returned only when Status is FAILED.
        self.error_message = error_message
        # The task status. Valid values:
        # - PROGRESS: The task is in progress.
        # - SUCCESS: The task is successful.
        # - FAILED: The task failed.
        # - CANCEL: The task is canceled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_table_id is not None:
            result['ArchiveTableId'] = self.archive_table_id

        if self.archive_table_name is not None:
            result['ArchiveTableName'] = self.archive_table_name

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveTableId') is not None:
            self.archive_table_id = m.get('ArchiveTableId')

        if m.get('ArchiveTableName') is not None:
            self.archive_table_name = m.get('ArchiveTableName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

