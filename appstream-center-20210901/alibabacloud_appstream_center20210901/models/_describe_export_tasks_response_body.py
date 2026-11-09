# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class DescribeExportTasksResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        export_task_model: List[main_models.DescribeExportTasksResponseBodyExportTaskModel] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The total number of tasks that meet the query conditions. This value is independent of the number of tasks returned on the current page and can be used with PageSize to calculate the total number of pages. If no tasks meet the conditions, 0 is returned.
        self.count = count
        # The list of export tasks, sorted in descending order of task creation time, with the most recently created tasks listed first. If no tasks meet the conditions, an empty array is returned.
        self.export_task_model = export_task_model
        # The actual page number used for this query, which is the echoed value of the PageNumber request parameter.
        self.page_number = page_number
        # The actual number of tasks per page used for this query, which is the echoed value of the PageSize request parameter.
        self.page_size = page_size
        # The ID of the request, which is used to locate call records and troubleshoot issues. The example value is partially masked.
        self.request_id = request_id

    def validate(self):
        if self.export_task_model:
            for v1 in self.export_task_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['ExportTaskModel'] = []
        if self.export_task_model is not None:
            for k1 in self.export_task_model:
                result['ExportTaskModel'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.export_task_model = []
        if m.get('ExportTaskModel') is not None:
            for k1 in m.get('ExportTaskModel'):
                temp_model = main_models.DescribeExportTasksResponseBodyExportTaskModel()
                self.export_task_model.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeExportTasksResponseBodyExportTaskModel(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        error_msg: str = None,
        export_file_name: str = None,
        progress: float = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The creation time of the task. The format is yyyy-MM-dd HH:mm:ss, accurate to seconds. The returned string does not include the time zone offset.
        self.create_time = create_time
        # The OSS pre-signed download URL of the export file. This field is returned only for tasks whose Status is FINISHED. The default maximum validity period of the signature is 1 hour and does not exceed the 24-hour validity period after the task is created. When the remaining validity period is less than 10 minutes, the server automatically refreshes and returns a new URL. If the task is not completed, the task has expired, or the URL refresh fails, this field is empty. The domain name and path in the example URL are for demonstration purposes. The actual returned value is a complete URL with signature parameters. Use the URL returned by the most recent query for downloading.
        self.download_url = download_url
        # The cause of the task execution failure. This field is returned only when Status is FAILED. The content is the English error description recorded by the server and can be directly displayed to users or used for troubleshooting. This field is empty in other states.
        self.error_msg = error_msg
        # The name of the export file. The name consists of the task type, task creation time in yyyyMMddHHmmss format, and the first 8 characters of the task ID, connected by underscores, with the .xlsx extension. If the file is not generated, this field is empty.
        self.export_file_name = export_file_name
        # The progress of the export task, in percentage. Valid values: 0 to 100. This value is updated based on the execution stage of the task and is 100 when the task is completed.
        self.progress = progress
        # The status of the export task. This operation returns the following valid values:
        # - INIT: The task is created and waiting to be executed. Continue polling.
        # - RUNNING: The export file is being generated. You can display the progress based on Progress and continue polling.
        # - FINISHED: The export file is generated. Stop polling and use DownloadUrl to download the file.
        # - FAILED: The task execution failed. Stop polling and check ErrorMsg.
        # 
        # The server also has an EXPIRED state, but this operation does not return tasks in this state.
        self.status = status
        # The ID of the export task, which is a 32-character UUID string without hyphens. You can use this value as the TaskId parameter for this operation to poll the task.
        self.task_id = task_id
        # The type of the export task. For the meaning of each value, see the TaskType request parameter.
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

        if self.export_file_name is not None:
            result['ExportFileName'] = self.export_file_name

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

        if m.get('ExportFileName') is not None:
            self.export_file_name = m.get('ExportFileName')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

