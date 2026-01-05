# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateScreenshotResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tasks: List[main_models.CreateScreenshotResponseBodyTasks] = None,
    ):
        # The ID of the request. If the request fails, share this ID with technical support to help diagnose the issue.
        self.request_id = request_id
        # The tasks.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.CreateScreenshotResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class CreateScreenshotResponseBodyTasks(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        screenshot_id: str = None,
        task_id: str = None,
    ):
        # The ID of the cloud phone instance.
        self.android_instance_id = android_instance_id
        self.screenshot_id = screenshot_id
        # The ID of the task. You can use the task ID with the DescribeTasks operation to get the download link for the screenshot.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

        if self.screenshot_id is not None:
            result['ScreenshotId'] = self.screenshot_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        if m.get('ScreenshotId') is not None:
            self.screenshot_id = m.get('ScreenshotId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

