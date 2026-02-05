# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListDownloadTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        download_tasks: main_models.ListDownloadTasksResponseBodyDownloadTasks = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.download_tasks = download_tasks
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.download_tasks:
            self.download_tasks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.download_tasks is not None:
            result['DownloadTasks'] = self.download_tasks.to_map()

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

        if m.get('DownloadTasks') is not None:
            temp_model = main_models.ListDownloadTasksResponseBodyDownloadTasks()
            self.download_tasks = temp_model.from_map(m.get('DownloadTasks'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDownloadTasksResponseBodyDownloadTasks(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListDownloadTasksResponseBodyDownloadTasksList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListDownloadTasksResponseBodyDownloadTasksList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDownloadTasksResponseBodyDownloadTasksList(DaraModel):
    def __init__(
        self,
        download_task_files: List[main_models.ListDownloadTasksResponseBodyDownloadTasksListDownloadTaskFiles] = None,
        expire_time: int = None,
        status: str = None,
        task_id: str = None,
        title: str = None,
    ):
        self.download_task_files = download_task_files
        self.expire_time = expire_time
        self.status = status
        self.task_id = task_id
        self.title = title

    def validate(self):
        if self.download_task_files:
            for v1 in self.download_task_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DownloadTaskFiles'] = []
        if self.download_task_files is not None:
            for k1 in self.download_task_files:
                result['DownloadTaskFiles'].append(k1.to_map() if k1 else None)

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.download_task_files = []
        if m.get('DownloadTaskFiles') is not None:
            for k1 in m.get('DownloadTaskFiles'):
                temp_model = main_models.ListDownloadTasksResponseBodyDownloadTasksListDownloadTaskFiles()
                self.download_task_files.append(temp_model.from_map(k1))

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ListDownloadTasksResponseBodyDownloadTasksListDownloadTaskFiles(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        progress: int = None,
        status: str = None,
        title: str = None,
    ):
        self.file_id = file_id
        self.progress = progress
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

