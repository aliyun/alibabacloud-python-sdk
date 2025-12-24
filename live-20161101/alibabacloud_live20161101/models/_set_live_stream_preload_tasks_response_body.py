# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class SetLiveStreamPreloadTasksResponseBody(DaraModel):
    def __init__(
        self,
        failed_url: int = None,
        preload_tasks_messages: main_models.SetLiveStreamPreloadTasksResponseBodyPreloadTasksMessages = None,
        request_id: str = None,
        status: str = None,
        success_url: int = None,
        total_url: int = None,
    ):
        # The number of URLs for which the prefetch task configuration failed.
        self.failed_url = failed_url
        # The details of the prefetch task.
        self.preload_tasks_messages = preload_tasks_messages
        # The ID of the request.
        self.request_id = request_id
        # The status of the prefetch task. Valid values:
        # 
        # *   Success
        # *   Failed
        # 
        # >  Success is returned only if the prefetch task is configured for all specified streaming URLs.
        self.status = status
        # The number of URLs for which the prefetch task is successfully configured.
        self.success_url = success_url
        # The total number of URLs.
        self.total_url = total_url

    def validate(self):
        if self.preload_tasks_messages:
            self.preload_tasks_messages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_url is not None:
            result['FailedURL'] = self.failed_url

        if self.preload_tasks_messages is not None:
            result['PreloadTasksMessages'] = self.preload_tasks_messages.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success_url is not None:
            result['SuccessURL'] = self.success_url

        if self.total_url is not None:
            result['TotalURL'] = self.total_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedURL') is not None:
            self.failed_url = m.get('FailedURL')

        if m.get('PreloadTasksMessages') is not None:
            temp_model = main_models.SetLiveStreamPreloadTasksResponseBodyPreloadTasksMessages()
            self.preload_tasks_messages = temp_model.from_map(m.get('PreloadTasksMessages'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessURL') is not None:
            self.success_url = m.get('SuccessURL')

        if m.get('TotalURL') is not None:
            self.total_url = m.get('TotalURL')

        return self

class SetLiveStreamPreloadTasksResponseBodyPreloadTasksMessages(DaraModel):
    def __init__(
        self,
        preload_tasks_message: List[main_models.SetLiveStreamPreloadTasksResponseBodyPreloadTasksMessagesPreloadTasksMessage] = None,
    ):
        self.preload_tasks_message = preload_tasks_message

    def validate(self):
        if self.preload_tasks_message:
            for v1 in self.preload_tasks_message:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreloadTasksMessage'] = []
        if self.preload_tasks_message is not None:
            for k1 in self.preload_tasks_message:
                result['PreloadTasksMessage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.preload_tasks_message = []
        if m.get('PreloadTasksMessage') is not None:
            for k1 in m.get('PreloadTasksMessage'):
                temp_model = main_models.SetLiveStreamPreloadTasksResponseBodyPreloadTasksMessagesPreloadTasksMessage()
                self.preload_tasks_message.append(temp_model.from_map(k1))

        return self

class SetLiveStreamPreloadTasksResponseBodyPreloadTasksMessagesPreloadTasksMessage(DaraModel):
    def __init__(
        self,
        description: str = None,
        play_url: str = None,
        task_id: str = None,
    ):
        # Indicates whether the prefetch task is successful. Valid values:
        # 
        # *   Successfully
        # *   InternalError
        self.description = description
        # The streaming URL.
        self.play_url = play_url
        # The ID of the prefetch task.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.play_url is not None:
            result['PlayUrl'] = self.play_url

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

