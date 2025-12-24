# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeEcdReportTasksResponseBody(DaraModel):
    def __init__(
        self,
        export_task_list: List[main_models.DescribeEcdReportTasksResponseBodyExportTaskList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The report export tasks.
        self.export_task_list = export_task_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.export_task_list:
            for v1 in self.export_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExportTaskList'] = []
        if self.export_task_list is not None:
            for k1 in self.export_task_list:
                result['ExportTaskList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.export_task_list = []
        if m.get('ExportTaskList') is not None:
            for k1 in m.get('ExportTaskList'):
                temp_model = main_models.DescribeEcdReportTasksResponseBodyExportTaskList()
                self.export_task_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEcdReportTasksResponseBodyExportTaskList(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        error_code: str = None,
        error_msg: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        progress: float = None,
        report_file_name: str = None,
        status: str = None,
        sub_type: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The download URL of the report file.
        self.download_url = download_url
        # The error code returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The time when the task was created.
        self.gmt_create = gmt_create
        # The time when the task was last modified.
        self.gmt_modified = gmt_modified
        # The progress of the report export task. Unit: %.
        self.progress = progress
        # The name of the report file.
        self.report_file_name = report_file_name
        # The task status.
        self.status = status
        # The sub-type of the report export task.
        # 
        # Valid value:
        # 
        # *   DESKTOP: cloud computer
        self.sub_type = sub_type
        # The ID of the report export task.
        self.task_id = task_id
        # The type of the report.
        # 
        # Valid value:
        # 
        # *   RESOURCE_REPORT
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.report_file_name is not None:
            result['ReportFileName'] = self.report_file_name

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ReportFileName') is not None:
            self.report_file_name = m.get('ReportFileName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

