# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class BatchGetVideoClipTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[main_models.BatchGetVideoClipTaskResponseBodyTaskList] = None,
    ):
        self.request_id = request_id
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['taskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['taskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.task_list = []
        if m.get('taskList') is not None:
            for k1 in m.get('taskList'):
                temp_model = main_models.BatchGetVideoClipTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        return self

class BatchGetVideoClipTaskResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
        total_duration: float = None,
        total_token: int = None,
        video_list: List[main_models.BatchGetVideoClipTaskResponseBodyTaskListVideoList] = None,
    ):
        self.status = status
        self.task_id = task_id
        self.total_duration = total_duration
        self.total_token = total_token
        self.video_list = video_list

    def validate(self):
        if self.video_list:
            for v1 in self.video_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.total_duration is not None:
            result['totalDuration'] = self.total_duration

        if self.total_token is not None:
            result['totalToken'] = self.total_token

        result['videoList'] = []
        if self.video_list is not None:
            for k1 in self.video_list:
                result['videoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('totalDuration') is not None:
            self.total_duration = m.get('totalDuration')

        if m.get('totalToken') is not None:
            self.total_token = m.get('totalToken')

        self.video_list = []
        if m.get('videoList') is not None:
            for k1 in m.get('videoList'):
                temp_model = main_models.BatchGetVideoClipTaskResponseBodyTaskListVideoList()
                self.video_list.append(temp_model.from_map(k1))

        return self

class BatchGetVideoClipTaskResponseBodyTaskListVideoList(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        description: str = None,
        end_time: int = None,
        error_msg: str = None,
        title: str = None,
        video_download_url: str = None,
        video_name: str = None,
        video_url: str = None,
    ):
        self.begin_time = begin_time
        self.description = description
        self.end_time = end_time
        self.error_msg = error_msg
        self.title = title
        self.video_download_url = video_download_url
        self.video_name = video_name
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time

        if self.description is not None:
            result['description'] = self.description

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.title is not None:
            result['title'] = self.title

        if self.video_download_url is not None:
            result['videoDownloadUrl'] = self.video_download_url

        if self.video_name is not None:
            result['videoName'] = self.video_name

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('videoDownloadUrl') is not None:
            self.video_download_url = m.get('videoDownloadUrl')

        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        return self

