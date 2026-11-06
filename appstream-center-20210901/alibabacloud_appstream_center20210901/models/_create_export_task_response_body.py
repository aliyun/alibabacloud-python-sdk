# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class CreateExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        export_task_model: main_models.CreateExportTaskResponseBodyExportTaskModel = None,
        request_id: str = None,
    ):
        # The information about the newly created export task. When the task is created, Status is INIT, Progress is 0, and the download URL and error message are empty.
        self.export_task_model = export_task_model
        # The ID of the request. You can use the ID to locate call records and troubleshoot issues. The example value is partially desensitized.
        self.request_id = request_id

    def validate(self):
        if self.export_task_model:
            self.export_task_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_task_model is not None:
            result['ExportTaskModel'] = self.export_task_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportTaskModel') is not None:
            temp_model = main_models.CreateExportTaskResponseBodyExportTaskModel()
            self.export_task_model = temp_model.from_map(m.get('ExportTaskModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateExportTaskResponseBodyExportTaskModel(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        error_msg: str = None,
        progress: float = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The time when the task was created. The time is in the yyyy-MM-dd HH:mm:ss format, accurate to seconds. The returned string does not include the time zone offset.
        self.create_time = create_time
        # The download URL of the exported file. When the task is created by calling this operation, the file is not generated and this field is empty. The null in the example represents a JSON null value, not the string "null". You can subsequently call DescribeExportTasks to query the latest download URL of the completed task and use it within the validity period.
        self.download_url = download_url
        # The error message when the task execution fails. When the task is created by calling this operation, this field is empty. The null in the example represents a JSON null value, not the string "null". When you query the task status and it is FAILED, you can use this field to identify the cause of the failure.
        self.error_msg = error_msg
        # The progress of the export task. The value is a percentage ranging from 0 to 100. When the task is created by calling this operation, 0 is returned. The value is updated based on the execution phase and reaches 100 when the task is completed.
        self.progress = progress
        # The status of the task. When the task is created by calling this operation, INIT (initialized and waiting for execution) is returned. You can subsequently call DescribeExportTasks to query RUNNING (executing), FINISHED (completed), or FAILED (failed). Do not treat INIT as export completion.
        self.status = status
        # The ID of the newly created export task. The value is a 32-character UUID string without hyphens. You can use this value as the TaskId parameter to query the task in DescribeExportTasks.
        self.task_id = task_id
        # The type of the export task. The value is the same as the TaskType in the request. For the meaning of each type, see the TaskType request parameter.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

